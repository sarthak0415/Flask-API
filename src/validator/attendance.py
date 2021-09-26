from marshmallow import Schema, fields

class BaseSchema(Schema):
    face_img = fields.Str(required=True)
    date = fields.DateTime(format='%Y-%m-%d', required=True)
    location = fields.List(fields.Integer(), required=True)


