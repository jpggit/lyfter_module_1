import FreeSimpleGUI as sg

from actions import (
    load_all,
    save_all,
    add_category,
    add_transaction,
    delete_transaction,
    list_transactions,
    list_category_names,
)

INCOME = "income"
EXPENSE = "expense"

# ------------------------
# Load data on start
# ------------------------
categories, transactions = load_all()

# ------------------------
# Layout
# ------------------------
headings = ["Index", "Date", "Description", "Category", "Amount", "Type"]

layout = [
    [sg.Text("Finance Tracker")],

    # Table
    [
        sg.Table(
            values=list_transactions(transactions),
            headings=headings,
            key="-TABLE-",
            auto_size_columns=True,
            justification="left",
            num_rows=10,
        )
    ],

    # Main buttons
    [
        sg.Button("Add Category"),
        sg.Button("Add Expense"),
        sg.Button("Add Income"),
        sg.Button("Delete Transaction"),
        sg.Button("Close Form"),
        sg.Button("Exit"),
    ],

    # --- Category form area (simple show/hide) ---
    [sg.Text("New Category", key="-CAT_TITLE-", visible=False)],
    [
        sg.Text("Name", key="-CAT_NAME_LABEL-", visible=False),
        sg.Input(key="-CAT_NAME-", visible=False),
        sg.Button("Save Category", visible=False),
    ],

    # --- Transaction form area (simple show/hide) ---
    [sg.Text("New Transaction", key="-TX_TITLE-", visible=False)],
    [
        sg.Text("Date (YYYY-MM-DD)", key="-DATE_LABEL-", visible=False),
        sg.Input(key="-DATE-", visible=False),
    ],
    [
        sg.Text("Title", key="-DESC_LABEL-", visible=False),
        sg.Input(key="-DESC-", visible=False),
    ],
    [
        sg.Text("Amount", key="-AMOUNT_LABEL-", visible=False),
        sg.Input(key="-AMOUNT-", visible=False),
    ],
    [
        sg.Text("Category", key="-CATEGORY_LABEL-", visible=False),
        sg.Combo(values=list_category_names(categories), key="-CATEGORY-", readonly=True, visible=False),
    ],
    [sg.Button("Save Transaction", visible=False)],
]

window = sg.Window("Finance App", layout)

# Track what kind of transaction we’re adding: "income" or "expense"
current_tx_type = None


def hide_all_forms():
    # Category form
    window["-CAT_TITLE-"].update(visible=False)
    window["-CAT_NAME_LABEL-"].update(visible=False)
    window["-CAT_NAME-"].update(value="", visible=False)
    window["Save Category"].update(visible=False)

    # Transaction form
    window["-TX_TITLE-"].update(visible=False)
    window["-DATE_LABEL-"].update(visible=False)
    window["-DATE-"].update(value="", visible=False)
    window["-DESC_LABEL-"].update(visible=False)
    window["-DESC-"].update(value="", visible=False)
    window["-AMOUNT_LABEL-"].update(visible=False)
    window["-AMOUNT-"].update(value="", visible=False)
    window["-CATEGORY_LABEL-"].update(visible=False)
    window["-CATEGORY-"].update(value="", values=list_category_names(categories), visible=False)
    window["Save Transaction"].update(visible=False)


def show_category_form():
    hide_all_forms()
    window["-CAT_TITLE-"].update(visible=True)
    window["-CAT_NAME_LABEL-"].update(visible=True)
    window["-CAT_NAME-"].update(visible=True)
    window["Save Category"].update(visible=True)


def show_transaction_form(tx_type):
    hide_all_forms()

    # Requirement: show error if no categories exist
    if not categories:
        sg.popup_error("You must create a category first.")
        return False

    title = "New Expense" if tx_type == EXPENSE else "New Income"
    window["-TX_TITLE-"].update(title, visible=True)

    window["-DATE_LABEL-"].update(visible=True)
    window["-DATE-"].update(visible=True)

    window["-DESC_LABEL-"].update(visible=True)
    window["-DESC-"].update(visible=True)

    window["-AMOUNT_LABEL-"].update(visible=True)
    window["-AMOUNT-"].update(visible=True)

    window["-CATEGORY_LABEL-"].update(visible=True)
    window["-CATEGORY-"].update(values=list_category_names(categories), visible=True)

    window["Save Transaction"].update(visible=True)
    return True


def refresh_table():
    window["-TABLE-"].update(values=list_transactions(transactions))


# ------------------------
# Event loop (lesson style)
# ------------------------
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        # Requirement: save on close
        save_all(categories, transactions)
        break

    elif event == "Add Category":
        current_tx_type = None
        show_category_form()

    elif event == "Add Expense":
        current_tx_type = EXPENSE
        show_transaction_form(EXPENSE)

    elif event == "Add Income":
        current_tx_type = INCOME
        show_transaction_form(INCOME)

    elif event == "Close Form":
        current_tx_type = None
        hide_all_forms()

    elif event == "Save Category":
        try:
            add_category(categories, values["-CAT_NAME-"])
            save_all(categories, transactions)  # save on change
            hide_all_forms()
            refresh_table()
        except Exception as e:
            sg.popup_error(str(e))

    elif event == "Save Transaction":
        try:
            add_transaction(
                transactions=transactions,
                categories=categories,
                date_str=values["-DATE-"],
                description=values["-DESC-"],
                category_name=values["-CATEGORY-"],
                amount_str=values["-AMOUNT-"],
                type_str=current_tx_type,  # "income" / "expense"
            )
            save_all(categories, transactions)  # save on change
            hide_all_forms()
            refresh_table()
        except Exception as e:
            sg.popup_error(str(e))

    elif event == "Delete Transaction":
        selected = values["-TABLE-"]

        if not selected:
            sg.popup_error("Please select a transaction to delete.")
            continue

        index = selected[0]  # table returns a list of selected row indexes

        try:
            delete_transaction(transactions, str(index))
            save_all(categories, transactions)
            refresh_table()
        except Exception as e:
            sg.popup_error(str(e))

window.close()