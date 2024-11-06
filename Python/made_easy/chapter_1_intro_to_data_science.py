# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---
"""Конспектирование 1 главы "Введение в Data Science"и решение упражнений."""

import math

# **Дата: 14/10/24**
#
# # Тезисный конспект к 1 главе "Введение в Data Science" книги "Python — это просто" .
#
# ## Введение в Data Science
# - **Data Science (Наука о данных)** — это междисциплинарная область, которая включает:
#   - Обработку данных, анализ, программирование, статистику и машинное обучение для получения знаний из данных.
#   - Основные составляющие:
#     1. **Математика и статистика** — для анализа данных.
#     2. **Программирование** — для автоматизации и создания моделей.
#     3. **Обработка данных** — сбор, очистка, структурирование данных.
#     4. **Машинное обучение** — создание моделей для прогнозирования и автоматизации.
#     5. **Бизнес-анализ** — применение знаний для принятия решений.
#
# ## Что такое алгоритм
# - **Алгоритм** — четкая последовательность шагов для решения задачи.
# - Алгоритмы могут быть представлены:
#   - Текстом, псевдокодом или графически — с помощью **блок-схем**.
# - **Блок-схема** — визуализация алгоритма с помощью символов, обозначающих действия или решения.
#
# ## Программирование
# - **Программирование** — процесс создания инструкций для компьютеров на языках программирования.
# - **Языки программирования** (Python, C++, Java) позволяют человеку давать команды компьютеру.
# - Основные характеристики хорошей программы:
#   1. **Читаемость** — легкость понимания кода другими программистами.
#   2. **Эффективность** — минимальное использование ресурсов.
#   3. **Безопасность** — защита от ошибок и угроз.
#   4. **Масштабируемость** — способность программы работать с увеличением объема данных.
#
# ## Компиляторы и интерпретаторы
# - **Компилятор** — программа, которая переводит код в машинный язык перед выполнением.
# - **Интерпретатор** — программа, выполняющая код построчно без перевода в машинный код.
# - Некоторые языки **компилируются**, другие **интерпретируются**, а некоторые поддерживают оба подхода.
#
# ## Data Science и будущее
# - Data Science будет развиваться за счет больших данных, искусственного интеллекта и автоматизации.
# - Специалисты по данным будут использовать **машинное обучение** и **AI** для улучшения бизнес-решений и предсказательной аналитики.
#
# ## Зачем изучать программирование
# - **Программирование** помогает автоматизировать рутинные задачи:
#   - Обработка данных, отправка отчетов, выполнение повторяющихся операций.
#   - Это улучшает производительность и решает повседневные задачи в бизнесе и жизни.

# # Упражнения
#
# ## 1.5.1. Ответы на вопросы
#
# 1. **Какие предметные области входят в Data Science? Что между ними общего и в чем различие?**
#    - В Data Science входят следующие области:
#      - **Статистика**: Используется для анализа и интерпретации данных.
#      - **Машинное обучение**: Включает в себя методы и алгоритмы для предсказания и классификации данных.
#      - **Программирование**: Необходимо для автоматизации обработки и анализа данных.
#      - **Бизнес-аналитика**: Применяется для извлечения инсайтов из данных для принятия бизнес-решений.
#      - **Большие данные**: Связаны с обработкой и анализом больших объемов данных.
#
#    Общим между этими областями является цель — извлечение полезной информации из данных. Различия заключаются в методах и инструментах, которые используются в каждой области.
#
# 2. **Как вы понимаете термин «алгоритм»? Как алгоритмы связаны с блок-схемами?**
#    - Алгоритм — это последовательность четких шагов, описывающих процесс решения задачи. Алгоритмы могут быть представлены в текстовом виде, псевдокодом или графически, например, с помощью блок-схем. Блок-схемы визуализируют алгоритм, показывая связи между шагами и принимаемыми решениями.
#
# 3. **Какую программу можно назвать хорошей? Запишите все характеристики, какие удастся придумать.**
#    - Хорошая программа должна обладать следующими характеристиками:
#      - Читаемость: код должен быть понятен другим разработчикам.
#      - Эффективность: минимальное использование ресурсов при выполнении.
#      - Безопасность: защита от ошибок и уязвимостей.
#      - Масштабируемость: способность работать с увеличением объема данных.
#      - Поддерживаемость: легкость внесения изменений и исправлений.
#
# 4. **Какой язык понимает компьютер?**
#    - Компьютер понимает машинный язык, который состоит из бинарных кодов (нулей и единиц), соответствующих операциям и командам, выполняемым процессором. Языки программирования, такие как Python или Java, сначала переводятся в машинный код с помощью компиляторов или интерпретаторов.
#
# 5. **Чем языки программирования отличаются от языков, на которых мы говорим?**
#    - Языки программирования отличаются от естественных языков тем, что они строго формализованы и предназначены для выполнения инструкций компьютером. В отличие от естественных языков, языки программирования требуют точности и отсутствия двусмысленности.
#
# ## 1.5.2. Правда или ложь
#
# 1. **Машинное обучение - это инструмент для извлечения знаний из данных.**
#    **Ответ: Правда.**
#
# 2. **Глубокое обучение - это то же самое, что машинное обучение.**
#    **Ответ: Ложь.** (Глубокое обучение — это подмножество машинного обучения, использующее нейронные сети.)
#
# 3. **Все инженеры-программисты также могут считаться специалистами по данным.**
#    **Ответ: Ложь.** (Не все инженеры-программисты имеют навыки в области Data Science.)
#
# 4. **Статистика - важный инструмент для специалистов по данным.**
#    **Ответ: Правда.**
#
# 5. **Компьютер может принимать решения, выходящие за рамки данных ему инструкций, подстраиваясь под изменения среды.**
#    **Ответ: Ложь.** (Компьютеры выполняют только те инструкции, которые им заданы.)
#
# 6. **Компьютеры понимают языки программирования «как есть».**
#    **Ответ: Ложь.** (Компьютеры понимают машинный язык, который является интерпретацией языков программирования.)
#
# 7. **Некоторые языки программирования компилируются, некоторые интерпретируются, а некоторые используют и то и другое.**
#    **Ответ: Правда.**
#
# 8. **Все программы выполняются последовательно.**
#    **Ответ: Ложь.** (Некоторые программы могут выполняться параллельно.)
#
# 9. **В ЮЕ есть встроенный текстовый редактор.**
#    **Ответ: Правда.**
#
# 10. **Компиляторы и интерпретаторы - это такие механизмы, наподобие привода для компакт-дисков.**
#     **Ответ: Ложь.** (Компиляторы и интерпретаторы — это программы для преобразования и выполнения кода.)

