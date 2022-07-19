import json
import time
import requests
import clipboard
import pyautogui
from PIL import Image
from pynput import keyboard
from pynput.keyboard import Controller
from notion.client import NotionClient
from notion.block import NumberedListBlock

key = Controller()

SAVE_FILE = "notion.json"


def save_data(d, filepath=None):
    if filepath is None:
        filepath = SAVE_FILE

    with open(filepath, "w") as f:
        json.dump(d, f)


def load_data(filepath=SAVE_FILE):
    try:
        with open(filepath, "r") as f:
            data = json.loads(f.read())
            return data
    except FileNotFoundError:
        save_data(filepath, paste())
        load_data(filepath)


def take_screenshot():
    print("Screenshot is taken")
    screenshot_name = pyautogui.prompt("Name you screen: ")
    time.sleep(0.5)
    pyautogui.screenshot(f"/home/nagual/Desktop/screenshots/{screenshot_name}.png")
    screenshot = Image.open(f"/home/nagual/Desktop/screenshots/{screenshot_name}.png")
    screenshot.show()


def paste():
    text = clipboard.paste()
    return text


def on_activate_i():
    data = load_data()
    if paste():
        data["notion"].append(paste())
        save_data(data)
    print("On Activate I")


def print_content():
    data = load_data()
    print(data)


def login(relog=None):
    if relog is None:
        re_log = pyautogui.confirm(text='Login', title='Login', buttons=['Login', 'Re-login'])
    else:
        re_log = "Re-login"
    if re_log == "Login":
        return load_data()["login"], load_data()["password"]
    elif re_log == "Re-login":
        log_in = pyautogui.prompt(text="Login", title="login")
        password = pyautogui.password(text='Password', title='password', default='', mask='☕')
        data = load_data()
        data["login"] = log_in
        data["password"] = password
        save_data(data)
        return load_data()["login"], load_data()["password"]


#
#
#
#
def push():
    data = load_data()
    if "title_name" in data:
        answer = pyautogui.confirm("Do you want to change you title?", buttons=["No", "Yes"])
        if answer == "Yes":
            title_name = pyautogui.prompt("Enter your new title: ")
            if title_name:
                data["title_name"] = title_name
            else:
                data["title_name"] = "None"
    else:
        title_name = pyautogui.prompt("Enter Title: ")
        data["title_name"] = title_name
    print(data)
    token = data["token_v2"]
    url = data["url"]
    client = NotionClient(token_v2=token)
    page = client.get_block(url)
    if data["notion"]:
        page.title = data["title_name"]
        for i, el in enumerate(data["notion"]):
            print(f"{i}. {el}")
            page.children.add_new(NumberedListBlock, title=f"{el}")
        data["notion"] = []
        save_data(data)
    else:
        print("List is mt")


#


#
#
#
# with open("page.txt", "w") as f:
#     f.write(page)
#
#
#
#
with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+i': push,
    '<ctrl>+<shift>+i': on_activate_i
}) as h:
    h.join()
