from flask_restful import Resource
from Klasy import Movie as m

def read_from_file(file_path):
    movies = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            movie_data = line.strip().split(',')
            movie = m.Movie(movie_data[0], movie_data[1], movie_data[2])
            movies.append(movie)
    return movies

class Movies(Resource):
    def get(self):
        movies = read_from_file('Database/movies.csv')
        serialized_movies = [movie.to_dict() for movie in movies]
        return serialized_movies