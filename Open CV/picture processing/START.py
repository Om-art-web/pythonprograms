import cv2 as pp

import imagefunctions as img
    
p1= "images/6.jpg"
pic = img.readimage(p1)
pic=img.horizontalswap(pic)
img.showimage("",pic)
# img.saveimage(pic,"save image.png")       # Save image 


