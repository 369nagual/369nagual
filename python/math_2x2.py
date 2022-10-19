# import json
# import random
#
# file_path = "/home/nagual/PycharmProjects/pythonProject/selenium/python/random.txt"
# with open(file_path, "w") as f:
#     f.write("")
#
# with open(file_path, "r") as f:
#     data = f.read()
#     data_l = data.split("\n")[:-1]
#
# count = 0
# try:
#     amount = int(input("Количество уравнений: "))
# except ValueError:
#     amount = 10
# while count < amount - len(data_l):
#     count += 1
#     with open(file_path, "a") as file:
#         for _ in range(2):
#             json.dump(random.randint(22, 99), file)
#             if _ != 1:
#                 file.write("*")
#             else:
#                 file.write("=")
#                 file.write("\n")
#
# with open(file_path, "r") as f:
#     data = f.read()
#     print(data_l := data.split("\n")[:-1])
#     data = [el + "?" for el in data_l]
#
#     for answer_number in range(len(data_l)):
#         first_num = data_l[answer_number].split("*")[0]
#         second_num = data_l[answer_number].split("*")[-1][:-1]
#         print(
#             f"{first_num} * {second_num} = {first_num} * ({second_num[0]} * 10)  = {int(first_num) * int(second_num[0])}"
#             f" * 10 = {int(first_num) * int(second_num[0]) * 10}")
#         try:
#             if int(input("Введите ответ: ")) == int(first_num) * int(second_num):
#                 print("Успех!")
#             else:
#                 print("Ошибка!")
#                 print(f"Правельно: {int(first_num) * int(second_num)}")
#         except ValueError:
#             print("ValueError!!!")


from random import randint
import colored
from colored import stylize
import time


def two_x_two():
    start = time.time()

    qnt = int(input("Кол-во уравнений: "))
    for _ in range(qnt):
        first = randint(11, 99)
        second = randint(11, 99)
        print(f"{first}*{second}=", end="")
        start_time = time.time()
        eqw = input()
        if int(first) * int(second) == int(eqw):
            print(stylize("Correct!", colored.fg("blue")))
        else:
            print(stylize("Wrong!", colored.fg("red")))
            print(stylize(f"{first}*{second}={str(int(first) * int(second))}", colored.fg("green")))
        end_time = time.time()
        print(
            f"Time: {(end_time - start_time) / 60 / 60:0.0f}h {(end_time - start_time) / 60:0.0f}m {(end_time - start_time) % 60:0.0f}s")
    end = time.time()
    print(f"Total Time: {(end - start) / 60 / 60:0.0f}h {(end - start) / 60:0.0f}m {(end - start) % 60:0.0f}")


two_x_two()
