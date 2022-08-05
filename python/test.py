# name = "Vitaly"
# ! total_solgers = int(input("Сколько солдат? "))
# * total_ruls = int(input("Сколько правил в уставе? "))
# + total_push_ups = 0
# ? print(total_solgers)

# for i in range(total_solgers - 4, 0, -4):
#     if int(input("Какой устав? ")) == total_ruls:
#         continue
#
#     print(f"i * 10 {i * 10}")
#     total_push_ups += i * 10
#
# print(total_push_ups)
#
#
# Задача 1. Космическая еда
# Сомолет и 100-кг гречки на сколько месяцов ее хватит если в месяц тратится 4 кг
#
# grechka = 100
#
# print(f"0 месяц {grechka}kg")
# for i, k in enumerate(range(grechka, -1, -4)):
#     print(i)
#     print(k)
#     print("+++++++++++++++++++++++++++++++++++++++")
#
#
# Задача 2. Долги
# debtor_amount = int(input("Введите количество должников: "))
#
# total_money = 0
#
# for n in range(0, debtor_amount, 5):
#     print(f"Должник с номером {n}")
#     total_money += int(input("Сколько должны? "))
#
# print(f"Общая сумма долга {total_money}")
#
# Задача 3. Это будет бомба
#
# seconds = int(input("Секунды: "))
#
# for s in range(seconds, 0, -1):
#     print(f"Времяни {s} осталось до взрыва!")
#     answer = int(input("Хочтите обезвредить бомбу? "))
#     if answer == 0:
#         continue
#     else:
#         print(f"Бомба обезврежена за {seconds - s} секунд")
#         break
#
#
# Задача 3. Функция if else
#
# y = None
# for i in range(1, 4):
#     x = int(input("Введите икс: "))
#     if x == 0:
#         y = 5
#         break
#     elif x < 0:
#         y = x ** 2
#         break
#     elif x > 0:
#         y = x - 12
#         break
#
# print(f"Игрек равен {y}")
#
#
# Задача 4. Среднее на отрезке
#
# a=10, b=20, c=5 (ввели)
# Числа в отрезке 10,15,20
# Среднее 15
# Как-то так думаю
#
# a, b, c = input("Введите номер: ").split(" ")
# a, b, c = int(a), int(b), int(c)
#
# print(a, b, c)
#
# counter = 0
# all_count = 0
# for i in range(a, b + c, c):
#     counter += 1
#     all_count += i
#
# print(all_count // 3)
#
#
# Задача 10. Кинотеатр
#
# boys = int(input("Введите количество мальчиков: "))
# girls = int(input("Введите количество девочек: "))
#
# answer = ""
#
# if (boys > 2 * girls) or (girls > 2 * boys):
#     print("Нет решения")
#
# elif boys >= girls:
#     k = boys - girls
#
#     for bgb in range(k):
#         answer += "BGB"
#
#     for bg in range(girls - k):
#         answer += "BG"
#
# else:
#     k = girls - boys
#
#     for gbg in range(k):
#         answer += "GBG"
#
#     for bg in range(boys - k):
#         answer += "GB"
#
# print(answer)
# #
#
# boys = int(input("Boys: "))
# girls = int(input("Girls: "))
#
# answer = ""
#
# if (boys > 2 * girls) or (girls > 2 * boys):
#     print("NONE")
#
# elif boys >= girls:
#     k = boys - girls
#
#     for bgb in range(k):
#         answer += "BGB"
#
#     for bg in range(girls - k):
#         answer += "BG"
#
# else:
#     k = girls - boys
#
#     for gbg in range(k):
#         answer += "GBG"
#
#     for gb in range(boys - k):
#         answer += "GB"
#
# print(answer)
#
# my_list = [34, 4224, 2324, 5231, 55, 51, 1, 2, 3]
#
# for i in range(len(my_list)):
#     lower = i
#
#     for j in range(i + 1, len(my_list)):
#         if my_list[j] < my_list[lower]:
#             lower = j
#
#     my_list[i], my_list[lower] = my_list[lower], my_list[i]
#
# print(my_list)
#
# names = ["Vitaly", "Marina", "Sasha", "Banana", "Mozart", "Kostya"]
#
#
# def linear_search(where, what):
#     for i, v in enumerate(where):
#         if v == what:
#             return f"Index {i}"
#     return None
#
#
# print(linear_search(names, "Kostya"))
#
# Binary Search
# nums = [2, 34, 1413, 41, 5, 13, 5123, 5, 1, 31, 123, ]
# nums.sort()
# print(nums)
#
# bad_grade_count = 0
#
# for student in range(5):
#     answer = input("Кто написал Евген и Анеги")
#     if answer == "Пушкин" or answer == "пушкин":
#         print("Верно!")
#         break
#
#     print("Не правельно, 2")
#     bad_grade_count += 1
#
# print("Количество двоек", bad_grade_count)
#
#
# phrase = input("Введите фразу: ")
#
# for symbol in phrase:
#     print(symbol * 5)
#
# text = input("Введите text: ")
# first_letter = input("Введите первую букву: ")
# second_letter = input("Введите вторую букву: ")
#
# first_sym_count = 0
# second_sym_count = 0
#
# for sym in text:
#     if sym == first_letter:
#         first_sym_count += 1
#
#     if sym == second_letter:
#         second_sym_count += 1
#
# print(f"Количество букв {first_letter} = {first_sym_count}")
# print(f"Количество букв {second_letter} = {second_sym_count}")
#
#
# first_number = int(input("Введите первое число"))
# step = int(input("Введите шаг"))
# summ = 0
#
# for count in range(3):
#     print(first_number, end=".")
#     summ += first_number
#     first_number += step
#
# print(summ)
#
# Filter
#
# text = input("Введите текст: ")
# text = "При19мер"
# summ = 0
# print("\nFiltered text:", end=" ")
# for sym in text:
#     if sym == "1" or sym == "9":
#         summ += int(sym)
#     else:
#         print(sym, end="")
# print("\nСумма: ", summ)
#
# string = input("Input letters")
# prev_sym = ""
# flag = False
#
# for letter in string:
#     if prev_sym == letter:
#         flag = True
#         break
#     else:
#         prev_sym = letter
#
# if flag:
#     print("GOOD")
#
# else:
#     print("BAD")
# nums = [3, 411, 41, 412, 433, 134, 185, 743, 111]
# nums.sort()
# print(nums)
#
# index = None
#
# search_for = 743
#
# lowest = 0
#
# highest = len(nums) - 1
#
# while index is None:
#     mid = (lowest + highest) // 2
#     if search_for == nums[mid]:
#         index = mid
#     else:
#         if search_for > nums[mid]:
#             lowest = mid + 1
#         else:
#             highest = mid - 1
#
# print(index)
# print(nums[index])
#
# nums = [3, 411, 41, 412, 433, 134, 185, 743, 111]
#
# search_for = 433
#
# for el in nums:
#     if el == search_for:
#         print("Элемент найден", end=" ")
#         print(el)
#         break
#
#
# Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13,
#
# def fibonacci(n):
#     if n == 1:
#         my_list = [0]
#
#     else:
#         my_list = [0, 1]
#         for i in range(1, n - 1):
#             my_list.append(my_list[i - 1] + my_list[i])
#
#     return my_list
#
#
# print(fibonacci(11))
#
#
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# def fibonacci_sequence(n):
#     sequence = []
#     for i in range(0, n):
#         sequence.append(fibonacci(i))
#
#     return sequence
#
#
# print(fibonacci_sequence(9))
#
#
# Binary Search
#
# my_list = [4134, 134, 14, 141, 41, 341]
#
# my_list.sort()
#
# print(my_list)
#
# search_for = 4134
#
# lowest = 0
# highest = len(my_list) - 1
#
# index = None
# while index is None:
#     mid = (lowest + highest) // 2
#
#     if search_for == my_list[mid]:
#         index = mid
#     else:
#         if search_for < my_list[mid]:
#             highest = mid - 1
#
#         else:
#             lowest = mid + 1
#
# print(index)
#
#
# for row in range(6):
#     for col in range(6):
#         print(row + col, end="  ")
#     print()
#
# size = int(input("Введите размер матрицы: "))
#
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if row % 2 == 0:
#             print(row, end=" ")
#         else:
#             print(col, end=" ")
#     print()
#
# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end="")
#         elif col == 24:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()
#
#
#
# size = int(input("Введите размер матрицы: "))
#
# for row in range(size):
#     for col in range(size):
#         if row < col:
#             print(0, end="  ")
#         elif row > col:
#             print(2, end="  ")
#         else:
#             print(1, end="  ")
#
#     print()
#
#
# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end="")
#
#         elif row + 29 == col:
#             print("\\", end="")
#
#         elif -row + 19 == col:
#             print("/", end="")
#         elif col == 24:
#             print("|", end="")
#
#         else:
#             print(" ", end="")
#     print()
#
#
# for row in range(20):
#     for col in range(30):
#         if row == 0:
#             print("-", end="")
#         elif col == 0 or col == 29:
#             print("|", end="")
#         else:
#             print(" ", end="")
#
#     print()
#
#
# matrix = int(input("Введите размер матрицы: "))
#
# # 0 0 0 0 1  row = 0  col = 4
# # 0 0 0 1 2  row = 1 col = 3
# # 0 0 1 2 2  row = 2 col = 2
# # 0 1 2 2 2  row = 3 col = 1
# # 1 2 2 2 2  row = 4 col = 0
#
# for row in range(matrix):
#     for col in range(matrix, 0, -1):
#         if row >= col:
#             print(2, end="  ")
#         elif row + 1 == col:
#             print(1, end="  ")
#         else:
#             print(0, end="  ")
#     print()
#
#
#
#
#
#
#
# people_in_line = int(input("Сколько людей в очереди? "))
# begin = 0
# for hour in range(people_in_line + 1):
#     print(f"Идёт час: {hour}")
#     for line in range(begin, people_in_line):
#         print(f"Номер в очереди {line}")
#
#     begin += 1
#     print()
# print("Очередь обслужена!")
#
# # or
#
# people_in_line = int(input("Сколько людей в очереди? "))
# for hour in range(people_in_line + 1):
#     print(f"Идёт час: {hour}")
#     for line in range(hour, people_in_line):
#         print(f"Номер в очереди {line}")
#
#     print()
# print("Очередь обслужена!")
#
# #
# seq_num = int(input("Количество чисел: "))
# search_for = int(input("Ищем эту цыфру: "))
# # +   11 or -1
# while 0 > search_for > 9:
#     search_for = int(input("Цыфра должна быть между 0 и 9: "))
#
# count = 0
# for numbers in range(seq_num):
#     nums = int(input(f"Введите {numbers + 1} -e число "))
#     while nums > 0:
#         if nums % 10 == search_for:
#             count += 1
#
#         nums //= 10
#
# print(count)
#
# seq_num = int(input("Введите N последовательность: "))
# count = 0
# for numbers in range(seq_num):
#     nums = int(input(f"Введите {numbers + 1} -e число "))
#     if nums <= 5:
#         continue
#     count += 1
#
# print(f"Всего найдено {count} цыфр больше 5")
#
#
# numbers = int(input("Лестница из чисел: "))
#
# for n in range(numbers + 1):
#     for i in range(n, numbers + 1):
#         print(i, end=" ")
#
#     print()
#
# Банкомат с while
# pin = int(input("Введите Пин-Код: "))
# amount = 3
# while pin != 7579:
#     if amount == 0:
#         print("Ваша карта заблокирована!")
#         break
#     pin = int(input(f"Введите Пин-Код, у вас осталось {amount} попыток:"))
#     amount -= 1
#
# else:
#     print("Пин-Код верный. Держите вашу зарплату!")
#
# Банкомат с for
#
# My own code
#
# pin = int(input("Введите пинкод: "))
#
# for i in range(3, 0, -1):
#     if pin == 7579:
#         print("Пин-Код верный. Держите вашу зарплату!")
#         break
#     else:
#         pin = int(input(f"Введите пинкод у вас осталось {i} попыток"))
#
# else:
#     print("Ваша карта заблокирована!")
#
#
# Skillbox Teacher's code (Practice Code)
#
# for attempt in range(1, 4):
#     pincode = int(input("Введите пинкод: "))
#     if pincode == 1234:
#         print(f"Пин-Код верный. Держите вашу зарплату!")
#         break
#     print(f"Попыток осталось {3 - attempt}")
# else:
#     print("Ваша карта заблокирована!")
#
#
# !  11.6 Практическая работа
#
# Задача 1. Тестовое задание
#
# for row in range(0, 6):
#     for col in range(row, 11 + row, 2):
#         print(col, end="\t")
#     print()
#
# Задача 2. Лестница
#
# numbers = int(input("Длина лестницы: "))
#
# for row in range(1, numbers + 1):
#     for col in range(row):
#         print(row, end=" ")
#     print()

