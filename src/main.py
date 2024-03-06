import time
import pyautogui as gui
import pandas as pd

WEBSITE_URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
CREDS = {
    "email": "mr.employee.man@gmail.com",
    "password": "strongpassword123"
}
TABLE_PATH = "resources/sample-products.csv"
SLEEP_TIME = 2

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
    gui.write("edge")
    gui.press("enter")

    time.sleep(SLEEP_TIME)

def open_website():
    gui.write(WEBSITE_URL)
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
    for _ in range(8):
        gui.hotkey("shift", "tab")


if __name__ == "__main__":
    main()
