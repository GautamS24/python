import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img2 = cv2.imread('IMG-20200721-WA0002.jpg')
window_name='Image'
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
faces2 = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces2:
    cv2.rectangle(img2, (x, y), (x+w, y+h), (255, 0, 0), 2)
P=cv2.imshow('Image', img2)
q=cv2.imwrite('img2.png',img2)
cv2.waitKey()