#
# Задача 3. Рамка
#
# width = int(input("Введите ширину: "))
# length = int(input("Введите длину: "))
#
# for row in range(length):
#     for col in range(width):
#         if row == 0 or row == length - 1:
#             if col == 0 or col == width - 1:
#                 print("|", end="")
#             else:
#                 print("-", end="")
#         elif col == 0 or col == width - 1:
#             print("|", end="")
#         else:
#             print("", end=" ")
#     print()
#
#
# Задача 4. Крест


# size = int(input("Введите размер креста: "))
# size = 10
#
# for row in range(size):
#     for col in range(size):
#         print(row, end=" ")  # ROW
#     print()
#
# print("- " * size)
# for row in range(size):
#     for col in range(size):
#         print(col, end=" ")  # COL
#     print()
#
# print("- " * size)
#
# for row in range(size):
#     for col in range(10):
#         if row == col or (size - 1) - row == col:
#             print("^", end="")
#         else:
#             print("", end="  ")
#     print()
#
#
#
# Задача 5. Простые числа
#
#
#
# seq_numbers = int(input("Введите последовательность:"))
#
# counter = 0
# for i in range(seq_numbers):
#     number = int(input("Введите число: "))
#     if number % 2 != 0:
#         counter += 1
#
# print(f"Количество простых чисел в последовательности: {counter}")
#


