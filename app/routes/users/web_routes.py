from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from datetime import datetime, timezone

from app.utils.models import User
from app.utils.forms import EditProfileForm
from app.extensions import db

# initialize blueprint
bp_users_web = Blueprint(
    name="users_web",
    import_name=__name__,
    template_folder="../../templates/users/",
    url_prefix="/users",
)


@bp_users_web.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()


@bp_users_web.route("/<username>")
@login_required
def profile(username):
    user = db.first_or_404(User.query.filter(User.username == username))
    posts = [{"author": user, "body": "Test post #1"}, {"author": user, "body": "Test post #2"}]
    return render_template("profile/profile.html", user=user, posts=posts, title="Profile")


@bp_users_web.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm()

    # ——— GET Request
    if request.method == "GET":
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        return render_template("edit_profile.html", title="Edit Profile", form=form)

    # ——— POST Request
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash("Your changes have been saved.", "success")
        return redirect(url_for("users_web.profile", username=current_user.username))
    else:
        flash("Please check the errors and try again.", "danger")
        return render_template("edit_profile.html", title="Edit Profile", form=form)
