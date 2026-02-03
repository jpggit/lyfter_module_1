from models import Category, Transaction, TransactionType
from data import load_categories, load_transactions, save_categories, save_transactions
from validators import normalize_text, parse_date, parse_amount, parse_index


class FinanceManager:
    def __init__(self):
        self.categories = []
        self.transactions = []

    # ----- Persistence -----
    def load(self):
        self.categories = load_categories()
        self.transactions = load_transactions()

    def save(self):
        save_categories(self.categories)
        save_transactions(self.transactions)

    # ----- Categories -----
    def add_category(self, name: str):
        normalized = normalize_text(name, "Category name").lower()
        existing = {c.name.strip().lower() for c in self.categories}
        if normalized in existing:
            raise ValueError("Category already exists")

        self.categories.append(Category(name=name.strip()))

    def category_names(self):
        return sorted(cat.name for cat in self.categories)

    def has_categories(self) -> bool:
        return len(self.categories) > 0

    # ----- Transactions -----
    def _require_category_exists(self, category_name: str) -> str:
        cat_name = normalize_text(category_name, "Category")
        existing = {c.name.strip().lower() for c in self.categories}
        if cat_name.lower() not in existing:
            raise ValueError("Category does not exist, create Category first")
        return cat_name

    def add_transaction(self, date_str, description, category_name, amount_str, type_str):
        if not self.categories:
            raise ValueError("No categories available. Create a category first.")

        tx_date = parse_date(date_str)
        desc = normalize_text(description, "Description")
        cat_name = self._require_category_exists(category_name)
        amount = parse_amount(amount_str)

        tx_type = TransactionType((type_str or "").strip().lower())

        # Business rule: user inputs positive, we enforce sign
        if tx_type == TransactionType.EXPENSE:
            amount = -abs(amount)
        else:
            amount = abs(amount)

        self.transactions.append(
            Transaction(
                tx_date=tx_date,
                description=desc,
                category=cat_name,
                amount=amount,
                tx_type=tx_type,
            )
        )

    def delete_transaction(self, index_str):
        index = parse_index(index_str)
        if index < 0 or index >= len(self.transactions):
            raise ValueError("Index entered out of range.")
        del self.transactions[index]

    def update_transaction(self, index_str, date_str, description, category_name, amount_str, type_str):
        index = parse_index(index_str)
        if index < 0 or index >= len(self.transactions):
            raise ValueError("Index entered out of range.")

        tx_date = parse_date(date_str)
        desc = normalize_text(description, "Description")
        cat_name = self._require_category_exists(category_name)
        amount = parse_amount(amount_str)

        tx_type = TransactionType((type_str or "").strip().lower())

        if tx_type == TransactionType.EXPENSE:
            amount = -abs(amount)
        else:
            amount = abs(amount)

        self.transactions[index] = Transaction(
            tx_date=tx_date,
            description=desc,
            category=cat_name,
            amount=amount,
            tx_type=tx_type,
        )

    # ----- Presentation helpers (for GUI table) -----
    def table_rows(self):
        rows = []
        for i, tx in enumerate(self.transactions):
            rows.append([
                i,
                tx.tx_date.isoformat(),
                tx.description,
                tx.category,
                tx.amount,
                tx.tx_type.value,
            ])
        return rows

    def balance(self):
        return sum(tx.amount for tx in self.transactions)