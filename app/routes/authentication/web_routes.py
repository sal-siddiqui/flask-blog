from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user

from app.utils.models import User
from app.utils.forms import LoginForm, RegistrationForm
from app.extensions import db

# initialize blueprint
bp_authentication_web = Blueprint(
    name="authentication_web",
    import_name=__name__,
    template_folder="../../templates/authentication/",
    url_prefix="/auth",
)


# login route
@bp_authentication_web.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # ——— Handle GET Request
    if request.method == "GET":
        return render_template("login.html", title="Login", form=form)

    # ——— Handle POST Request
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()

        # check if user exists and credentials are valid
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f"You have successfully logged in as {user.username}.", "success")

            # redirect to the next page or home page
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("core_web.home"))
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for("authentication_web.login"))
    else:
        flash("Check the form and try again.", "danger")
        return render_template("login.html", title="Login", form=form)


# logout route
@bp_authentication_web.route("/logout")
def logout():
    logout_user()
    flash("You haved successfully logged out.", "info")
    return redirect(url_for("authentication_web.login"))


# registration route
@bp_authentication_web.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    # ——— GET Request
    if request.method == "GET":
        return render_template("registration.html", title="Registration", form=form)

    # ——— POST Request
    if form.validate_on_submit():
        # register user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user), db.session.commit()
        flash("You have successfully registered.", "success")

        # redirect to login
        return redirect(url_for("authentication_web.login"))
    else:
        flash("Check the form and try again.", "danger")
        return render_template("registration.html", title="Registration", form=form)
