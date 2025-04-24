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
        "author": "Jane Doe",
        "title": "Exploring the Mountains",
        "content": "Had an amazing experience hiking through the Rockies!",
        "date_posted": "March 14, 2022",
    },
    {
        "author": "John Smith",
        "title": "The Future of AI",
        "content": "Artificial Intelligence is changing the world at an unprecedented pace.",
        "date_posted": "June 3, 2023",
    },
    {
        "author": "Alicia Keys",
        "title": "Music and Mindfulness",
        "content": "Combining meditation with music can elevate your daily practice.",
        "date_posted": "January 22, 2021",
    },
    {
        "author": "Brian Cox",
        "title": "Black Holes and Beyond",
        "content": "Discussing the latest theories on black holes and quantum gravity.",
        "date_posted": "August 30, 2020",
    },
    {
        "author": "Samantha Lee",
        "title": "Digital Nomad Life",
        "content": "Tips and tools for working remotely while traveling the world.",
        "date_posted": "October 11, 2023",
    },
]


@bp_default_web.route("/home")
@bp_default_web.route("/")
def home():
    return render_template("home.html", posts=posts)


@bp_default_web.route("/about")
def about():
    return render_template("about.html", title="About")
