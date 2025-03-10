import cv2 as pp


def size(pic):
    my, mx, mz = pic.shape
    return my, mz


def toBlackWhite(originalimagepath):

    pic = pp.imread(originalimagepath)

    # print()

    if pic is None:

        print("Picture not found")

    else:

        # print(type(pic))

        mx, my = size(pic)
        # print(mx, my, mz)

        for x in range(mx):

            for y in range(my):

                b = int(pic[x][y][0])  # Blue Value

                g = int(pic[x][y][1])  # Green Value

                r = int(pic[x][y][2])  # Red Value

                bwvalue = int((r+g+b)//3)  # Average RGB

                pic[x][y][0] = bwvalue  # Blue

                pic[x][y][1] = bwvalue  # Green Color

                pic[x][y][2] = bwvalue  # Red

                # print(r,g,b)

        return pic
    


p1 = "2.png"
# pic = pp.imread(p1)
output = toBlackWhite(p1)
print(output)
output = pp.imshow("Show Picture", output)

output = pp.waitKey(0)