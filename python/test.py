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
import os

import socks

# import random
# import re

# from urllib.request import proxy_bypass_macosx_sysconf

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

# pack = []
# decode = []
# bad_packs = 0


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

# 18.3 List comprehensions с условиями. Модуль random

# squares_odds = [x ** 2 for x in range(1, 10 + 1) if x % 2 != 0]
# cubes_even = [x ** 3 for x in range(1, 10 + 1) if x % 2 == 0]
# squares_cubes = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(1, 10 + 1)]
#
# print(squares_odds)
# print(cubes_even)
# print(squares_cubes)

# import random
#
# fst_squad = [random.randint(50, 80) for _ in range(10)]
# snd_squad = [random.randint(30, 60) for _ in range(10)]
# print(fst_squad)
# print(snd_squad)
# squad_conditions = [("Dead" if fst_squad[i] + snd_squad[i] > 100 else "Alive") for i in range(10)]
# print(squad_conditions)


# Задача 1. Список чётных чисел

# left_range = int(input("Left Range: "))
# right_range = int(input("Right Range: "))
#
# even_list = [even for even in range(left_range, right_range + 1) if even % 2 == 0]
# print(even_list)


# Задача 2. Магазин

# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
#
# print(original_prices)
# new_prices = [0 if new < 0 else new for new in original_prices]
# print(new_prices)
# # or
# new_prices = [new for new in original_prices if new > 0]
# print(new_prices)

# Задача 3. Отряды

# monsters = 10
#
# fst_squad = [random.randint(50, 80) for _ in range(monsters)]
# snd_squad = [random.randint(30, 60) for _ in range(monsters)]
# print(fst_squad)
# print(snd_squad)
# trd_squad = [("DEAD" if fst_squad[i] + snd_squad[i] > 100 else "ALIVE") for i in range(monsters)]
#
# print(trd_squad)


# 18.4 Срезы списков
# Video Example
# server_numbers = [num for num in range(1, 100 + 1) if num % 10 == 0]
# print(server_numbers)
# new_list = server_numbers[:]
# new_list[3] = 0
#
# new_list.extend(server_numbers)
# print(new_list)
#
# out = [unic if new_list.count(unic) <= 1 else f"!{unic}" for unic in new_list]
# unic_list = [unic_only for unic_only in out if isinstance(unic_only, int)]
# print(out)
# print(unic_list)
# print(server_numbers)
# print(server_numbers[::-1])
# print(server_numbers.reverse())
# print(server_numbers)


# Задача 1. Анализ цен

# original_prices = [-12, 3, 5, -2, 1]
#
# new_prices = original_prices[:]
# print(new_prices)
# count_money_lose = [money for money in new_prices if money < 0]
# count = 0
# count_money_lose = abs([count := count - count_money_lose[i] for i in range(len(count_money_lose))][-1])
# print(count_money_lose)
#
# import random
#
# original_prices = [random.randrange(-20, 35) for _ in range(5)]
# new_prices = original_prices[:]
# print(f"Copy: {new_prices}")
#
# sum_of_lost_prices = [el for el in new_prices if el < 0]
# new_prices = [0 if minus < 0 else minus for minus in new_prices]
# print(f"Negative is Zero: {new_prices}")
# print(f"Sum of lost money: {abs(sum(sum_of_lost_prices))}")
#
# enter_str = "\n"
# print(f"{enter_str * 10}")
#
# char = "$"
# rows = 9
# rows_i = [0, rows - 1]
#
# cols = 13
# cols_i = cols - 1
#
# for row in range(rows):
#     print(f"{char}", end=" ")
#     for col in range(cols):
#         if row == rows_i[0] or row == rows_i[-1]:
#             print(f"{char}", end=" ")
#         elif col == cols_i:
#             print(f"{char}", end=" ")
#         else:
#             print(f" ", end=" ")
#     print()

# new_prices = original_prices[:]
# print(f"Copy: {new_prices}")
# new_prices = [0 if negative < 0 else negative for negative in new_prices]
# print(f"Negative is Zero: {new_prices}")
#
# print(f"Sum of lost money: {sum(new_prices) - sum(original_prices)}")


# Задача 2. Срезы

# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
#
# print(f"1. {nums[:5]}")
# print(f"2. {nums[:-2]}")
# print(f"3. {[nums[i] for i in range(len(nums)) if i % 2 == 0]}")
# print(f"4. {[nums[i] for i in range(len(nums)) if i % 2 != 0]}")
# print(f"5. {nums[::-1]}")
# print(f"6. {nums[::-2]}")


# Задача 3. Удаление части
# from random import randint
#
#
# def random_a_b(range_a=1, range_b=99):
#     a = randint(range_a, range_b)
#     b = randint(range_a, range_b)
#     while a >= b:
#         a = randint(range_a, range_b)
#         b = randint(range_a, range_b)
#
#     return [a, b]
#
#
# list_len = int(input("Length of array: "))
# # list_len = 5
# random_list = [randint(1, 99) for _ in range(list_len)]
# print(random_list)
# a_b_list = random_a_b(0, len(random_list))
# random_list = random_list[a_b_list[0]:a_b_list[1]]
# print(random_list)
# print(a_b_list)

#  18.5 Строки: индексы и срезы

# word = input("Enter word: ")
# word = "Привет"
#
# half_word = len(word) // 2
#
# first_half = word[:half_word]
# second_half = word[half_word:]
# print(first_half)
# print(second_half)
# print(first_half[::-1] + second_half[::-1])


# 18.7 Практическая работа
# Задача 1. Гласные буквы
# def intput(text):
#     return int(input(text))


# text = input("Введите текст: ")
#
# vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
#
# list_of_vowels = [vowel for vowel in text if vowel in vowels]
#
# print(f"Список гласных букв: {list_of_vowels}")
# print(f"Длина списка: {len(list_of_vowels)}")
#
#
# # Задача 2. Генерация
#
# list_len = intput("Введите длину списка: ")
#
# numbers = [1 if num % 2 == 0 else num % 5 for num in range(list_len)]
#
# print(f"Результат: {numbers}")

# Задача 3. Случайные соревнования

# import random
#
# first_group = [random.uniform(5.00, 10.00) for _ in range(20)]
# second_group = [random.uniform(5.00, 10.00) for _ in range(20)]
#
# print(f"Первая команда: {first_group}")
# print(f"Вторая команда: {second_group}")
# winners = [first_group[i] if first_group[i] > second_group[i] else second_group[i] for i in range(20)]
#
# print(f"Победители тура: {winners}")


# Задача 4. Тренируемся со срезами

# alphabet = 'abcdefg'
#
# print(f"1. {alphabet[:]}")
# print(f"2. {alphabet[::-1]}")
# print(f"3. {alphabet[::2]}")
# print(f"4. {alphabet[1::2]}")
# print(f"5. {alphabet[:1]}")
# print(f"6. {alphabet[:-2:-1]}")
# print(f"7. {alphabet[3:4]}")
# print(f"8. {alphabet[-3:]}")
# print(f"9. {alphabet[3:5]}")
# print(f"10. {alphabet[-3:-5:-1]}")


# Задача 5. Разворот

# hh = "hhqwerh"
# # hh = intput("Введите строку: ")
#
# print(hh)
# print("First H index: " + str(first_h := hh.index("h")))
# print("Last H index: " + str(last_h := hh.rindex("h")))
#
# print("Развёрнутая последовательность между первым и последним h: ", (hh[last_h - 1:first_h:-1]))


# Задача 6. Сжатие списка
# import random
#
# list_length = 10
# random_numbers = [random.randint(0, 2) for num in range(list_length)]
# print(f"Список до сжатия: {random_numbers}")
#
# zero_count = -random_numbers.count(0) if random_numbers.count(0) > 0 else len(random_numbers)
# print(zero_count)
#
# random_numbers = [x for x in random_numbers if x != 0]
# random_numbers.extend([0 for _ in range(-zero_count) if zero_count != len(random_numbers)])
#
# print(f"Переместить в конец: {random_numbers}")
# print(f"Список после сжатия: {random_numbers[:zero_count]}")

# Задача 7. Двумерный список

# amt_lists = 5
# matrix_list = [[x, x + amt_lists, x + amt_lists * 2] for x in range(1, amt_lists + 1)]
# print(matrix_list)

# Задача 8. Развлечение
# TO-DO: Проверить можно ли перевести это все в  list comprehensions
# import random
#
# sticks = intput("Количество палок: ")
# stones = intput("Количество бросков: ")
#
# list_of_sticks = list("|" * sticks)
# random_range = [[8, 10], [2, 5], [3, 6]]
# for stone in range(stones):
#     # random_range = [right_i := random.randint(1, sticks), left_i := right_i + 3]
#     print(f"Бросок {stone + 1}. Сбиты палки с номера {random_range[stone][0]}\nпо номер {random_range[stone][1]}.")
#     for j in range(len(list_of_sticks)):
#         if random_range[stone][0] <= j + 1 <= random_range[stone][1]:
#             list_of_sticks[j] = "."
# print(f"Результат: {''.join(list_of_sticks)}")
#
# '''
# Бросок 1. Сбиты палки с номера 3
# по номер 6.
# Бросок 2. Сбиты палки с номера 8
# по номер 11.
# Бросок 3. Сбиты палки с номера 3
# по номер 6.
# Результат: ||....|...'''


# Задача 9. Список списков
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20], [21], [22]]]
# open_list = [last for first in nice_list for second in first for last in second]
# print(open_list)

# open_list = []
# for first in range(len(nice_list)):
#     for second in range(len(nice_list[first])):
#         for third in range(len(nice_list[first][second])):
#             open_list.append(nice_list[first][second][third])

# print(open_list)

