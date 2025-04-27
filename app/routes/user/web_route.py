from flask import Blueprint, render_template
from flask_login import login_required


bp_user_web = Blueprint(
    name="user_web",
    import_name=__name__,
    template_folder="../../templates/user/",
    url_prefix="/user/",
)


@bp_user_web.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")
