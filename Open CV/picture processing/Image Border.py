import cv2 as pp

pic= pp.imread("images/4.jpg")

my,mx,mz=pic.shape
print(my,mx,mz)
# a=2
# b=a
for y in range(my):
    for x in range(mx):
        if y <=10:
            pic[y][x][0] = 255
        if x <=10:
            pic[y][x][0] = 255
        if my-y <10:
            pic[y][x][0] = 255
        if mx-x <10:
            pic[y][x][0] = 255
        
pp.imshow('image',pic)
pp.waitKey(0)
