import os

list_dir = os.listdir()

for i, file in enumerate(list_dir):
    if ".py" in file:
        if "reformat" not in file:
            os.system("mkdir -p python")
            os.system(f"mv {file} python")
    elif ".png" in file or ".jpg" in file:
        os.system("mkdir -p images")
        os.system(f"mv {file} images")
