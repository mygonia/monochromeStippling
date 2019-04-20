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

8. Repeated for all pixels until finished
