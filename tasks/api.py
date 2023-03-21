from flask import Blueprint


tasks_app = Blueprint("tasks", __name__, url_prefix="/tasks")


@tasks_app.route("/welcome")
def welcome():
    return "hello world from tasks sub-application"