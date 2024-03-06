import time
import pyautogui as gui
import pandas as pd

WEBSITE_URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
TABLE_PATH = "resources/produtos.csv"

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
    time.sleep(1)
    gui.write("edge")
    gui.press("enter")

    time.sleep(3)

def open_website():
    gui.write(WEBSITE_URL)
    gui.press("enter")

    time.sleep(3)

def log_in():
    gui.press("tab")
    gui.write("mr.employee.man@gmail.com")
    gui.press("tab")
    gui.write("strongpassword123")
    gui.press("tab")
    gui.press("enter")

    time.sleep(3)

def register_product(table: pd.DataFrame, prod_line: int):
    for column in table.columns:
        gui.press("tab")

        value: any = table.loc[prod_line, column]
        if not pd.isna(value):
            gui.write(str(value))

    for _ in range(2):
        gui.press("tab")
        gui.press("enter")

def rollback():
    for _ in range(9):
        gui.hotkey("shift", "tab")


if __name__ == "__main__":
    main()
