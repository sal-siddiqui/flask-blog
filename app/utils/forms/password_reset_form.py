from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class PasswordResetForm(FlaskForm):
    password_new = PasswordField("New Password", validators=[DataRequired()])
    password_confirm = PasswordField(
        "Confirm New Password", validators=[DataRequired(), EqualTo("password_new")]
    )
    submit = SubmitField("Submit")
