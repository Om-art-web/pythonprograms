import cv2 as pp

def size(pic):                         #  (Size) Function Is Use for 
    my,mx,mz=pic.shape           # the shape attritbute to find the dimension like Height, Width , Channel
    return my,mx                          # (pic.shape)



def showimage(name,image):        # pp.imshow function is used to display images
    pp.imshow(name,image)      
    pp.waitKey(0)

def readimage(imagepath):      # pp.imread function is use to read an image file
    pic=pp.imread(imagepath)         # from the given directory 
    return pic




def greyscale(image):           # (greyscale) function convert the normal colour image 
    # pic=pp.imread(image)                    #into a greyscale image

                                   
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





def blackandwhite(image):            # (blackandwhite) function is used to cinvert 
                                              #image into black and white
        
    # pic=pp.imread(image)
 
        my,mx = size(image)

        for y in range(my):
            for x in range(mx):
                b=int(image[y][x][0])  # Blue 
                g=int(image[y][x][1])  # Green
                r=int(image[y][x][2])  #Red

                bwvalue= int((r+g+b)//3)  # Average RGB
                if bwvalue<128:
                     bwvalue=0
                else:
                     bwvalue=255

                image[y][x][0] = bwvalue  # Blue
                image[y][x][1] = bwvalue  # Green
                image[y][x][2] = bwvalue  # Red
        return image





def reverseblackandwhite(image):      # (reverseblackandwhite) this fucntion is totally reverse the
     my,mx=size(image)                        # function of (blackandwhite)                
     for y in range(my):
          for x in range(mx):

               
          
               image[y][x][0] = 255-image[y][x][0]# Blue
               image[y][x][1] = 255-image[y][x][1]  # Green
               image[y][x][2] = 255-image[y][x][2]  # Red
     return image

            


def toblue(image):              # (toblue)  function is used to convert normal image into a blue image 
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




def togreen(image):         # (togreen)  function is used to convert normal image into a green image
     my,mx=size(image)

     for y in range(my):
          for x in range(mx):
               b=int(image[y][x][0])  # Blue
               g=int(image[y][x][1])  # Green
               r=int(image[y][x][2])  # Red

               bwvalue=int((r+g+b)//3)  # Average RGB

               image[y][x][1] = 255   # GREEN
     return image



        
def tored(image):         # (tored) function is used to convert normal image into a red image
     my,mx=size(image)

     for y in range(my):
          for x in range(mx):
               b=int(image[y][x][0])  # Blue
               g=int(image[y][x][1])  # Green
               r=int(image[y][x][2])  # Red

               bwvalue=int((r+g+b)//3)  # Average RGB

               image[y][x][2] = 255   # RED
     return image

def horizontalswap(image):       # (horizontalswap) fucntion is use for swapping or mirroring an image 
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





def verticalswap(image):   # (verticalswap) fuction is use for flipping or mirroring an image 
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


def repeathorizontal(image):      # (repearhorizontal) fucntion is use for 
     my,mx=size(image)
     for y in range(my):
          left=0
          right=mx-1
          while left<right:
               image[y][left][0]=image[y][right][0]
               image[y][left][1]=image[y][right][1]
               image[y][left][2]=image[y][right][2]

               left+=1
               right-=1
     return image

def copyhorizontal(image):
     my,mx=size(image)
     for y in range(my):
          left=0
          right=mx-1
          while left<right:
               image[y][right][0]=image[y][left][0]
               image[y][right][1]=image[y][left][1]
               image[y][right][2]=image[y][left][2]
               left+=1
               right-=1
     return image

def getmaxvalueandminvalue(image):
    maxvalue=-1
    minvalue=256
    my,mx=size(image)
    print(my,mx)
    for y in range(my):
        for x in range(mx):
            b=int(image[y][x][0]) # Blue
            g=int(image[y][x][1]) # Green
            r=int(image[y][x][2]) # Red
                

            bwvalue=int((r+g+b)//3)  # Average RGB
            # print(bwvalue)
            if bwvalue>maxvalue:
                maxvalue=bwvalue
            if bwvalue<minvalue:
                minvalue=bwvalue
        
        
                

            
        return maxvalue,minvalue
    
def qualityincrease(image,maxvalue,minvalue):     # (qualityincrease) function is use to increase
    print("max =",maxvalue,"min =",minvalue)      # quality of an image 
    my,mx=size(image)
    print(my,mx)
    multiplier=(maxvalue-minvalue)
    multiplier=255/multiplier
    print(multiplier)
    for y in range(my):
            for x in range(mx):
                b=int(image[y][x][0]) # Blue
                g=int(image[y][x][1]) # Green
                r=int(image[y][x][2]) # Red
                
                bwvalue=int((r+g+b)//3)  # Average RGB    
                bwvalue=bwvalue-minvalue
                if bwvalue<0:
                     bwvalue=0
                bwvalue=bwvalue*multiplier
                bwvalue=int(bwvalue)
                if bwvalue<0:
                     bwvalue=0
                if bwvalue>255:
                     bwvalue=255

                image[y][x][0] = bwvalue  # Blue
                image[y][x][1] = bwvalue  # Green
                image[y][x][2] = bwvalue  # Red
                maxvalue

    return image

def combineimage(img1,img2,shiftx,shifty):     # (combineimage) funciton is use for insert a image on a
                                                            # background image 
     my1,mx1=size(img1) 
     my2,mx2=size(img2)
     print(my1,mx1,my2,mx2)
     for y in range(my1):
          for x in range(mx1):
               img2[shifty+y][shiftx + x][0] = img1[y][x][0]# Blue
               img2[shifty+y][shiftx+x][1] = img1[y][x][1]  # Green
               img2[shifty+y][shiftx+x][2] = img1[y][x][2]  # Red
     return img2







                

def saveimage(image,imagepath):        # (saveimage) [imwrite]  function is use for to save your image
     pp.imwrite(imagepath,image)                  #  on your memory disk 
     
     


         
         