# Задача 6. Сумма факториалов
# 1! + 2! + 3! + ... n!

# factorial = int(input("Введите сколько будет факториалов: "))
# multy = 1
# summ = 0
# for i in range(1, factorial + 1):
#     for j in range(1, i + 1):
#         multy *= j
#     summ += multy
#     multy = 1
#     print()
#
# print(summ)

# OR
#
# n = int(input())
# partial_factorial = 1
# partial_sum = 0
# for i in range(1, n + 1):
#     partial_factorial *= i
#     partial_sum += partial_factorial
# print(partial_sum)


# ? Задача 7. Наибольшая сумма цифр
# seq_nums = int(input("Введите "))

# Задача 8. Пирамидка

# height = int(input("Введите высоту пирамиды: "))
# height = 5
# for row in range(1, height * 2, 2):
#     for col in range(height):
#         if col == height // height:
#             print(" " * (height - row // 2), end="")
#             print("#" * row, end="")
#         else:
#             print("", end=" ")
#     print()
# #
# k = int(input("Enter the number of rows"))
# for i in range(1, k + 1):
#     print(" " * (k - i) + "#" * (2 * i - 1))

# OR
# numbers = 1
# for row in range(height):
#     print(" " * (height - row) + "#" * numbers)
#     numbers += 2

#
#
#


# height = int(input("Введите число уровней пирамиды: "))
#
# height = 5
# numbers = 1
# for row in range(1, height + 1):
#     print("\t" * (height - row), end="")
#     for col in range(row):
#         print(numbers, end="\t\t")
#         numbers += 2
#     print()

#

#
# 1
# 3 5
# 7 9 11
# 13 15 17 19
# 21 23 25 27  29
# 31 33 35 37 39 41


# ? Задача 10. Яма

# depth = int(input("Введите длину: "))
# depth = 10
# for row in range(depth):
#     for left_num in range(depth, depth - row - 1, -1):
#         print(left_num, end="")
#     print(".." * (depth - row - 1), end="")
#     for right_num in range(depth - row, depth + 1):
#         print(right_num, end="")
#     print()

# # REGEX testing
import re

#
# # Текст
# text = "something 77782508000068 al aswalsdf asdf 123 as 8381829 23 2 somet nothin 77010070840299 g 12341231341988"
#
# # Паттерн
# pattern = "\s\d{14}\s"
#
# # Создание списка элементов совпадающих с паттерном
# # [паттерн, паттерн, ..., ..., ..., ..., ..., ...]
# result = re.findall(pattern, text)

