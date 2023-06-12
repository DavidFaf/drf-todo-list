# drf-todo-list
Todo List API with django rest framework

### Created with django rest framework 

It's a To-do List API created with django-rest-frammework. Developed in a Mac-OS enviroment . SQlite database

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

- Clone the repo `git clone {repo-link}`
- Create virtualenv (advisable)
      - cd into preferred directory then `python -m venv {enviroment name}`
- Intall requirements `pip install -r requirements.txt`
- Run the commands to generate the database :
  `python manage.py makemigrations`
  `python manage.py migrate`
- Generate SuperUser `python manage.py createsuperuser`
- Run the server `python manage.py runserver` • default port is localhost:8000
