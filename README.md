# PaintOnAir

Welcome to PaintOnAir, a project that emulates the functionality of the classic Paint application using OpenCV.

## Color Detection

**ColorDetection.py**: To begin, run the color detection code. Follow these steps:

1. Adjust the trackbars until only your desired color remains white while other colors turn black.
2. Be mindful of selecting a background that differs from your chosen sketch pen color.

## Virtual Paint

**VirtualPaint.py**: The trackbar values set in the previous step will be used for your `myColors` variable. 
**Please note the order: `[HueMin, SatMin, ValMin, HueMax, SatMax, ValMax]`. The order is different from the trackbar order in the colorDetection's output.**

To select colors, use this [link](http://www.cloford.com/resources/colours/500col.htm) to obtain BGR color values (note the order is BGR, not RGB) closest to your sketch pen's color. The variable `myColorValues` stores this information.

After setting the `myColorValues` and `myColors` variables in `VirtualPaint.py`, you can start painting in the air by waving your sketch pens in front of your webcam!

## Prerequisites

Ensure you have the following packages installed:

- opencv-python
- numpy

## Usage

1. Clone the repository: `git clone https://github.com/ask-1710/PaintOnAir.git`
2. Navigate to the project directory: `cd PaintOnAir`
4. Run the `ColorDetection.py` script.
6. Follow the instructions to set trackbar values.
7. Update the `myColorValues` value with the trackbar values in previous step. (instructions above)
8. Run the `VirtualPaint.py` script and start painting in the air!

Unleash your creativity with PaintOnAir – paint in the air with your sketch pens and watch your creations come to life!


---

If you find PaintOnAir interesting, consider giving it a ⭐️ to show your support.
