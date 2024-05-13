from flask import Flask, render_template
from flask_restful import Api, Resource
from Klasy import Photo as pht
from Klasy import PhotoURL as phtURL
from Klasy import PhotoPOST as phtPOST

app = Flask(__name__)
api = Api(app)
api.add_resource(pht.Photo, '/photo')
api.add_resource(phtURL.PhotoURL, '/photoURL/<path:url>')
api.add_resource(phtPOST.PhotoPOST, '/photoPOST', methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True)