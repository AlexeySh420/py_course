import csv
import sqlite3

groceries = []

db = sqlite3.connect("groceries.db", check_same_thread=False)

db.row_factory = sqlite3.Row


class Groceries:
    def __init__(self, item, quantity, status):
        self.item = item
        self.quantity = quantity
        self.status = status

    @classmethod
    def get(cls):
        item = input("What would you like to purchase? ")
        quantity = input("How many? ")
        status = "to buy"

        db.execute(
            "INSERT INTO groceries(item, quantity, status) VALUES (?, ?, ?);",
            (item, quantity, status)
        )
        db.commit()

        with open("groceries.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["item", "quantity", "status"])
            writer.writerow({"item": item, "quantity": quantity, "status": status})

    @staticmethod
    def check():
        position = input("What item did you purchase? ")

        db.execute(
            "UPDATE groceries SET status = 'Checked' WHERE item = ?;",
            (position,)
        )
        db.commit()

        groceries.clear()

        with open("groceries.csv", "r") as file:
            reader = csv.DictReader(file)
            for cell in reader:
                if cell["item"] == position:
                    groceries.append({
                        "item": cell["item"],
                        "quantity": cell["quantity"],
                        "status": "Checked"
                    })
                else:
                    groceries.append(cell)

        with open("groceries.csv", "w", newline="") as change:
            writer = csv.DictWriter(change, fieldnames=["item", "quantity", "status"])
            writer.writeheader()
            writer.writerows(groceries)

    @staticmethod
    def remove():
        position = input("What item would you like to remove from the list? ")

        db.execute(
            "DELETE FROM groceries WHERE item = ?;",
            (position,)
        )
        db.commit()

        groceries.clear()

        with open("groceries.csv", "r") as file:
            reader = csv.DictReader(file)
            for cell in reader:
                if cell["item"] != position:
                    groceries.append(cell)

        with open("groceries.csv", "w", newline="") as change:
            writer = csv.DictWriter(change, fieldnames=["item", "quantity", "status"])
            writer.writeheader()
            writer.writerows(groceries)

    @staticmethod
    def list():
        rows = db.execute("SELECT * FROM groceries")

        for row in rows:
            print(row["quantity"], row["item"], row["status"])

    @staticmethod
    def csv():
        with open("groceries.csv", "r") as file:
            reader = csv.DictReader(file)
            for cell in reader:
                print(cell["quantity"], cell["item"], cell["status"])
