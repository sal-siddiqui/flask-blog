from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, logout_user

from app.extensions import db, bcrypt
from app.utils.forms import AccountUpdateForm, RequestPasswordResetForm, PasswordResetForm
from app.utils.helpers import send_email  # noqa: F401
from app.utils.models import Post, User

bp_user_web = Blueprint(
    name="user_web",
    import_name=__name__,
    template_folder="../../templates/user/",
    url_prefix="/user/",
)


@bp_user_web.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account.html", title="Account")


@bp_user_web.route("/update-account", methods=["GET", "POST"])
@login_required
def update_form():
    form = AccountUpdateForm()

    # -- Handle GET Request
    if request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
        return render_template("update-form.html", title="Update Account", form=form)

    # -- Handle POST Request
    if not form.validate_on_submit():
        flash("Error updating account. Please check the fields and try again.", category="danger")
        return render_template("update-form.html", title="Update Account", form=form)

    # update user details
    current_user.username = form.username.data
    current_user.email = form.email.data
    db.session.commit()

    flash("Your account has been updated.", category="success")
    return redirect(url_for("user_web.account"))


@bp_user_web.route("<string:username>/posts")
def user_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get("page", default=1, type=int)
    posts = (
        Post.query.filter_by(author=user)
        .order_by(Post.date_posted.desc())
        .paginate(page=page, per_page=2)
    )
    return render_template(
        "user-posts.html", title=user.username, posts=posts, user=user, username=user.username
    )


@bp_user_web.route("/reset_password", methods=["GET", "POST"])
def reset_password_request():
    form = RequestPasswordResetForm()

    # -- Handle GET Request
    if request.method == "GET":
        return render_template(
            "request-password-reset-form.html", title="Request Password Reset", form=form
        )

    # -- Handle POST Request
    if not form.validate_on_submit():
        flash("Error submitting form. Please check the fields and try again.", category="danger")
        return render_template(
            "request-password-reset-form.html", title="Request Password Reset", form=form
        )

    # Send user token
    user = User.query.filter_by(email=form.email.data).first()
    # send_email(user) # I could not authenticate by google account
    flash(
        f"An email has been sent to <b>{user.email}</b> with instructions to reset the password",
        category="info",
    )
    flash(
        f"If you did not receive any email, please use this link: {url_for('user_web.reset_password', token=user.get_reset_token(), _external=True)}",
        category="info",
    )
    return redirect(url_for("authentication_web.login"))


@bp_user_web.route("/reset_password/<string:token>", methods=["GET", "POST"])
def reset_password(token):
    user = User.verify_reset_token(token)
    if not user:
        flash("Token is invalid or expired.", category="warning")
        return redirect(url_for("user_web.reset_password_request"))

    form = PasswordResetForm()

    # -- Handle GET Request
    if request.method == "GET":
        return render_template("password-reset-form.html", title="Password Reset", form=form)

    # -- Handle POST Request
    if not form.validate_on_submit():
        flash("Error submitting form. Please check the fields and try again.", category="danger")
        return render_template("password-reset-form.html", title="Password Reset", form=form)

    # update the user password
    password_hashed = bcrypt.generate_password_hash(form.password_new.data).decode("utf-8")
    user.password = password_hashed
    db.session.commit()
    flash("Your password was successfully updated.", category="success")
    logout_user()
    return redirect(url_for("authentication_web.login"))