# players, groups, alliance = 4, 2, 2
# nice_list = [list(list(third for third in range(players)) for second in range(groups)) for first in
#              range(alliance)]

# count_of_players = 0
# unic_names = []
# for one in range(len(open_list)):
#     for two in range(len(open_list[one])):
#         for three in range(len((open_list[one][two]))):
#             if open_list[one][two][three] not in unic_names:
#                 unic_names.append(open_list[one][two][three])
#                 count_of_players += 1
#             else:
#                 print(f"not unic {open_list[one][two][three]}")
#
# print(f"Count of total player: {count_of_players}")
# print(f"Or in one line of code: {players * groups * alliance}")
# print(open_list)

# for first in range(len(nice_list)):
#     for second in range(len(nice_list[first])):
#         for third in range(len(nice_list[first][second])):
#             open_list.append(nice_list[first][second][third])

# open_list = [list(list(nice_list[first][second][third] for third in range(len(nice_list[first][second]))) for second in
#                   range(len(nice_list[first]))) for first in range(len(nice_list))]
#
# print(open_list)
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# open_list = [third for first in nice_list for second in first for third in second]
#
# print(nice_list)
# print(open_list)


# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[314, 412]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#              [[19, 20], [21], [22]]]
#
# open_list = [third_and_last for first in nice_list for second in first for third_and_last in second]
#
# print(open_list)
#
# sep_list = [list(open_list[last] for last in range(len(open_list)))]
# print(sep_list)
# players, groups, alliance = 5, 3, 3
# nice_list = [list(list(third for third in range(players)) for second in range(groups)) for first in range(alliance)]

# players = 5
# groups = 3
# alliance = 2
# sep_players_list = [list(list(list() for grp in range(groups)) for alli in range(alliance))]
# fill_with_players = []
# print(sep_players_list)


# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20], [21], [22]]]
#
# print(len(nice_list))
# print(len(nice_list[0]))
# print(len(nice_list[0][0]))
# open_list = [numbers for first in nice_list for second in first for numbers in second]
# print(open_list)
#


# Задача 10. Шифр Цезаря

# alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
#             "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
#
#
# text = "это я сделел питон"
# shift = 777
#
# encoded_text = ""
# for i in range(len(text)):
#     if text[i] in alphabet:
#         index = alphabet.index(text[i])
#         encoded_text += alphabet[(index + shift) % len(alphabet)]
#     else:
#         encoded_text += " "
#
# print(encoded_text)

# Задача 10. Шифр Цезаря Teacher
# alphabet = "".join(alphabet)


# def caeser_cipher(string, user_shift):
#     char_lsit = [alphabet[(alphabet.index(sym) + user_shift) % 33] if sym in alphabet else sym for sym in string]
#     return "".join(char_lsit)


# input_str = "это же я питон"
# shift = 3
# output_str = caeser_cipher(input_str, shift)
# print(output_str)

# 17.6 Практическая работа

# Задача 8. Считалка

# people = 5
# shift = 7
# people_list = list(range(1, people + 1))
#
# print(people_list)
#
# current = 0
#
# for _ in range(len(people_list) - 1):
#     start_count = current % len(people_list)
#     current = (start_count + shift - 1) % len(people_list)
#     people_list.remove(people_list[current])
#     print(people_list)


# 19.2 Форматирование строк: format и f-strings


# while True:
#     grants_template = input("Введите шаблон поздравления, в шаблоне использовать конструкцию {name} и {age}: ")
#
#     if "{name}" in grants_template and "{age}" in grants_template:
#         break
#     print("Ошибка! Нет {name} и {age} в шаблоне.")
#
# print("Введине список имен (end) ")
#
# name_list = input("Список людей через ,:").split(", ")
# ages_str = input("Возраст через пробел: ")
# ages = [int(i_num) for i_num in ages_str.split()]
#
# for i_man in range(len(name_list)):
#     print(grants_template.format(name=name_list[i_man], age=ages[i_man]))
#
# people = [
#     " ".join([name_list[i_man], str(ages[i_man])])
#     for i_man in range(len(name_list))]
#
# people_str = ", ".join(people)
#
# print(": ".join(["Имининики", people_str]))


# HOOMEWORK

# Задача 1. Заказ
#
# name = input("Enter your name: ")
# s_number = int(input("Enter number: "))
#
# print("Здравствуйте, {name}! Ваш номер заказа: {number}.  Приятного дня!".format(name=name, number=s_number))

# Задача 2. Долги

# name = input("Имя: ")
# dolg = int(input("Долг: "))
#
# text = "{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!".format(name, dolg)
#
# print(text)

# Задача 3. IP-адрес

# while True:
#     ip_address = input("Шаблон {num}: ")
#     if "{num}" in ip_address:
#         break
#     else:
#         print("Enter {num}")
#
# ip = []
# for _ in range(4):
#     num = int(input("Введите номер: "))
#     if 0 <= num <= 255:
#         ip.append(str(num))
#     else:
#         print("Такого номера не существует.")
#         break
#
# print(ip_address.format(num=".".join(ip)))


# 19.3 Методы строк: split и join

# Задача 1. Улучшенная лингвистика 2


# 19.4 Методы строк: startswith, endswith, upper, lower

# while True:
#     user_name = input("Username: ")
#     file_name = input("File Name: ")
#     disk_name = input("Disk Name: ")
#
#     path = "{disk}:/{user}/folder/{file}".format(disk=disk_name.upper(), user=user_name, file=file_name)
#
#     if not path.endswith(".txt"):
#         print("Ошибка ввода файла. Файл должен быть текстовым.")
#     elif not path.startswith("C:/"):
#         print("Ошибка ввода диска. Диск должен быть системным.")
#     else:
#         print("Путь к файлу:", path)
#
#     if input() == "end":
#         break


# Задача 1. Шифр Цезаря 2


# def caesar(string, shift):
#     string = string.lower()
#     char_list = [alphabet[(alphabet.index(sym) + shift) % 33] if sym != " " else " " for sym in string]
#     return "".join(char_list)
#
#
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#
# print(caesar("пРивет Это же Я", 5))


# Задача 2. Путь к файлу

# user_path = input("Путь к файлу: ")
#
# correct_drive = "На каком диске должен лежать файл: C"
# corrent_extnsion = "Требуемое расширение файла: .txt"
# print(correct_drive)
# print(corrent_extnsion)
#
# if not user_path.startswith("C:/"):
#     print("Не правельный диск.")
# elif not user_path.endswith(".txt"):
#     print("Не правельное расширение файла.")
# else:
#     print("Путь корректен!")


# Задача 3. Удаление части


# text = input("Text: ")
#
# low = len([sym for sym in text if sym.islower()])
# upp = len([sym for sym in text if sym.isupper()])
#
# if low > upp:
#     print(text.lower())
# else:
#     print(text.upper())


# 19.6 Практическая работа

# Задача 1. Меню ресторана


# menu = ", ".join(input("Menu exmple;example2: ").split(";"))
#
# print(menu)

# Задача 2. Самое длинное слово

# text = input("Введите строку: ").split()
#
# print("Самое длинное слово: {}".format(height_word := max(text, key=len)))
# print("Длина этого слова: ", len(text[text.index(height_word)]))

# Задача 3. Файлы

# deprecated_char = ["@", "№", "$", "%", "^", "&", "*", "()"]
# exepted_extensions = [".txt", ".docx"]
#
# file = input("Название файла: ")
#
# if not file.endswith(tuple(exepted_extensions)):
#     print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
#
# elif file.startswith(tuple(deprecated_char)):
#     print("Ошибка: название начинается на один из специальных символов.")
# else:
#     print('Файл назван верно:', file)

# Задача 4. Заглавные буквы

# def capital_letter_each_word(string):
#     print(string)
#     return " ".join([word.capitalize() for word in string])
#
#
# some_text_input = input("First letter of all words are capital: ").split()
# changed_text = capital_letter_each_word(some_text_input)
#
# print(changed_text)


# Задача 5. Пароль


# min_char_included = 8
# min_upper_letter = 1
# min_amt_numbers = 3
#
# flag = True
# while flag:
#     current_upper_letter = 0
#     current_amt_numbers = 0
#     password = input("Придумайте пароль: ")
#
#     for char in password:
#         if char.isdigit():
#             current_amt_numbers += 1
#         elif char.isupper():
#             current_upper_letter += 1
#
#     if len(password) >= min_amt_numbers \
#             and current_upper_letter >= min_upper_letter \
#             and current_amt_numbers >= min_amt_numbers:
#         print("Это надёжный пароль!")
#         flag = False
#     else:
#         print("Пароль ненадёжный. Попробуйте ещё раз.")


# Задача 6. Сжатие

# long_string = "aaAAAabbFFbcddffeeg"
#
# short_string = ""
# count = 0
# letter_count = long_string[0]
#
# long_string += "1"
# for i_letter in range(len(long_string)):
#     if letter_count == long_string[i_letter]:
#         count += 1
#     elif letter_count != long_string[i_letter]:
#         if count > 1:
#             short_string += letter_count + str(count)
#         else:
#             short_string += letter_count
#         count = 1
#         letter_count = long_string[i_letter]
#
# print(short_string)


# v=2

# long_string = "aaAAAabbFFbcddffeegggeefeewwwwee"
#
# short_string = ""
#
# long_string += " "
# count = 1
# for letter in range(len(long_string) - 1):
#     if long_string[letter] != long_string[letter + 1]:
#         short_string += long_string[letter] + str(count)
#         count = 1
#     else:
#         count += 1
#
# print(short_string)
# import pyautogui

