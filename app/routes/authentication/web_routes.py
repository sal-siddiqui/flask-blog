from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.utils.forms import RegistrationForm, LoginForm

# initialize blueprint
bp_authentication_web = Blueprint(
    name="authentication_web",
    import_name=__name__,
    template_folder="../../templates/authentication/",
    url_prefix="/auth/",
)


@bp_authentication_web.route("/register", methods=["GET", "POST"])
def register():
    # Handle GET request
    if request.method == "GET":
        form = RegistrationForm()
        return render_template("registration-form.html", form=form, title="Registration")
    # Handle POST request
    if request.method == "POST":
        form = RegistrationForm()
        if form.validate_on_submit():
            flash(f"Account created successfully for {form.username.data}.", category="success")
            return redirect(url_for("default_web.home"))
        else:
            flash(
                "Error submitting form. Please check the fields and try again.", category="danger"
            )
            return render_template("registration-form.html", form=form, title="Registration")


@bp_authentication_web.route("/login")
def login():
    form = LoginForm()
    return render_template("login-form.html", form=form, title="Login")
