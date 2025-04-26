from flask import Blueprint, render_template, request, flash, redirect, url_for
from markupsafe import Markup
from app.utils.forms import RegistrationForm, LoginForm


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
        return render_template("registration-form.html", form=form, title="Registration", zip=zip)
    # -- Handle POST request
    if form.validate_on_submit():
        flash(f"Account created successfully for {form.username.data}.", category="success")
        return redirect(url_for("default_web.home"))
    else:
        flash("Error submitting form. Please check the fields and try again.", category="danger")
        return render_template("registration-form.html", form=form, title="Registration", zip=zip)


@bp_authentication_web.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # -- Handle GET request
    if request.method == "GET":
        return render_template("login-form.html", form=form, title="Login", zip=zip)
    # -- Handle POST request
    if form.validate_on_submit():
        flash(Markup(f"Logged in as <strong>{form.email.data}</strong>."), category="success")
        return redirect(url_for("default_web.home"))
    else:
        flash("Error logging in. Please check the fields and try again.", category="danger")
        return render_template("login-form.html", form=form, title="Login", zip=zip)
