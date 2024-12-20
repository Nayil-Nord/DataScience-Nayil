"""Логирование уроков."""

# **Date:** 24/11/24
#
# # Lesson 11:
# - Повторили пройденные темы по теорверу и комбинаторике
# - Решили примеры задач

# **Date:** 13/11/24
#
# # Lesson 10:
# - Повторили пройденные темы по теорверу и комбинаторике
# - Решили примеры задач
# - Разобрали процесс закрытия pull request  квиза
#

# **Date:** 9/11/24
#
# # Lesson 9:
#
# - отработка отправки коммита через PR , через форка Nayil-Nord/DataScience-Nayil в основной репозиторий SENATOROVAI/DataScience-Nayil.
# - обсуждение кто важнее py или ipynb
# - попытка решить проблемы с jupytext
# - рассказывал что я прошел в теорвер и комбинаторике
# - боевой опыт решения неработающих плагинов

# **Date:** 6/11/24
#
# # Lesson 8:
#
# - продолжение знакомства с ебунту
# - настройка и обновление ебунту

# **Date:** 3/11/24
#
# # Lesson 7:
#
#
# ## Installing Linux and System Setup
#
# ## Tasks Completed / Выполненные задачи
#
# - **Preparing the Installation Disk / Подготовка установочного диска**
#   - Used **Ventoy 1.0.99** to create a bootable disk. / Использован Ventoy 1.0.99.
#   - Prepared **Lubuntu 18.04.5** image. / Подготовлен образ Lubuntu 18.04.5.
#
# - **Disk Partitioning / Разметка диска**
#   - Original Disk: **Windows 10** / Исходный диск: Windows 10.
#   - Allocated space: **200 GB out of 800 GB** / Выделено пространство: 200 ГБ из 800 ГБ.
#   - System type: **Dual boot (Windows 10 + Lubuntu)** / Система: Dual boot (Windows 10 + Lubuntu).
#
# - **Software Installation / Установка программного обеспечения**
#   - Successfully installed **Anydesk**. / Успешно установлен Anydesk.
#   - Attempted **Telegram installation** (issues encountered). / Попытка установки Telegram (возникли проблемы).

# **Date:** 2/11/24
#
# # Lesson 6
#
#
# ## Notes: Working with GitHub Pull Requests / Конспект: Работа в GitHub с Pull Requests
#
# ### Main Topics / Основные темы
#
# - **Creating Issues / Создание Issues**
#   - Creating project tasks (Issues) for work management. / Создание задач (Issues) для управления работой над проектом.
#   - Using `Reference new issue` to generate issues from code discussions. / Создание через `Reference new issue`.
#
# - **Using Copy Permalink / Использование Copy Permalink**
#   - Copying permanent links to lines of code for referencing in discussions and documentation. / Копирование постоянной ссылки на строку кода для упоминания в обсуждениях и документации.
#
# - **Conducting Code Review / Проведение Code Review**
#   - Reviewing code before merging to ensure project quality and standards. / Проверка кода перед слиянием для обеспечения качества и стандартов проекта.
#
# - **Closing Pull Requests / Закрытие Pull Requests**
#   - Completing Pull Requests after successful review or changes. / Завершение Pull Requests после успешной проверки или изменений.
#   - Automatically closing related Issues when a Pull Request is merged. / Автоматическое закрытие связанных Issues при слиянии Pull Request.
#

# **Дата: 19/10/24**
#
# # Урок 5
#
# ## Конспект: Начали разбирать комбинаторику
#
# Основные формулы комбинаторики: [Формулы комбинаторики](http://mathprofi.ru/formuly_kombinatoriki.pdf)
#
# - Рассмотрели факториал (надо знать до \(5!\))
# - Разобрали понятия и формулы:
#   - Перестановки
#   - Сочетания
#   - Размещения
# - Разобрали биномиальную теорему (бином Ньютона) и треугольник Паскаля.
#
# ### Примеры
# - Решили несколько задач для закрепления материала.

