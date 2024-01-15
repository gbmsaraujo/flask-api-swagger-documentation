from flask import Flask, request
from src.main.mock.users_response import users
from src.main.swagger.config import api
from src.main.swagger.users_doc import ns_user

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_flask():
    return {
        "status_code":200,
        "msg": "Sucesso",
        "data": "Bem-Vindo ao Flask"
    }

@app.route("/users", methods=["GET"])
def get_users():
    return {
        "status_code":200,
        "msg": "Sucesso",
        "data": users
    }

@app.route("/user", methods=["POST"])
def post_users():
    payload = request.json
    return  {
        "status_code":200,
        "msg": "Usuário Cadastrado Com Sucesso",
        "data": payload
    }

api.init_app(app)
api.add_namespace(ns_user)