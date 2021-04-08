import os
import platform
from flask import Flask
from flask_migrate import Migrate
from .views import init_app as routes_init
from .models import configure as db_init
from .serializer import configure as mars_init

current_path = os.path.dirname(os.path.abspath(__file__))
slqlite_win = 'sqlite:///'
slqlite_linux = 'sqlite:////'


def create_app():
    app = Flask(__name__)
    if(platform.system() == "Windows"):
        app.config['SQLALCHEMY_DATABASE_URI'] = '%s%s/testWin.db' % (
            slqlite_win, current_path)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = '%s%s/testLinux.db' % (
            slqlite_linux, current_path)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    routes_init(app)
    db_init(app)
    mars_init(app)

    Migrate(app, app.db)

    return app
