groceries = []

def main():

    print("\nGroceries \nCommands: add, check, remove, list, exit")

    while True:
        command = input("\nCommand: ").strip().lower()

        if command == "add":
            add_item()
        elif command == "check":
            check_item()
        elif command == "remove":
            remove_item()
        elif command == "list":
            list_items()
        elif command == "exit":
            print("Goodbye.")
            break
        else:
            print("Unknown command.")

def add_item():
    item = input("Item: ")
    quantity = input("Quantity: ")

    groceries.append({
        "item": item,
        "quantity": quantity,
        "status": "to buy"
    })

    print(f"Added {quantity} {item}.")


def check_item():
    name = input("Which item did you purchase? ")

    for g in groceries:
        if g["item"] == name:
            g["status"] = "Checked"
            print(f"Marked {name} as purchased.")
            return

    print(f"{name} not found.")


def remove_item():
    name = input("Which item do you want to remove? ")

    for g in groceries:
        if g["item"] == name:
            groceries.remove(g)
            print(f"Removed {name}.")
            return

    print(f"{name} not found.")


def list_items():
    if not groceries:
        print("Your list is empty.")
        return

    print("\nGrocery List:")
    for g in groceries:
        print(f"{g['quantity']} {g['item']} — {g['status']}")
    print()



if __name__ == "__main__":
    main()
    