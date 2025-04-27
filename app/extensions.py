from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# -- SQLAlchemy
db = SQLAlchemy()

# -- Encryption
bcrypt = Bcrypt()

# -- Login Management
login_manager = LoginManager()

login_manager.login_view = "authentication_web.login"
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "warning"