# Вывод списка
# print(result)
# #
# # # Так?
# for i, el in enumerate(result):
#     result.remove(el)
#     el = el.strip()
#     result.insert(i, el)
# print(result)

# result.append("Last")
# for prev, number in zip(result, result[1:]):
#     print(f'"{number.rjust(len(number) + 1)}"')
#     number = number.rjust(len(number) + 1)
#     number = number.ljust(len(number) + 1)
#     print(f'"{number}"')
#     print(f'"{prev}"')
#
# # Или так?
#
#
# new_result = []
# for el in result:
#     new_result.append(el.strip())
# print(new_result)
# print(result)

# text = int(input("Test"))
# text = 12341235
# print(text % 100)
# print(str(text)[-2:])


# boys = int(input("Boys"))
# girls = int(input("Girls"))
#
# answer = ""
# if boys > 2 * girls or girls > 2 * boys:
#     print("NOT GOOD")
#
# elif boys >= girls:
#     k = boys - girls
#
#     for bgb in range(k):
#         answer += "BGB"
#     for bg in range(k - girls):
#         answer += "BG"
# else:
#     k = girls - boys
#
#     for gbg in range(k):
#         answer += "GBG"
#     for gb in range(k - boys):
#         answer += "GB"
#
# print(answer)


# ? Пирамидка 2 Учитель
# row = int(input("Введите число строк: "))
# row = 8
# new_num = 1
#
# for line in range(row):
#     space_count = row - line - 1
#     print("   " * space_count, end="")
#     for number in range(line + 1):
#         print(new_num, end="    ")
#         new_num += 2
#     print()

# while True:
#     force = float(input("Сила удара: "))
#     force *= 10
#     print(f"Бал: {int(force)}")


# x = float(input("Расположение по горизонтали"))
# y = float(input("Расположение по вертикали"))
#
# x_square = int(x * 10)
# y_square = int(y * 10)
# print(f"Фигуна находится в клетке: {x_square} и {y_square}")


import math

#
# x = float(input("Расположение по горизонтали"))
# y = float(input("Расположение по вертикали"))
#
# distance = math.sqrt(x ** 2 + y ** 2)
# print("Ростояние:", distance)

# distance = float(input("Растояние до танка"))
# angle = float(input("Угол в градусах"))
#
# angle /= 57.2958
# x = math.cos(angle) * distance
# y = math.sin(angle) * distance
#
# print(x, y)
# a, b, d = 1.1, 2.2, 3.3
# c = a + b
#
# print(abs(c - d))
#
# print(type(4j))
# print(4j)
# if c - d < 1e-16:
#     print("Equally")
# else:
#     print("Not Equally")

# import math
#
# precision = 0.1
# while precision != 0.12341234:
#     # e = 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ... 1/n! +
#     precision = float(input("Точность: "))
#
#     result = 0
#     i = 0
#     addMember = 1
#
#     while precision < addMember:
#         addMember = 1 / math.factorial(i)
#         i += 1
#         result += addMember
#     print(result)
#     print(math.e)

# num = int(input("Введите число"))
# summery = 0
# while num != 0:
#     last_num = num % 10
#     num //= 10
#     summery += last_num
#     if last_num == 5:
#         print("Обнаружен разрыв")
#         break
#
# print(summery)

# 15.7 Практическая работа
#   Задача 7. Годы

#
# floor = input("Введите начало года!")
# roof = input("Введите конец года!")
# if len(floor) == 4 and len(roof) == 4:
#     for current_year in range(int(floor), int(roof) + 1):
#         # print(current_year)
#         a = current_year // 1000
#         # print(a)
#         b = current_year // 100 % 10
#         # print(b)
#         c = current_year // 10 % 10
#         # print(c)
#         d = current_year % 10
#         # print(d)
#         if a == b == c or b == c == d or a == c == d or a == c == d:
#             print(current_year)
# else:
#     print("Enter 4 digits")


# Задача 1. Информация о системе

# import platform
# import sys
#
# info = 'OS info is \n{}\n\nPython version is {} {}'.format(
#     platform.uname(),
#     sys.version,
#     platform.architecture(),
# )
# print(info)
#
# with open('os_info.txt', 'w', encoding='utf8') as file:
#     file.write(info)

#

# books_id = [50, 34, -1, -1, 2, 23, -1]
# new_books_id = []
# returned = 0
# print(books_id)
#
# for _ in range(3):
#     id = input("Enter id of a book")
#     books_id.append(id)
#
# for id in books_id:
#     if id == -1 or id == '-1':
#         returned += 1
#     else:
#         new_books_id.append(id)
# print(new_books_id)
# print(returned)
#
#

# Аркадию нужна помошь

# numbers = [3, 7, 5]
# try:
#     while True:
#
#         number = input('Новое число: ')
#         print(f"'{number}'")
#         number = int(number)
#
#         numbers.append(number)
#
#         print('Текущий список чисел:', numbers)
#
#         for i in numbers:
#             print(i ** 2, i ** 3, i ** 4)
#
#         print()
# except ValueError:
#     print("ValueError")
#     print(number)


# numbers = []
#
# for number in range(0, 101):
#     numbers.append(number)
#
# print(numbers)

