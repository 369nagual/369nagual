#!/usr/bin/python3.10
from PIL import Image
import sys
import pyautogui

photo_url = '/home/nagual/PycharmProjects/pythonProject/selenium/Photo_cards'
if len(sys.argv) >= 2:
    hundreds = str(sys.argv[1])
else:
    hundreds = str(pyautogui.prompt('Please enter your'))

if len(hundreds) < 3:
    if len(hundreds) < 2:
        if hundreds == '0':
            card = Image.open(f"{photo_url}/00-99/0.jpg")
        else:
            card = Image.open(f"{photo_url}/00-99/0{hundreds}.jpg")
    else:
        card = Image.open(f"{photo_url}/00-99/{hundreds}.jpg")
else:
    card = Image.open(f"{photo_url}/{hundreds[:1] + '00'}-{hundreds[:1] + '99'}/{hundreds}.jpg")
card.show()
