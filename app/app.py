from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import join, dirname, realpath
import os


app = Flask(__name__)
app.config.from_object('config')
UPLOAD_FOLDER = join(dirname(realpath(__name__)), "static\images\cars")
ALLOWED_EXTENSIONS = {"png","jpg","jpeg"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


db = SQLAlchemy(app)

