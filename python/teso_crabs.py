import json
import subprocess
import time

import clipboard
import pyautogui
from PIL import Image
from notion.block import NumberedListBlock
from notion.block import HeaderBlock
from notion.block import TextBlock
from notion.client import NotionClient
from pynput import keyboard
from pynput.keyboard import Controller

key = Controller()

SAVE_FILE = "notion.json"


def create_file():
    with open(SAVE_FILE, "w") as f:
        json.dump({
            "notion": [],
            "login": "",
            "password": "",
            "secret": "secret_11KR5LWffeAbJYccYrBjlXDHmFcZZDB1UBm48Bq4qUo",
            "url": "https://www.notion.so/c53543c9d40a4a6ba298118038e87550",
            "database_id": "bd892a721a994e0598d5d5870910e688",
            "token_v2": "ae937ea231d9ab3ea4e0a5880822d8c15d0fd0a01f186c740c90905326fdcfa197b38cf0a2aeb015bcb3c8be6b18d9bd74501982fd75801998f55bb1a6d1c5eebfb7e838a92fe320222b05fa77b0",
            "title_name": "Marishka Test"
        }, f)


def save_data(d, filepath=None):
    if filepath is None:
        filepath = SAVE_FILE
    with open(filepath, "w") as f:
        json.dump(d, f)


def load_data(filepath=SAVE_FILE):
    try:
        with open(filepath, "r") as f:
            return json.loads(f.read())

    except FileNotFoundError:
        create_file()
        with open(filepath, "r") as f:
            return json.loads(f.read())


def on_activate_i():
    data = load_data()
    if paste() and data:
        if len(data["notion"]) > 0 and data["notion"][-1] == paste():
            send_message("This is the same text!")
        else:
            data["notion"].append(paste())
            save_data(data)
    else:
        send_message("No paste() or data")

    print("On Activate I")


def paste():
    text = clipboard.paste()
    return text


def print_content():
    print(load_data())


def push():
    data = load_data()
    client = NotionClient(
        token_v2="ae937ea231d9ab3ea4e0a5880822d8c15d0fd0a01f186c740c90905326fdcfa197b38cf0a2aeb015bcb3c8be6b18d9bd74501982fd75801998f55bb1a6d1c5eebfb7e838a92fe320222b05fa77b0")
    page = client.get_block("https://www.notion.so/c53543c9d40a4a6ba298118038e87550")
    if not data["notion"]:
        send_message("Списак пуст")
    else:
        header_one = pyautogui.prompt(text="Header", title="Enter H2")
        source = pyautogui.prompt(text="Введите искочник")
        page.children.add_new(HeaderBlock, title=f"{header_one}")
        page.children.add_new(TextBlock, title=f"Link: {source}")
        for i, el in enumerate(data["notion"]):
            print(f"{i + 1}.{el}")
            page.children.add_new(NumberedListBlock, title=el)
    data["notion"] = []
    save_data(data)


def send_message(message):
    subprocess.Popen(['notify-send', message])


def clear_paste():
    data = load_data()
    data["notion"] = []
    save_data(data)


# def insert_info():
#     data = load_data()
#     change = pyautogui.confirm("Что хотите изменить", buttons=["PAGE", "TOKEN", "Не хочу"])
#     if change == "TOKEN":
#         token = pyautogui.prompt("Token")
#         data["token_v2"] = token
#     elif change == "PAGE":
#         page = pyautogui.prompt("Page")
#         data["url"] = page
#     elif change == "Не хочу":
#         return None


def take_screenshot():
    print("Screenshot is taken")
    screenshot_name = pyautogui.prompt("Name you screen: ")
    time.sleep(0.5)
    pyautogui.screenshot(f"/home/nagual/Desktop/screenshots/{screenshot_name}.png")
    screenshot = Image.open(f"/home/nagual/Desktop/screenshots/{screenshot_name}.png")
    screenshot.show()


#
#
#


#


#

#
#
#
#
#
with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+i': push,
    '<ctrl>+<alt>+o': on_activate_i,
    '<ctrl>+<alt>+c': clear_paste
}) as h:
    h.join()
