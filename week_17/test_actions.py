import pytest
from models import Category, TransactionType
from finance_manager import FinanceManager


def make_manager_with_categories():
    m = FinanceManager()
    m.categories = [Category("Food"), Category("Housing")]
    m.transactions = []
    return m


# -------------------------
# Category tests (2)
# -------------------------
def test_manager_add_category_adds_new_category():
    m = FinanceManager()
    m.add_category("Food")
    assert [c.name for c in m.categories] == ["Food"]


def test_manager_add_category_rejects_duplicates_case_insensitive():
    m = FinanceManager()
    m.categories = [Category("Food")]
    with pytest.raises(ValueError, match="already exists"):
        m.add_category("  food  ")


# -------------------------
# Transaction tests (4)
# -------------------------
def test_manager_add_transaction_requires_existing_category():
    m = FinanceManager()
    m.categories = [Category("Food")]

    with pytest.raises(ValueError, match="does not exist"):
        m.add_transaction("2024-01-01", "Bus", "Transport", "10", "expense")


def test_manager_add_transaction_sets_expense_negative():
    m = make_manager_with_categories()
    m.add_transaction("2024-01-02", "Groceries", "Food", "25", "expense")

    assert len(m.transactions) == 1
    tx = m.transactions[0]
    assert tx.tx_type == TransactionType.EXPENSE
    assert tx.amount < 0


def test_manager_add_transaction_sets_income_positive():
    m = make_manager_with_categories()
    m.add_transaction("2024-01-03", "Salary", "Housing", "1000", "income")

    tx = m.transactions[0]
    assert tx.tx_type == TransactionType.INCOME
    assert tx.amount > 0


def test_manager_add_transaction_rejects_bad_date():
    m = make_manager_with_categories()
    with pytest.raises(ValueError, match="YYYY-MM-DD"):
        m.add_transaction("01-03-2024", "Salary", "Housing", "1000", "income")


# -------------------------
# Delete tests (2)
# -------------------------
def test_manager_delete_transaction_removes_item():
    m = make_manager_with_categories()
    m.add_transaction("2024-01-01", "Groceries", "Food", "10", "expense")
    m.add_transaction("2024-01-02", "Rent", "Housing", "500", "expense")

    m.delete_transaction("0")

    assert len(m.transactions) == 1
    assert m.transactions[0].description == "Rent"


def test_manager_delete_transaction_rejects_out_of_range():
    m = make_manager_with_categories()
    m.add_transaction("2024-01-01", "Groceries", "Food", "10", "expense")

    with pytest.raises(ValueError, match="out of range"):
        m.delete_transaction("5")