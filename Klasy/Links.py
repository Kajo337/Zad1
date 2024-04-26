from flask_restful import Resource
from Klasy import Link as lk

def read_from_file(file_path):
    movies = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            movie_data = line.strip().split(',')
            movie = lk.Link(movie_data[0], movie_data[1], movie_data[2])
            movies.append(movie)
    return movies

class Links(Resource):
    def get(self):
        movies = read_from_file('Database/links.csv')
        serialized_movies = [movie.to_dict() for movie in movies]
        return serialized_movies