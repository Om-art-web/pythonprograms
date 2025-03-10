import cv2 as pp

pic = pp.imread("4.jpg")
print(pic)
# pp.imshow("Show Picture",pic)
pp.waitKey(0)
my, mx, mz = pic.shape
print(my, mx, mz, pic.shape, end=",")
input()
top = 0
down = my-1
for x in range(mx):

    while top < down:
        print("top ",top, " down  ",down)
        pos=0

        t = pic[top][x][pos]
        pic[top][x][pos] = pic[down][x][pos]
        pic[down][x][pos] = t
        pos=1   
        t = pic[top][x][pos]
        pic[top][x][pos] = pic[down][x][pos]
        pic[down][x][pos] = t
        
        pos=2

        t = pic[top][x][pos]
        pic[top][x][pos] = pic[down][x][pos]
        pic[down][x][pos] = t
        

        top += 1
        down -= 1

output=pp.imshow("Show Picture",pic)
pp.waitKey(0)