# **Дата: 16/10/24**
#
# # Урок 4
#
# # Конспект: Повторили основные понятия теории вероятностей. Подготовка к комбинаторике.
#
# ## Виды событий
# - **Независимые события** — исход одного события не влияет на исход другого.
# - **Зависимые события** — исход одного события влияет на исход другого.
# - **Несовместные события** — два события не могут произойти одновременно.
# - **Совместные события** — события могут происходить одновременно.
#
# ## Случайность и равновозможность событий
# - **Случайное событие** — событие, которое может произойти или не произойти при определённых условиях.
# - **Равновозможные события** — события с одинаковыми шансами наступления (например, идеальная монета или кубик).
#
# ## Совместные и несовместные события
# - **Совместные события** — могут происходить одновременно (например, выпадение чётного числа и числа меньше 5 при броске кубика).
# - **Несовместные события** — не могут произойти одновременно (например, выпадение орла и решки при одном броске монеты).
#
# ## Полная группа событий и противоположные события
# - **Полная группа событий** — совокупность всех возможных исходов эксперимента, одно из которых обязательно произойдёт.
# - **Противоположные события** — два события, одно из которых исключает другое (например, «лампа перегорела» и «лампа не перегорела»).
#
# ## Сложение и умножение вероятностей
# - **Сложение вероятностей** — используется для несовместных событий: \( P(A \cup B) = P(A) + P(B) \).
# - **Умножение вероятностей** — применяется для независимых событий: \( P(A \cap B) = P(A) \times P(B) \).
#
# ## Вероятность события
# - **Вероятность события** — числовая мера возможности его наступления, принимает значения от 0 до 1:
#   - \( P(A) = 0 \) — событие невозможно.
#   - \( P(A) = 1 \) — событие обязательно произойдёт.
#   - \( 0 < P(A) < 1 \) — частичная вероятность.
#
# ## Теорема сложения вероятностей
# - Теорема сложения вероятностей помогает найти вероятность событий, образующих полную группу, так как их сумма равна 1:
#   \[
#   P(A_1) + P(A_2) + ... + P(A_n) = 1
#   \]
#
# ## Дополнительно
# - Рассмотрели, как бизнес использует теорию вероятностей: когда среднее количество случаев неизвестно, важно определить достаточное количество экспериментов для приближения к среднему значению в бизнес-задачах.

# **Дата: 12/10/24**
#
# # Урок 3
#
# # Термины и понятия теории вероятностей
#
# ## Основные типы событий
#
# * **Достоверное событие:** Событие, которое обязательно произойдет в данном испытании.
#   * *Пример:* Выпадение любого числа при броске кубика.
#
# * **Невозможное событие:** Событие, которое точно не произойдет в данном испытании.
#   * *Пример:* Выпадение числа 8 при броске шестигранного кубика.
#
# * **Случайное событие:** Событие, которое может произойти или не произойти в данном испытании. Вероятность такого события лежит в интервале от 0 до 1.
#   * *Пример:* Выпадение четного числа при броске кубика.
#
# ## Равновозможные и равновероятные события
#
# * **Равновозможные события:** События, у которых одинаковые шансы наступления.
#   * *Пример:* Выпадение любой грани при броске идеального кубика в идеальный условиях.
#
# * **Равновероятные события:** События, имеющие одинаковую вероятность.
#   * *Примечание:* Равновозможные события всегда равновероятны.
#
# ## Совместные и несовместные события
#
# * **Совместные события:** События, которые могут произойти одновременно в одном испытании.
#   * *Пример:* Выпадение четного числа и числа, большего 3, при броске кубика.
#
# * **Несовместные события:** События, которые не могут произойти одновременно в одном испытании.
#   * *Пример:* Выпадение числа 1 и числа 6 при одном броске кубика.
#
# * **Противоположные события:** Два события, образующие полную группу событий. Одно из них обязательно произойдет, а другое - нет.
#   * *Пример:* Выпадение четного числа и выпадение нечетного числа при броске кубика.
#
# ## Элементарные и сложные события
#
# * **Элементарное событие:** Событие, которое не может быть разложено на более простые события.
#   * *Пример:* Выпадение числа 1 при броске кубика.
#
# * **Сложное событие:** Событие, которое состоит из нескольких элементарных событий.
#   * *Пример:* Выпадение четного числа при броске кубика.
#
# ## Полная группа событий
#
# * **Полная группа событий:** Совокупность всех возможных несовместных событий в данном испытании.
#   * *Пример:* При броске кубика полную группу событий образуют события: выпадение 1, 2, 3, 4, 5 или 6.
#
# ## Операции над событиями
#
# * **Сложение событий (дизъюнкция):** Объединение событий. Обозначается символом ∪ или словом "или".
#   * *Пример:* А ∪ В - событие, состоящее в наступлении события А или события В.
#
# * **Умножение событий (конъюнкция):** Совместное наступление событий. Обозначается символом ∩ или словом "и".
#   * *Пример:* А ∩ В - событие, состоящее в наступлении события А и события В.
#
# ## Теория множеств и алгебра событий
#
# * **Теория множеств:** Математическая теория, изучающая свойства множеств и операции над ними. Понятия теории множеств широко используются в теории вероятностей.
#
# * **Алгебра событий:** Часть теории вероятностей, изучающая операции над событиями.
#
# * **Язык алгебры событий:** Формальный язык, используемый для описания событий и операций над ними.
#
# ## Дополнительные замечания
#
# * **Амперсанд (&)** в программировании часто используется для обозначения логического "И" (конъюнкции).
#
# * **Побитовые сдвиги**
#
# * **Таблицы истинности**

