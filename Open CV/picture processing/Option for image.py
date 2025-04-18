import cv2 as pp 

import imagefunctions as img


while True:
    print("0-Exit , 1-Read Image , 2-Show Image , 3-Blackandwhite , 4-Set Image to Mid")
    option=int(input("Read Option : "))
    # print(option)
    if option==0:
        break
    if option==1:
        imagepath=input("Enter the imagepath = ")
        imagepath="images/" + imagepath
        pic=pp.imread(imagepath)
    if option==2:
        pp.imshow("Image",pic)
        pp.waitKey(0)
    if option==3:
        
        my,mx,mz=pic.shape
        print(my,mx,mz)

        for y in range(my):
            for x in range(mx):
                b=int(pic[y][x][0])
                g=int(pic[y][x][1])
                r=int(pic[y][x][2])

                bwvalue=int((r+g+b)//3)
                if bwvalue<128:
                     bwvalue=0
                else:
                     bwvalue=255

                pic[y][x][0]= bwvalue
                pic[y][x][1]= bwvalue
                pic[y][x][2]= bwvalue
        pp.imshow("Image",pic)
        pp.waitKey(0)
    if option==4:
        pic1=pp.imread("images/4.jpg")
        pic2=pp.imread("images/Anime.jpg")
        img.combineimage
        pp.imshow("",pic1)
        pp.waitKey(0)
        pp.imshow("",pic2)
        pp.waitKey(0)
        





   


