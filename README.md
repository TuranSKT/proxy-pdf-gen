# Proxy Card PDF Generator

Generate a PDF with multiple proxy cards for tabletop games using your own card images.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Upscaling](#upscaling)
- [Contributing](#contributing)
- [License](#license)

## Overview

This tool allows users to generate a PDF containing multiple proxy cards for tabletop games. Optionally, the images of these cards can be upscaled using OpenCV's super resolution models to ensure high quality.

## Installation

1. **Prerequisites**: Ensure you have Python and the necessary libraries installed.
2. **Clone the Repository**:
    ```bash
    git clone <YOUR_REPOSITORY_LINK>
    ```
3. **Navigate to the project directory**:
    ```bash
    cd proxy_maker
    ```
4. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```
5. **Download OpenCV Models**: If you plan to use the upscaling feature, ensure you have the necessary OpenCV models downloaded.
    - [Download the Models folder here](<https://github.com/Araxeus/PNG-Upscale/tree/main/Models>).
    - Follow the instructions provided in the [provided article](<https://towardsdatascience.com/deep-learning-based-super-resolution-with-opencv-4fd736678066>).

## Usage

1. Place your card images in the `cards` directory.
2. Run the script:
    ```bash
    python generate_pdf.py
    ```
3. Retrieve the generated `output.pdf` in the main directory.

## Upscaling

To upscale the card images using OpenCV's super resolution models:

1. Ensure you've followed the installation steps related to OpenCV models.
2. Run the script with the `--upscale` flag:
    ```bash
    python generate_pdf.py --upscale
    ```

This will upscale the card images and include them in the generated PDF.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

