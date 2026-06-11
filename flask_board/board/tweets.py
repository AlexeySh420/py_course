from flask import (
    Blueprint,
    render_template,
    request,
)

from board.database import get_db

bp = Blueprint("tweets", __name__)


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        content = request.form["content"]

        if content:
            db = get_db()
            db.execute(
                "INSERT INTO tweet (author, content) VALUES (?, ?)",
                (author, content),
            )
            db.commit()

    return render_template("tweets/create.html")


@bp.route("/tweets")
def tweets():
    db = get_db()
    tweets = db.execute(
        "SELECT author, content, created FROM tweet ORDER BY created DESC"
    ).fetchall()
    return render_template("tweets/tweets.html", tweets=tweets)
