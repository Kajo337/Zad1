from flask import Flask, jsonify
from flask_restful import Api, Resource
from Klasy import HelloWorld as hw


app = Flask(__name__)
api = Api(app)
api.add_resource(hw.HelloWorld, '/test')


class Movie(Resource):
    def __init__(self, movie_id, title, genres):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres

    def to_dict(self):
        return {
            'movieId': self.movie_id,
            'title': self.title,
            'genres': self.genres.split('|')
        }

def read_movies_from_file(file_path):
    movies = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            movie_data = line.strip().split(',')
            movie = Movie(movie_data[0], movie_data[1], movie_data[2])
            movies.append(movie)
    return movies

class Movies(Resource):
    def get(self):
        movies = read_movies_from_file('Database/movies.csv')
        serialized_movies = [movie.to_dict() for movie in movies]
        return serialized_movies

api.add_resource(Movies, '/movies')

if __name__ == '__main__':
    app.run(debug=True)