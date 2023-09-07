# Importing Python Packages

from PIL import Image
from PIL import ImageOps
from numpy import interp

# Declaring Variables

    # No need to specify type - just figures it out


# This is a dark to light of text characters
gradient = '@@@@@@@@@@@@%%%%%%%%#########********+++++++++===='[::-1]

# Making size of image (can only do square currently)

x = 150
size = (x,x*2) # I stretch the image so that when text spacing is applied it looks normal

# To Do

# Make Gradient Diff Function

# Make Size Function to get appropriate size, so any ratio works

# Add Init + Convert into terminal use app
    # With use flags for
        # Size
        # Inversion
        
        # eg | $ py pictotxt.py <inputfile | String> 
            # -o <outputname | String> 
            # -i <Invert | Bool> 
            # -s <Size (In Line Count) | Int> 

file = Image.open('in.png') # Reading in the image
file = file.rotate(90) # Rotating to overcome flip when changed to text
file = file.resize(size) # Re-Size image to overall image size
file = file.convert("L") # Turning Image Greyscale
file = ImageOps.flip(file) # Another flip to overcome text flip
file.save('out.png') # Save output into a file
file.close() # Close original image

file = Image.open('out.png') # Open output image

max_val = 0 # Creating a variable for max pixel value (anywhere from 0-255)
            # if its lower we can spread the letter gradient differently
for xPixel in range(size[0]): # for loop - goes through every pixel in x axis
        for yPixel in range(size[1]): # for loop- goes through every Y pixel for each X ect
            xy = (xPixel, yPixel) # current coordinate from loop count/index (xPixel/yPixel)
            pixel = file.getpixel(xy) # Get current value of xy pixel (x, y) - stored in tuple
            if pixel > max_val: # looking for mex value
                 max_val = pixel + 1 # adding 1 for saftey

with open('output.txt', 'w') as out: # writing new text file (closes as end of statement automatically)
    for xPixel in range(size[0]): # Same as foor loop above - not writing it again
        line = '' # Line variable (for each pixel on X)
        for yPixel in range(size[1]):
            xy = (xPixel, yPixel)
            pixel = file.getpixel(xy)
            gradentDiff = interp(pixel, [1,max_val], [0, len(gradient)]) # This is mapping the pixel value from the scale of 0-255
            try:                                                         # to the Scale of the length of the text gradient (then getting a character)
                line += gradient[int(gradentDiff-1)]
            except:                                     # Catching an error - ill fix soon
                 
                 # Fix 
                 print('g',gradentDiff, 'm', max_val)

        print(line)# Write line to terminal (auto newline)
        out.write(line+'\n')# Write to output.txt -> '\n' is newline


