from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user
from app.utils.forms import RegistrationForm, LoginForm
from app.extensions import bcrypt, db
from app.utils.models import User


bp_authentication_web = Blueprint(
    name="authentication_web",
    import_name=__name__,
    template_folder="../../templates/authentication/",
    url_prefix="/auth/",
)


@bp_authentication_web.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    # -- Handle GET request
    if request.method == "GET":
        return render_template("registration-form.html", form=form, title="Registration")

    # -- Handle POST request
    if not form.validate_on_submit():
        flash("Error submitting form. Please check the fields and try again.", category="danger")
        return render_template("registration-form.html", form=form, title="Registration")

    # create the user
    password_hashed = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
    user = User(username=form.username.data, email=form.email.data, password=password_hashed)
    db.session.add(user), db.session.commit()

    flash(
        f"Account created successfully for <b>{user.username}</b>. Kindly log in.",
        category="success",
    )
    return redirect(url_for("authentication_web.login"))


@bp_authentication_web.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # -- Handle GET request
    if request.method == "GET":
        return render_template("login-form.html", form=form, title="Login")

    # -- Handle POST request
    if not form.validate_on_submit():
        flash("Error logging in. Please check the fields and try again.", category="danger")
        return render_template("login-form.html", form=form, title="Login")

    # log the user in
    user = User.query.filter_by(email=form.email.data).first()
    login_user(user, remember=form.remember_me.data)
    flash(f"Logged in as <b>{user.username}</b>.", category="success")

    # redirect the user
    next_page = request.args.get("next")
    return redirect(next_page) if next_page else redirect(url_for("default_web.home"))


@bp_authentication_web.route("/logout")
def logout():
    logout_user()
    flash("You logged out succesfully.", category="info")
    return redirect(url_for("authentication_web.login"))
