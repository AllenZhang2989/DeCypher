import numpy as np
import emnist
import mnist
import cv2
import wordninja
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from PIL import Image
from emnist import list_datasets
from emnist import extract_training_samples
from emnist import extract_test_samples




dimages, dlabels = extract_training_samples('digits')
dtimages, dtlabels = extract_test_samples('digits')
images, labels = extract_training_samples('letters')
timages, tlabels = extract_test_samples('letters')
labels = to_categorical(labels)
print(labels.shape)
tlabels = to_categorical(tlabels)
print(tlabels.shape)
dimages = (dimages/255) - 0.5
dtimages = (dtimages/255)- 0.5
images = (images/255) - 0.5
timages = (timages/255)-0.5


dimages = dimages.reshape((-1,784))#240000
dtimages = dimages.reshape((-1,784))#240000
images = images.reshape((-1,784))#124800
timages = timages.reshape((-1,784))#20800

model = Sequential()
model.add(Dense(64, activation = 'relu',input_dim = 784))
model.add(Dense(64, activation = 'relu'))
model.add(Dense(27, activation= 'softmax'))

model.compile(
    optimizer='adam',
     loss = 'categorical_crossentropy',
     metrics = ['accuracy']
    )

model.fit(
    images,
     labels, #ex fnn returns 2 it expects [0,0,0,0,0,0,0,0,0,0,0,0]
     epochs = 5, #number of iterations
     batch_size = 32
    )

model.evaluate(
   timages, 
      tlabels
    )
end = 10
totalValue = ""
for i in range(0,end):
    image = cv2.imread(r"C:\Users\Adam\Desktop\Newhacks2020\Image OCR\ImageOCR\ImageOCR\char"+str(i)+".png")
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    side = 28
    dim = (side,side)
    newim = cv2.resize(image, dim, interpolation= cv2.INTER_AREA)
    #cv2.imshow("image",newim)
    #cv2.imwrite("tester.jpg",newim)
    #cv2.waitKey(0)
    #newim = np.expand_dims(newim,0)
    newim = 255-newim
    newim = (newim/255)-0.5
    newim = newim.reshape(-1,784)
    predictions = model.predict(newim)
    #print (predictions)
    input = str(np.argmax(predictions, axis = 1))
    totalValue = totalValue+input
    #firstim = np.array(newim, dtype='float')
    #pixels = firstim.reshape(28,28)
    #plt.imshow(pixels)
    #plt.show()
f=open("output.txt", "w+") 
for x in wordninja.split(totalValue):
    f.write(x+" ")
f.close()
#predictions = model.predict(timages[:20])
#print(predictions)
#print(np.argmax(predictions, axis = 1))
#for i in range(0,20):
#    first_image = timages[i]
#    first_image = np.array(first_image, dtype='float')
#    pixels = first_image.reshape(28,28)
#    plt.imshow(pixels)
#    plt.show()


