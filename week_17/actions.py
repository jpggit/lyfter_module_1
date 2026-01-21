from datetime import datetime
from models import Category, Transaction, TransactionType
from data import (
    load_transactions,
    save_transactions,
    load_categories,
    save_categories,
)

# -----------------------------------------------
# Load / Save of all transactions and categories
# -----------------------------------------------
def load_all():
    categories = load_categories()
    transactions = load_transactions()
    return categories, transactions

def save_all(categories, transactions):
    save_categories(categories)
    save_transactions(transactions)
    return True

# -----------------------------------------------
# Add a categories
# -----------------------------------------------

def add_category (categories, name):
    normalized = name.strip().lower()
    if not normalized:
        raise ValueError("Category name cannot be empty.")
    if normalized in {c.name.strip().lower() for c in categories}:
        raise ValueError("Category already exists")
    
    new_cat = Category(name)
    categories.append(new_cat)
    return categories

# -----------------------------------------------
# Transactions
# -----------------------------------------------

def add_transaction(transactions, categories, date_str, description, category_name, amount_str, type_str):

    ### Normalize and validate all data types
    cat_name = category_name.strip()
    if not cat_name:
        raise ValueError ("Category cannot be empty.")

    existing_cat_names = {c.name.strip().lower() for c in categories}
    if cat_name.lower() not in existing_cat_names:
        raise ValueError("Category does not exist, create Category first")

    ###Validate date format (from googling - need to learn more)
    try:
        tx_date = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")
    
    desc = description.strip()
    if not desc:
        raise ValueError("Description cannot be empty.")

    try:
        amount = float(amount_str)
    except ValueError:
        raise ValueError("Amount must be a number.")

    type_normalized = type_str.strip().lower()
    try:
        tx_type = TransactionType(type_normalized)
    except ValueError:
        raise ValueError("Type must be 'income' or 'expense'.")
    
    if tx_type == TransactionType.EXPENSE: #Turn number to a negative for expenses
        amount = -abs(amount)
    else:
        amount = abs(amount)
    ### ------------------------------------

    tx = Transaction(
        tx_date = tx_date,
        description = desc,
        category = cat_name,
        amount = amount,
        tx_type = tx_type
    )

    transactions.append(tx)
    return transactions

def delete_transaction(transactions, index_str):
    #validate index provided
    try:
        index = int(index_str.strip())
    except ValueError:
        raise ValueError("Index must be a number.")
    
    if index < 0 or index >=len(transactions):
        raise ValueError("Index entered out of range.")
    
    del transactions[index]
    return transactions


def update_transaction(transactions, index_str, categories, date_str, description, category_name, amount_str, type_str) :
    #validate index provided
    try:
        index = int(index_str.strip())
    except ValueError:
        raise ValueError("Index must be a number.")
    
    if index < 0 or index >=len(transactions):
        raise ValueError("Index entered out of range.")
    
    ### Normalize and validate all data types
    cat_name = category_name.strip()
    if not cat_name:
        raise ValueError ("Category cannot be empty.")

    existing_cat_names = {c.name.strip().lower() for c in categories}
    if cat_name.lower() not in existing_cat_names:
        raise ValueError("Category does not exist, create Category first")

    ###Validate date format (from googling - need to learn more)
    try:
        tx_date = datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")
    
    desc = description.strip()
    if not desc:
        raise ValueError("Description cannot be empty.")

    try:
        amount = float(amount_str)
    except ValueError:
        raise ValueError("Amount must be a number.")

    type_normalized = type_str.strip().lower()
    try:
        tx_type = TransactionType(type_normalized)
    except ValueError:
        raise ValueError("Type must be 'income' or 'expense'.")
    ### ------------------------------------

    tx = Transaction(
        tx_date = tx_date,
        description = desc,
        category = cat_name,
        amount = amount,
        tx_type = tx_type
    )

    transactions[index] = tx
    return transactions


### List transcations
def list_transactions(transactions):
    rows = []
    for i, tx in enumerate(transactions):
        row = [
            i,
            tx.tx_date.isoformat(),
            tx.description,
            tx.category,
            tx.amount,
            tx.tx_type.value,
        ]
        rows.append(row)
    return rows

### List categories for dropdown
def list_category_names(categories):
    return sorted(cat.name for cat in categories)