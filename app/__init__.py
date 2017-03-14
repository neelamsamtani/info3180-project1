from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = "r@nD0rn"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://proj1:password@localhost/proj1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)

UPLOAD_FOLDER = "./app/static/uploads"

app.config.from_object(__name__)
from app import views
from app import models