# thoughts = "Я не могу принять тот факт, что в нашей жизни" \
#            " писутствуют люди которые полностью не соответствуют моим" \
#            " предстовлением о человечности."
#
# additional_thoughts = "Я тебя очень люблю. Но ты же знаешь, что у меня привалирует логика над всем остальным?" \
#                       " Я знаю, что будет со мной если они останутся в нашей жизни, с нашими отнашениями." \
#                       "Я не хочу, чтоб мы страдали в них. И да, я прекрасно понимаю, что ты скажешь, что при принятии" \
#                       " условий страдать будешь ты. Но я утверждаю, что при откланении страдать будем оба и наши" \
#                       " отношения будет деградировать." \
#                       " это не обратимо. Я своего отнашения к ним поменять не смогу. А ты не будешь счаслива со мной" \
#                       " ведь у меня постоянно присутствует к ним отвращение." \
#                       ""
#
#
# def key_changer(string):
#     russian = "йцукенгшщзхъфывапролджэячсмитьбю."
#     english = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
#
#     new_text = ""
#     for char in string:
#         if char.lower() in russian or char == " ":
#
#             if char != " ":
#                 i = russian.index(char.lower())
#                 new_text += english[i].upper() if char.isupper() else english[i]
#             else:
#                 new_text += " "
#         else:
#             new_text += ""
#     return new_text
#


# Задача 7. IP-адрес 2

# address = input("Введите IP address: ").split(".")
#
# if len(address) != 4:
#     print("Адрес — это четыре числа, разделённые точками.")
# else:
#     correct = None
#     for num in address:
#         if not num.isdigit():
#             print("{0} — это не целое число.".format(num))
#             correct = False
#             break
#         elif not 0 < int(num) <= 255:
#             print("{0} превышает 255.".format(num))
#             correct = False
#             break
#         else:
#             correct = True
#     if correct:
#         print("IP-адрес корректен.")


# address = input("Введите IP address: ").split(".")
#
#
# def check(number):
#     if not number.isdigit():
#         return 0
#     elif not 0 <= int(number) <= 255:
#         return 1
#     else:
#         return 2
#
#
# def answer(code, err):
#     if code == 0:
#         print("{0} — это не целое число.".format(err))
#     elif code == 1:
#         print("{0} превышает 255.".format(err))
#     elif code == 2:
#         print("IP-адрес корректен.")
#
#
# if len(address) != 4:
#     print("Адрес — это четыре числа, разделённые точками.")
# else:
#     res = None
#     num = None
#     for num in address:
#         res = check(num)
#         if res != 2:
#             answer(res, num)
#             break
#     else:
#         answer(res, num)

# 20.1 Словарь: основы

# student_str = input("Введите информацию о студенте\n"
#                     "(имя, фамилия, город, место учебы, оценки:")
# student_str = "Vitaly Kashubin Moscow MIT 5 1 81 2"
# student_keys = ["Имя", "Фамилия", "Город", "Место учебы", "Оценки"]
# student_info = student_str.split()
# student = dict()
# for i in range(len(student_keys)):
#     student[student_keys[i]] = student_info[i]
#     if student_keys[-1] == student_keys[i]:
#         student[student_keys[i]] = " ".join(student_info[i:])
#
# print(student)
#
# for i_info in student:
#     if i_info == "Оценки":
#         print("{0} - {1}".format(i_info, ", ".join(student[i_info].split())))
#     else:
#         print("{0} - {1}".format(i_info, student[i_info]))
#


# Задача 1. Словарь квадратов чисе

# num = int(input("Max Key: "))
#
# res_dict = dict()
# for key in range(1, num + 1):
#     res_dict[key] = key ** 2
#
# print(res_dict)


# Задача 2. Студент

# student_info_string = input(
#     "Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ").split()
#
# student_info_dict = dict()
# student_pre_info = "имя, фамилия, город, место учёбы, оценки".title().split(", ")
#
# size_difference = len(student_pre_info) - len(student_info_string)  # if !0 delete cut len tail
#
# for i_info in range(len(student_pre_info) - 1):
#     student_info_dict[student_pre_info[i_info]] = student_info_string[i_info]
#     print("{0} - {1}".format(student_pre_info[i_info], student_info_string[i_info]))
# else:
#     scores = ", ".join(student_info_string[len(student_pre_info) - 1:])
#     student_info_dict[student_pre_info[-1]] = scores
#     print("{0} - [{1}]".format(student_pre_info[-1], scores))


# Задача 3. Контакты

# amount_of_contacts = int(input("Сколько контактов?"))
#
# contacts_book = dict()
#
# while amount_of_contacts != 0:
#     print("Текущие контакты на телефоне:")
#     if len(contacts_book) > 0:
#         for contact in contacts_book:
#             print("{name} {phone}".format(name=contact, phone=contacts_book[contact]))
#     else:
#         print("<Пусто>")
#     print()
#     contact_name = input("Name: ")
#     contact_phone = input("Tel: ")
#     print()
#     contacts_book[contact_name] = contact_phone
#     amount_of_contacts -= 1
# else:
#     for contact in contacts_book:
#         print("{name} {phone}".format(name=contact, phone=contacts_book[contact]))
#
# print()


# 20.2 Методы словарей
# 1
# def histogram(string):
#     sym_dict = dict()
#     for sym in string:
#         if sym in sym_dict:
#             sym_dict[sym] += 1
#         elif sym != " ":
#             sym_dict[sym] = 1
#
#     return sym_dict
#
#
# text = input("Введите текст: ").lower()
#
# hist = histogram(text)
#
# print(hist)
#
# for i_sym in sorted(hist.keys()):
#     print("{0} : {1}".format(i_sym, hist[i_sym]))
#
# print("Max value: {0}".format(max(hist.values())))


# 2

# phone_book = {
#     "Vitaly": 100,
#     "Marina": 1907,
#     "Tenzin": 1001
# }
#
# other_book = {
#     "Sonya": 123,
#     "Boekin": 112,
#     "Tenzin": 1
# }
#
# phone_book.update(other_book)
# phone_book.pop("Boekin")
# print(phone_book)


# Задача 1. Склады


# small_storage = {
#
#     'гвозди': 5000,
#
#     'шурупы': 3040,
#
#     'саморезы': 2000
#
# }
#
# big_storage = {
#
#     'доски': 1000,
#
#     'балки': 150,
#
#     'рейки': 600
#
# }
#
# big_storage.update(small_storage)
#
# search_item = input("Введите название тавара: ").lower()
#
# if big_storage.get(search_item):
#     print("Кол-во {1} тавара {0}".format(search_item, big_storage.get(search_item)))
#
# else:
#     print("Такого товара у нас нет")


# Задача 2. Кризис фруктов


# incomes = {
#
#     'apple': 5600.20,
#
#     'orange': 3500.45,
#
#     'banana': 5000.00,
#
#     'bergamot': 3700.56,
#
#     'durian': 5987.23,
#
#     'grapefruit': 300.40,
#
#     'peach': 10000.50,
#
#     'pear': 1020.00,
#
#     'persimmon': 310.00,
#
# }
#
# total_salary = 0
#
# for fruit_price in incomes.values():
#     total_salary += fruit_price
#
# print("Общий доход за год составил {0} рублей".format(total_salary))
# print()
# for fruit, price in incomes.items():
#     if price == min(incomes.values()):
#         print("Самый маленький доход у {fuit}. Он составляет {price} рублей".format(fuit=fruit, price=price))
#         print()
#         incomes.pop(fruit)
#         break
#
# print(incomes)


#  20.3 Вложенные словари и значения по умолчанию в get

# Задача 1. Член семьи

# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
#
#
# def find_child_name(name):
#     for child in family_member["children"]:
#         for el in child.values():
#             print(el, end=" ")
#         print()
#
#
# find_child_name("Bob")
# # find_child_name("Rob")


# Задача 2. Игроки


# players_dict = {
#
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
#
# }
#
# print("1. Все члены команды из команды А, которые отдыхают.")
# first_line = [player.get("name") for player in players_dict.values() if
#               player.get("team") == "A" and player.get("status") == "Rest"]
#
# print(first_line)
# print("2. Все члены команды из группы B, которые тренируются.")
#
# second_ling = [player.get("name") for player in players_dict.values() if
#                player.get("team") == "B" and player.get("status") == "Training"]
#
# print(second_ling)
#
# print("3. Все члены команды из команды C, которые путешествуют.")
#
# third_line = [player.get("name") for player in players_dict.values() if
#               player.get("team") == "C" and player.get("status") == "Travel"]

# print(third_line)

# 20.4 Множества. Функция set

# import random
#
# number_list = [random.randint(1, 4) for _ in range(10)]
# print(number_list)
#
# print(set(number_list))

# Задача 1. Пунктуация


# string = input("Введите строку:")
#
# char_includes = {".", ",", ";", ":", "!", "?"}
# count = 0
# for char in string:
#     if char in char_includes:
#         count += 1
#
# print("Количество знаков пунктуации: {0}".format(count))


# Задача 2. Семинар
# import random
#
# nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
# nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21,
#           21]
# nums_1 = set(nums_1)
# nums_2 = set(nums_2)
# print("1-е множество: {0}".format(nums_1))
# print("2-е множество: {0}".format(nums_2))
#
# print()
# print("Минимальный элемент 1-го множества: {0}".format(min(nums_1)))
# print("Минимальный элемент 2-го множества: {0}".format(min(nums_2)))
# nums_1.discard(min(nums_1))
# nums_2.discard(min(nums_2))
#
# random_num_1 = random.randint(100, 200)
# random_num_2 = random.randint(100, 200)
# print()
# print("Случайное число для 1-го множества: {0}".format(random_num_1))
# print("Случайное число для 2-го множества: {0}".format(random_num_2))
#
# nums_1 |= {random_num_1}
# nums_2 |= {random_num_2}
#
# print()
# print("Объединение множеств: {0}".format(nums_1 | nums_2))
#
# print("Пересечение множеств: {0}".format(nums_1 & nums_2))
#
# print("Элементы, входящие в nums_2, но не входящие в nums_1: {0}".format(nums_2 - nums_1))


