from flask_restful import Resource
import cv2
import numpy as np
import requests

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
response = requests.get("https://bi.im-g.pl/im/08/22/19/z26354440AMP,Nowy-dworzec-autobusowy-przy-ul--Sadowej-w-Katowic.jpg")
img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
img = cv2.imdecode(img_array, -1)

def get_count_of_people(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    boxes, weights = hog.detectMultiScale(gray, winStride=(10,10))
    boxes = np.array([[x, y, x+w, y+h] for (x, y, w, h) in boxes])

    #Wyświetlenie zdjęcia z narysowanymi prostokątami
    for (xA, yA, xB, yB) in boxes:
        cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)
    cv2.imshow('img', img)
    #cv2.imshow('gray', gray)
    cv2.waitKey(0)

    return len(boxes)

print(get_count_of_people(img))