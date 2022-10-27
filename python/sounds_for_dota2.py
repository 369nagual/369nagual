import pyautogui
import time
import pandas as pd
import os
import subprocess

print(subprocess)


def copy(text=None):
    if text is None:
        text = "None"
    df = pd.DataFrame([text])
    df.to_clipboard(index=False, header=False)


def create_folder_if_not_exists(folder=None):
    if folder is None:
        folder = os.path.abspath(os.path.join(os.path.sep, "dota_sound"))

    if os.path.exists(folder):
        print("Path exists.")
    else:
        print("Path is created!")
        os.mkdir(folder)
    return folder


def open_file(file, path=None):
    if path is None:
        path = os.path.abspath(os.path.join(os.path.sep, "dota_sound"))
    # vlc_path = '"' + os.path.abspath(os.path.join(os.path.sep, "Program Files", "VideoLAN", "VLC", "vlc.exe"))+'"'
    vlc_path = "vlc"
    os.system(vlc_path +
              " --qt-start-minimized " + os.path.join(path, file))


all_files = os.listdir(create_folder_if_not_exists())
# path_to_folder = os.path.abspath(os.path.join(os.path.sep, "dota_wd"))
path_to_folder = None
# print(all_files)
# all_files = os.listdir(create_folder_if_not_exists(os.path.abspath(os.path.join(os.path.sep, "dota_wd"))))
if len(all_files) > 0:
    shift = 6
    start = 0
    end = shift

    while True:
        sound_track = pyautogui.confirm(text='Dota 2 Sounds', title='dota2',
                                        buttons=["<==", *all_files[start:end], "==>"])
        if not sound_track:
            break
        if sound_track == "==>":
            start += shift
            end += shift
            continue
        if sound_track == "<==":
            start -= shift
            end -= shift
            continue

        delay = pyautogui.prompt("Delay: ")
        if delay:
            time.sleep(int(delay))
        open_file(file=sound_track, path=path_to_folder)
else:
    print("Папка пуста!")



