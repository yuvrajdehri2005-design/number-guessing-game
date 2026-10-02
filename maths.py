import json
import os

FILE = "expenses.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add(data):
    name = input("Kis cheez ka kharcha? ")
    try:
        amount = float(input("Kitna? "))
    except ValueError:
        print("Number daalo!")
        return
    data.append({"name": name, "amount": amount})
    save(data)
    print("Add ho gaya!")

def show(data):
    if not data:
        print("Abhi kuch nahi hai.")
        return
    for i, item in enumerate(data, 1):
        print(f"{i}. {item['name']} - Rs {item['amount']}")
    total = sum(item["amount"] for item in data)
    print(f"Total: Rs {total}")

def delete(data):
    show(data)
    try:
        n = int(input("Kaunsa number delete karna hai? "))
        if 1 <= n <= len(data):
            data.pop(n - 1)
            save(data)
            print("Delete ho gaya!")
        else:
            print("Aisa number list mein nahi hai.")
    except ValueError:
        print("Number daalo!")

def main():
    data = load()
    while True:
        print("\n1. Add  2. Show  3. Delete  4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add(data)
        elif choice == "2":
            show(data)
        elif choice == "3":
            delete(data)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Galat option!")

main()






