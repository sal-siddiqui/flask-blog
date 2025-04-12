from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import Length

from app.utils.models import User


class EditProfileForm(FlaskForm):
    username = StringField("Username")
    about_me = TextAreaField("About Me", validators=[Length(min=0, max=140)])
    submit = SubmitField("Submit")

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data == self.original_username:
            raise ValidationError("Username is the same as the original one.")

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username taken. Please try a different one.")
