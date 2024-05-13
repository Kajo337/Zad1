import base64

from flask_restful import Resource, reqparse
import cv2
import numpy as np

class PhotoPOST(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('photo', type=str, required=True, help='Brak zdjęcia w żądaniu')
        super(PhotoPOST, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        photo_file = args['photo'].split(",")[-1]

        data = base64.b64decode(photo_file)
        photo = np.frombuffer(data, np.uint8)

        return self.get_count_of_people(photo)

    def get_count_of_people(self, photo_file):
        img = cv2.imdecode(photo_file, cv2.IMREAD_COLOR)

        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        boxes, _ = hog.detectMultiScale(gray, winStride=(10, 10))
        count = len(boxes)
        return {"liczba_osob": count}