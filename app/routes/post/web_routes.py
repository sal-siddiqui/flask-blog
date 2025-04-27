from datetime import datetime
from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user

from app.extensions import db
from app.utils.forms import PostForm
from app.utils.models import Post

bp_post_web = Blueprint(
    name="post_web",
    import_name=__name__,
    template_folder="../../templates/post/",
    url_prefix="/post/",
)


@bp_post_web.route("/new", methods=["GET", "POST"])
def new_post():
    form = PostForm()

    # -- Handle GET Request
    if request.method == "GET":
        return render_template("post-form.html", title="New Post", form=form, zip=zip)

    # -- Handle POST Request
    if not form.validate_on_submit():
        flash("Error submitting form. Please check the fields and try again.", category="danger")
        return render_template("post-form.html", title="New Post", form=form, zip=zip)

    # create post
    post = Post(
        title=form.title.data,
        content=form.content.data,
        date_posted=datetime.now(),
        author=current_user,
    )
    db.session.add(post)
    db.session.commit()

    flash(f"Post '<b>{form.title.data}</b>' created successfully.", category="success")
    return redirect(url_for("default_web.home"))


@bp_post_web.route("/<int:post_id>")
def post_page(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        abort(404)
    return render_template("single-post.html", title=post.title, post=post)
