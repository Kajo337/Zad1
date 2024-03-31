from flask_restful import Resource

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
