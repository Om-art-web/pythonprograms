import cv2 as pp


def size(pic):
    my, mx, mz = pic.shape
    return my, mz


def toBandW(originalimagepath):

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


def tored(originalimagepath):
    pic = pp.imread(originalimagepath)

    if pic is None:
        print("Picture not")

    else:
        mx, my = size(pic)

        for x in range(mx):
            for y in range(my):

                b = int(pic[x][y][0])  # Blue

                g = int(pic[x][y][1])  # Green

                r = int(pic[x][y][2])  # Red

                bwvalue = int((r+g+b)//3)  # Average RGB

                pic[x][y][0] = r

        return pic


def togreen(originalimagepath):
    pic = pp.imread(originalimagepath)

    if pic is None:
        print("Not")
    else:
        my, mx = size(pic)

        for x in range(mx):
            for y in range(my):
                b = int(pic[x][y][0])  # BLue

                g = int(pic[x][y][1])  # Green

                r = int(pic[x][y][2])  # Red

                bwvalue = int((r+g+b)//3)  # Average RGB

                pic[y][x][0] = g
                pic[y][x][1] = g
                pic[y][x][2] = g
    output = pp.imshow("Show Picture", pic)

    output = pp.waitKey(0)


    return pic


def toblue(originalimagepath):
    pic = pp.imread(originalimagepath)

    if pic is None:
        print('Error')

    else:
        my, mx = size(pic)

        for x in range(mx):
            for y in range(my):

                b = int(pic[x][y][0])

                g = int(pic[x][y][1])

                r = int(pic[x][y][2])

                bwvalue = ((r+g+b)//3)

                pic[x][y][0] = b

        return pic


def imageswap(originalimagepath):
    pic = pp.imread(originalimagepath)

    if pic is None:
        print('Invalid')

    else:
        my, mx = size(pic)

        for y in range(mx):
            left = 0
            right = my-1
            while (left < right):
                t = pic[y][left][0]
                pic[y][left][0] = pic[y][right][0]
                pic[y][right][0] = t

                t = pic[y][left][1]
                pic[y][left][1] = pic[y][right][1]
                pic[y][right][1] = t

                t = pic[y][left][2]
                pic[y][left][0] = pic[y][right][2]
                pic[y][right][2] = t
                left, right = left+1, right-1

        return pic


def doubleimage(pic):
    my, mx = size(pic)
    print(my,mx)

    for y in range(my):
        left, right = 0, mx-1
        while left < right:

            pic[y][right][0] =255# pic[y][left][0]
            pic[y][right][1] =255# pic[y][left][1]
            pic[y][right][2] =255# pic[y][left][2]
            left += 1
            right -= 1
    print("dbl image")
    return pic




# pp.imwrite("D:\pythonprograms\Open CV/save.jpg",pic)#Save to disk


p1 = "1.png"
# pic = pp.imread(p1)
output = toBandW(p1)
print(output)
output = pp.imshow("Show Picture", output)

output = pp.waitKey(0)

 