from flask import Blueprint

# initialize blueprint
bp_default_web = Blueprint(
    name="default_web",
    import_name=__name__,
    template_folder="../../templates/default/",
    url_prefix="/",
)


@bp_default_web.route("/home")
@bp_default_web.route("/")
def home():
    return "<h1>Hello, Flask!</h1>"


@bp_default_web.route("/about")
def about():
    return "<h1>About Page</h1>"
