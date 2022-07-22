# file to create and manage package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'


# function to create flask app instance
def create_app():
    from .views import views
    from .auth import auth
    from .models import User

    app = Flask(__name__)
    app.config['SECRET__KEY'] = 'dummyDevKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# checks is a DB already exists and creates one if none found
def create_db(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Database created successfully!')
