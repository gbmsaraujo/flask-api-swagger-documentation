from flask_restx import fields
from src.main.swagger.config import api


user_payload = api.model(
    "Payload",
    {
        "name": fields.String,
        "last_name": fields.String,
        "age": fields.Integer,
        "email": fields.String,
    },
)

user_response = api.model(
    "Response",
    {
        "status_code": fields.Integer,
        "msg": fields.String,
        "data": fields.Nested(user_payload),
    },
)
