# file to create and manage package
from flask import Flask


# function to create flask app instance
def create_app():
    app = Flask(__name__)
    app.config['SECRET__KEY'] = 'dummyDevKey'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app