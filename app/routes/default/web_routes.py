from flask import Blueprint, render_template

# initialize blueprint
bp_default_web = Blueprint(
    name="default_web",
    import_name=__name__,
    template_folder="../../templates/default/",
    url_prefix="/",
)

posts = [
    {
        "author": "Corey Schafer",
        "titler": "Blog Post 1",
        "content": "First post Content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Corey Schafer",
        "titler": "Blog Post 1",
        "content": "First post Content",
        "date_posted": "April 20, 2018",
    },
]


@bp_default_web.route("/home")
@bp_default_web.route("/")
def home():
    return render_template("home.html")


@bp_default_web.route("/about")
def about():
    return render_template("about.html")
