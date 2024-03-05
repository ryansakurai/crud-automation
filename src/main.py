import time
import pyautogui as gui

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


def main():
    open_browser()
    open_website()


if __name__ == "__main__":
    main()
