from flask_restful import Resource
from flask import jsonify
import boto3

class Test(Resource):

    def get(self):
        response = "Hello, World!"
        return jsonify(response)

    def post(self):
        pass


