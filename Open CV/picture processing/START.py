import cv2 as pp

import imagefunctions as img
    
p1= "images/4.jpg"
p2= "images/Anime.jpg"
pic1 = img.readimage(p1)
pic2 = img.readimage(p2)
pic=img.combineimage(pic1,pic2,70,10)
img.showimage("",pic)
# img.saveimage(pic,"save image.png")       # Save image 


