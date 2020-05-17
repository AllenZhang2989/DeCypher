import cv2
import wordninja

def str_append(l2,s):
    l2.append(s)
    return''. join(l2)

#joining the strings
a='fam'
b=["heywasgood"]
c=str_append(b,a) #join b to a

#splits and outputs the words to textfile
f=open("output.txt", "w+") 
for x in wordninja.split(c):
    f.write(x+" ")
f.close()
#display image
image= cv2.imread(r"C:\xampp\htdocs\uploads\picture.jpg")
cv2.imshow("image",image)
cv2.waitKey(0)


