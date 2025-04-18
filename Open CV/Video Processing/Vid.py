import cv2 as pp 

pic1=pp.imread("images/4.png")
pic2=pp.imread("images/mylogo.png")

my1,mx1=pic1.shape
my2,mx2=pic2.shape
print(my1,mx1,my2,mx2)
shifty=50
shiftx=50
for y in range(my1):
    for x in range(mx1):
        pic1[shifty][shiftx][0]=pic2[y][x][0]  # Blue
        pic1[shifty][shiftx][1]=pic2[y][x][1]  # Green
        pic1[shifty][shiftx][2]=pic2[y][x][2]  # Red

pp.imshow("Result",pic1)
pp.imshow("Resul 2",pic2)
pp.waitKey(0)