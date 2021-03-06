from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource

from flask import Flask
from flask_jwt import JWT
from security import authenticate, identity
from items import Item, ItemList
from users import UserRegister
from table import createtables


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

createtables()

jwt = JWT(app, authenticate, identity)
api = Api(app)

api.add_resource(Item, '/items/<name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(debug=True)
