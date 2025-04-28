from flask import Blueprint, render_template, request
from flask_login import login_required

from app.utils.models import Post

# initialize blueprint
bp_default_web = Blueprint(
    name="default_web",
    import_name=__name__,
    template_folder="../../templates/default/",
    url_prefix="/",
)


@bp_default_web.route("/home")
@bp_default_web.route("/")
@login_required
def home():
    page = request.args.get("page", default=1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=2, page=page)
    return render_template("home.html", posts=posts)


@bp_default_web.route("/test")
def test():
    params = dict(a=5, b=7)
    return render_template("test.html", title="Testing", **params)
