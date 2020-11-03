from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.static_folder = 'static'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.sql"
db = SQLAlchemy(app)
app.config.from_object('config')

from app import routes, models