from bson import ObjectId
from utils.database import db

def getTodos():
  try:
    todosObjects = db.todos.find()
    todos = []
    
    for todo in todosObjects:
      todos.append({ **todo, '_id': str(todo['_id']) })
    
    return todos
  except Exception as e:
    print(e)
    return False

def saveTodo(todo):
  try:
    _id = db.todos.insert_one({ **todo }).inserted_id
    return { **todo, '_id': str(_id) }
  except Exception as e:
    print(e)
    return False

def updateTodo(_id, todo):
  try:
    todo = db.todos.update_one({ '_id': ObjectId(_id) }, { '$set': { **todo } })
    return { 'found': todo.matched_count, 'updated': todo.modified_count }
  except Exception as e:
    print(e)
    return False

def deleteTodo(_id):
  try:
    todo = db.todos.delete_one({ '_id': ObjectId(_id) })
    return { 'deleted': todo.deleted_count }
  except Exception as e:
    print(e)
    return False