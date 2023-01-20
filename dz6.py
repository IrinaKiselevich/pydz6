#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

#num = input('Введите число: ')
# sum = 0
# for a in num:
#   if a.isdigit():
#         sum += int(a)

# print(f"Сумма {num} равна: ", sum)

# res =list(filter(lambda a:a.isdigit(),num))
# print (res)
# total = 0
# for number in res:
#     total += number
# print(total)


#Задайте список из n чисел последовательности (1+1/n)^n  и выведите на экран их сумму.
#*Пример:*
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Введите число: '))

# #def get_squer(n):
#  #	return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]
# #nums = get_squer(n)
# #print(nums)
# #print(round(sum(nums), 5))

# get_squer =lambda x, f :[round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]
# nums=get_squer (n)
# print(get_squer)
# #print(round(sum(nums), 5))

#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# from functools import reduce
# dot_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
# dot_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
# def dot_range(dot_1, dot_2):
#      rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
#      return round(rng, 2)
# print(dot_range(dot_1, dot_2))

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# from math import factorial
# n = int(input('Введите число N: '))
# print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,n+1)))))  