#
# amount_of_employees = int(input("Amount of Employee: "))
#
# employees = []
# for _ in range(amount_of_employees):
#     employee_id = int(input("Employee ID"))
#     employees.append(employee_id)
#
# search_for_employee_id = int(input("Is employee with this ID here? "))
#
# if search_for_employee_id in employees:
#     print("Yes he is down here")
#
# else:
#     print("No he is not down here")
# monsters_count = 0
# mage_index = 1
# while monsters_count < mage_index:
#     monsters_count = int(input("Number of monsters: "))
#     mage_index = int(input("Number mage in list: "))
# monster_damage = []
#
# for monster in range(1, monsters_count + 1):
#     print(f"Урон у {monster} монстра: ", end=" ")
#     damage = int(input())
#     monster_damage.append(damage)
#
# print(monster_damage)
#
# for i_monster in range(monsters_count):
#     if monster_damage[i_monster] < 100 and i_monster != mage_index - 1:
#         monster_damage[i_monster] += monster_damage[mage_index - 1]
#
# print(monster_damage)

'''
Однако он столкнулся с проблемой. Если брать, к примеру, количество чисел 5, то на тестах -1 -2 -3 -4 -5 и 1 2 3 4 5 программа выводит неверный результат. 

Доработайте программу так, чтобы она выводила верный результат. Подсказка: для отладки используйте точки останова.

'''
# nums_list = []
#
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#
#     nums_list.append(num)
#
# maximum = 0
#
# minimum = 0
#
# for index, i in enumerate(nums_list):
#
#     if maximum < i:
#         maximum = i
#         if index == 0:
#             minimum = maximum
#     if minimum > i:
#         minimum = i
#         if index == 0:
#             maximum = minimum
#
# print('Максимальное число в списке:', maximum)
#
# print('Минимальное число в списке:', minimum)


'''
Задача 2. Кратность

Пользователь вводит список из N чисел и число K. Напишите код, выводящий на экран сумму индексов элементов списка, которые кратны K.
Пример:

'''
# list_of_numbers = []
#
# items_amount = int(input("Кол-во чисел в списке: "))
# for i in range(1, items_amount + 1):
#     number = int(input(f"Введите {i} число: "))
#     list_of_numbers.append(number)
#
# print()  # \n
# k = int(input("Введите делитель: "))
#
# index_count = 0
#
# print()  # \n
# for i, element in enumerate(list_of_numbers):
#     if element % k == 0:
#         print(f"Индекс числа {element}: {i}", end="\n\n")
#         index_count += i
# print(f"Сумма индексов: {index_count}")

'''
Кол-во чисел в списке: 4

Введите 1 число: 1

Введите 2 число: 20

Введите 3 число: 30

Введите 4 число: 4


Введите делитель: 10


Индекс числа 20: 1

Индекс числа 30: 2

Сумма индексов: 3'''

#
# word = input("Введите слово: ")
#
# replace_num = int(input("Номер буквы для замены: "))
# replace_sym = input("На что заменить")
#
# new_word = ""
# for i, letter in enumerate(word):
#     if i + 1 != replace_num:
#         new_word += letter
#     else:
#         new_word += replace_sym
#
# print(new_word)


# word = input("Введите слово: ")
#
# replace_num = int(input("Номер буквы для замены: "))
# replace_sym = input("На что заменить")
# sym_list = list(word)
#
# sym_list[replace_num - 1] = replace_sym
#
# new_word = ""
# for sym in sym_list:
#     new_word += sym
#
# print(new_word)


# words_list = []
#
# counts = [0, 0, 0]
#
# for i in range(3):
#     print(f"Введите {i + 1} слово: ", end=" ")
#     word = input()
#     words_list.append(word)
#
# print(words_list)
#
# text = input("Текст : ")
# text = text.split(" ")
#
# for index in range(3):
#     for i in range(len(text)):
#         if words_list[index] == text[i]:
#             counts[index] += 1
#
# print(text)
# print(words_list)
# for i in range(3):
#     print(f"{words_list[i]}: {counts[i]}")


# word = input("Word")
# change_num = int(input("Number of charecter to change"))
# chege_to_char = input("Charecter that will replace")

# new_word = ""
# for i, letter in enumerate(word):
#     if i == (change_num - 1):
#         new_word += chege_to_char
#     else:
#         new_word += letter
#
# print(new_word)

# word = list(word)
# word[change_num - 1] = chege_to_char
# for letter in word:
#     print(letter, end='')


# def length(player_list):
#     player_count = 0
#     for _ in player_list:
#         player_count += 1
#     return player_count
#
#
# scores = [8, 5, 10, 7, 6]
# scores[1] += length(scores)
# scores.append(0)
# scores[2] += length(scores)
# print(scores)

#  Задача 1. Генерация списка

# N = int(input("Введите число: "))
#
# my_list = []
# for i in range(1, N + 1, 2):
#     my_list.append(i)
#
# print(f"Список из нечётных чисел от одного до N: {my_list}")


# Задача 2. Турнир

# players_list = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
#
# new_list = []
# for i in range(len(players_list)):
#     if i % 2 == 0:
#         new_list.append(players_list[i])
#
# print(f"Первый день: {new_list}")


# Задача 3. Клетки
# list_of_cels = [3, 0, 6, 2, 10, 4, 2, 34, 12, 3441, 23, 4, 1, 341, 10]
#
# for i, cel in enumerate(list_of_cels):
#     print(f"Эффективность {i + 1} клетки: {cel}")
#
# not_used_cels = []
# text = "Неподходящие значения: "
# for i, cel in enumerate(list_of_cels):
#     if cel < i:
#         text += str(cel) + " "
#
# print(text)


# Задача 4. Видеокарты

# def maximun_in_list(_list):
#     sorted_list = []
#     while len(_list) > 0:
#         max = 0
#         for el in _list:
#             if el > max:
#                 max = el
#         sorted_list.insert(0, max)
#         del _list[_list.index(max)]
#     for el in sorted_list:
#         _list.append(el)
#     return _list


