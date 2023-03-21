blueprints
We use blueprints so we can register multiple sub-applications to the main application
Blueprint is an object which is similar to Flask class object. It has same set set of attributes.
But we only use blueprints only when we want to create sub-applications
By using blueprint we can do "seperation of concerns"
We can logically separate each sub-application from each other
Every sub-application can have its own static files, template folder and view files
from flask import Blueprint

blueprint_app = Blueprint("name_of_blueprint", __name__, url_prefix="/mysubapp")
Let's assume you've a project structure like this -

project_dir   (project-root)
    - IDAM (sub-application1)
        - __init__.py
        - auth.py
    - saving_account (sub-application2)
        - __init__.py
        - saving.py 
        
    - requirements.txt
    - venv
    - main.py (entrypoint of main application)
