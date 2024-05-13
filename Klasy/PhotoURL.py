from flask_restful import Resource
import cv2
import numpy as np
import requests

class PhotoURL(Resource):
    def get(self, url):
        try:
            # Pobierz zdjęcie z podanego URL
            response = requests.get(url)
            img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
            img = cv2.imdecode(img_array, -1)
            # Sprawdź, czy zdjęcie zostało prawidłowo wczytane
            if img is None:
                return {"message": "Nie udało się wczytać zdjęcia"}, 404
            # Wywołaj funkcję zliczającą osoby na zdjęciu
            count = self.get_count_of_people(img)
            return {"liczba_osob": count}, 200
        except Exception as e:
            return {"message": "Wystąpił błąd podczas przetwarzania zdjęcia: {}".format(str(e))}, 500

    def get_count_of_people(self, img):
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        boxes, weights = hog.detectMultiScale(gray, winStride=(10, 10))
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        # Wyświetlenie zdjęcia z narysowanymi prostokątami
        # for (xA, yA, xB, yB) in boxes:
        # cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)
        # cv2.imshow('img', img)
        # cv2.imshow('gray', gray)
        # cv2.waitKey(0)

        return len(boxes)