# number_of_cards = int(input("Количество видеокарт: "))
# list_of_cards = []
# for i in range(1, number_of_cards + 1):
#     card = int(input(f"{i}. Видеокарта: "))
#     list_of_cards.append(card)
#
# print(f"Старый список видеокарт:{list_of_cards}")
#
# for card in list_of_cards:
#     if card == max(list_of_cards):
#         list_of_cards.pop(list_of_cards.index(card))
#
# print(f"Новый список видеокарт:{list_of_cards}")

# Задача 5. Кино

# films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо",
#          "Отступники", "Деревня"]
#
# film_count = int(input("Сколько фильмов хотите добавить? "))
# fav_films = []
# for _ in range(film_count):
#     find_film = input("Введите название фильма: ")
#     if find_film in films:
#         fav_films.append(find_film)
#     else:
#         text = f"Ошибка: фильма {find_film} у нас нет :("
#         print(text)
#
# output_fav_films = f"Ваш список любимых фильмов: "
# for film in fav_films:
#     if fav_films[-1] == film:
#         output_fav_films += film
#     else:
#         output_fav_films += film + ", "
#
# print(output_fav_films)


# Задача 6. Анализ слова


# word = input("Введите слово: ")
# 1
# print(f"Количество уникальных букв: {len([element for element in word if word.count(element) == 1])}")
# 2
# new_word_list = []
# for letter in word:
#     if letter in new_word_list:
#         del new_word_list[new_word_list.index(letter)]
#     else:
#         new_word_list.append(letter)
#
# print(f"Количество уникальных букв: {len(new_word_list)}")


# Задача 7. Контейнеры
# #
# amount_of_containers = None
# while True:
#     amount_of_containers = input("Количество контейнеров: ")
#     if amount_of_containers == "end":
#         break
#     else:
#         try:
#             amount_of_containers = int(amount_of_containers)
#         except ValueError or TypeError:
#             print("Введите цифру!")
#             continue
#     new_list = []
#     root = 200
#     current_range = 0
#     while len(new_list) != amount_of_containers:
#         try:
#             for _ in range(current_range, amount_of_containers):
#                 current_range = _
#                 container_weight = int(input("Введите вес контейнера: "))
#                 if current_range == 0:
#                     current_weight = container_weight
#                 if container_weight <= 200:
#                     if container_weight <= current_weight:
#                         new_list.append(container_weight)
#                         current_weight = container_weight
#                     else:
#                         print("Вес не должен привышать вес предыдущего контейнера!")
#                 else:
#                     print("Вес должен быть не больше 200")
#                     break
#         except ValueError:
#             print("Введите цифру!")
#             continue
#     print(new_list)
#
#     while True:
#         new_container = int(input("Введите вес нового контейнера: "))
#         if new_container <= 200:
#             for i, el in enumerate(new_list):
#                 if el < new_container:
#                     print(f"Номер, который получит новый контейнер: {i + 1}")
#                     new_list.insert(i, new_container)
#                     break
#                 elif len(new_list) > i + 1:
#                     if new_list[i] > new_container > new_list[i + 1]:
#                         new_list.insert(i + 1, new_container)
#                         break
#                 else:
#                     new_list.insert(len(new_list), new_container)
#                     break
#             print(new_list)
#
#         else:
#             print("Вес должен быть не больше 200")
#             continue


# Задача 8. Бегущие цифры

# N = int(input("Enter number of element you want in list: "))
# list_of_elements = []
# for _ in range(N):
#     el = int(input("Enter elemens: "))
#     list_of_elements.append(el)
#
# shift = int(input("Shijft elements in list: "))
# print(f"Изначальный список: {list_of_elements}")
#
# new_list = list_of_elements[:-shift]
# new_list = list_of_elements[-shift:] + list_of_elements[:-shift]
# print(f"Сдвинутый список: {new_list}")


# Задача 9. Анализ слова 2

# word = input("Введите слово: ")
#
# normal_word_list = []
# reversed_word_list = []
#
# for letter in word:
#     normal_word_list.append(letter)
#
# for r_index in range(len(word) - 1, -1, -1):
#     reversed_word_list.append(word[r_index])
#
# if reversed_word_list == normal_word_list:
#     print(f"Слово является палиндромом!")
# else:
#     print(f"Слово не является палиндромом!")


# Задача 10. Сортировка

# random_list = [1, 4, -3, 0, 444, 12, 3, 5, -12, 10]

# 1
# count = 0
# while True:
#     for el in range(1, len(random_list)):
#         if random_list[el - 1] > random_list[el]:
#             random_list[el], random_list[el - 1] = random_list[el - 1], random_list[el]
#             break
#     count += 1
#     if count == len(random_list) * len(random_list):
#         break

# print(random_list)

# 2
# for _ in range(len(random_list)):
#     for el in range(1, len(random_list)):
#         if random_list[el - 1] > random_list[el]:
#             random_list[el], random_list[el - 1] = random_list[el - 1], random_list[el]
#
# print(random_list)


# 3
# def selection_sort(my_list):
#     for i in range(len(my_list)):
#         for el in range(i + 1, len(my_list)):
#             if my_list[i] > my_list[el]:
#                 my_list[i], my_list[el] = my_list[el], my_list[i]


# random_list = [4, 9, 7, 6, 3, 1, 2, 22, 31, 11, 23, 12, 8]
# selection_sort(random_list)
# print(random_list)
#
###
#
#
#
# lang = ["Python", "Java", "JS", "SQL"]
# print(f"insert C++ after Java")
# print(f"current list {lang}")
# index_of_java = lang.index("Java")
# print(f"index of Java {index_of_java}")
# print(f"then insert C++ on index 2")
# lang.insert(index_of_java + 1, "C++")
# print(f"current list {lang}")