# Задача 3. Различные цифры


# char_string = input("Введите строку: ")
# # char_string = "ab1n32kz2"
#
# diff_char = set()
# for char in char_string:
#     if char.isdigit():
#         diff_char.add(char)
#         diff_char |= {char}
#
# print("Различные цифры строки: {0}".format("".join(sorted(list(diff_char)))))

# 20.5 Генерация словарей

# data = [
#     {"id": 10, "user": "Bob"},
#     {"id": 11, "user": "Misha"},
#     {"id": 12, "user": "Anton"},
#     {"id": 10, "user": "Bob"},
#     {"id": 11, "user": "Misha"},
#     {"id": 11, "user": "Misha"},
#     {"id": 11, "user": "Misha"},
#     {"id": 144, "user": "Masha"},
#
# ]
#
# unique_data = []
# #
# for entry in data:
#     if entry not in unique_data:
#         unique_data.append(entry)
#
# print(unique_data)
# unique_data = []
# ##
# for entry in data:
#     data_exist = False
#     for unique_entry in unique_data:
#         if entry["id"] == unique_entry["id"]:
#             data_exist = True
#
#     if not data_exist:
#         unique_data.append(entry)
#
# print(unique_data)
# ###
# unique_data_dict = {entry["id"]: entry for entry in data}
#
# print(unique_data_dict)

# 20.6 Практическая работа

# Задача 1. Песни 2

# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }

# number_of_songs = int(input("Сколько песен выбрать? "))
# if number_of_songs > len(violator_songs):
#     print("Кол-во песен меньше {0}. Ввдедите число от 1 до {1}".format(number_of_songs, len(violator_songs)))
#
# total_song_time = 0
# for i in range(1, number_of_songs + 1):
#     song_name = input("Название {0} песни: ".format(i))
#     if song_name in violator_songs:
#         total_song_time += violator_songs[song_name]
#     else:
#         print("There is no song named {0}".format(song_name))
#
# print("Общее время звучания песен: {0} минут".format(round(total_song_time, 2)))


# Задача 2. География

# number_of_countries = int(input("Кол-во стран: "))
#
# country_info_dict = {}
# for i in range(1, number_of_countries + 1):
#     name_of_countrie = input("{0} страна: ".format(i)).split()
#     country_info_dict |= {name_of_countrie[0]: name_of_countrie[1:]}
#
# print(country_info_dict)
#
# for i in range(1, 4):
#     city = input("{0} город: ".format(i))
#
#     for country in country_info_dict:
#         if city in country_info_dict[country]:
#             print(f"Город {city} расположен в стране {country}")
#             break
#     else:
#         print(f"По городу {city} данных нет.")
#     print()


# Задача 3. Криптовалюта


# data = {
#     "address": "0x544444444444",
#     "ETH": {
#         "balance": 444,
#         "totalIn": 444,
#         "totalOut": 4
#     },
#     "count_txs": 2,
#     "tokens": [
#         {
#             "fst_token_info": {
#                 "address": "0x44444",
#                 "name": "fdf",
#                 "decimals": 0,
#                 "symbol": "dsfdsf",
#                 "total_supply": "3228562189",
#                 "owner": "0x44444",
#                 "last_updated": 1519022607901,
#                 "issuances_count": 0,
#                 "holders_count": 137528,
#                 "price": False
#             },
#             "balance": 5000,
#             "totalIn": 0,
#             "total_out": 1
#         },
#         {
#             "sec_token_info": {
#                 "address": "0x44444",
#                 "name": "ggg",
#                 "decimals": "2",
#                 "symbol": "fff",
#                 "total_supply": "250000000000",
#                 "owner": "0x44444",
#                 "last_updated": 1520452201,
#                 "issuances_count": 0,
#                 "holders_count": 20707,
#                 "price": False
#             },
#             "balance": 500,
#             "totalIn": 0,
#             "total_out": 2
#         }
#     ]
# }
#
# print("DATA ")
# print(data)
# print()
#
# print("1. Вывести списки ключей и значений словаря.")
# print(data.keys())
# print(data.values())
# print()
#
# print("2. В “ETH” добавить ключ “total_diff” со значением 100.")
# data["ETH"]["total_diff"] = 100
# print("ETH:", data["ETH"])
# print()
#
# print("3. Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.")
# data["tokens"][0]["fst_token_info"]["name"] = "doge"
# print(data)
# print()
#
# print("4. Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.")
# data["ETH"]["total_out"] = 0
# for token in data["tokens"]:
#     data["ETH"]["total_out"] += token.pop("total_out")
#
# print(data)
# print()
#
# print("5. Внутри 'sec_token_info' изменить название ключа 'price' на 'total_price'.")
# data["tokens"][1]["sec_token_info"]["total_price"] = data["tokens"][1]["sec_token_info"].pop("price")
# print(data)
# print()


# Задача 4. Товары


# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678'
# }
#
# store = {
#     '12345': [
#         {
#             'quantity': 27,
#             'price': 42
#         }
#     ],
#     '23456': [
#         {
#             'quantity': 22,
#             'price': 510
#         },
#         {
#             'quantity': 32,
#             'price': 520
#         },
#     ],
#     '34567': [
#         {
#             'quantity': 2,
#             'price': 1200
#         },
#         {
#             'quantity': 1,
#             'price': 1150
#         }
#     ],
#     '45678': [
#         {
#             'quantity': 50,
#             'price': 100
#         },
#         {
#             'quantity': 12,
#             'price': 95
#         },
#         {
#             'quantity': 43,
#             'price': 97
#         }
#     ]
# }
# all_items = ""
#
# for item in goods:
#     code = goods[item]
#     all_items += str(store[code]) + "\n"
#     total_quantity = 0
#     total_price = 0
#     for qnt in store[code]:
#         total_quantity += qnt["quantity"]
#         total_price += qnt["quantity"] * qnt["price"]
#     print(f"{item} - {total_quantity} шт, стоимость {total_price} руб", end="\n")

# Задача 5. Гистограмма частоты 2

# text = input("Enter text: ")
# def count_chars(string):
#     # string = "".join(string.split(" "))
#     new_dict = {}
#     for char in string:
#         if char not in new_dict:
#             new_dict[char] = 1
#         else:
#             new_dict[char] += 1
#     # print(", \n".join(str(new_dict).split(", ")))
#     return new_dict
#
#
# def invert_dict(dictionary):
#     new_dict = {}
#     for key, values in dictionary.items():
#         if values not in new_dict:
#             new_dict[values] = [key]
#         else:
#             new_dict[values].append(key)
#     return new_dict
#
#
# text = "Здесь что-то написано"
#
# my_dict = count_chars(text)
#
# print("Оригинальный словарь частот:\n\n" + ",\n".join(str(my_dict).split(", "))[1:-1])
# print()
# print("Инвертированный словарь частот:\n\n" + "],\n".join(str(invert_dict(my_dict)).split("], "))[1:-1])


# Задача 6. Словарь синонимов

# number_of_pairs = int(input("Введите количество пар слов: "))
#
# dict_pairs = {}
# for i in range(1, number_of_pairs + 1):
#     pair = input("{0} пара: ".format(i)).split(" - ")
#     dict_pairs[pair[0]] = pair[1]
#
# word = input("Введите слово: ").title()
#
# if word in dict_pairs:
#     synonim = dict_pairs[word]
#     print("Синоним: {0}".format(synonim))
# elif word in dict_pairs.values():
#     for el in dict_pairs:
#         if dict_pairs[el] == word:
#             print("Синоним: {0}".format(el))
# else:
#     print("Такого слова в словаре нет.")

# Задача 7. Пицца

# orders_N = int(input("Введите кол-во заказов: "))
# #
# name = None
# pizza = None
# count_pizza = 0
#
# pizza_orders = {}
# #
# for i in range(1, orders_N + 1):
#     name, pizza = input("{0} заказ: ".format(i)).split()
#     if name not in pizza_orders:
#         pizza_orders["name"] = {}
#     if pizza in pizza_orders[name]:
#         pizza_orders[name][pizza] += int(count_pizza)
#     else:
#         pizza_orders[name][pizza] = int(count_pizza)
# #
# print(pizza_orders)

# Задача 8. Угадай число

# import random

# max_guess_N = int(input("Введите максимальное число: "))

# random_number = str(random.randint(1, max_guess_N))
# random_number = "3"
# print(random_number)
#
# include_set = set()
# bad_list = []
# while True:
#     list_of_guesses = input("Нужное число есть среди вот этих чисел: ").split()
#
#     if list_of_guesses[0] == "Помогите!" or not list_of_guesses[0].isdigit():
#         break
#     elif random_number in list_of_guesses:
#         answer = "Да"
#         include_set |= {num for num in list_of_guesses}
#     else:
#         answer = "Нет"
#         bad_list.extend(list_of_guesses)
#
#     print("Ответ Артёма: {0}".format(answer))
#
# print("Артём мог загадать следующие числа: {0}".format(include_set - set(bad_list)))


# Задача 9. Родословная


# people_N = int(input("Введите количество человек: "))
#
# tree = {}
# for i in range(1, people_N):
#     pair = input("{0} пара: ".format(i)).split()
#     if pair[-1] not in tree:
#         tree[pair[-1]] = {pair[0]: {}}
#     else:
#         tree[pair[-1]][pair[0]] = {}
#     print(tree)
#
# print(tree.values())


# 21.1 Разбор домашнего задания

