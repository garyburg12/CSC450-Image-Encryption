from PIL import Image
# Import an image from directory:
image = Image.open("grayscale.png")
  
# Extracting pixel map:
pixel_map = image.load()
  
# Extracting the width and height 
# of the image:
width, height = image.size
c: int =0
d: int = 0
k=0
# taking half of the width:
for i in range(width):
    for j in range(height):
        
        # getting the RGB pixel value.
        r, g, b, p = image.getpixel((i, j))
#        if(i > round(width/4) and j > round(height/4) and i < round(3 * width/4) and j < round(3 * height/4)):
#          pixel_map[i, j] = (255, 255, 255, 255)
#        else:
#             pixel_map[i, j] = (0, 0, 0, 255)
        r=str(r)
        g=str(g)
        b=str(b)
        while(len(r) < 3):
             r = "0" + r
        while(len(g) < 3):
             g = "0" + g
        while(len(b) < 3):
             b = "0" + b
        c=r + g + b
        print(c)
                
# Saving the final output
# as "grayscale.png":
image.save("grayscale.png")