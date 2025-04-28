from flask import url_for
from flask_mail import Message
from app.utils.models import User
from app.extensions import mail


def send_email(user: User):
    message = Message(
        subject="Reset Password Token",
        recipients=[user.email],
    )
    token = user.get_reset_token()
    message.html = f"""
    <html>
        <body>
            <h2>Password Reset Request</h2>
            <p>Hello {user.username},</p>
            <p>We received a request to reset your password. 
            Click the button below to reset it. This link will expire in 30 minutes.</p>
            <p><a href="{url_for("user_web.reset_password", token=token, _external=True)}" style="padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px;">Reset Password</a></p>
            <p>If you did not make this request, please ignore this email.</p>
            <p>Thank you,<br>Flask Blog Team</p>
        </body>
    </html>
    """
    mail.send(message)
