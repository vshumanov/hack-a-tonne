from app import api
from flask_restful import Resource
from app.models import User

class TestEndpoint(Resource):
    def get(self):
        return {'test' : 'test'}

class UserProfile(Resource):
    def get(self, user_id=None):
        if not user_id:
            return {'error' : 'no user_id provided'}
        user = User.query.filter_by(id=user_id).first()
        if user:
            return user.to_dict()
        else:
            return {'error' : 'no such user'}

