import cv2 as pp

import imagefunctions as img
    
originalimagepath= "images/Anime.jpg"
originalimage = img.readimage(originalimagepath)
img.showimage("",originalimage)
pic=img.blackandwhite(originalimage)
img.showimage("",pic)
# img.saveimage("saveimage",pic)       # Save image


