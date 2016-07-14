"""
Print text from an image using ImageMagick and Tesseract

The image is:
  - converted to black and white with ImageMagick
  - read using OCR (tesseract)
"""
import argparse
import subprocess
import os
import io

from PIL import Image
import pytesseract


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image', help='path to an image')
    args = parser.parse_args()

    # black and white is much better to do OCR, especially when dealing with
    # anti-aliased fonts
    cmd = [
        'convert',
        os.path.abspath(args.image),
        '-resize',
        '300%',
        '-black-threshold',
        '50%',
        '-white-threshold',
        '50%',
        '-',
    ]

    binimage = subprocess.check_output(cmd)

    # OCR with tesseract
    image = Image.open(io.BytesIO(binimage))
    text = pytesseract.image_to_string(image)

    # raw output
    print(text)
