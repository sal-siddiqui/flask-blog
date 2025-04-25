from flask import Blueprint, render_template
from app.utils.forms import RegistrationForm, LoginForm

# initialize blueprint
bp_authentication_web = Blueprint(
    name="authentication_web",
    import_name=__name__,
    template_folder="../../templates/authentication/",
    url_prefix="/auth/",
)


@bp_authentication_web.route("/register")
def register():
    form = RegistrationForm()
    print(form.confirm_password.label)
    return render_template("registration-form.html", form=form, title="Registration")


@bp_authentication_web.route("/login")
def login():
    form = LoginForm()
    return render_template("login-form.html", form=form, title="Login")
