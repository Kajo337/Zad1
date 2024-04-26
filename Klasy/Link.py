from flask_restful import Resource

class Link(Resource):
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id

    def to_dict(self):
        return {
            'movieId': self.movie_id,
            'title': self.imdb_id,
            'genres': self.imdb_id
        }
