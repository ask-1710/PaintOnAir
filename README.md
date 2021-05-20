# PaintOnAir
Replicate Paint using Opencv

ColorDetection.py:
First, run the color detection code :
  Adjust the trackbars until only your color remains white while the other colours have turned black. Try avoiding backgrounds with the same color as your sketch pen.

VirtualPaint.py:

The trackbar values will be the values for your myColors variable. (mind the order: [HueMin, SatMin, ValMin, HueMax, SatMax, ValMax].The order differs from the trackbar order from the previous file)

Use www.cloford.com/resources/colours/500col.htm link to get the BGR (mind the order, it is not RGB) values for colors closest to your sketch pen's. ( Variable 'myColorValues' holds this value ) 
 
 Now, just wave the sketch pens in front of your web cam and you are already painting on air !!
