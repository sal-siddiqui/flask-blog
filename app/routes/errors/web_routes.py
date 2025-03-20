from flask import Blueprint, render_template

from app.extensions import db

# initialize blueprint
bp_errors_web = Blueprint(
    name="errors_web",
    import_name=__name__,
    template_folder="../../templates/errors/",
    url_prefix="/errors",
)


@bp_errors_web.app_errorhandler(404)
def error_404(error):
    return render_template("error.html", error=error), 404


@bp_errors_web.app_errorhandler(500)
def error_500(error):
    db.session.rollback()
    return render_template("error.html", error=error, append="The administrator has been notified. Sorry for the inconvenience!"), 500
