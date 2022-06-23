#!/usr/bin/env python3
from selenium.common import TimeoutException
driver = None

def main():
    from sensitive_data import data
    import pyautogui
    import time
    import os
    import pyperclip
    import urllib3
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.common.by import By
    # geckodriver’ executable needs to be in PATH
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    def test_what_class_work():
        to_list = "CatalogBlock__itemsContainer _audio_pl"

        from_list = to_list.split(" ")
        print(from_list)
        return from_list

    def selenium(music="все будет хорошо", info=False):
        global driver
        if info:
            print("Selenium test function")

        else:
            try:
                os.environ['GH_TOKEN'] = data["GH_TOKEN"]
                service = Service(GeckoDriverManager().install())
                driver = webdriver.Firefox(service=service)
                url = "https://vk.com"
                driver.get(url)
                # "//*[ text() = 'Sign in' ]"
                sing_in_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".VkIdForm__form>:first-child")))
                sing_in_button.click()
                # Sign in end
                # Email input TextField
                login = driver.find_element(By.CSS_SELECTOR, ".vkc__TextField__input")
                login.send_keys(data["vk_login"])
                continue_button = driver.find_element(By.CSS_SELECTOR, ".vkc__Button__title")
                continue_button.click()
                pyautogui.write(data["vk_password"])
                continue_button2 = driver.find_element(By.CSS_SELECTOR, ".vkc__EnterPasswordNoUserInfo__buttonWrap")
                continue_button2.click()
                music_button_left = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#l_aud")))
                music_button_left.click()
                music_search_input = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#audio_search")))
                music_search_input.send_keys(music)
                time.sleep(10)
                # my_list = test_what_class_work()
                # for i, el in enumerate(my_list):
                #     top = driver.find_element(By.CSS_SELECTOR, f".{el}")
                #     print(f"{i}-{top.text}")
                #     print(f"Name:{my_list[i]}")
                #     print("====================>")
                first_child = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f".audio_page__audio_rows_list>:first-child")))
                first_child.click()
            except TimeoutException:
                print("TimeoutException")
                driver.close()
                change_keyboard_language()
                selenium()
            # >:first-child
            # choice = pyautogui.confirm(text="Exit", buttons=["exit", "stay"])
            # if choice == "exit":
            #     driver.close()

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

    def vk_find_first_artist(url="https://vk.com/"):
        http_pool = urllib3.connection_from_url(url)
        r = http_pool.urlopen('GET', url)
        file = open("write_in_here.html", "w")
        file.write(r.data.decode("utf-8"))

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

    # song = pyautogui.prompt(text="Введите музыку", title="Музыка", default="25/17")
    # if song is None:
    #     exit()
    # m = input("Песня или Артист:")
    m = pyautogui.prompt(text="Введите Песню или Артиста или Артиста и песню!", title="music_search", default="Новый вирус 25/17")
    change_keyboard_language()
    selenium(music=m)

    # time.sleep(1)
    # firefox(info=True)
    # vk(info=True)
    # time.sleep(2)
    # vk_music(sng=song, info=True)
    # next_music(info=True)
    # selenium()
    # os.system('spd-say "Finished"')
    restart = pyautogui.confirm(text="Program is finished!", title="Finished", buttons=['Restart', 'Exit'])
    if restart == "Restart":
        main()
    else:
        exit()


main()
