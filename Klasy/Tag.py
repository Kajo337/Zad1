from flask_restful import Resource

class Tag(Resource):
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'userID': self.userId,
            'movieID': self.movieId,
            'tags': self.tag,
            'timestamp': self.timestamp
        }