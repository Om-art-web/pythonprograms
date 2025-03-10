import cv2 as pp
pic = pp.imread("D:/pythonprograms\Open CV/6.jpg")
print()
if pic is None:
    print("Picture not found")
else:
    print(type(pic))
    output=pp.imshow("Show Picture", pic)
    print(output)
    output=pp.waitKey(0)
    print(output)
