from PIL import Image
# Import an image from directory:
image = Image.open("test.png")
  
# Extracting pixel map:
pixel_map = image.load()
  
# Extracting the width and height 
# of the image:
width, height = image.size
  
# taking half of the width:
for i in range(width):
    for j in range(height):
        
        # getting the RGB pixel value.
        r, g, b, p = image.getpixel((i, j))
          
        # Apply formula of grayscale:
        grayscale = (0.5*r + 0.587*g + 0.5*b)
  
        # setting the pixel value.
        pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))
  
# Saving the final output
# as "grayscale.png":
image.save("grayscale.png")