


import cv2 as pp 

image= pp.imread("images/4.jpg")

verticalimage = pp.flip(image,0)

pp.imshow('Vertical Image',verticalimage)
pp.waitKey(0)