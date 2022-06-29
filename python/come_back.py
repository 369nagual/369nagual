import pyautogui
import time
import os


def first_func():
    if (login == "Nagual" or login == "nagual") and password == correct_password:
        value = pyautogui.confirm(text='Выберете функцию', title='Функции',
                                  buttons=["Save To File", 'Exit(dev)', 'Paint', "==>"])
        if value == "==>":
            return second_func()
        elif value == "Paint":
            paint()
        elif value == "Save To File":
            note()
        elif value == "Exit(dev)":
            print("Developing")
        return value


def second_func():
    value = pyautogui.confirm(text="Выберете функцию", title="Функции 2", buttons=["<==", "Sound"])
    if value == "<==":
        return first_func()
    elif value == "Sound":
        run_sound()
    return value


def paint(distance=100):
    time.sleep(1.8)
    while distance > 0:
        pyautogui.drag(distance, 0, duration=0)  # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0)  # move down
        pyautogui.drag(-distance, 0, duration=0)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0)  # move up


def note():
    text = pyautogui.prompt(text="Введите что нужно записать!", title="Save", default="")
    local_time = time.localtime()
    current_time = time.strftime('%d.%m.%Y %H:%M', local_time)
    file = open(file="./text.txt", mode="a")
    if text is not None:
        file.write(f"{current_time} ==> {text}\n")
        file.close()
        first_func()
        return True

    else:
        return False


def run_sound():
    print("Running sound")
    flag_inner = True
    default_value = 100
    while flag_inner:
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
                flag_inner = False
                return first_func()


flag = True

while flag:
    correct_password = "Yustas2008"
    login = pyautogui.prompt(text='Login:', title='Title', default='Nagual')
    if login is not None:
        password = pyautogui.password(text='Password:', title='Title', default='Yustas2008', mask='*')
        first_func()

    elif login is None:
        flag = False
    else:
        pyautogui.alert("Failed")
