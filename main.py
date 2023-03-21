from flask import Flask

from resources.starwars import starwar_app
from tasks.api import tasks_app


app = Flask(__name__)


# register all the sub-applications here
app.register_blueprint(starwar_app)   # /starwars
app.register_blueprint(tasks_app)     # /tasks


# TODO
"""
1. convert swapi project task1, task2, task3 into Blueprints
2. register all blueprints with main application
3. endpoints will be like following
    - 127.0.0.1:8000/v1/taskone
    - 127.0.0.1:8000/v2/tasktwo
    - 127.0.0.1:8000/v3/taskthree
"""