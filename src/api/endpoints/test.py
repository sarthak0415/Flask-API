from flask_restful import Resource
from flask import jsonify
from src.db.models.attendance import Attendance

class Test(Resource):

    def get(self, Req):
        user = Attendance(1, '2021-09-25')
        user.is_marked = True
        user.save()
        response = "Hello, World!"
        return jsonify(response)

    def post(self):
        pass