# def is_poly(string):
#     char_dict = {}
#     for i_char in string:
#         char_dict[i_char] = char_dict.get(i_char, 0) + 1
#
#     count = 0
#     for odd in char_dict.values():
#         if odd % 2 == 0:
#             count += 1
#     if count > 1:
#         return True
#     else:
#         return False
#
#
# my_string = input("Введите строку: ")
#
# if is_poly(my_string):
#     print("Можно сделать полиндромом")
# else:
#     print("Нельзя сделать полиндромом")


# 21.2 Кортежи

# Задача 1. Создание кортежей

# import random
#
# random_number = random.randint(1, 6)
#
# my_tuple_1 = tuple([random.randint(1, 5) for _ in range(5)])
# my_tuple_2 = tuple([random.randint(-5, 0) for _ in range(5)])
#
# print(my_tuple_1)
# print(my_tuple_2)
#
# my_tuple_3 = tuple(list(my_tuple_1) + list(my_tuple_2))
#
# print(my_tuple_3)
#
# print("Num of 0`s: {0}".format(my_tuple_3.count(0)))


# Задача 2. Цилиндр

# r = int(input("Введите радиус: "))
# h = int(input("Введите высоту: "))
#
#
# def cylinder_area(radius, height):
#     pi = 3.141592653589793
#     S = pi * r ** 2
#     side = 2.0 * pi * r * h
#     full = side + 2 * S
#     return side, full
#
#
# print("Площадь боковой поверхности (r — радиус, h — высота): {0}".format(cylinder_area(r, h)[0]))
#
# print("Полная площадь (S — площадь круга): {0}".format(cylinder_area(r, h)[1]))

# Задача 3. Неправильный код


# import random
#
#
# def change(nums):
#     nums = list(nums)
#     index = random.randint(0, 4)
#
#     value = random.randint(100, 1000)
#
#     nums[index] = value
#
#     return nums, value
#
#
# my_nums = 1, 2, 3, 4, 5
#
# new_nums, rand_val = change(my_nums)
#
# print(new_nums, rand_val)
#
# new_tuple = change(my_nums)
#
# new_nums = new_tuple[0]
# rand_val += new_tuple[1]
#
# print(new_nums, rand_val)


# 21.3 Функция enumerate. Перебор нескольких значений

# Задача 1. Саботаж!

# text = input("Введите текст: ")
#
# find_index_of_el = "~"
#
# total_i_of_el = ""
#
# for i, char in enumerate(text):
#     if char == find_index_of_el:
#         total_i_of_el += "{index} ".format(index=str(i))
#
# else:
#     if len(total_i_of_el) == 0:
#         print("Not {0} found".format(find_index_of_el))
#     else:
#         print(total_i_of_el)


# Задача 2. Словари из списков


# import random

# input_letter = input("Letter: ")
# first_letter = ord(input_letter)
# print(first_letter)
#
# while input_letter != "stop":
#     letter = input("Letter: ")
#     first_letter = ord(letter)
#     print(first_letter)

###########

# import string
# import random

# letter_list = random.choices(string.ascii_lowercase, k=10)

# a = ord(input("Диапозон букв (а, я): "))
# b = ord(input("Диапозон букв (а, я): "))
# start_range = ord("а")
# end_range = ord("я")
# letter_list_1 = []
# letter_list_2 = []
#
# for _ in range(10):
#     letter_list_1.append(chr(random.randint(start_range, end_range)))
#     letter_list_2.append(chr(random.randint(start_range, end_range)))
#
# print("Первый список: {0}".format(letter_list_1))
# print("Второй список: {0}".format(letter_list_2))
#
# print()
# letter_dict_1 = {i: letter for i, letter in enumerate(letter_list_1)}
# letter_dict_2 = {i: letter for i, letter in enumerate(letter_list_2)}
#
# print("Первый словарь: {0}".format(letter_dict_1))
# print("Второй словарь: {0}".format(letter_dict_2))

# Задача 3. Универсальная программа

# text = 100, 200, 300, 'буква', 0, 2, 'а'

# text = "О Дивный Новый мир!"


# text = [100, 200, 300, 'буква', 0, 2, 'а']


# text = {1: "100", 2: "200", 3: "300", 4: "буква", 5: "0", 6: "2", 7: "a"}


# def iter_list(i_object):
#     new_list = []
#     if isinstance(i_object, dict):
#         for index, value in enumerate(i_object.values()):
#             if index % 2 == 0:
#                 new_list.append({index + 1: value})
#     else:
#         for index, element in enumerate(i_object):
#             if index % 2 == 0:
#                 new_list.append(element)
#
#     return new_list
#
#
# print(iter_list(text))


#  21.4 Перебор ключей и значений в словаре. Метод items

# Задача 1. Кризис миновал

# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00
# }
#
# for fruit, price in incomes.items():
#     print("{0}--{1}".format(fruit, price))
#     print()


# Задача 2. Сервер

# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     },
# }
# for key, value in server_data.items():
#     if isinstance(value, dict):
#         print("{key}:".format(key=key))
#         for inner_key, inner_value in value.items():
#             print("\t{key}: {value}".format(key=inner_key, value=inner_value))
#     else:
#         print("{key}: {value}".format(key=key, value=value))


# Задача 3. В одну строчку

# print([value for key, value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if key % 2 == 0])


# 21.5 Составные ключи


# Задача 1. Паспортные данные

# passport_data = {
#
#     (5000, 123456): ('Иванов', 'Василий'),
#
#     (6000, 111111): ('Иванов', 'Петр'),
#
#     (7000, 222222): ('Медведев', 'Алексей'),
#
#     (8000, 333333): ('Алексеев', 'Георгий'),
#
#     (9000, 444444): ('Георгиева', 'Мария')
#
# }
# #
# find_by_pass = input("Введите номер и серию паспорта: ")
#
# for pass_info, user_info in passport_data.items():
#     if str(pass_info[0]) in find_by_pass and str(pass_info[1]) in find_by_pass:
#         print(user_info)

# Задача 2. Контакты 2


# contact_book = {}
# while True:
#     contact_name = input("Введите имя: ")
#     contact_surname = input("Введите фамилию: ")
#     contact_phone = int(input("Введите телефон: "))
#
#     if f"{contact_name}.{contact_surname}." in contact_book:
#         print("{0} уже в базе.".format(contact_name))
#         change = input("Хотите изменить номер телефона?>")
#     else:
#         contact_book["{name}.{surname}.".format(name=contact_name, surname=contact_surname)] = contact_phone
#     print(contact_book)

# 21.8 Практическая работа


# students = {
#     1: {
#         'name': 'Bob',
#         'surname': 'Vazovski',
#         'age': 23,
#         'interests': ['biology, swimming']
#     },
#     2: {
#         'name': 'Rob',
#         'surname': 'Stepanov',
#         'age': 24,
#         'interests': ['math', 'computer games', 'running']
#     },
#     3: {
#         'name': 'Alexander',
#         'surname': 'Krug',
#         'age': 22,
#         'interests': ['languages', 'health food']
#     }
# }
#
# for i_id, i_student in students.items():
#     print("{0} - {1}".format(i_id, i_student["age"]))
#
#
# def get_total_hobby_and_family(dictionary):
#     total_fam_len = 0
#     total_hobbies_list = []
#     for student in dictionary.values():
#         total_fam_len += len(student["surname"])
#         total_hobbies_list.extend(student["interests"])
#     return total_hobbies_list, total_fam_len
#
#
# total_hobbies, total_family_len = get_total_hobby_and_family(students)

# students = {
#     1: {
#         'name': 'Bob',
#         'surname': 'Vazovski',
#         'age': 23,
#         'interests': ['biology, swimming']
#     },
#     2: {
#         'name': 'Rob',
#         'surname': 'Stepanov',
#         'age': 24,
#         'interests': ['math', 'computer games', 'running']
#     },
#     3: {
#         'name': 'Alexander',
#         'surname': 'Krug',
#         'age': 22,
#         'interests': ['languages', 'health food']
#     }
# }
#
#
# def get_total_hobby_and_family(dictionary):
#     total_hobbies = []
#     string = ''
#
#     for key, value in dictionary.items():
#         total_hobbies += (dictionary[key]['interests'])
#         string += dictionary[key]['surname']
#
#     total_fam_len = 0
#     for _ in string:
#         total_fam_len += 1
#
#     return total_hobbies, total_fam_len
#
#
# pairs = []
#
# for i in students:
#     pairs += (i, students[i]['age'])
#
# my_lst = get_total_hobby_and_family(students)[0]
#
# l = get_total_hobby_and_family(students)[1]
#
# print(my_lst, l)


# students = {
#
#     1: {
#
#         'name': 'Bob',
#
#         'surname': 'Vazovski',
#
#         'age': 23,
#
#         'interests': ['biology', 'swimming']
#
#     },
#
#     2: {
#
#         'name': 'Rob',
#
#         'surname': 'Stepanov',
#
#         'age': 24,
#
#         'interests': ['math', 'computer games', 'running']
#
#     },
#
#     3: {
#
#         'name': 'Alexander',
#
#         'surname': 'Krug',
#
#         'age': 22,
#
#         'interests': ['languages', 'health food']
#
#     }
#
# }
#
#
# def get_all_hobbies_and_get_total_fam_len(my_dict):
#     all_hobbies = []
#     total_len_fam = 0
#     for student in my_dict:
#         all_hobbies.extend(my_dict[student]['interests'])
#         total_len_fam += len(my_dict[student]['surname'])
#
#     return all_hobbies, total_len_fam
#
#
# pairs = []
#
# for student_id, student in students.items():
#     pairs.extend((student_id, student['age']))
#
# total_amt_hobbies, family_char_length = get_all_hobbies_and_get_total_fam_len(students)
#
# print(pairs)
# print(total_amt_hobbies, family_char_length)

# Задача 2. Универсальная программа 2

