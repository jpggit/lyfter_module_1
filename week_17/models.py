from dataclasses import dataclass
from datetime import date
from enum import Enum


###---------------------------------------------
### Define the Category class of a transaction
###---------------------------------------------
@dataclass (frozen = True)
class Category:
    name: str

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError ("Category cannot be empty.")


###---------------------------------------------
### Enumerate the possible transaction types
###---------------------------------------------
class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


###---------------------------------------------
### Define the Transaction class
###---------------------------------------------
@dataclass (frozen = True)
class Transaction:
    tx_date: date
    description: str
    category: str
    amount: float
    tx_type: TransactionType

    def __post_init__(self):
        if not self.category or not self.category.strip():
            raise ValueError ("Category cannot be empty.")
        if not isinstance (self.amount, (int, float)):
            raise ValueError ("Amount must be a number.")
        if self.amount == 0:
            raise ValueError ("Transaction amount cannot be Zero.")
        if self.amount > 0 and self.tx_type == TransactionType.EXPENSE:
            raise ValueError("Expense must be negative.")
        if self.amount < 0 and self.tx_type == TransactionType.INCOME:
            raise ValueError("Income must be positive.")

    def to_dict(self):
        return {
            "date": self.tx_date.isoformat(), #isoformat = built-in python method to standardize the output on CSV output
            "description": self.description,
            "category": self.category,
            "amount": f"{self.amount:.2f}", #:.2f -> to format as 2 decimal float
            "type": self.tx_type.value, #use .value bc tx_type is an Enum, and must extract the string value
        }

    @staticmethod #we use static method because we do not need to call an instance
    def from_dict(row: dict): 
        tx_type_str = (row.get("type", "") or "").strip().lower() # "" and .strip() to remove all empty or spacing errors

        if tx_type_str == "income":
            tx_type = TransactionType.INCOME
        elif tx_type_str == "expense":
            tx_type = TransactionType.EXPENSE
        else:
            raise ValueError (f"Invalid transaction type: {tx_type_str}")

        return Transaction(
            tx_date = date.fromisoformat(row["date"]), #converts to date
            description = row.get("description", ""), #make optional in case it's empty
            category = row.get("category"),
            amount = float(row["amount"]), #convert str to float
            tx_type=tx_type #we already converted this earlier to make sure it's either INCOME or EXPENSE
        )
