# Importing the modules

import cv2

image = cv2.imread('/Users/srimanikanta/Desktop/Image-processing/Basics/Images/ImageSet-2/lena_color_512.tif')

# showing the color images in a number format.

print(image)
# getting the type of an object.
print(type(image))
# getting the datatype of an object.
print(image.dtype)
# knowing the shape of the image
print(image.shape)
# getting the size of an image.
print(image.size)

# Showing the greyscale images in number format.

grey_image = cv2.imread('/Users/srimanikanta/Desktop/Image-processing/Basics/Images/ImageSet-2/lena_gray_512.tif')

print(grey_image)
print(type(grey_image))
print(grey_image.dtype)
print(grey_image.shape)
print(grey_image.size)

# Getting results with opencv2 grey format

grey_image1 = cv2.imread('/Users/srimanikanta/Desktop/Image-processing/Basics/Images/ImageSet-2/lena_gray_512.tif',0)

print(grey_image1)
print(type(grey_image1))
print(grey_image1.dtype)
print(grey_image1.shape)
print(grey_image1.size)


# Showing the image in a visual format.
'''
cv2.imshow('Lena',image)
cv2.waitKey(0)
cv2.destroyAllwindows()
'''