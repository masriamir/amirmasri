from flask import Flask

app = Flask(__name__)
app.config.from_envvar('CFG_AMIRMASRI')

from app import views
from app import mongo
