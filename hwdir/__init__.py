from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))
from flask_sqlalchemy import SQLAlchemy

# create Flask class object named myobj
app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='does-not-matter',
    # location of sqlite database
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db = SQLAlchemy(app)

from hwdir import routes, models
