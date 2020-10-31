# Object_Measurement in Python OpenCV

In this project i create a code to read an image and identify various objects on it, with one object being reference object, it identifies dimension of all other objects in the image with respect to it. As a result an the dimensions of all objects in image is returned.

# Modules Used

Python 3

OpenCV

Numpy

Imutils

# Image Constraints

Backround: background must be significantly light/ dark with respeect to objects.

Distance: Considerble distance b/w object should be maintained.

Size: Object must be significantly big to be measured.

# Steps Followed

Read an image. 

Convert image into grayscale.

Find contours.

Remove small contours.

Sort contours from left to right to find the reference object.

Reference object (here leftmost box 2 cm * 2cm ).

Calculate pixels per cm.

Calculate Results. 

Draw boundary boxes around each object and calculate its height and width.

# Output

![images](Output_03.png)

# Limitations

Only work for clear 2D objects.

Image should be in perfect top-down view.

Not very accurate.

# Authors

Jahanvi Jeswani

# Acknowledgments

https://www.pyimagesearch.com/
