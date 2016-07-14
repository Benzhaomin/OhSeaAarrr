# OhSeeAarrr

Print text from an image using ImageMagick and Tesseract.

The image is:

- converted to black and white with ImageMagick
- read using OCR (tesseract)

# Requirements

- python3
- imagemagick
- tesseract

## Arch Linux

`pacman -Syu tesseract tesseract-data-eng`

## Debian

`apt-get install tesseract-ocr tesseract-ocr-eng`

# Installation

With a venv:

```shell
virtualenv3 .
source bin/activate
```
Then

```shell
make
```
