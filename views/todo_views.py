from flask import request
from flask_restful import Resource

from controllers.todo_controller import deleteTodo, getTodos, saveTodo, updateTodo

class TodoViews (Resource):
  def get (self):
    todos = getTodos()

    return { 'todos': todos }, 200

  def post (self):
    try:
      body = request.get_json()
      
      todo = {
        'task': body['task'],
        'status': 0,
      }

      if 'description' in body:
        todo['description'] = body['description']
      
      if 'status' in body:
        todo['status'] = body['status']


      savedTodo = saveTodo(todo)

      return { 'todo': savedTodo }, 201
    except KeyError:
      return { 'error': 'Invalid request. "task" is required.' }, 400

  def put (self):
    _id = request.args.get('_id', None)

    if not _id:
      return { 'error': 'Task ?_id= query parameter is required' }
    

    body = request.get_json()

    todo = {}

    if 'description' in body:
      todo['description'] = body['description']
    
    if 'status' in body:
      todo['status'] = body['status']

    if 'task' in body:
      todo['task'] = body['task']

    updatedTodo = updateTodo(_id, todo)

    return { 'todo': updatedTodo }, 201
  
  def delete (self):
    _id = request.args.get('_id', None)

    if not _id:
      return { 'error': 'Task ?_id= query parameter is required' }
    
    deletedTodo = deleteTodo(_id)

    return { 'todo': deletedTodo }, 202