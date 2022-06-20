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

num = int(input("Введите число"))
summery = 0
while num != 0:
    last_num = num % 10
    num //= 10
    summery += last_num
    if last_num == 5:
        print("Обнаружен разрыв")
        break

print(summery)
