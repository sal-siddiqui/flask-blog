from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from app.utils.models import User


# --- Registration Form
class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    register = SubmitField("Register")

    def vaidate_username(self, username):
        user = User.query.filter(User.username == username.data).first()
        if user:
            raise ValidationError("Username taken. Please try a different one.")

    def validate_email(self, email):
        user = User.query.filter(User.email == email.data).first()
        if user:
            raise ValidationError("Email taken. Please try a different one.")
