import cv2
#JUST PUTPUTTING TO TEXT massiah
f=open("output.txt", "w+") 
f.write("OUTPUT FROM TENSOR")
f.close()
#display image
image= cv2.imread(r"C:\xampp\htdocs\uploads\picture.jpg")
cv2.imshow("image",image)
cv2.waitKey(0)


