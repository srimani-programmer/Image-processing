# Importing the library

import cv2
import numpy as np

image = np.ones((512,512,3),dtype=np.uint8)

# Drawing the shape of a line.
# line(imagename,(x1,y1),(x2,y2),(color coordinates),thickness)
cv2.line(image, (225,325),(155,165),(123,211,183),5)

# Drawing the shape of the rectangle.
# rectangle(imagename,(x1,y1),(x2,y2),(color cordinates),thickness)
cv2.rectangle(image,(410,325),(440,340),(211,252,119),4)

# Drawing the shape of the circle

# circle(image,coordinatepoints,radius,colorcode,thickness)

cv2.circle(image,(125,125),20,(234,255,199),5)

cv2.imshow('Sample Image',image)
cv2.waitKey(0)
cv2.destroyAllwindows()