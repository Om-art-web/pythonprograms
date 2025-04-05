  

 #  Open cv is a open source library which is used for computer vision
 
 #  and Artificial intelligence, machine learning and face recognition


 #  It has C++ , python  , Java 

 # It supports Windows , linux , Android And mac OS

 # Release Date June 2000 (24 Years)



import cv2 as pp 

pic = pp.imread("images/5.jpg")

my,mx,mz=pic.shape
print(my,mx,mz)

for y in range(my):
    for x in range(mx):
        b=int(pic[y][x][0]) # Blue
        g=int(pic[y][x][1]) # Green
        r=int(pic[y][x][2]) # Red

        bwvalue=int((r+g+b)//3) # Average RGB

        

        pic[y][x][0] = bwvalue  # Blue
        # pic[y][x][1] = bwvalue  # Green
        # pic[y][x][2] = bwvalue  # Red



pp.imshow("",pic)
pp.waitKey(0)




