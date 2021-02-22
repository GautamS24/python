import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img1 = cv2.imread('20200824034018_IMG_9819.jpg')

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
faces1 = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces1:
    cv2.rectangle(img1, (x, y), (x+w, y+h), (255, 0, 0), 2)
I=cv2.imshow('img1', img1)
cv2.waitKey()
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img2 = cv2.imread('20200824035257_IMG_9855.jpg')

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
faces2 = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces2:
    cv2.rectangle(img2, (x, y), (x+w, y+h), (255, 0, 0), 2)
P=cv2.imshow('img2', img2)
cv2.waitKey()
if(I==P):
    print("he is the person")
else:
    print("not a chance")

