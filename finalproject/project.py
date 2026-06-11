import sys

from .groceries_class import Groceries, db

# from groceries_class import Groceries, db  # Terminal
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


def main():
    if len(sys.argv) == 1:
        while True:
            try:
                Groceries.get()
            except EOFError:
                print("\n")
                Groceries.list()
                sys.exit()

    check_item()
    delete_item()
    list_item()
    csv_item()


def check_item():
    if sys.argv[1] == "check":
        Groceries.check()


def delete_item():
    if sys.argv[1] == "delete":
        Groceries.remove()


def list_item():
    if sys.argv[1] == "list":
        Groceries.list()


def csv_item():
    if sys.argv[1] == "csv":
        Groceries.csv()
    main()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        item = request.form.get("item")
        quantity = request.form.get("quantity")

        if request.form.get("action") == "add":
            db.execute(
                "INSERT INTO groceries(item, quantity, status) VALUES (?, ?, 'to buy');",
                (item, quantity)
            )
            db.commit()

        elif request.form.get("action") == "check":
            db.execute(
                "UPDATE groceries SET status = 'Checked' WHERE item = ?;",
                (item,)
            )
            db.commit()

        elif request.form.get("action") == "remove":
            db.execute(
                "DELETE FROM groceries WHERE item = ?;",
                (item,)
            )
            db.commit()

    return "", 204



@app.route("/list")
def list():
    rows = db.execute(f"SELECT * FROM groceries")
    return render_template("list.html", rows=rows)


# if __name__ == "__main__":
#   app.run()
