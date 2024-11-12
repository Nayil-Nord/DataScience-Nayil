"""Глава 5 Операторы управления потоком."""

# # Глава 5 Операторы управления потоком
#
# ## 5.1 Управление потоком
# - Обычно код выполняется последовательно сверху вниз
# - Операторы управления потоком позволяют изменять порядок выполнения кода в зависимости от условий
#
# ## 5.2 Операторы if
# ### 5.2.1 Простой if
# - Используется для проверки условия
# - Синтаксис: `if условие: код блока if`
# - Блок кода должен иметь отступ
# - Пример использования: скидки в магазине при сумме > 50000
#
# ### 5.2.2 Оператор if-else
# - Позволяет выполнить альтернативный код если условие ложно
# - Синтаксис:
# ```python
# # if условие:
# # код блока if
# # else:
# # код блока else
# ```
# - Блок else необязателен

# Проверяем, больше ли число 11
number = int(input("Enter a number: "))
if number > 11:
    print(f"{number} is greater than 11")
else:
    print(f"{number} is smaller than 11")

# +
# Расчет скидки в зависимости от суммы покупки
# Скидка 20% при покупке свыше 25000
# Скидка 5% в остальных случаях

total_amount = int(input("Введите общую сумму покупок: "))

if total_amount > 25000:
    discount = (total_amount * 20) / 100
else:
    discount = (total_amount * 5) / 100

final_amount = total_amount - discount
print(f"Итоговая сумма к оплате: {final_amount},скидка составила: {discount}")
# -

#
# ### 5.2.3 Оператор if-elif-else
# - elif - комбинация else и if
# - Может быть множество elif блоков
# - else необязателен
# - Позволяет проверить несколько условий последовательно
#
# ## 5.3 Цикл for
# - Используется для итерации по элементам последовательности
# - Синтаксис: `for переменная in последовательность: блок кода`
# - Может иметь блок else, который выполняется после завершения цикла
#
# ## 5.4 Функция range()
# - Генерирует последовательность чисел
# - Может задавать начало, конец и шаг
# - Возвращает итерируемый объект
# - Часто используется с циклом for
#
# ## 5.5 Цикл while
# - Выполняет код, пока условие истинно
# - Используется когда неизвестно количество итераций
# - Важно обновлять счетчик в теле цикла
# - Может иметь блок else
#
# ## 5.6 Операторы break и continue
# ### 5.6.1 Break
# - Прерывает выполнение цикла
# - При использовании break блок else не выполняется
#
# ### 5.6.2 Continue
# - Пропускает оставшуюся часть текущей итерации
# - Переходит к следующей итерации цикла
#
# ## 5.7 Оператор pass
# - Ничего не делает
# - Используется как заполнитель, когда требуется синтаксически
# - Часто применяется при создании пустых классов или функций

# # 5.9 Упражнения
#
# ## 5.9.1 Ответьте на вопросы
#
# ### 1. Каков порядок выполнения выражений в программе Python? Как его изменить?
# - По умолчанию выражения выполняются последовательно сверху вниз
# - Изменить порядок можно с помощью операторов управления потоком (if, for, while, break, continue)
#
# ### 2. Что делают приведенные фрагменты кода?
#
# а) ```python
# a = 50
# if a >= 100:
#     print("Value of a is {}".format(a))
# ```
# - Ничего не выведет, так как условие ложно (50 не >= 100)
#
# б) ```python
# a = 90
# if a <= 100:
#     print("Value of a is {}".format(a))
# ```
# - Выведет "Value of a is 90", так как 90 <= 100
#
# в) ```python
# x = 50
# if x >= 10:
#     print("Value of x is {}".format(x))
# else:
#     print("Value of x is less than 10")
# ```
# - Выведет "Value of x is 50", так как 50 >= 10
#
# г) ```python
# x = 5
# if x >= 10:
#     print("Value of x is {}".format(x))
# else:
#     print("Value of x is less than 10")
# ```
# - Выведет "Value of x is less than 10", так как 5 < 10
#
# д) ```python
# x = 0
# while x < 5:
#     print(x)
#     x += 1
# ```
# - Выведет числа от 0 до 4
#
# е) ```python
# for i in range(5, 25, 5):
#     print(i)
# ```
# - Выведет числа 5, 10, 15, 20
#
# ### 3. Есть ли ошибки в приведенных фрагментах? Если да, то какие.
#

# а) ```python
# a = 12
# if a == 10
# print("a is equal to 10")
# ```
#

variable_a = 12
if variable_a == 10:
    print("variable_a is equal to 10")

# б) ```python
# a = 90, b = 15
# if a <= 100:
#     print("Value of a is less than 100")
# ```
# - Ошибка: неправильное присваивание нескольких переменных

var_a, var_b = 90, 15
if var_a <= 100:
    print("Value of var_a is less than 100")

# в) ```python
# x = 22
# if x >= 10:
#     print("x is bigger than 10")
# else
#     print("x is less than 10")
# ```
# - Ошибка: отсутствует двоеточие после else

var_x = 22
if var_x >= 10:
    print("'var_x' is bigger than 10")
else:
    print("'var_x' is less than 10")

# г) ```python
# x = 5
# if x >= 10:
#     print("Value of x is {}".format(x))
# else x < 10:
#     print("Value of x is less than 10")
# ```
# - Ошибка: else не должен иметь условия

