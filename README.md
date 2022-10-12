# Flask Restful Todo App

## Setup
***

Requirements: `python`

### Create Virtual Environment
```bash
python -m venv env
```
### Activate Virtual Environment
```bash
source env/bin/activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```

## Starting Server
***

### Actiavting Virtual Environment
```bash
source env/bin/activate
```
### Starting Server
```bash
python app.py
```

## API Usage
***

## Get All Todos
REQUEST:
```json
GET http://127.0.0.1:8080
```
RESPONSE:
```json
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.10.7
Date: Wed, 12 Oct 2022 16:59:37 GMT
Content-Type: application/json
Content-Length: 2856
Connection: close

{
  "todos": [
    {
      "_id": "63468d4d643a69aa05a75ff6",
      "task": "This is from POST method!",
      "status": 1,
      "description": "This is from POST method! A short description in 255 characters."
    },
    {
      "_id": "63468d74865cdf7935e9fa9a",
      "task": "This is from POST method!",
      "status": 1,
      "description": "This is from POST method! A short description in 255 characters."
    },
    {
      "_id": "63468d9bf0425ba6fe41f2f0",
      "task": "This is from POST method!",
      "status": 1,
      "description": "This is from POST method! A short description in 255 characters."
    },
    {
      "_id": "63468db56ebdc8666c3ad9ef",
      "task": "This is from POST method!",
      "status": 1,
      "description": "This is from POST method! A short description in 255 characters."
    },
    {
      "_id": "63468ddb9ce0761a02664f67",
      "task": "This is from POST method!",
      "status": 1,
      "description": "This is from POST method! A short description in 255 characters."
    }
  ]
}
```

## Add New Todo
REQUEST:
```json
POST http://127.0.0.1:8080
Content-Type: application/json

{
  "task": "This is from POST method!",
  "description": "This is from POST method! A short description in 255 characters.",
  "status": 1
}
```
RESPONSE:
```json
HTTP/1.1 201 CREATED
Server: Werkzeug/2.2.2 Python/3.10.7
Date: Wed, 12 Oct 2022 17:00:17 GMT
Content-Type: application/json
Content-Length: 223
Connection: close

{
  "todo": {
    "task": "This is from POST method!",
    "status": 1,
    "description": "This is from POST method! A short description in 255 characters.",
    "_id": "6346f2a1dbbfa702c48904e9"
  }
}
```

## Update Todo
REQUEST:
```json
PUT http://127.0.0.1:8080?_id=63468cf825c72882f632a171
Content-Type: application/json

{
  "task": "This is from PUT method!",
  "status": 0
}
```
RESPONSE:
```json
HTTP/1.1 201 CREATED
Server: Werkzeug/2.2.2 Python/3.10.7
Date: Wed, 12 Oct 2022 17:01:37 GMT
Content-Type: application/json
Content-Length: 65
Connection: close

{
  "todo": {
    "found": 1,
    "updated": 1
  }
}
```

## Delete Todo
REQUEST:
```json
DELETE http://127.0.0.1:8080?_id=63468cf825c72882f632a171
```
RESPONSE:
```json
HTTP/1.1 202 ACCEPTED
Server: Werkzeug/2.2.2 Python/3.10.7
Date: Wed, 12 Oct 2022 17:02:29 GMT
Content-Type: application/json
Content-Length: 45
Connection: close

{
  "todo": {
    "deleted": 1
  }
}
```