from flask import Blueprint, render_template

# initialize blueprint
bp_error_web = Blueprint(
    name="error_web",
    import_name=__name__,
    template_folder="../../templates/error/",
    url_prefix="/error",
)


@bp_error_web.app_errorhandler(404)
@bp_error_web.app_errorhandler(403)
@bp_error_web.app_errorhandler(500)
def error_handler(error):
    return render_template("error.html", error=error, title="Error Page"), error.code
