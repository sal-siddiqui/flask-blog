from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.utils.models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )

    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        already_exists = User.query.filter_by(username=username.data).first()
        if already_exists:
            raise ValidationError("Username already taken. Please choose a different one.")

    def validate_email(self, email):
        already_exists = User.query.filter_by(email=email.data).first()
        if already_exists:
            raise ValidationError("Email already taken. Please choose a different one.")
