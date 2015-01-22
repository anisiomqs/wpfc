from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import tweepy

def initialize_api(app):
    consumer_key=app.config['CONSUMER_KEY']
    consumer_secret=app.config['CONSUMER_SECRET']

    access_token=app.config['ACCESS_TOKEN']
    access_token_secret=app.config['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

app = Flask(__name__)
app.config.from_object('config')
api = initialize_api(app)
db = SQLAlchemy(app)

from app import views,models
