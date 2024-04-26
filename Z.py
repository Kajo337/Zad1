from flask import Flask
from flask_restful import Api, Resource
from Klasy import HelloWorld as hw
from Klasy import Movies as ms
from Klasy import Links as lks
from Klasy import Ratings as rgs
from Klasy import Tags as tgs

app = Flask(__name__)
api = Api(app)
api.add_resource(hw.HelloWorld, '/test')
api.add_resource(ms.Movies, '/movies')
api.add_resource(lks.Links, '/links')
api.add_resource(rgs.Ratings, '/ratings')
api.add_resource(tgs.Tags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)