from flask_restful import Resource
from flask import jsonify
import boto3


class FaceRecognition(Resource):

    def get(self):
        s3_client = boto3.client(
            's3',
            aws_access_key_id='AKIA3LYDTWN6IACBP2W5',
            aws_secret_access_key='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',
            region_name='ap-south-1'
        )

        rekognition_client = boto3.client(
            'rekognition',
            aws_access_key_id='AKIA3LYDTWN6IACBP2W5',
            aws_secret_access_key='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',
            region_name='ap-south-1'
        )
        response = rekognition_client.compare_faces(
            SourceImage={
                'S3Object': {
                    'Bucket': 'nexfac-dev',
                    'Name': '1.jpg',
                }
            },
            TargetImage={
                'S3Object': {
                    'Bucket': 'nexfac-dev',
                    'Name': '2.jpg',
                }
            },
        )
        return jsonify(response)

    def post(self):
        pass