# text = 100, 200, 300, 'буква', 0, 2, 'а'
# text = "О Дивный Новый мир!"
# text = [100, 200, 300, 'буква', 0, 2, 'а', 1, 3, 4, 5, 6, 12, 33, 13, 44, 41, 123, 32]

# text = {1: "100", 2: "200", 3: "300", 4: "буква", 5: "0", 6: "2", 7: "a", 8: "b", 9: "as",
#         10: 'sorry', 11: "else", 12: "no", 13: "so", 14: "bam", 15: "nana", 16: "lapa", 17: "22",
#         18: "naman", 19: "12222"}


# def is_prime(iterable):
#     new_list = []
#     if isinstance(iterable, dict):
#         iterable = iterable.items()
#     else:
#         iterable = enumerate(iterable)
#
#     for index, el in iterable:
#         count = 0
#         if index >= 2:
#             for idx in range(index, 0, -1):
#                 if index % idx == 0:
#                     count += 1
#             if count <= 2:
#                 new_list.append(el)

# return new_list


# print(is_prime(text))


# for i_find_el in is_prime(text):
#     if isinstance(text, list):
#         print(text.index(i_find_el))
#     elif isinstance(text, dict):
#         print(i_find_el)


# second try


# def is_prime(num):
#     count = 0
#     if num >= 2:
#         for i in range(num, 0, -1):
#             if num % i == 0:
#                 count += 1
#         if count > 2:
#             return False
#         else:
#             return True
#
#     else:
#         return False
#
#
# def make_list(iterable):
#     new_list = []
#     if isinstance(iterable, dict):
#         iterable = iterable.items()
#     else:
#         iterable = enumerate(iterable)
#
#     for i, el in iterable:
#         if is_prime(i):
#             new_list.append(el)
#
#     return new_list
#
#
# print(make_list(text))


# Задача 3. Функция


# iterable = (1, 2, 3, 4, 5, "ly", 6, "5", "la", 7, 3, 112, "5", 3,
#             1, 3, 12, 1, 2, 3, 4, 5, 6, 7, "la", "ly", 3, "12")


# def recreate_tuple(my_tuple=None, random_el=None):
#     if not my_tuple:
#         import string
#         my_tuple = tuple(el.lower() for el in string.ascii_letters)
#         print("tuple with ascii lower: {0}".format(my_tuple))
#     my_tuple = list(my_tuple)
#     if not random_el:
#         random_el = input("Введите рандомный элемент: ")
#
#     if random_el in my_tuple or int(random_el) in my_tuple:
#         if random_el.isdigit():
#             random_el = int(random_el)
#
#         if my_tuple.count(random_el) and my_tuple.count(random_el) <= 1:
#             index_of = my_tuple.index(random_el)
#
#             return tuple(el for el in my_tuple[index_of:None])
#
#         else:
#             i_start = my_tuple.index(random_el)
#             my_tuple.reverse()
#             i_end = my_tuple.index(random_el)
#             my_tuple.reverse()
#             return tuple(el for el in my_tuple[i_start:-i_end])
#
#     else:
#         return tuple()
#
#
# res = recreate_tuple()
# print(res, type(res))

# Задача 4. Игроки


# players = {
#     ("Ivan", "Volkin"): (10, 5, 13),
#     ("Bob", "Robbin"): (7, 5, 14),
#     ("Rob", "Bobbin"): (12, 8, 2)
# }

# №_1
# list_of_keys_and_values = []
# for key, value in enumerate(players.items()):
#     together = list(value[0])
#     together.extend(tuple(value[1]))
#     list_of_keys_and_values.append(tuple(together))

# print(list_of_keys_and_values)

# №_2

# list_of_keys_and_values = [tuple([*key, *value]) for key, value in players.items()]
#
# print(list_of_keys_and_values)


# №_3
# list_of_keys_and_values = [sum((key, value), ()) for key, value in players.items()]
# or
# list_of_keys_and_values = [key + value for key, value in players.items()]
# print(list_of_keys_and_values)

# Задача 5. Одна семья

# family = {
#     "Сидоров Никита": "35",
#     "Сидорова Алина": "34",
#     "Сидоров Павел": "10",
#     "Кашубин Виталий": "23",
#     "Кашубина Марина": "28",
#     "Кашубина Светлана": "47",
#     "Артемов Артем": "24"
# }
#

# name = input("Введите фамилию: ").title()
#
# for person, age in family.items():
#     if name in person or name[:-1] in person:
#         print("{0} {1}".format(person, age))


# Задача 6. По парам

# import random
#
# original_list = list(random.randint(0, 9) for _ in range(10))
# print(original_list)
#
# new_list = [(original_list[i - 1], original_list[i]) for i in range(1, len(original_list), 2)]
#
# print(new_list)


# Задача 7. Функция сортировки


# №_2
#
# def build_in_sort_tuple(my_tuple=None):
#     if not my_tuple:
#         my_tuple = tuple(sorted(random.randint(1, 9) for _ in range(10)))
#     return my_tuple
#
#
# print(build_in_sort_tuple())
#
# №_2
#
# def sort_tuple(my_tuple=None):
#     if not my_tuple:
#         my_tuple = list(random.randint(1, 9) for _ in range(10))
#     for _ in range(len(my_tuple)):
#         for i in range(1, len(my_tuple)):
#             if my_tuple[i - 1] > my_tuple[i]:
#                 my_tuple[i], my_tuple[i - 1] = my_tuple[i - 1], my_tuple[i]
#
#     return tuple(my_tuple)
#
#
# print(sort_tuple())

# Задача 8. Контакты 3

# contact_book = {}
# while True:
#     action = input("Какое действие вы хотите произвести?\n1. Добавить контакт\n"
#                    "2. Поиск человека по фамилии\nВвод:>").lower()
#
#     action_add_contact = "1"
#     action_search_family = "2"
#     if action == action_add_contact:
#         print("Текущий контактный список: {0}".format(contact_book))
#         print("Чтобы добавить контакт, введите имя, фамилию и номер телефона: ")
#         name = input("Введите имя: ").title()
#         surname = input("Введите фамилию: ").title()
#         phone = int(input("Введите номер телефона: "))
#         contact_book[(name, surname)] = phone
#         print(contact_book)
#     elif action == action_search_family:
#         search_for = input("Введите фамилию для поиска:>").lower()
#         for contact, phone in contact_book.items():
#             if search_for == contact[-1].lower():
#                 print(f"Нашелся контакт: {contact[0]} {contact[-1]}. и ее номер телефона {phone}")
#         print()

# Задача 9. Протокол соревнований

# record_num = int(input("Сколько записей вносится в протокол? "))
# record_num = 5
# if record_num >= 3:
#     current_i = 1
#     repeat = True
#     players = {'Vitaly': '2828', 'Marina': '2324', 'Tenia': '234', 'Lapka': '234', 'Last': '23444442'}
# while True:
#     for i in range(current_i, record_num + 1):
#
#         record = input("{0} запись".format(i)).split()
#         number = record[0]
#         name = record[-1]
#         if number.isdigit() and name.isalpha():
#             if i == record_num:
#                 repeat = False
#
#             if players.get(name):
#                 if int(players[name]) < int(number):
#                     players[name] = number
#             else:
#                 players[name] = number
#
#             print(players)
#
#         else:
#             print("Введите номер и имя через пробел вот так: (Номер Имя)")
#             current_i = i
#             break
#
#     if not repeat:
#         break

# for key, value in players.items():
#     print(key, value)
# else:
#     print("Гарантируется, что в соревнованиях не менее трёх участников.")


# Задача 10. Своя функция zip (необязательная)

# def shortest_seq_range(string, tpl):
#     return min(len(string), len(tpl))
#
#
# sym_string = "abc"
# tuple_num = tuple(range(10, 90 + 1, 10))
# print("Строка: {0}".format(sym_string))
# print("Кортеж чисел: {0}".format(tuple_num))
#
# generator = ((sym_string[i], tuple_num[i]) for i in range(shortest_seq_range(sym_string, tuple_num)))
#
# print(generator)
#
# for el in generator:
#     print(el)


#  22.2 Рекурсия

# def factorial(number):
#     if number == 1:
#         return 1
#     return number * factorial(number - 1)
#
#
# print(factorial(8))


# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
#
# def find_key(stuct, key):
#     if key in stuct:
#         return stuct[key]
#     for sub_struct in stuct.values():
#         if isinstance(sub_struct, dict):
#             res = find_key(sub_struct, key)
#             if res:
#                 break
#     else:
#         res = None
#
#     return res
#
#
# find = "h2"
# print(find_key(site, "title"))


# Домашнее задание 22.2


# Задача 1. Challenge

# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)


# Задача 2. Степень числа


# import math
#
#
# def power_math(a, n):
#     return math.pow(a, n)
#
#
# def power(a, n):
#     return a ** n
#
#
# float_num = float(input('Введите вещественное число: '))
#
# int_num = int(input('Введите степень числа: '))
#
# print(float_num, '**', int_num, '=', power(float_num, int_num))


# Задача 3. Поиск элемента


# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
#
# def find_element(html_doom, element):
#     if element in html_doom:
#         return html_doom[element]
#
#     for sub_dict in html_doom.values():
#         if isinstance(sub_dict, dict):
#             res = find_element(sub_dict, element)
#             if res:
#                 break
#     else:
#         res = False
#
#     return res
#
#
# print(find_element(site, "h2"))


# 22.3 Передача изменяемых и неизменяемых данных в функцию


