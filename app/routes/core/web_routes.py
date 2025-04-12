from flask import Blueprint, render_template
from flask_login import login_required

# initialize blueprint
bp_core_web = Blueprint(
    name="core_web",
    import_name=__name__,
    template_folder="../../templates/core/",
    url_prefix="/",
)


# home route
@bp_core_web.route("/home")
@login_required
def home():
    return render_template("home.html")
