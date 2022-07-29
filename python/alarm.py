from time import *
import os
import sys
import pyautogui
from pynput import keyboard

hours = 0


def system_argv():
    if sys.argv[1] == "-h":
        print("Hours")
        hours = float(sys.argv[2])
    elif sys.argv[1] == "-m":
        print("Minutes")
        print(sys.argv)
        print(sys.argv[2])
        hours = float(sys.argv[2]) / 60

    return hours


def gui_display():
    hours = pyautogui.prompt("Hours")
    print(hours)
    if hours is None or hours == "":
        return 4
    hours = hours.split(" ")

    if len(hours) > 1:
        print("Enter time")
        if hours[0] == "-h":
            print("Hours")
            hours = float(hours[1])
        elif hours[0] == "-m":
            print("Minutes")
            hours = float(hours[1]) / 60
    else:
        hours = int(hours[0])

    return hours


def main():
    print("MainMain" * 10)

    try:
        if len(sys.argv) > 1:
            hours = system_argv()
        else:
            hours = gui_display()
        print(strftime("%Y-%m-%d %H:%M:%S"))
        minutes = hours * 60
        seconds = minutes * 60
        print(f"Sleeping for {int(seconds)} seconds")
        sleep(seconds)
        yes_please = ["yes", "y", "Yes", "YES"]
        while True:
            sleep(seconds)
            print(f"Sleeping for {int(seconds)} seconds")
            file = '/home/nagual/PycharmProjects/pythonProject/selenium/alarm_sound.mp3'
            os.system("nvlc " + file)
            repeat = input("repeat? Y/n")
            if repeat in yes_please:
                print("Go again")
                continue
            else:
                break
    except KeyboardInterrupt:
        print("\nExited with Ctrl-C")


if __name__ == "__main__":
    main()
