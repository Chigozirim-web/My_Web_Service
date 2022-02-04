from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
#from sqlalchemy import create_engine


db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['SECRET_KEY'] = 'hhhhhettytiu'  #to encrypt cookies 

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{USERNAME}:{PASSWORD}@localhost/{DB_NAME}"   #location of this database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    Bootstrap(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from . import model
    
    with app.app_context():
        db.create_all()

    return app

