import os
import pymongo
from pymongo.server_api import ServerApi

DB_URL = os.getenv('DB_URL')

client = pymongo.MongoClient(DB_URL, server_api = ServerApi('1'))
db = client.todo_app