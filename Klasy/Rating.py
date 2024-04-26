from flask_restful import Resource

class Rating(Resource):
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'userID': self.userId,
            'movieID': self.movieId,
            'rating': self.rating,
            'timestamp': self.timestamp
        }
