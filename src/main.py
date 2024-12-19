import time
import pyautogui as gui
import pandas as pd
import os

SLEEP_TIME = 3
BROWSER = "edge"
current_dir = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(current_dir, "../resources/dummy-app/login.html")
CREDS = {
    "email": "mr.employee.man@gmail.com",
    "password": "strongpassword123"
}
TABLE_PATH = "resources/spreadsheets/sample-products.csv"

def main():
    open_browser()
    open_website()
    log_in()

    table: pd.DataFrame = pd.read_csv(TABLE_PATH)

    for line in table.index:
        register_product(table, line)
        rollback()

def open_browser():
    gui.press("win")
    time.sleep(SLEEP_TIME)
    gui.write(BROWSER)
    gui.press("enter")

    time.sleep(SLEEP_TIME)

def open_website():
    gui.write(app_path)
    gui.press("enter")

    time.sleep(SLEEP_TIME)

def log_in():
    gui.press("tab")
    gui.write(CREDS["email"])
    gui.press("tab")
    gui.write(CREDS["password"])
    gui.press("tab")
    gui.press("enter")

    time.sleep(SLEEP_TIME)

def register_product(table: pd.DataFrame, prod_line: int):
    for column in table.columns:
        gui.press("tab")

        value: any = table.loc[prod_line, column]
        if not pd.isna(value):
            gui.write(str(value))

    gui.press("tab")
    gui.press("enter")

def rollback():
    # it'd probably be faster using scroll and click
    for _ in range(8):
        gui.hotkey("shift", "tab")


if __name__ == "__main__":
    main()