# import random
#
# Задача 1. Ошибка
#
# def change_dict(dct):
#     num = random.randint(1, 100)
#
#     for i_key, i_value in dct.items():
#
#         if isinstance(i_value, list):
#             i_value.append(num)
#
#         elif isinstance(i_value, dict):
#             i_value[i_key + 1] = num
#
#         elif isinstance(i_value, set):
#             i_value.add(num)
#
#
# nums_list = [1, 2, 3]
#
# some_dict = {1: 'text', 2: 'another text'}
#
# uniq_nums = {1, 2, 3}
#
# common_dict = {1: nums_list.copy(), 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}
#
# change_dict(common_dict)
#
# print(common_dict)
#
# print(nums_list)
# print(some_dict)
# print(uniq_nums)


# Задача 2. Непонятно!

# def while_error():
#     print("Тип данных: str (строка)")
#     return "str", str(any_object)
#
#
# any_object = input("Введите данные: ")
# list_of_mutable = ["dict", "list", "set"]
# list_of_immutable = ["int", "float", "str", "tuple", "bool"]
# list_of_classes = list_of_mutable + list_of_immutable
# try:
#     str_to_obj = eval(any_object)
#
#     ru_object_name = ["словарь", "список", "множество", "целое число",
#                       "дробное число", "строка", "кортеж", "логическое"]
#
#     type_name = str(type(str_to_obj)).strip("<>'").split("'")[-1]
#     index_of_all_types = list_of_classes.index(type_name)
#
#     print("Тип данных: {0} ({1})".format(type_name, ru_object_name[index_of_all_types]))
#
# except (NameError, SyntaxError, TypeError):
#     type_name, str_to_obj = while_error()
#
# if type_name in list_of_mutable:
#     print("Изменяемый (mutable)")
#
# elif type_name in list_of_immutable:
#     print("Неизменяемый (immutable)")
#
# print("\nId объекта: {id}\n"
#       "Object: {object}\n"
#       "Type объекта: {o_types}\n".format(id=id(any_object),
#                                          object=any_object,
#                                          o_types=type(str_to_obj)))

# 22.4 Именованные аргументы и значения по умолчанию

# Задача 1. Работа с файлом


# def working_with_files(question=None, error=None, retry=3):
#     if not error:
#         error = "Неверный ввод. Пожалуйста, введите 'да' или 'нет'."
#     if not question:
#         question = "Нет вопросов?"
#     crr_answer = ("yes", "no", "да", "нет")
#     while True:
#         if retry == -1:
#             break
#         answer = input(question).lower()
#         if answer not in crr_answer:
#             print(error)
#             print("Осталось попыток: {0}".format(retry))
#             retry -= 1
#         else:
#             if answer in crr_answer[:-1:2]:
#                 return working_with_files("Do you speek english?", "Error: type yes or no!")
#             else:
#                 return print("Бывай тогда.")
#
#
# working_with_files("Хочешь начать?")


# def working_with_files(question=None, error=None, retry=3):
#     if not error:
#         error = "Неверный ввод. Пожалуйста, введите 'да' или 'нет'."
#     if not question:
#         question = "Нет вопросов?"
#     crr_answer = ("yes", "no", "да", "нет")
#     while True:
#         if retry == -1:
#             break
#         answer = input(question).lower()
#         if answer not in crr_answer:
#             print(error)
#             print("Осталось попыток: {0}".format(retry))
#             retry -= 1
#         else:
#             if answer in crr_answer[:-1:2]:
#                 return working_with_files("Do you speek english?", "Error: type yes or no!")
#             else:
#                 return print("Бывай тогда.")
#
#
# # TODO Дописать возможность вводить список из вопросов которые будут задаватся после правельного ответа
# question_counter = 0
# question_list = ["Тебе 20 лет?", ""]
# working_with_files()

# Задача 2. Накопление значений

# from this =>
# def num_and_list(num, list=[]):
#     list.append(num)
#     return list


# to this =>
# def num_and_list(num, list=None):
#     if not list:
#         list = []
#     list.append(num)
#     return list
#
#
# print(num_and_list(666))
#
# print(num_and_list(5))
#
# print(num_and_list(2))
# print(num_and_list.__defaults__)


# Задача 3. Помощь другу


# def create_dict(some_data, temp=None):
#     print("Type of data: {0}".format(type(some_data)))
#     if not temp:
#         temp = dict()
#     if isinstance(some_data, (str, float, int)):
#         temp[some_data] = some_data
#         return temp
#     elif isinstance(some_data, dict):
#         return some_data
#     else:
#         return
#
#
# def data_preparation(old_list):
#     new_list = []
#     for i_element in old_list:
#         if res := create_dict(i_element):
#             new_list.append(res)
#
#     return new_list
#
#
# data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
#
# data = data_preparation(data)
#
# print(data)


# 22.6 Практическая работа

# Задача 1. Challenge — 2


# def recursion_range(num, counter=1, reverse=False):
#     if num == 0:
#         return ""
#
#     if not reverse:
#         print(counter)
#     else:
#         print(num)
#
#     return recursion_range(num - 1, counter + 1, reverse=reverse)
#
# print(recursion_range(10))
# print(recursion_range(5, reverse=True))
# print(recursion_range(3, reverse=True))

# Задача 2. Свой zip — 2

# def my_zip(iter1, iter2):
#     iter1 = list(iter1)
#     iter2 = list(iter2)
#     zip_out = ((f_el, iter2[i]) for i, f_el in enumerate(iter1))
#     return zip_out
#
# some_list_1 = list(range(1, 11))
# some_list_2 = list(range(10, 0, -1))
# print("List: ")
# print(some_list_1)
# print(some_list_2)
# print("Own function: ", list(my_zip(some_list_1, some_list_2)))
# print("Zip: ", list(zip(some_list_1, some_list_2)))
#
# print("Dict: ")
# some_dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4}
# some_dict_2 = {31: "a", 21: "b", 3: "c", 4: "d"}
# print(some_dict_1)
# print(some_dict_2)
# print("Own function: ", list(my_zip(some_dict_1, some_dict_2)))
# print("Zip: ", list(zip(some_dict_1, some_dict_2)))
# print()
#
# print("Set: ")
# some_set_1 = {3, 1, 2, 44, "a", "l"}
# some_set_2 = {"b", "c", "h", "q", "z", 12}
# print(some_set_1)
# print(some_set_2)
# print("Own function: ", list(my_zip(some_set_1, some_set_2)))
# print("Zip: ", list(zip(some_set_1, some_set_2)))


# Задача 3. Ряд Фибоначчи
# num_pos = int(input("Введите позицию числа в ряде Фибоначчи: "))
#
#
# #  1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181.
#
# def fibonacci(n):
#     if n < 1:
#         return abs(n)
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print("Число: {0}".format(fibonacci(num_pos)))


# Задача 4. Поиск элемента — 2


# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац',
#             "bod": {
#                 "hadsones": {
#                     'html': {
#                         'head': {
#                             'title': 'Мой сайт'
#                         },
#                         'body': {
#                             'bbs': 'удет мой',
#                             'gog': 'Тут, наверное',
#                             'p1': 'A здесь новый сайт',
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }
#
#
# def find_key(struct, key, depth=None):
#     if key in struct:
#         return struct[key]
#
#     if depth:
#         depth -= 1
#         if depth <= 0:
#             return None
#
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             res = find_key(sub_struct, key, depth)
#             if res:
#                 break
#     else:
#         res = None
#     return res
#
#
# search_key = input("Введите ключь: ")
# q_set_depth = input("Будете вводить глубину? Y/N ")
#
# lst_of_answers = ["yes", "y", "no", "n"]
#
# if q_set_depth.lower() in lst_of_answers:
#     if q_set_depth.lower()[:1] == "y":
#         print("Yes")
#         max_depth = int(input("Введите глубину: "))
#         print(find_key(site, search_key, depth=max_depth))
#     else:
#         print(find_key(site, search_key))


# Задача 5. Ускоряем работу функции

# def calculating_math_func(data, default={}):
#     if data in default:
#         return default[data]
#     else:
#         result = 1
#         for index in range(1, data + 1):
#             result *= index
#         result /= data ** 3
#         result = result ** 10
#         default[data] = result
#         return result
#
#
# print(calculating_math_func(5))
# print(calculating_math_func(5))
# print(calculating_math_func(5))

# Задача 6. Глубокое копирование


# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам телефон недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на iPhone',
#             'div': 'Купить',
#             'p': 'Продать'
#         }
#     }
# }
# copy_site = {
#     'html.1': {
#         'head.2': {
#             'title.3': 'Куплю/продам {0} недорого',
#         },
#         'body.2': {
#             'h2.3': 'У нас самая низкая цена на {0}',
#             'div.3': 'Купить',
#             'p.3': 'Продать',
#             "div.3": {
#                 "p2.4": {
#                     "h2.5": "This is product - {0}"
#                 }
#             }
#         }
#     }
# }

# def main(run=True):
#     if not run:
#         return False
#
#     print("Main Function:", end="\n\n")
#
#     def rec_key_replace(struct, product="Phone_228"):
#         if isinstance(struct, dict):
#             return {
#                 key: rec_key_replace(val, product)
#                 if key != "title" and key != "h2"
#                 else val.format(new_product=product)
#                 for key, val in struct.items()
#             }
#
#         return struct
#
#     amount_of_sites = int(input("Сколько сайтов: "))
#     all_sites_dict = {}
#     for _ in range(amount_of_sites):
#         current_product_name = input("Введите название продукта для нового сайта: ")
#         all_sites_dict["Сайт для {0}:".format(current_product_name)] = rec_key_replace(site, current_product_name)
#         for k, v in all_sites_dict.items():
#             print(k, end="\n")
#             print(v)

# if __name__ == '__main__':
#     main(run=True)


# import re

