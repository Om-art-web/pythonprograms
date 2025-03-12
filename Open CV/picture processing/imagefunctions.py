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
 
        my,mx = size(image)

        for y in range(my):
            for x in range(mx):
                b=int(image[y][x][0])  # Blue 
                g=int(image[y][x][1])  # Green
                r=int(image[y][x][2])  #Red

                bwvalue= int((r+g+b)//3)  # Average RGB

                image[y][x][0] = bwvalue  # Blue
                image[y][x][1] = bwvalue  # Green
                image[y][x][2] = bwvalue  # Red
        return image
   
def toblue(image):
     my,mx=size(image)

     for y in range(my):
          for x in range(mx):
               b=int(image[y][x][0])  # Blue
               g=int(image[y][x][1])  # Green
               r=int(image[y][x][2])  # Red

               bwvalue = int((r+g+b)//3)  # Average RGB

               image[y][x][0] = 255   # BLUE
            #    image[y][x][1] = 0
            #    image[y][x][2] = 0
     return image

def togreen(image):
     my,mx=size(image)

     for y in range(my):
          for x in range(mx):
               b=int(image[y][x][0])  # Blue
               g=int(image[y][x][1])  # Green
               r=int(image[y][x][2])  # Red

               bwvalue=int((r+g+b)//3)  # Average RGB

               image[y][x][1] = 255   # GREEN
     return image

        
def tored(image):
     my,mx=size(image)

     for y in range(my):
          for x in range(mx):
               b=int(image[y][x][0])  # Blue
               g=int(image[y][x][1])  # Green
               r=int(image[y][x][2])  # Red

               bwvalue=int((r+g+b)//3)  # Average RGB

               image[y][x][2] = 255   # RED
     return image

def horizontalswap(image):
     my,mx,=size(image)
     print("Height : ",my,"Breadth : ",mx)
     for y in range(my):
          left = 0
          right = mx-1
          while left<right:
               
               t=image[y][left][0]
               image[y][left][0]=image[y][right][0]
               image[y][right][0]=t

               t=image[y][left][1]
               image[y][left][1]=image[y][right][1]
               image[y][right][1]=t

               t=image[y][left][2]
               image[y][left][2]=image[y][right][2]
               image[y][right][2]=t

               left+=1
               right-=1
     return image

def verticalswap(image):
     my,mx=size(image)
     top=0
     down=my-1
     while top<down:
          for x in range(mx):

               t=image[top][x][0]
               image[top][x][0]=image[down][x][0]
               image[down][x][0]=t

               t=image[top][x][1]
               image[top][x][1]=image[down][x][1]
               image[down][x][1]=t

               t=image[top][x][2]
               image[top][x][2]=image[down][x][2]
               image[down][x][2]=t

          down-=1
          top+=1
     return image
               




def saveimage(image,imagepath):
     pp.imwrite(imagepath,image) 
     
     


         
