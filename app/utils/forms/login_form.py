from typing import override
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

from app.utils.models import User
from app.extensions import bcrypt


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")

    submit = SubmitField("Login")

    @override
    def validate(self, **kwargs):
        # Run the parent class's validation first
        if not super().validate(**kwargs):
            return False

        email = self.email.data
        password = self.password.data

        user = User.query.filter_by(email=email).first()

        if not user:
            self.email.errors.append("No account was found with this email address.")
            return False

        if not bcrypt.check_password_hash(user.password, password):
            self.password.errors.append("Incorrect password.")
            return False

        return True
