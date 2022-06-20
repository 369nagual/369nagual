import os
import pyautogui


def run_sound():
    print("Running sound")
    flag = True
    default_value = 100
    while flag:
        value = pyautogui.prompt(text="Введите громкость!", title="Sound", default=default_value)
        if value:
            command = f'''pactl set-sink-volume "$(LANG=C pactl info | grep 'Default Sink' | awk '{{print $3}}')" {value}%
    '''
            os.system(command)
            default_value = int(value)
            default_value += 10
        else:

            exit_point = pyautogui.confirm(text="Точно выйти?", title="Exit", buttons=["Нет", "Да"])
            default_value = 100
            if exit_point == "Нет":
                continue
            elif exit_point == "Да":
                flag = False
