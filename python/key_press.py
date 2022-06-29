#!/usr/bin/env python3
driver = None

a = 1
b = 2
c = 3


def main():
    from unused_func import change_keyboard_language
    from selenium.common import TimeoutException
    import pyautogui
    import os
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.common.by import By
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from database import data

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
                sing_in_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".VkIdForm__form>:first-child")))
                sing_in_button.click()
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
                first_child = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, f".audio_page__audio_rows_list>:first-child")))
                first_child.click()
            except TimeoutException:
                driver.close()
                change_keyboard_language()
                selenium(music)

    m = pyautogui.prompt(text="Введите Песню или Артиста или Артиста и песню!", title="music_search",
                         default="Новый вирус 25/17")
    list_of_char = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
                    'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    for letter in m:
        if letter in list_of_char is None:
            change_keyboard_language()
            break
    selenium(music=m)


if __name__ == "__main__":
    main()
