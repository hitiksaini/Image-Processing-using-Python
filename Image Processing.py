#!/usr/bin/env python
# coding: utf-8

# In[1]:

#image flipping
from PIL import Image
img = Image.open('example.jpg')  #opens the image
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)  #FLIPPED IMAGE
#SAVING NEW FILE NOW
transposed_img.save('flipped.jpg')  #specify the path to save new file


# In[ ]:

#image enhancement   CLAHE
import cv2  # to run instal OPENCV to anaconda cloud on terminal

img = cv2.imread('example.jpg')
clahe= cv2.createCLAHE()   #preparing the clahe
#convert to gray scale 
gray_img= cv2.cvtColor(img, Color_BGR2GRAY)
enh_img=clahe.apply(gray_img)
#save a new file
cv2.imwrite('enhanced.jpg')


# resizing
image = Image.open('example.jpg')
new_image = image.resize((128, 128))
new_image.save('image_400.jpg')
print(image.size) # Output: (1200, 776)
print(new_image.size) # Output: (400, 400)


# changing extension
im = Image.open('example.jpg')
im.save('extension.png')


# rotating
image = Image.open('example.jpg')
image_rot_90 = image.rotate(90)
image_rot_90.save('image_rot_90.jpg')

# Convert files to JPEG
from __future__ import print_function
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)
            
 ## Good Luck ! more will be added to it soon
