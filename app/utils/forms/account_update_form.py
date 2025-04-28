from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from app.utils.models import User


class AccountUpdateForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])

    submit = SubmitField("Update")

    def validate(self, **kwargs):
        # Run the parent class's validation first
        if not super().validate(**kwargs):
            return False

        username = self.username.data
        email = self.email.data

        # Ensure the user did not submit the original username and password
        if username == current_user.username and email == current_user.email:
            self.username.errors.append("New username is same as original username.")
            self.email.errors.append("New email is same as original email.")
            return False

        # Ensure the username is not used by another user
        user = User.query.filter_by(username=username).first()

        if user and user.id != current_user.id:
            self.username.errors.append("Username already taken. Please choose a different one.")
            return False

        # Ensure the email is not used by another user
        user = User.query.filter_by(email=email).first()

        if user and user.id != current_user.id:
            self.email.errors.append("Email already taken. Please choose a different one.")
            return False

        return True
