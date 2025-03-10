import cv2 as pp

def size(pic):
    my,mx,mz=pic.shape
    return my,mx

def showimage(name,image):
    pp.imshow(name,image)
    pp.waitKey(0)

def readimage(imagepath):
    pic=pp.imread(imagepath)
    return pic




def toblackwhite(image):
    # pic=pp.imread(image)
 
        mx,my = size(image)

        for x in range(mx):
            for y in range(my):
                b=int(image[x][y][0])  # Blue 
                g=int(image[x][y][1])  # Green
                r=int(image[x][y][2])  #Red

                bwvalue= int((r+g+b)//3)  # Average RGB

                image[x][y][0] = bwvalue  # Blue
                image[x][y][1] = bwvalue  # Green
                image[x][y][2] = bwvalue  # Red
        return image
   
def toblue(image):
     mx,my=size(image)

     for x in range(mx):
          for y in range(my):
               b=int(image[x][y][0])  # Blue
               g=int(image[x][y][1])  # Green
               r=int(image[x][y][2])  # Red

               bwvalue = int((r+g+b)//3)  # Average RGB

            #    image[x][y][0] = 255   # BLUE
               image[x][y][1] = 0
               image[x][y][2] = 0
     return image

        





 

