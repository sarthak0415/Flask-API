from flask_restful import Resource
from flask import jsonify, request
from src.db.models.attendance import Attendance
from flask_jwt_extended import jwt_required

class Test(Resource):
    @jwt_required()
    def get(self):
        json = request.args
        print('======')
        print(json)
        print('======')
        user = Attendance(1, '2021-09-25')
        user.is_marked = True
        user.save()
        response = "Hello, World!"
        return jsonify(json)

    def post(self):
        pass


