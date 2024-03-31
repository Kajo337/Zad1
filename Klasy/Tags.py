from flask_restful import Resource
from Klasy import Tag as tg

def read_movies_from_file(file_path):
    movies = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            movie_data = line.strip().split(',')
            movie = tg.Tag(movie_data[0], movie_data[1], movie_data[2], movie_data[3])
            movies.append(movie)
    return movies

class Tags(Resource):
    def get(self):
        movies = read_movies_from_file('Database/tags.csv')
        serialized_movies = [movie.to_dict() for movie in movies]
        return serialized_movies