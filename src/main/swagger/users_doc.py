from flask_restx import Resource, Namespace
from src.main.swagger.config import api
from src.main.mock.users_response import users
from src.main.swagger.users_model import user_payload, user_response

ns_user = Namespace("Users Routes", description="users operations")

@ns_user.route("/users")
class UsersResource(Resource):
    @ns_user.doc("get_all_users")
    def get(self):
        """Obtém a lista de users"""
        return {"status_code": 200, "msg": "Sucesso", "data": users}


@ns_user.route("/user")
class UserResoursePost(Resource):
    @ns_user.doc("post_a_user")
    @ns_user.expect(user_payload)
    @ns_user.marshal_with(user_response)
    def post(self):
        payload = {
            "name": ns_user.payload["name"],
            "last_name": ns_user.payload["last_name"],
            "age": ns_user.payload["age"],
            "email": ns_user.payload["email"],
        }

        return {"status_code": 200, "msg": "Sucesso", "data": payload}
