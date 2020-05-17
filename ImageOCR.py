import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
#C:\Users\Adam\Desktop\Newhacks2020\Image OCR\ImageOCR\ImageOCR\picture.JPG
image = cv2.imread(r"C:\xampp\htdocs\uploads\picture.JPG")
image = cv2.medianBlur(image,5)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow("gausian",th3)

#ret,th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
#cv2.imshow("ex", th)
#cv2.waitKey(0)
#th = (255-th)
#ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
#thresh = cv2.adaptiveThreshold (gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
   # cv2.THRESH_BINARY,11,2)      

kernel = np.ones((8,8),np.uint8)

img_dilation = cv2.dilate(thresh, kernel, iterations=1)
ctrs, hierarcy = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#RETR_EXTERNAL to see rectangles

sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[1])
count = 0
for i, ctr in enumerate(sorted_ctrs):
    x, y, w, h = cv2.boundingRect(ctr)

    roi = gray[y:y+h, x:x+w]
    ret,roi = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    kernel = np.ones((6,6),np.uint8)
    roi = cv2.dilate(roi,kernel,iterations =1)
    roi = 255-roi;

    #cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    if w>=14 and h>15:
        cv2.imwrite('char{}.png'.format(count),roi)
        count= count +1

for i in range(0,count):
   def white_bg_square(img):
        size = (100,100)
        layer = Image.new('RGB',size,(255,255,255))
        layer.paste(img, tuple(map(lambda x:int((x[0]-x[1])/2), zip(size, img.size))))
        return layer
   img = Image.open(r"C:\xampp\htdocs\uploads\char"+str(i)+".png")
   w, h = img.size
   if w>100 and h > 100:
       dim = (80,80)
       img = cv2.resize(img, dim, interpolation= cv2.INTER_AREA)
   img = white_bg_square(img)
   img.save(r"C:\xampp\htdocs\uploads\char"+str(i)+".png")

#cv2.imshow("markedareas",image)
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
#dilated = cv2.dilate(thresh,kernel,iterations = 0)
#contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#i=5
#for contour in contours:

 #   [x,y,w,h] = cv2.boundingRect(contour)
  #  if (w > 5 and h > 5):
  #      cv2.imwrite(str(i)+".jpg",image[y:y+h,x:x+w])
   #     i=i+1
#for e in range (10):
#    image = cv2.imread(r"C:\Users\Adam\Desktop\Newhacks2020\Image OCR\ImageOCR\ImageOCR/"+str(e+5)+".jpg")
 #   print(image.shape)
  #  cv2.waitKey(0)
   # sides = 28
    #dim = (sides,sides)
    #resizedim = cv2.resize(image, dim, interpolation= cv2.INTER_AREA)
    #cv2.imshow("image",image)
    #cv2.waitKey(0)
    #cv2.imshow("Resized",resizedim)
    #cv2.waitKey(0)
    #print(resizedim.shape)

  
