# wpfc
## [Worst Personal Finances Control - NLP+NLTK+Twitter](http://anisiomarxjr.github.io/python/2015/01/19/o-pior-controle-financeiro-do-mundo/)

Simple project using Python 3 to apply natural language processing to a simple money tracker.

### Dependencies

```
$ pip install flask
$ pip install flask-sqlalchemy
$ pip install sqlalchemy-migrate
```

### General instructions:

First, get a Twitter secret and key for your app. Then, put it on `config.py`:

```
CONSUMER_KEY=os.environ['CONSUMER_KEY']
CONSUMER_SECRET=os.environ['CONSUMER_SECRET']
ACCESS_TOKEN=os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET=os.environ['ACCESS_TOKEN_SECRET']
```

Then, run it:

```
flask/bin/python run.py
```

(Supposing you used something like `virtualenv` and you have the dependencies in a `flask` named folder.)
