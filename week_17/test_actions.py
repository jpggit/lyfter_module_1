import pytest
from datetime import date

from actions import (
    add_category,
    add_transaction,
    delete_transaction,
    update_transaction,
    list_transactions,
    list_category_names,
)

from models import Category, TransactionType

# -------------------------
# Helpers for tests
# -------------------------
def make_categories():
    return [Category("Food"), Category("Housing")]

def make_transactions():
    return []

INCOME_STR = "income"
EXPENSE_STR = "expense"

# -------------------------
# Category tests (2)
# -------------------------
def test_add_category_adds_new_category():
    categories = []
    add_category(categories, "Food")
    assert len(categories) == 1
    assert categories[0].name == "Food"


def test_add_category_rejects_duplicate_case_insensitive():
    categories = [Category("Food")]
    with pytest.raises(ValueError, match="already exists"):
        add_category(categories, "  food  ")


# -------------------------
# Transaction tests (5)
# -------------------------
def test_add_transaction_requires_existing_category():
    categories = [Category("Food")]
    transactions = []

    # Category called "Transport" does not exist
    with pytest.raises(ValueError, match="does not exist"):
        add_transaction(
            transactions, categories,
            "2024-01-01", "Bus", "Transport", "10", EXPENSE_STR
        )


def test_add_transaction_converts_and_sets_expense_negative():
    categories = make_categories()
    transactions = make_transactions()

    add_transaction(
        transactions, categories,
        "2024-01-02", "Groceries", "Food", "25", EXPENSE_STR
    )

    assert len(transactions) == 1
    tx = transactions[0]
    assert tx.amount < 0  # should be negative
    assert tx.tx_type == TransactionType.EXPENSE


def test_add_transaction_converts_and_sets_income_positive():
    categories = make_categories()
    transactions = make_transactions()

    add_transaction(
        transactions, categories,
        "2024-01-03", "Salary", "Housing", "1000", INCOME_STR
    )

    assert len(transactions) == 1
    tx = transactions[0]
    assert tx.amount > 0  # should be positive
    assert tx.tx_type == TransactionType.INCOME


def test_add_transaction_rejects_bad_date_format():
    categories = make_categories()
    transactions = make_transactions()

    with pytest.raises(ValueError, match="YYYY-MM-DD"):
        add_transaction(
            transactions, categories,
            "01-03-2024", "Salary", "Housing", "1000", INCOME_STR
        )

def test_add_transaction_rejects_empty_description():
    categories = [Category("Food")]
    transactions = []

    with pytest.raises(ValueError, match="Description cannot be empty"):
        add_transaction(
            transactions, categories,
            "2024-01-01", "", "Food", "10", "expense"
        )

# -------------------------
# Delete tests (3)
# -------------------------
def test_delete_transaction_removes_item():
    categories = make_categories()
    transactions = make_transactions()

    add_transaction(transactions, categories, "2024-01-01", "Groceries", "Food", "10", EXPENSE_STR)
    add_transaction(transactions, categories, "2024-01-02", "Rent", "Housing", "500", EXPENSE_STR)

    delete_transaction(transactions, "0")

    assert len(transactions) == 1
    assert transactions[0].description == "Rent"

def test_delete_transaction_rejects_out_of_range_index():
    categories = [Category("Food")]
    transactions = []

    add_transaction(
        transactions, categories,
        "2024-01-01", "Groceries", "Food", "10", "expense"
    )

    with pytest.raises(ValueError, match="out of range"):
        delete_transaction(transactions, "5")