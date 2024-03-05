import time
import pyautogui as gui

def main():
    open_browser()
    open_website()
    log_in()

def open_browser():
    gui.press("win")
    time.sleep(1)
    gui.write("edge")
    gui.press("enter")

    time.sleep(3)

def open_website():
    gui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
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


if __name__ == "__main__":
    main()
