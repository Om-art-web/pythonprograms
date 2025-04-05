import cv2 as pp

img=pp.imread("images/Whi.jpg")

my,mx,mz=img.shape

print(my,mx,mz)
for y in range(my):
    for x in range(mx):  
        if y<= x+10 and y>=x-10:
            img[y][x][1] = 255
        # if y+x==my+1:
        #     img[y][x][2] = 255
        # if x==mx//2 and y==my//2:
        #     img[y][x][0] = 255

pp.imshow('image',img)
pp.waitKey(0)