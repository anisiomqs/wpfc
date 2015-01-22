import os

WTF_CSRF_ENABLED=True
SECRET_KEY='12034u8iojfw049u5irwpqei'
CONSUMER_KEY=os.environ['CONSUMER_KEY'] 
CONSUMER_SECRET=os.environ['CONSUMER_SECRET'] 
ACCESS_TOKEN=os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET=os.environ['ACCESS_TOKEN_SECRET']

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
