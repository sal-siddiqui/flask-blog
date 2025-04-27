from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app.extensions import db
from app.utils.forms import AccountUpdateForm

bp_user_web = Blueprint(
    name="user_web",
    import_name=__name__,
    template_folder="../../templates/user/",
    url_prefix="/user/",
)


@bp_user_web.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account.html", title="Account", zip=zip)


@bp_user_web.route("/update-account", methods=["GET", "POST"])
@login_required
def update_form():
    form = AccountUpdateForm()

    # -- Handle GET Request
    if request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
        return render_template("update-form.html", title="Update Account", form=form, zip=zip)

    # -- Handle POST Request
    if not form.validate_on_submit():
        flash("Error updating account. Please check the fields and try again.", category="danger")
        return render_template("update-form.html", title="Update Account", form=form, zip=zip)

    # update user details
    current_user.username = form.username.data
    current_user.email = form.email.data
    db.session.commit()

    flash("Your account has been updated.", category="success")
    return redirect(url_for("user_web.account"))
