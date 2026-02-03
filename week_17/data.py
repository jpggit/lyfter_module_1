import csv
from models import Transaction, Category

#all caps = constant
TRANSACTIONS_FILE = "data/transactions.csv" 
CATEGORIES_FILE = "data/categories.csv"

TRANSACTION_FIELDS = ["date", "description", "category", "amount", "type"]
CATEGORY_FIELDS = ["name"]


# -----------------------------
# Transactions
# -----------------------------
def load_transactions():
    transactions = []
    try: 
        with open (TRANSACTIONS_FILE, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                transactions.append(Transaction.from_dict(row))
    except FileNotFoundError:
        # If file does not exist yet then no transactions have been done yet
        pass

    return transactions

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TRANSACTION_FIELDS)
        writer.writeheader()
        for tx in transactions:
            writer.writerow(tx.to_dict())


# -----------------------------
# Categories
# -----------------------------
def load_categories():
    categories = []

    try:
        with open(CATEGORIES_FILE, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = (row.get("name", "") or "").strip()
                if name:
                    categories.append(Category(name=name))
    except FileNotFoundError:
        # File does not exist yet == no categories
        pass

    return categories


def save_categories(categories):
    with open(CATEGORIES_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CATEGORY_FIELDS)
        writer.writeheader()
        for cat in categories:
            writer.writerow({"name": cat.name})

