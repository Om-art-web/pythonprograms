import cv2 as pp

pic = pp.imread("Moon.jpg")

my, mx, mz = pic.shape
print(my, mx, mz, pic.shape, end=",")
for y in range(my):
    left=0
    right=mx-1
    while left<right:
        
                t=pic[y][left][0]
                pic[y][left][0]=pic[y][right][0]
                pic[y][right][0]=t

                t=pic[y][left][1]
                pic[y][left][1]=pic[y][right][1]
                pic[y][right][1]=t

                t=pic[y][left][2]
                pic[y][left][2]=pic[y][right][2]
                pic[y][right][2]=t
                left+=1
                right-=1


output=pp.imshow('Show Pictures',pic)
pp.waitKey(0)




              


