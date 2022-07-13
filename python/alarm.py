from time import *
import os
import sys

hours = 0


def main():
    global hours
    try:
        if len(sys.argv) > 1:
            print("Enter time")
            if sys.argv[1] == "-h":
                print("Hours")
                hours = float(sys.argv[2])
            elif sys.argv[1] == "-m":
                print("Minutes")
                print(sys.argv)
                print(sys.argv[2])
                hours = float(sys.argv[2]) / 60
        else:
            hours = 4
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

'''


logs/*
*.log
.idea/
__pycache__/
sensitive_data.py
ssh_marina.py
python/hh.py
python/alarm.py
alarm_sound.mp3







def delete_last_element():
    element = list(collection.find())[-1]
    collection.delete_one({'_id': ObjectId(element["_id"])})



'''
