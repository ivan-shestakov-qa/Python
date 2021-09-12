import random
# 1) Создать 2 переменных типа String с разными значениями
Word = "Hello Word"
word = "hello word"

# 2) 2) Создать 4 переменных типа Integer с разными значениями
my_year = 1983
wife_year = 1982
son_year = 2000
daughter_year = 2004

# 3) Создать 3 переменных типа Float с разными значениями

my_wieght = 73.4
son_wieght = 80.3
daughter_wieght = 50.5

# 4) Реализовать 15 варианта сравнения int переменных с операторами
#   >, <, >=, <=, !=. Pезультаты весвести в консоль.
v_1 = my_year > wife_year
v_2 = my_year > son_year
v_3 = my_year > daughter_year
v_4 = my_year < wife_year
v_5 = my_year < son_year
v_6 = my_year < daughter_year
v_7 = my_year <= wife_year
v_8 = my_year <= daughter_year
v_9 = my_year <= son_year
v_10 = my_year >= wife_year
v_11 = my_year >= son_year
v_12 = my_year >= daughter_year
v_13 = my_year != wife_year
v_14 = my_year != son_year
v_15 = my_year != daughter_year
print("Сравнение int --",v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10, v_11, v_12, v_13, v_14, v_15) # для вертикального вывода,в конце добавить  sep = "\n"

# 5) Реализовать 9 варианта сравнения Float переменных
#    с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
m_1 = my_wieght > son_wieght
m_2 = my_wieght > daughter_wieght
m_3 = my_wieght < son_wieght
m_4 = my_wieght < daughter_wieght
m_5 = my_wieght >= son_wieght
m_6 = my_wieght >= daughter_wieght
m_7 = my_wieght <= son_wieght
m_8 = my_wieght <= daughter_wieght
m_9 = my_wieght != son_wieght
print("Сравнение Float --",m_1,m_2, m_3, m_4, m_5, m_6, m_7, m_8, m_9)

# 6) Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, !=
#    и условными выражениями (end, or, not). Pезультаты весвести в консоль.
l_1 = my_year > wife_year and son_year > daughter_year
l_2 = my_year < wife_year and son_year < daughter_year
l_3 = my_year >= wife_year and son_year >= daughter_year
l_4 = my_year <= wife_year and son_year <= daughter_year
l_5 = my_year != wife_year or son_year < daughter_year
l_6 = my_year < wife_year or son_year != daughter_year
l_7 = my_year > wife_year or son_year >= daughter_year
l_8 = my_year < wife_year or son_year > daughter_year
l_9 = not my_year != wife_year
l_10 = not my_year <= wife_year
print("Сравнение and or not ", l_1, l_2, l_3, l_4, l_5, l_6, l_7, l_8, l_9, l_10)

# 7) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"
# age = int(input("Введите свой возраст:"))
# age_1 =30
# if age == age_1:
#     print("Вы вели число = ", age, "которое равно 30")
# elif age < 30:
#     print("Вы вели число = ", age, "которое меньше 30")
# else:
#     print("Вы вели число = ", age, "которое больше 30")

# 8) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"
# age = int(input("Введите свой возраст:"))
# age_1 = random.randint(1, 100)
# if age == age_1:
#     print("Вы вели число = ", age, "которое равно ", age_1)
# elif age < age_1:
#     print("Вы вели число = ", age, "которое меньше ", age_1)
# else:
#     print("Вы вели число = ", age, "которое больше ", age_1)
# 9) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное 2 целых числа (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно)
#        сгенерированному числу"
age = int(input("Введите свой возраст:"))
age_1 = random.randint(1, 100)
if age == age_1:
    print("Вы вели число = ", age, "которое равно ",age_1, age_1 and age == age_1)
elif age < age_1:
    print("Вы вели число = ", age, "которое меньше ", age_1, age_1 and age < age_1)
else:
    print("Вы вели число = ", age, "которое больше ", age_1, age_1 and age > age_1)