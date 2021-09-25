from flask_restful import Api
from src.api.endpoints.test import Test
from src.api.endpoints.attendance import FaceRecognition

# Flask API Configuration
api = Api(
    catch_all_404s=True,
    prefix='/api'
)

api.add_resource(Test, '/')
api.add_resource(FaceRecognition, '/face')
#api.add_resource(BoundingBox, '/bounding-box')