# ## 1.5.3. Практические задания:

# 1. **Напишите алгоритм для расчета простых процентов от некоторой суммы.**
#
# Начальная сумма = X Процентная ставка = R Период времени = T Простые проценты = (X * R * T) / 100

# +
# Заданные значения
principal = 1000  # Начальная сумма
rate = 5  # Процентная ставка
time = 2  # Период времени в годах

# Расчет простых процентов
simple_interest = (principal * rate * time) / 100

# Вывод результата
print(f"Простые проценты: {simple_interest:.2f}")
# -

# 2. **Напишите алгоритм для вычисления площади прямоугольника.**
#
# Длина = L
# Ширина = W
# Площадь = L * W

# +
# Ввод данных
length = 5  # Длина (L)
width = 3  # Ширина (W)

# Вычисление площади прямоугольника
area_rectangle = length * width

# Вывод результата
print(f"Площадь прямоугольника: {area_rectangle}")
# -

# 3. **Напишите алгоритм вычисления периметра круга.**
#
# Радиус = R Периметр = 2 * π * R

# +
# Ввод данных
radius_circle = 5  # Радиус (R)

# Вычисление периметра
perimeter_circle = 2 * math.pi * radius_circle

# Вывод результата
print(f"Периметр круга: {round(perimeter_circle, 2)}")
# -

# 4. **Напишите алгоритм, который находит все простые числа меньше 100.**
#
# Для числа от 2 до 99: Если число не делится нацело на другие числа от 2 до √число: Простое число

# +
# Список для хранения простых чисел
prime_numbers = []

# Поиск простых чисел от 2 до 99
for number in range(2, 100):
    is_prime = True
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(number)

# Вывод результата
print("Простые числа меньше 100:", prime_numbers)
# -

# 5. **Напишите алгоритм превращения предложения, написанного в верхнем регистре, в обычный для предложений регистр.**
#
# Входное предложение = "ПРИМЕР С ТЕКСТОМ" Результат = Входное предложение.lower().capitalize()

# +
# Входное предложение
input_sentence = "ПРИМЕР С ТЕКСТОМ"

# Преобразование в обычный регистр
result_converted = input_sentence.lower().capitalize()

# Вывод результата
print("Результат:", result_converted)
# -

# 6. **Составьте блок-схему приготовления льда из кипяченой воды с помощью холодильника.**
# - Начать
# - Кипятить воду
# - Налить кипяченую воду в формы для льда
# - Поставить формы в холодильник
# - Ждать 3-4 часа
# - Проверить, замерз ли лед
# - Вынуть лед из форм
# - Конец

# 7. **Составьте блок-схему для нахождения суммы всех четных чисел меньше ста.**
# - Начать
# - Сумма = 0
# - Для i от 2 до 99 с шагом 2:
#     - Сумма += i
# - Конец

# +
# Инициализация суммы
total_sum = 0

# Цикл для нахождения суммы четных чисел меньше 100
for i in range(2, 100, 2):
    total_sum += i

# Вывод результата
print("Сумма всех четных чисел меньше 100:", total_sum)
# -

# 8. **Составьте блок-схему для вычисления квадрата всех нечетных чисел от 1 до 15 включительно.**
# - Начать
# - Для i от 1 до 15:
#     - Если i нечетное:
#         - Квадрат = i * i
# - Конец

# Цикл для вычисления квадратов нечетных чисел от 1 до 15
for i in range(1, 16):
    if i % 2 != 0:  # Проверка на нечетность
        square = i * i
        print(f"Квадрат числа {i} равен {square}")

# 9. **Составьте блок-схему вывода таблицы умножения на 3.**
# - Начать
# - Для i от 1 до 10:
#     - Результат = 3 * i
#     - Вывести Результат
# - Конец

# Вывод таблицы умножения на 3
for i in range(1, 11):
    multiplication_table_result = 3 * i
    print(f"3 * {i} = {multiplication_table_result}")

# 10. **Составьте блок-схему для расчета сложных процентов (с капитализацией).**
#  - Начать
#  - Начальная сумма = P
#  - Процентная ставка = R
#  - Количество периодов = n
#  - Сложные проценты = P * (1 + R/n)^(n*t)
#  - Конец
