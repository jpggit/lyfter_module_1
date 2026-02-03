import FreeSimpleGUI as sg
from finance_manager import FinanceManager
from models import TransactionType

INCOME = "income"
EXPENSE = "expense"


def run_app():
    manager = FinanceManager()
    manager.load()

    headings = ["Index", "Date", "Description", "Category", "Amount", "Type"]

    layout = [
        [sg.Text("Finance Tracker")],
        [sg.Text("Balance:"), sg.Text(str(manager.balance()), key="-BAL-")],

        [sg.Table(values=manager.table_rows(), headings=headings, key="-TABLE-", num_rows=10)],

        [
            sg.Button("Add Category"),
            sg.Button("Add Expense"),
            sg.Button("Add Income"),
            sg.Button("Delete Transaction"),
            sg.Button("Close Form"),
            sg.Button("Exit"),
        ],

        [sg.Text("New Category", key="-CAT_TITLE-", visible=False)],
        [
            sg.Text("Name", key="-CAT_NAME_LABEL-", visible=False),
            sg.Input(key="-CAT_NAME-", visible=False),
            sg.Button("Save Category", visible=False),
        ],

        [sg.Text("New Transaction", key="-TX_TITLE-", visible=False)],
        [
            sg.Text("Date", key="-DATE_LABEL-", visible=False),
            sg.Input(key="-DATE-", visible=False),
            sg.CalendarButton("Pick Date", target="-DATE-", format="%Y-%m-%d", visible=False, key="-CAL-"),
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
            sg.Combo(values=manager.category_names(), key="-CATEGORY-", readonly=True, visible=False),
        ],
        [sg.Button("Save Transaction", visible=False)],
    ]

    window = sg.Window("Finance App", layout)
    current_tx_type = None

    def hide_all_forms():
        window["-CAT_TITLE-"].update(visible=False)
        window["-CAT_NAME_LABEL-"].update(visible=False)
        window["-CAT_NAME-"].update(value="", visible=False)
        window["Save Category"].update(visible=False)

        window["-TX_TITLE-"].update(visible=False)
        window["-DATE_LABEL-"].update(visible=False)
        window["-DATE-"].update(value="", visible=False)
        window["-CAL-"].update(visible=False)
        window["-DESC_LABEL-"].update(visible=False)
        window["-DESC-"].update(value="", visible=False)
        window["-AMOUNT_LABEL-"].update(visible=False)
        window["-AMOUNT-"].update(value="", visible=False)
        window["-CATEGORY_LABEL-"].update(visible=False)
        window["-CATEGORY-"].update(value="", values=manager.category_names(), visible=False)
        window["Save Transaction"].update(visible=False)

    def refresh():
        window["-TABLE-"].update(values=manager.table_rows())
        window["-BAL-"].update(str(manager.balance()))

    def show_category_form():
        hide_all_forms()
        window["-CAT_TITLE-"].update(visible=True)
        window["-CAT_NAME_LABEL-"].update(visible=True)
        window["-CAT_NAME-"].update(visible=True)
        window["Save Category"].update(visible=True)

    def show_transaction_form(tx_type):
        hide_all_forms()
        if not manager.has_categories():
            sg.popup_error("You must create a category first.")
            return

        title = "New Expense" if tx_type == EXPENSE else "New Income"
        window["-TX_TITLE-"].update(title, visible=True)
        window["-DATE_LABEL-"].update(visible=True)
        window["-DATE-"].update(visible=True)
        window["-CAL-"].update(visible=True)
        window["-DESC_LABEL-"].update(visible=True)
        window["-DESC-"].update(visible=True)
        window["-AMOUNT_LABEL-"].update(visible=True)
        window["-AMOUNT-"].update(visible=True)
        window["-CATEGORY_LABEL-"].update(visible=True)
        window["-CATEGORY-"].update(values=manager.category_names(), visible=True)
        window["Save Transaction"].update(visible=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            manager.save()
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
                manager.add_category(values["-CAT_NAME-"])
                manager.save()
                hide_all_forms()
                refresh()
            except Exception as e:
                sg.popup_error(str(e))

        elif event == "Save Transaction":
            try:
                manager.add_transaction(
                    date_str=values["-DATE-"],
                    description=values["-DESC-"],
                    category_name=values["-CATEGORY-"],
                    amount_str=values["-AMOUNT-"],
                    type_str=current_tx_type,
                )
                manager.save()
                hide_all_forms()
                refresh()
            except Exception as e:
                sg.popup_error(str(e))

        elif event == "Delete Transaction":
            selected = values["-TABLE-"]
            if not selected:
                sg.popup_error("Please select a transaction to delete.")
                continue

            try:
                manager.delete_transaction(str(selected[0]))
                manager.save()
                refresh()
            except Exception as e:
                sg.popup_error(str(e))

    window.close()