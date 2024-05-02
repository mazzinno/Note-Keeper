from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DBNAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'onlyfortesting2003'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DBNAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User, Note

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
