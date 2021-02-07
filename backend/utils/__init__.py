'''
This file is used to create app 、database and loginmanager
'''
import sys
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_apscheduler import APScheduler

from werkzeug.routing import BaseConverter

from .config import Config

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.session_protection = 'strong'

db = SQLAlchemy()
scheduler = APScheduler()

class RegexConverter(BaseConverter):
    '''
    use for analysing regex route
    '''
    def __init__(self, url, *items):
        super(RegexConverter).__init__(url)
        self.regex = items[0]

def init_app():
    '''
    return flask app
    '''
    app = Flask(__name__)
    app.config.from_object(Config())
    app.url_map.converters['reg'] = RegexConverter
    db.init_app(app)
    login_manager.init_app(app)
    scheduler.init_app(app)
    with app.app_context():
        db.create_all()
    from ..views.blogs import blogs
    from ..views.users import users
    from ..views.comments import comments
    app.register_blueprint(blogs, url_prefix="/api/blogs")
    app.register_blueprint(users, url_prefix="/api/users")
    app.register_blueprint(comments, url_prefix="/api/comments")
    return app
    
