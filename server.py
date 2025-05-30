import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return "Zaid Userbot is Up & Running!"

api.add_resource(Greeting, '/')
git clone https://github.com/PrimeSujoy/STRANGER-USERBOT2.0
