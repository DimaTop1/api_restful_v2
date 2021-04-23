import sqlite3
from flask_restful import reqparse, abort, Api, Resource
from flask_jwt import JWT, jwt_required, current_identity


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

    @staticmethod
    def find_by_username(username):
        con = sqlite3.connect('data2.db')
        cur = con.cursor()

        query = 'SELECT * FROM users WHERE username = ?'
        row = cur.execute(query, (username,)).fetchone()

        con.close()

        user = User(*row) if row else None
        return user

    @staticmethod
    def find_by_id(_id):
        con = sqlite3.connect('data2.db')
        cur = con.cursor()

        query = 'SELECT * FROM users WHERE id = ?'
        row = cur.execute(query, (_id,)).fetchone()

        con.close()

        user = User(*row) if row else None
        return user

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help="Username cannot be blank!")
        parser.add_argument('password', help="Password cannot be blank!")
        args = parser.parse_args()
        connection = sqlite3.connect('data2.db')
        cursor = connection.cursor()

        create_user = 'INSERT INTO users(id, username, password) VALUES (NULL, ?, ?)'
        user = (args['username'], args['password'])
        if User.find_by_username(user[0]):
            return f"user {user[0]} already exists"
        cursor.execute(create_user, user)
        connection.commit()
        connection.close()
        return f"user {user[0]} is added"