# **Дата: 09/10/24**
#
# # Урок 2
#
# - Обсудили работу с Git.
# - Проверили текущее состояние с домашним заданием.
# - Начали изучать теорию вероятностей:
#   - Виды событий:
#     - Достоверные и недостоверные события.
#     - Случайные события.
#     - Совместимые и несовместимые события.
#   - Понятие исходов.
#   - Событие \( A' \) (дополнение к событию A).
# - В качестве доски использовали новый инструмент [Jamboard](https://jamboard.google.com/d/1eZ5ykHXoVNUfvVcTLccq8I07vCroZBHN4Oh8MUvbCyY/edit?usp=sharing).
# - Получил дополнительное задание - переписать конспект теорвер до 30 страниц - [ссылка на задание](https://t.me/c/1937296927/22697/22754).

# **Дата: 03/10**
#
# # Урок 1. Основы математики
#
# ## Классификация чисел с помощью диаграммы Венна
#
# Диаграмма Венна — это схематичное изображение всех возможных отношений подмножеств универсального множества. Рассмотрим различные множества чисел с помощью диаграммы Венна:
#
# - **N** (Natural) — Натуральные числа: 1, 2, 3, 4, 5, ...
# - **W** (Whole) — Целые неотрицательные числа: 0, 1, 2, 3, ...
# - **Z** (Integers) — Целые числа: ..., -3, -2, -1, 0, 1, 2, 3, ...
# - **Q** (Rational) — Рациональные числа: любые числа, которые можно представить в виде дроби. Например: 1/2, -3/4, 5, ...
# - **I** (Irrational) — Иррациональные числа: числа, которые не могут быть представлены в виде простой дроби, например, √2, π.
# - **R** (Real) — Вещественные числа: объединение рациональных и иррациональных чисел.
# - **C** (Complex) — Комплексные числа: числа вида a + bi, где a и b — вещественные числа, а i — мнимая единица (i² = -1). Пример: √-1 = i.
#
# ## Множества
#
# Множество — это совокупность объектов, которые имеют общие свойства.
#
# ### Операции над множествами:
#
# - **Union (Объединение)** — объединение двух или более множеств включает все элементы этих множеств, без дублирования. Операция обозначается символом ∪.
#   **Пример**: A ∪ B — множество всех элементов, которые принадлежат хотя бы одному из множеств A или B.
#   **Пример на числах**: A = {1, 2, 3}, B = {3, 4, 5}
#   Тогда A ∪ B = {1, 2, 3, 4, 5}.
#
# - **Intersection (Пересечение)** — пересечение двух множеств включает только те элементы, которые принадлежат одновременно обоим множествам. Операция обозначается символом ∩.
#   **Пример**: A ∩ B — множество всех элементов, которые принадлежат и множеству A, и множеству B.
#   **Пример на числах**: A = {1, 2, 3}, B = {3, 4, 5}
#   Тогда A ∩ B = {3}.
#
# - **Difference (Разность)** — разность множеств включает элементы, которые принадлежат первому множеству, но не принадлежат второму. Операция обозначается символом \ или −.
#   **Пример**: A \ B — множество всех элементов, которые принадлежат множеству A, но не принадлежат множеству B.
#   **Пример на числах**: A = {1, 2, 3}, B = {3, 4, 5}
#   Тогда A \ B = {1, 2}.
#
# - **Symmetric Difference (Симметрическая разность)** — симметрическая разность двух множеств включает те элементы, которые принадлежат одному из множеств, но не принадлежат обоим одновременно. Операция обозначается символом Δ.
#   **Пример**: A Δ B — множество всех элементов, которые принадлежат только одному из множеств A или B, но не обоим сразу.
#   **Пример на числах**: A = {1, 2, 3}, B = {3, 4, 5}
#   Тогда A Δ B = {1, 2, 4, 5}.
#
# - **Complement (Дополнение)** — дополнение множества A (обозначается как A') включает все элементы универсального множества, которые не принадлежат множеству A.
#   **Пример**: Если универсальное множество U = {1, 2, 3, 4, 5} и A = {1, 2}, то A' = {3, 4, 5}.
#
# Мы также затронули функции, неравенства, уравнения и вопросы тригонометрии.
#
# ## Условные обозначения и кванторы:
#
# Разобрали некоторые условные обозначения:
# - **∈** — "принадлежит" (элемент принадлежит множеству).
#   **Пример**: 1 ∈ N означает, что число 1 принадлежит множеству N.
#
# - **∉** — "не принадлежит" (элемент не принадлежит множеству).
#   **Пример**: 1 ∉ N означает, что число 1 не принадлежит множеству N.
#
# - **⊂** — "собственное подмножество" (множество A является подмножеством B, но не равно ему).
#   **Пример**: N ⊂ Z означает, что N — подмножество Z, но N ≠ Z.
#
# ## Важный нюанс:
#
# В математике существуют две основные операции — сложение и умножение, а все остальные операции происходят из этих двух фундаментальных операций!
