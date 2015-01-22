from flask import render_template, flash, redirect
from app import app,api,db
#from .forms import LoginForm
from flask import redirect
from app.tagger import tagger,chunker
from .models import Entry
from datetime import datetime
import re

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',tweets=process_tweets())

def process_tweets():
    tweets = api.user_timeline()
    result = []
    for tweet in tweets:
        tweet_parts = chunk_tweet(tweet.text)
        what = concat_words(tweet_parts['WHAT'])
        where = concat_words(tweet_parts['LOC'])
        when = datetime.utcnow()
        involveds = concat_words(tweet_parts['INVOLVED'])
        reference = concat_words(tweet_parts['REFERENCE'])
        how_much = float(replace_comma(concat_words(tweet_parts['HOW_MUCH'])))
        classification = tweet_parts['CLASSIFICATION']
        entry = Entry(text=tweet.text,what=what,
                      where=where,when=None,
                      involveds=involveds,reference=reference,
                      how_much=how_much,classification=classification)
        db.session.add(entry)
        db.session.commit()

        result.append(entry)

    return result

def concat_words(words):
    return ' '.join(words)

def replace_comma(value):
    return value.replace(',','.')

def i_o(list_o, list_i):
    if length(list_o) > 0:
        return False
    else:
        return True

def normalize(sent):
    return re.sub(r'(?!\$)\W+', ' ', sent.lower())

def chunk_tweet(tweet):
    norm_tweet = normalize(tweet)
    tagged_sent = tagger.tag(norm_tweet)
    chunks = chunker.chunk(tagged_sent,norm_tweet)
    return chunks