variable_x = 5
if variable_x >= 10:
    print(f"Value of 'variable_x' is {variable_x}!")
else:
    print("Value of 'variable_x' is less than 10")

# д) ```python
# x = 5
# if x > 10:
#     print("Value of x is more than 10")
# else:
#     print("Value of x is less than 10")
# elif x == 10:
#     print("Value of x is equal to 10")
# ```
# - Ошибка: elif не может идти после else

variab_x = 5
if variab_x > 10:
    print("Value of 'variab_x' is more than 10")
elif variab_x == 10:
    print("Value of 'variab_x' is equal to 10")
else:
    print("Value of 'variab_x' is less than 10")

# е) ```python
# x = 0
# while x < 5
# print(x) x =+ 1
# ```
# - Ошибки: отсутствует двоеточие после условия, неправильный отступ, неправильный оператор инкремента

# ## 5.9.2 Правда или ложь
#
# 1. "Когда оператор if имеет значение true, он выполняет лишь одну инструкцию в коде."
# - Ложь. Он выполняет весь блок кода с отступом
#
# 2. "Блок кода сразу после оператора if - это блок if, который выполняется, когда условие возвращает True."
# - Правда
#
# 3. "Оператор else обязательно есть после каждого оператора if."
# - Ложь. else необязателен
#
# 4. "Оператор elif представляет собой комбинацию операторов else и if в одной строке."
# - Правда
#
# 5. "Оператор else также может использоваться с циклом for."
# - Правда
#
# 6. "Объект в теле цикла for должен быть объектом-итератором."
# - Правда
#
# 7. "Цикл while выполняет блок кода, пока выполняется условие."
# - Правда
#
# 8. "Оператор break прерывает самый внутренний цикл for."
# - Правда
#
# 9. "Оператор continue используется для пропуска всех оставшихся итераций цикла."
# - Ложь. Пропускает только текущую итерацию
#
# 10. "Оператор pass ничего не делает."
# - Правда

# # 5.9.3 Практические задания с решениями

# ### 1. Расчет прибыли/убытка трейдера

# +
buy_price = float(input("Введите цену покупки: "))
sell_price = float(input("Введите цену продажи: "))

profit = sell_price - buy_price

if profit > 0:
    print(f"Получена прибыль в размере: {profit}")
else:
    print(f"Получен убыток в размере: {abs(profit)}")
# -

# ### 2. Проверка високосного года

# +
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} - високосный год")
else:
    print(f"{year} - не високосный год")
# -

# ### 3. Сравнение опыта работы

# +
samir = float(input("Опыт работы Самира (лет): "))
pravin = float(input("Опыт работы Правина (лет): "))
mohit = float(input("Опыт работы Мохита (лет): "))

most_exp = max(samir, pravin, mohit)
least_exp = min(samir, pravin, mohit)

print(f"Наибольший опыт: {most_exp} лет")
print(f"Наименьший опыт: {least_exp} лет")
# -

# ### 4. Проверка существования треугольника

# +
angle1 = float(input("Введите первый угол: "))
angle2 = float(input("Введите второй угол: "))
angle3 = float(input("Введите третий угол: "))

is_valid_sum = angle1 + angle2 + angle3 == 180
is_valid_angles = angle1 > 0 and angle2 > 0 and angle3 > 0

if is_valid_sum and is_valid_angles:
    print("Это треугольник")
else:
    print("Это не треугольник")
# -

# ### 5. Проверка прямоугольного треугольника

# +
angle1 = float(input("Введите первый угол: "))
angle2 = float(input("Введите второй угол: "))
angle3 = float(input("Введите третий угол: "))

has_right_angle = angle1 == 90 or angle2 == 90 or angle3 == 90
is_valid_triangle = angle1 + angle2 + angle3 == 180

if has_right_angle and is_valid_triangle:
    print("Это прямоугольный треугольник")
else:
    print("Это не прямоугольный треугольник")
# -

# ### 6. Генерация трехзначных чисел

# +
# Подсчет трехзначных чисел из цифр 1, 2, 3
count = 0
digits = [1, 2, 3]

for first in digits:
    for second in digits:
        for third in digits:
            # Проверяем что все цифры разные
            if first != second and second != third and first != third:
                print(f"{first}{second}{third}")
                count += 1

print(f"Всего чисел: {count}")
# -

# ### 7. Таблица умножения

# +
# Ввод числа для таблицы умножения
number = int(input("Введите число для таблицы умножения: "))

# Вывод таблицы умножения
for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
# -

# ### 8. Простые числа до 500

# Поиск простых чисел до 500
for num in range(2, 501):
    is_prime = True

    # Проверяем делится ли число на что-то кроме 1 и себя
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break

    # Если число простое - выводим его
    if is_prime:
        print(num, end=" ")

# ### 9. Числа, кратные 9, меньше 300

for num in range(0, 300, 9):
    print(num, end=" ")

# ### 10. Расчет минимального срока службы машины

# +
purchase_price = 1000000
annual_income = 200000
final_value = 250000
interest_rate = 0.08

years = 1
while True:
    # Доход от машины
    machine_income = annual_income * years + final_value - purchase_price

    # Доход от альтернативных инвестиций
    alternative_income = purchase_price * ((1 + interest_rate) ** years - 1)

    if machine_income > alternative_income:
        print(f"Минимальный срок службы: {years} лет")
        break

    years += 1
