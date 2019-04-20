# monochromeStippling
This takes an image, turns it monochrome, and modifies it to look like art made using a stippling technique.

This uses the PIL module.

1. A source image is taken

2. It is converted to monochrome

3. A new image file is created of the same dimensions as the source image

4. A for loop goes through each pixel in the source image

5. The shade of the pixel is noted

6. A random number is chosen to determine whether to fill in a black pixel in the new image

7. The shade of the pixel in the source determines the likelihood of its corresponding pixel in the new image being filled in

8. Repeat for all pixels until finished

<h1>Example</h1>
The repository contains three additional files as an example: ricePaddy.jpg, ricePaddyMonochrome.png, and ricePaddyStippled.png


ricePaddy is the source image obtained from Pixabay on https://www.pexels.com/photo/scenic-view-of-rice-paddy-247599/

ricePaddyMonochrome is the image converted into monochrome

ricePaddyStippled in the final, processed image made to look like it made using a stippling technique
