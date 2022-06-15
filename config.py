import os
SECRET_KEY = 'hjshjhdjah kjshkjdhjs'

APP_ID = 1200420960103822

SQLALCHEMY_DATABASE_URI = 'sqlite:///appdb.db'
#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

