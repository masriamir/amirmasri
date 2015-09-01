from flask import render_template
from app import app, mongo


@app.route('/')
def index():
    poem = mongo.get_poem()
    return render_template('index.html', poem=poem)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
