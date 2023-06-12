# Todo List API with django rest framework

### Created with django rest framework 

It's a To-do List API created with django-rest-frammework. Developed in a Mac-OS enviroment . SQlite database 

Let me know if you need a docker image

## Postman Collection with example of payload request and responses 

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/20481461-3ad3dea2-a771-4242-9fc4-add7738b70bd?action=collection%2Ffork&collection-url=entityId%3D20481461-3ad3dea2-a771-4242-9fc4-add7738b70bd%26entityType%3Dcollection%26workspaceId%3Decf9a3bf-25b8-4294-b87d-48ef85b88edd)

## End points

* `POST /api/token/`
* `POST /api/token/refresh/`
* `POST /api/token/verify/`

* `POST /api/create-user/`
* `POST /api/logout-user/`
* `POST /api/lists/`
* `GET /api/lists/`
* `GET /api/lists/{id}`
* `PUT /api/lists/{id}/update`
* `DELETE /api/lists/{id}/delete`
* `GET /api/lists/folder/`
* `GET /api/lists/{id}/folder/`
* `PUT /api/lists/{id}/folder/update/`
* `DELETE /api/lists/{id}/folder/delete/`

## Get the code 

- Clone the repo `git clone https://github.com/DavidFaf/drf-todo-list.git`
- Create virtualenv (advisable)
      - cd into preferred directory then `python -m venv {enviroment name}`
- Intall requirements `pip install -r requirements.txt`
- Run the commands to generate the database :
  `python manage.py makemigrations`
  `python manage.py migrate`
- Generate SuperUser `python manage.py createsuperuser`
- Run the server `python manage.py runserver` • default port is localhost:8000
