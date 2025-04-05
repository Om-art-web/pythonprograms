import cv2 as pp 

 # Load images

img1=pp.imread("images/4.jpg")
img2=pp.imread("images/Anime.jpg")

 # Resize to same size (if needed)

img1=pp.resize(img1, (300,300))
img2=pp.resize(img2, (300,300))

 # Combine Side By Side

combined=pp.hconcat([img1,img2])

 # Show the Result

pp.imshow("Combined",combined)
pp.waitKey(0)
pp.destroyAllWindows()

