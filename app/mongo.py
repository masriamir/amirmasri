from pymongo import MongoClient
from app import app

client = MongoClient(app.config['MONGO_URI'])
db = client.amirmasri
poems = db.poems


def get_poem():
    return poems.find(projection={'_id': False}).sort('created', -1).limit(1)[0]
