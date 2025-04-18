import cv2 as pp

import imagefunctions as img
    
p1= "images/Ghost.png"
p2= "images/mylogo.png"
pic1 = img.readimage(p1)
pic2 = img.readimage(p2)
pic=img.combineimage(pic2,pic1,0,0)
img.showimage("",pic)
# img.saveimage("saveimage",pic)       # Save image