# films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо",
#          "Отступники", "Деревня"]
#
# my_fav = []
#
# while True:
#     print("\nВаш топ фильмов", my_fav)
#     new_movie = input("Навзание фильма: ")
#     if new_movie in films:
#         print("Команды: добавить, удалить, вставить")
#         command = input("Введите команду: ")
#         if command == "добавить":
#             if new_movie in my_fav:
#                 print("Такой фильм уже у вас есть!")
#             else:
#                 my_fav.append(new_movie)
#
#         elif command == "удалить":
#             if new_movie in my_fav:
#                 my_fav.remove(new_movie)
#             else:
#                 print("Нет такого фильма")
#
#         elif command == "вставить":
#             if new_movie in my_fav:
#                 print("Такой фильм уже у вас есть!")
#             else:
#                 index = int(input("На какое место"))
#                 my_fav.insert(index - 1, new_movie)
#
#     else:
#
#         print("Такого фильма нет в списке!")


# my_love = ["Marina", "Tenia", "Nelepost`"]
# your_love = ["Vitaly", "Tenia", "Nelepost`"]
#
# my_love.extend(your_love)
# print(my_love)
# name = input("Enter you name")
# change_char = input("Enter char to replace")
# index_char_to_change = int(input("Index to change!"))
#
# list_of_char = []
#
# list_of_char.extend(name)
# list_of_char[index_char_to_change] = change_char
# new_name = ""
#
# for letter in list_of_char:
#     new_name += letter
#
# print(new_name)
#


# Задача "Пакеты"
# My try
# pack = []
# decode = []
# bad_packs = 0
#
# packs_amt = int(input("Num of packets"))
#
# for i_pack_num in range(packs_amt):
#     bad_packs = 0
#     pack = []
#     print("\nПакет номер ", i_pack_num + 1)
#     print(pack)
#     print(decode)
#     print(bad_packs)
#     for _ in range(4):
#         bit = input("Bits in packets 4: ")
#         pack.append(int(bit))
#         if bit == "1":
#             bad_packs += 1
#     if bad_packs <= 1:
#         decode.extend(pack)
#
# print(decode)

# Teachers program

pack = []
decode = []
bad_packs = 0

# packs_amt = int(input("Amount of packets: "))

# for i_pack_num in range(packs_amt):
#     print("\nPacket number", i_pack_num + 1)
#     for i_bit in range(4):
#         print(i_bit + 1, "bit:", end=" ")
#         num = int(input())
#         pack.append(num)
#
#    if pack.count(-1) <= 1:
#        pass


# for i_pack_num in range(packs_amt):
#     print("\nPacket number", i_pack_num + 1)
#     for i_bit in range(4):
#         print(i_bit + 1, "bit:", end=" ")
#         num = int(input())
#         pack.append(num)
#     if pack.count(1) <= 1:
#         decode.extend(pack)
#     else:
#         print("Error: To many 1 in packets")
#         bad_packs += 1
#     pack = []
#
# print(f"\nПолученое сообщение: {decode}")
# print(f"Кол-во ошибокв сообщении: {decode.count(1)}")
# print(f"Кол-во потерянных пакетов: {bad_packs}")

#
# random_list = [4, 9, 7, 6, 3, 1, 2, 1.4, 22, 31, 11, 23, 12, 8]
# count_1 = 0
# count_2 = 0
# for index in range(len(random_list)):
#     count_1 += 1
#     for i in range(len(random_list)):
#         count_2 += 1
#         if random_list[index] < random_list[i]:
#             random_list[index], random_list[i] = random_list[i], random_list[index]
#
# print(random_list)
# print(f"Count_1: {count_1}")
# print(f"Count_2: {count_2}")
#
# random_list = [4, 9, 7, 6, 3, 1, 2, 1.4, 22, 31, 11, 23, 12, 8]
# count_1 = 0
# count_2 = 0
#
# for _ in range(len(random_list)):
#     count_1 += 1
#     for i in range(1, len(random_list)):
#         count_2 += 1
#         if random_list[i - 1] > random_list[i]:
#             random_list[i - 1], random_list[i] = random_list[i], random_list[i - 1]
#
# print(random_list)
# print(f"Count_1: {count_1}")
# print(f"Count_2: {count_2}")
#
# random_list = [4, 9, 7, 6, 3, 1, 2, 1.4, 22, 31, 11, 23, 12, 8]
# count_1 = 0
# count_2 = 0
# for i in range(len(random_list)):
#     count_1 += 1
#     for el in range(i + 1, len(random_list)):
#         count_2 += 1
#         if random_list[i] > random_list[el]:
#             random_list[i], random_list[el] = random_list[el], random_list[i]
#
# print(random_list)
# print(f"Count_1: {count_1}")
# print(f"Count_2: {count_2}")
#

# # Задача 1. Задачи компаний
#
# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
#
# first_company = [0, 0, 0]
#
# second_company = [1, 0, 0, 1, 1]
#
# third_company = [1, 1, 1, 0, 1]
#
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
# print(f"Общий список задач: {main}")
# print(f"Кол-во невыполненных задач: {main.count(0)}")

# # Задача 2. Вредоносное ПО
# first_message = input("Первое сообщение: ")
# second_message = input("Второе сообщение: ")
# #
# first_count = 0
# first_count += first_message.count("!")
# first_count += first_message.count("?")
# second_count = 0
# second_count += second_message.count("!")
# second_count += second_message.count("?")
#
# if first_count > second_count:
#     print(f"{first_message} {second_message}")
#
# elif second_count > first_count:
#     print(f"{second_message} {first_message}")
# else:
#     print("Oops")

