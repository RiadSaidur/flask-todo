from flask import Flask
from flask_restful import Api

from views.todo_views import TodoViews


server = Flask(__name__)
api = Api(server)


api.add_resource(TodoViews, '/')


if __name__ == '__main__':
  server.run(debug = True, port=8080)