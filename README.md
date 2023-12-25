[![banner image](https://github.com/Ongenix/Turtle-Image-Library/blob/0ce23fc298620fe9133e8cb53cd6abc8277fd22a/banner.png)](https://github.com/Ongenix/Turtle-Image-Library/blob/0ce23fc298620fe9133e8cb53cd6abc8277fd22a/banner.png)

<p align="center">
  <a href="#features">Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a>
</p>

<br><br>
<h2 style="background-color:red;">$${\color{red}PIL \space notes\space that it isn't recommended to loop over every pixel, as the pixel list will become too large. This project doesn't store every pixel but instead instantly draws them.}$$</h2>
<br><br>

<h1 align="center" id="features">
  Features
</h1>
• Uses a premade turtle window (no need to initialize new instances)<br>
• Supports any size<br>
• Transparency support<br>
• Should support Turtle-PIL (https://github.com/jutge-org/pil-turtle)<br>

<h1 align="center" id="how-to-use">
  Tutorial
</h1>
<br>

```
import turtle
from library import turtleImage # Remember to change the filename

t = turtle.Turtle() # Initialize the turtle object

draw = turtleImage(t) # Pass in the turtle object (or RawTurtle object)
draw.draw_image("my_image.jpeg", 0, 0) # Draw the image
```
<h1 align="center" id="download">
  Download
</h1>
<p>Download library.py and include "import library" inside your python code.</p>

<h1 align="center" id="credits">
  Credits
</h1>
<p>Thanks to the amazing turtle library and PIL.</p>