# def create_deep_copy(struct, product, key=None):
#     if isinstance(struct, dict):
#         return {key: create_deep_copy(val, product, key) for key, val in struct.items()}
#     elif isinstance(struct, str):
#         if key != "title" and key != "h2":
#             return struct.format(product)
#
#
# def create_copy(struct, product="something"):
#     if isinstance(struct, dict):
#         return {
#             key: create_copy(val, product)
#             if key != "h2.3" and key != "title.3"
#             else val.format(product)
#             for key, val in struct.items()}
#     return struct
#
#
# print(create_copy(copy_site, "soos"))
#
#
# def rec_key_replace(struct, product="Phone_228"):
#     if isinstance(struct, dict):
#         return {
#             key: rec_key_replace(val, product)
#             if not re.match("^title\.\d+$", key) and not re.match(r"^h2\.\d+$", key)
#             else val.format(product)
#             for key, val in struct.items()
#         }
#
#     return struct
#
#
# print(rec_key_replace(copy_site, "lala"))
# print(create_copy(copy_site, "so"))


# Задача 7. Продвинутая функция sum


# def sum_pro(*lst_nums, result=0):
#     for sub_el in lst_nums:
#         if isinstance(sub_el, list):
#             result = sum_pro(*(el for el in sub_el), result=result)
#         else:
#             result += sub_el
#
#     return result
#
#
# print(sum_pro([[1, 2, [3]], [1], 3]))
#
# print(sum_pro(1, 2, 3, 4, 5))


# Задача 8. Список списков — 2


# def open_lists(lst, new_list=None):
#     if new_list is None:
#         new_list = []
#     for el in lst:
#         if isinstance(el, list):
#             open_lists(el, new_list)
#         else:
#             new_list.append(el)
#
#     return new_list


# nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15, 99, [101]], [16, 17, 18]]]
#
# print(open_lists(nice_list))
#
# some_list = [[1, 2, 3], 1, [4, 5], [6, 7, 8], [9, [123451, [13, 3], 351234123], 10], [11, 11, [111], 12, 13],
#              [14, 15, 16]]
#
# print(open_lists(some_list))


# Задача 9. Ханойские башни
# https://pythobyte.com/tower-of-hanoi-python-01725/


# 23.1 Модуль os: генерация путей и метод listdir
# import os


# def print_dirs(project, inner=0, lvl=None):
#     print("\n {0}Папка".format("\t" * inner), project)
#     if lvl == inner:
#         return ""
#
#     for i_elem in os.listdir(project):
#         if "." in i_elem:
#             print("\t" * (inner + 1), os.path.join(project, i_elem))
#         else:
#             print_dirs(os.path.join(project, i_elem), inner=inner + 1, lvl=lvl)
#
#
# projects_list = ["homework", "selenium", "marishatest"][-1:]
#
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join("..", "..", i_project))
#     print_dirs(path_to_project, lvl=1)

# Задача 1. Сисадмин

# file_name = "admin.bat"
# folder_name = "access"
# file_path = '..', '..', folder_name, file_name
#
# print(os.path.abspath(os.path.join(*file_path)))
# print(os.path.join(*file_path[-2:]))
#

# Задача 2. Содержимое

# for i_elem in os.listdir(os.path.abspath(os.path.join(os.path.sep, "home", "nagual"))):
#     print(os.path.abspath(i_elem))

#
# 23.2 Модуль os: проверки
# def find_file(curr_path, file_name):
#     # or this #1
#     if file_name in os.listdir(curr_path):
#         return os.path.abspath(os.path.join(curr_path, file_name))
#     for i_elem in os.listdir(curr_path):
#         i_elem = os.path.join(curr_path, i_elem)
#         if os.path.isdir(i_elem):
#             res = find_file(i_elem, file_name)
#             if res:
#                 break
#     # or this #2
#     # elif file_name.lower() in i_elem.lower():
#     #         return i_elem
#     else:
#         res = None
#
#     return res


# os.system("xdg-open {0}".format(os.path.sep.join(find_file("/home", "test.py").split(os.path.sep)[:-1])))

# Задача 1. Иконки

# file = find_file("/home", "python.py")  # 4641
#
# folder = os.path.sep.join(file.split(os.path.sep)[:-1])

# print(file)
# print(folder)

# def what_path_end(abs_path):
#     print("Путь: {0}".format(abs_path))
#     if os.path.exists(abs_path):
#         if os.path.isfile(abs_path):
#             print("Это файл")
#             print("Размер файла: {0} байт".format(os.path.getsize(abs_path)))
#         elif os.path.isdir(abs_path):
#             print("Это папка")
#         elif os.path.islink(abs_path):
#             print("Это ссылка")
#     else:
#         print("Указанного пути не существует")
#
#
# what_path_end(file)

# Задача 2. Поиск файла

# def find_all_same_name_files(abs_path, file_name, all_file_path=None):
#     if all_file_path is None:
#         all_file_path = list()
#     if file_name in os.listdir(abs_path):
#         all_file_path.append(os.path.abspath(os.path.join(abs_path, file_name)))
#     for i_elem in os.listdir(abs_path):
#         abs_i_elem = os.path.abspath(os.path.join(abs_path, i_elem))
#         if os.path.isdir(abs_i_elem):
#             find_all_same_name_files(abs_i_elem, file_name, all_file_path)
#     else:
#         return all_file_path
#
#
# print(find_all_same_name_files(os.path.abspath(os.path.join("..", "..")), "text.txt"))
#
# print(find_all_same_name_files(os.path.abspath(os.path.join("..", "..")), "img.png"))


# 23.3 Базовые операции с файлами: open, close, read


# Задача 1. Результаты

# group_1 = open(os.path.abspath("/task/group_1.txt"), "r", encoding="utf-8")
# group_2 = open(os.path.abspath("/task/Additional_info/group_2.txt"), "r", encoding="utf-8")
#
# summa = 0
# diff = 0
# for i, i_line in enumerate(group_1):
#     if i == 0:
#         diff = int(i_line.split(' ')[-1])
#     else:
#         diff -= int(i_line.split(' ')[-1])
#
#     summa += int(i_line.split(' ')[-1])
#
# group_1.close()
#
# print('Сумма очков первой группы: ', summa)
#
# print('Разность очков первой группы: ', diff)
#
# mult = 1
#
# for i_line in group_2:
#     mult *= int(i_line.split(' ')[-1])
#
# group_2.close()
# print("Произведение очков второй группы: ", mult)

# with open(os.path.abspath("/task/group_1.txt"), "r", encoding="utf-8") as group_1:
#     summa = 0
#     diff = 0
#     for i, i_line in enumerate(group_1):
#         if i == 0:
#             diff = int(i_line.split(' ')[-1])
#         else:
#             diff -= int(i_line.split(' ')[-1])
#
#         summa += int(i_line.split(' ')[-1])
#
#     print('Сумма очков первой группы: ', summa)
#
#     print('Разность очков первой группы: ', diff)
#
# with open(os.path.abspath("/task/Additional_info/group_2.txt"), "r", encoding="utf-8") as group_2:
#     mult = 1
#     for i_line in group_2:
#         mult *= int(i_line.split(' ')[-1])
#
#     print("Произведение очков второй группы: ", mult)
# Задача 2. Поиск файла 2
#
# import random
#
#
# def find_files_by_name(path, file_name, all_files=None):
#     if all_files is None:
#         all_files = []
#     if file_name in os.listdir(path):
#         file_found = os.path.abspath(os.path.join(path, file_name))
#         file_to_rename_to = os.path.abspath(os.path.join(path, "text.py"))
#
#         os.rename(file_found, file_to_rename_to)
#         all_files.append(file_to_rename_to)
#
#     for i_elem in os.listdir(path):
#         check_path = os.path.abspath(os.path.abspath(os.path.join(path, i_elem)))
#         if os.path.isdir(check_path):
#             find_files_by_name(check_path, file_name, all_files)
#     else:
#         return all_files, len(all_files)
#
#
# file_to_find = "text.txt"
# path_to_search = "/home/nagual/projects"
# list_of_found_paths = find_files_by_name(path_to_search, file_to_find)[0]
# print(list_of_found_paths)
# random_file_choice = random.choice(list_of_found_paths)
#
# print(random_file_choice)
# with open(random_file_choice, 'r', encoding='utf-8') as file:
#     for i, i_line in enumerate(file):
#         print(i_line, end="")


# 23.4 Метод write. Режимы записи


# Задача 1. Сумма чисел


# file_with_nums = open(os.path.abspath(os.path.join(".", "numbers.txt")), 'r')
#
# summa = 0
#
# for i_nums in file_with_nums:
#     summa += int(i_nums)
#
# print(summa)
#
# file_with_nums.close()
#
# file_with_sum_of_nums = open(os.path.abspath(os.path.join(".", "answer.txt")), 'w')
# file_with_sum_of_nums.write(str(summa))
# file_with_sum_of_nums.close()

# Задача 2. Всё в одном


# path_to_project = os.path.abspath(os.path.join("."))
# print(path_to_project)


# def all_files_to_one(path):
#     for each_file in os.listdir(path):
#         if os.path.isfile(os.path.abspath(os.path.join(path, each_file))):
#             file = open(os.path.abspath(os.path.join(path, each_file)), 'r', encoding="utf-8")
#             new_file = open(os.path.abspath(os.path.join(path, "..", "scripts.txt")), 'a', encoding="utf-8")
#             count_lines = 0
#             for i, i_line in enumerate(file):
#                 count_lines += 1
#                 new_file.write(i_line)
#             else:
#                 new_file.write("\nPath: {0} has {1}".format(
#                     os.path.abspath(os.path.join(path, each_file)),
#                     count_lines))
#                 new_file.write("\n{0}\n".format("*" * 100))
#                 new_file.close()
#
#             file.close()
#
#
# all_files_to_one(path_to_project)


# 23.5 Перемещение курсора в файле. Метод seek

name = input("")
age = int(input(""))
job = input("")
