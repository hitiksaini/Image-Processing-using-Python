# Image-Processing-using-Python
A simple demonstration of handling images with python
## pip install PIL 
After importing this module you can perform n number of funtions I've tried to show the most common in this repo.

I've commented the important you need to follow and also a sample example of flipping the image using this same code.
 NOTE:
 You need to set path of the images and specify the same in your python code.
 ## Reference:
PIL.Image.open(fp, mode='r')
Opens and identifies the given image file.

This is a lazy operation; this function identifies the file, but the file remains open and the actual image data is not read from the file until you try to process the data (or call the load() method). See new(). See File Handling in Pillow.

Parameters:	
fp – A filename (string), pathlib.Path object or a file object. The file object must implement read(), seek(), and tell() methods, and be opened in binary mode.
mode – The mode. If given, this argument must be “r”.
Returns:	
An Image object.

Raises:	
FileNotFoundError – If the file cannot be found.
PIL.UnidentifiedImageError – If the image cannot be opened and identified.
ValueError – If the mode is not “r”, or if a StringIO instance is used for fp.
