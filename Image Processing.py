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

