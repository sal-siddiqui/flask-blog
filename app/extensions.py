from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# database
db = SQLAlchemy()
migrate = Migrate()

# password encryption
bcrypt = Bcrypt()

# login management
login = LoginManager()
login.login_view = "authentication_web.login"

# mail
mail = Mail()
