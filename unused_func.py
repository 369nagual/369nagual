import pyautogui
import time
import os
import pyperclip


def vk(info=False):
    if info is True:
        print("vk() ==>", end=" ")
        print("If you are in browser in new tab search for VK.COM and make zoom page 100%")
    elif info is False:
        time.sleep(1)
        pyautogui.keyDown("ctrl")
        pyautogui.press("t")
        pyautogui.keyUp("ctrl")
        pyautogui.keyDown("ctrl")
        pyautogui.press("l")
        pyautogui.keyUp("ctrl")
        pyautogui.write("vk.com")
        pyautogui.press("enter")
        pyautogui.click(x=1521, y=90)


def vk_music(sng="25/17", info=False):
    if info is True:
        print("vk_music() ==>", end=" ")
        print("If your browser is open you get open new tab and VK.COM on it and resize it to 100%")
    elif info is False:
        time.sleep(6)
        # 100%
        pyautogui.click(x=1521, y=90)
        pyautogui.press("esc")
        # 170%
        for i in range(5):
            pyautogui.keyDown("ctrl")
            pyautogui.press("+")
            pyautogui.keyUp("ctrl")
        # get music button
        exit_point(os.getcwd() + "/img/vk_music")
        time.sleep(2)
        # get search button
        exit_point(os.getcwd() + "/img/search_music")
        paste(sng)
        time.sleep(2)
        pyautogui.click(x=498, y=667)


def next_music():
    question = pyautogui.confirm(text="Сделующую песню?", title="Next?", buttons=["Да", "Нет"])
    if question == "Да":
        time.sleep(1)
        pyautogui.moveTo(x=558, y=265)
        pyautogui.click(x=558, y=266)
        time.sleep(5)
        next_music()
    else:
        return None


def firefox(info=False):
    if info is True:
        print("firefox() ==>", end=" ")
        print("It will open firefox")
    elif info is False:
        time.sleep(1)
        pyautogui.press("win")
        time.sleep(1)
        pyautogui.typewrite("firefox")
        time.sleep(1)
        pyautogui.press("enter")


def exit_point(path, info=False):
    if info is True:
        print("exit_point() ==>", end=" ")
        print("Matches list of images from path. If found: break")
    elif info is False:
        path_to_img = os.listdir(path)
        exit_locate = None
        for file in path_to_img:
            print(file)
            exit_locate = pyautogui.locateOnScreen(f"{path}/{file}")
            if exit_locate is None:
                continue
            else:
                break
        exit_p = pyautogui.center(exit_locate)
        a, b = exit_p
        pyautogui.click(a, b)


def paste(text, info=False):
    if info is True:
        print("paste() ==>", end=" ")
        print("Copying text and pasting it!")
    elif info is False:
        pyperclip.copy(text)
        pyautogui.keyDown("ctrl")
        pyautogui.press("v")
        pyautogui.keyUp("ctrl")


def change_keyboard_language(info=False):
    if info is True:
        print("change_keyboard_language() ==>", end=" ")
        print("Changes current keyboard language!")

    elif info is False:
        pyautogui.keyDown("win")
        pyautogui.press("space")
        time.sleep(.2)
        pyautogui.keyUp("win")
        time.sleep(1)
