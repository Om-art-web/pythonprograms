import cv2 as pp
def toBandW(originalimagepath):

    pic = pp.imread(originalimagepath)

    print()

    if pic is None:

        print("Picture not found")

    else:

        print(type(pic))

        mx, my, mz = pic.shape
        print(mx, my, mz)

        for x in range(mx):

            for y in range(my):

                b = int(pic[x][y][0])  # Blue Value

                g = int(pic[x][y][1])  # Green Value

                r = int(pic[x][y][2])  # Red Value

                bwvalue = int((r+g+b)//3)  # Average RGB

                pic[x][y][0] = bwvalue

                pic[x][y][1] = bwvalue

                pic[x][y][2] = bwvalue

                # print(r,g,b)

        return pic
        
        # pp.imwrite("D:\pythonprograms\Open CV/save.jpg",pic)#Save to disk


p1="roses.png"
output=toBandW(p1)
output = pp.imshow("Show Picture", output)
        
output = pp.waitKey(0)
        # return pic.copy()

        # print(output)
