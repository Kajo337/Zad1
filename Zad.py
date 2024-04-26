import cv2
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

img = cv2.imread('zdjecie.jpg')

def get_count_of_people(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    boxes, weights = hog.detectMultiScale(gray, winStride=(10,10))
    boxes = np.array([[x, y, x+w, y+h] for (x, y, w, h) in boxes])
    return len(boxes)
#for (xA, yA, xB, yB) in boxes:
 #   cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)

#cv2.imshow('img', img)
#cv2.imshow('gray', gray)
#cv2.waitKey(0)
print(get_count_of_people(img))
