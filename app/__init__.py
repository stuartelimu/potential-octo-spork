from flask import Flask

# initializa application
app = Flask(__name__, instance_relative_config=True)

# load the views
from app import views

# load the config file
app.config.from_object('config')