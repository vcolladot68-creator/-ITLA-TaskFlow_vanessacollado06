


import os

from sqlalchemy import URL
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

load_dotenv()

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
csrf = CSRFProtect()


# Cargar usuarios durante la sesión
@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return db.session.get(User, int(user_id))


def create_app():
    app = Flask(__name__)

    # Configuración general
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Protección de cookies de sesión
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

    # Conexión a MySQL
    app.config["SQLALCHEMY_DATABASE_URI"] = URL.create(
        drivername="mysql+pymysql",
        username=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host="127.0.0.1",
        port=3308,
        database=os.getenv("MYSQL_DATABASE")
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Conectar extensiones con Flask
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    # Registrar los modelos
    from app import models

    # Registrar las rutas de autenticación
    from app.routes.auth import auth
    app.register_blueprint(auth)

    # Registrar las rutas principales
    from app.routes.main import main
    app.register_blueprint(main)

    # Registrar las rutas de tareas (CRUD)
    from app.routes.tasks import tasks
    app.register_blueprint(tasks)

    # Configuración de Flask-Login
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Inicia sesión para continuar."

    return app

