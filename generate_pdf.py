from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os
import cv2
from cv2 import dnn_superres

# Constants
CARD_WIDTH_INCH = 2.31
CARD_HEIGHT_INCH = 3.38
PAGE_WIDTH, PAGE_HEIGHT = A4  # Dimensions of an A4 paper in points
CARDS_PER_ROW = 3
CARDS_PER_COL = 3
CARDS_PER_PAGE = CARDS_PER_ROW * CARDS_PER_COL
MARGIN = 0.5 * inch
CARD_FOLDER = "cards"
OUTPUT_PDF = "output.pdf"
MODEL_PATH = "Models/EDSRx3.pb"  # Change to the path of the model you downloaded

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()
sr.readModel(MODEL_PATH)
sr.setModel("edsr", 3)  # You can change the model name and scale based on which model you're using


def upscale_image_with_opencv(image_path):
    image = cv2.imread(image_path)
    result = sr.upsample(image)
    upscaled_image_path = "/tmp/upscaled_image.png"
    cv2.imwrite(upscaled_image_path, result)
    return upscaled_image_path


def generate_pdf_from_cards(card_folder, output_pdf):
    card_files = [f for f in os.listdir(card_folder) if f.lower().endswith(('.png', '.jpg'))]
    card_files.sort()  # Ensure a consistent order

    c = canvas.Canvas(output_pdf, pagesize=A4)
    x_offset, y_offset = MARGIN, PAGE_HEIGHT - CARD_HEIGHT_INCH * inch - MARGIN

    for idx, card_file in enumerate(card_files):
        card_image_path = os.path.join(card_folder, card_file)
        upscaled_image_path = upscale_image_with_opencv(card_image_path)

        card_image = Image.open(upscaled_image_path)
        card_image = card_image.resize((int(CARD_WIDTH_INCH * inch), int(CARD_HEIGHT_INCH * inch)), Image.LANCZOS)

        for _ in range(3):
            c.drawInlineImage(upscaled_image_path, x_offset, y_offset, width=CARD_WIDTH_INCH * inch, height=CARD_HEIGHT_INCH * inch)

            x_offset += CARD_WIDTH_INCH * inch
            if x_offset + CARD_WIDTH_INCH * inch > PAGE_WIDTH - MARGIN:
                x_offset = MARGIN
                y_offset -= CARD_HEIGHT_INCH * inch

            if y_offset < MARGIN:
                c.showPage()
                y_offset = PAGE_HEIGHT - CARD_HEIGHT_INCH * inch - MARGIN

    c.save()

generate_pdf_from_cards(CARD_FOLDER, OUTPUT_PDF)
print(f"PDF generated at {OUTPUT_PDF}")

