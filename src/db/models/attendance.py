from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute, BooleanAttribute, JSONAttribute

class Attendance(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = "attendances"
        aws_access_key_id = "AKIA3LYDTWN6IACBP2W5"
        aws_secret_access_key = "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"
        region = 'ap-south-1'
    user_id = NumberAttribute(hash_key=True)
    date = UnicodeAttribute(range_key=True)
    face_image_url = UnicodeAttribute(null=True)
    location = JSONAttribute(null=True)
    is_marked = BooleanAttribute(null=True)
    is_geo_verified = BooleanAttribute(null=True)
    is_face_biometric_verified = BooleanAttribute(null=True)
    created_at_timestamp = UnicodeAttribute(null=True)
    updated_at_timestamp = UnicodeAttribute(null=True)