# # Задача 3. Пакеты
# packets = int(input("Кол-во пакетов: "))
# temp_packets = []
# decode = []
# bad_packs = 0
# for i in range(packets):
#     print(f"Пакет номер {i + 1}")
#     temp_packets = []
#     for el in range(4):
#         bit = int(input(f"{el + 1} бит: "))
#         temp_packets.append(bit)
#     if temp_packets.count(-1) <= 1:
#         decode.extend(temp_packets)
#     else:
#         bad_packs += 1
#
# print(f"Полученное сообщение: {decode}")
# print(f"Кол-во ошибок в сообщении: {decode.count(-1)}")
# print(f"Кол-во потерянных пакетов: {bad_packs}")


# 17.4 Вложенные списки
# My try
# people = int(input("How many people are playing: "))
# list_of_people = []
# last_index = 0
# for i in range(people // 3):
#     list_of_people.append(list())
#     for el in range(last_index, last_index + 3):
#         list_of_people[i].append(el + 1)
#     last_index = list_of_people[i][-1]
#
# print(list_of_people)
#
# grp_num = int(input("Group number: "))
# print(list_of_people[grp_num])
#
# gr_plyr_num = int(input("Player number: "))
# print(list_of_people[grp_num][gr_plyr_num])

# Teacher's code (Practice Code)

# N = int(input("Кол-во учасников: "))
# # N = 9
# members = []
# number = 1
# for _ in range(N // 3):
#     members.append(list(range(number, number + 3)))
#     number += 3
# print(members)
#
#
#
# word_list = [["", 0], ["", 0], ["", 0]]
#
# for i_num in range(3):
#     word = input(f"Введите {i_num + 1} слово: ")
#     word_list[i_num][0] = word
# print(word_list)
# text = input("Слово из текста: ")
# while text != "end":
#     for index in range(3):
#         if text == word_list[index][0]:
#             word_list[index][1] += 1
#     text = input("Слово из текста: ")
#
# print("\n Подсчет слов тексте")
# for index in range(3):
#     print(word_list[index][0], ":", word_list[index][1])
#
#

# Задача 1. Матрица

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i_list in matrix:
#     for i_el in i_list:
#         print(i_el, end=" ")
#     print()


# people = int(input("People playing: "))
# gr_num = int(input("Separate by group: "))
# people = 12
# gr_num = 2
# begin = 1
# if people % gr_num == 0:
#     list_of_list = list()
#
#     for i_list in range(people // gr_num):
#         print(i_list)
#         list_of_list.append(list(range(begin, gr_num + begin)))
#         begin += gr_num
#
#     print(f"Общий список команд: {list_of_list}")
#
# else:
#     print(f"\n{people} участников невозможно поделить на команды по {gr_num} человек!")


# Задача 3. Лавка

# goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
#
# fruit_name = input("Новый фрукт: ")
# price = int(input("Его цена: "))
# percentage = 8  # %
# goods.append([fruit_name, price])
#
# print(f"Новый ассортимент: {goods}")
#
# for i_list in goods:
#     i_list[1] = round(i_list[1] * (1 + percentage / 100), 2)
#
# print(f"Новый ассортимент с увел. ценой: {goods}")

# List comprehensions

# square = [x ** 2 for x in range(10)]
# print(square)

# def get_higher_price(percent, price):
#     return round(price * (1 + percent / 100), 2)
#
#
# price_now = [1.09, 23.56, 57.84, 4.56, 6.78]
# first_percent = int(input("Повышение на первый год:"))
# second_percent = int(input("Повышение на второй год:"))
#
# prices_first = [get_higher_price(first_percent, el) for el in price_now]
# prices_second = [get_higher_price(second_percent, el) for el in price_now]
#
# print(round(sum(price_now)))
# print(round(sum(prices_first)))
# print(round(sum(prices_second)))

# Задача 1. Кубы и квадраты
# start_of_range = int(input("Левая граница: "))
# end_of_range = int(input("Правая граница: "))
#
# cubes_of_range = [num ** 3 for num in range(start_of_range, end_of_range + 1)]
# square_of_range = [num ** 2 for num in range(start_of_range, end_of_range + 1)]
#
# print(f"Список кубов чисел в диапазоне от {start_of_range} до {end_of_range}: {cubes_of_range}")
# print(f"Список квадратов чисел в диапазоне от {start_of_range} до {end_of_range}: {square_of_range}")


# Задача 2. Сообщение


# word = input("Введите строку: ")
# char = input("Введите дополнительный символ: ")
# dubble_and_sep_word = [dubble * 2 for dubble in word]
# glued_word_char = [char_add + char for char_add in dubble_and_sep_word]
#
# print(f"Список удвоенных символов: {dubble_and_sep_word}")
#
# print(f"Склейка с дополнительным символом: {glued_word_char}")


# Задача 3. Повышение цен

# def formula_increasing_percent(percent, price):
#     return price * (1 + percent / 100)
#
#
# def formula_decreasing_percent(percent, price):
#     return price * (1 - percent / 100)
#
#
# current_price = [round(float(input("Цена на товар: ")), 2) for _ in range(5)]
# # current_price = [1.09, 23.56, 57.84, 4.56, 6.78]
# first_percent = int(input("Повышение на первый год: "))
# second_percent = int(input("Повышение на второй год: "))
#
# first_year = [formula_increasing_percent(first_percent, price) for price in current_price]
# second_year = [formula_increasing_percent(second_percent, price) for price in current_price]
#
# print(f"Sum of first year: {round(sum(current_price), 2)}, {round(sum(first_year), 2)}, {round(sum(second_year), 2)}")
