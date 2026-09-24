import random


def generate_random_array(length, min_value, max_value):
    """Генерує масив випадкових цілих чисел заданої довжини в діапазоні."""
    return [random.randint(min_value, max_value) for _ in range(length)]



# ЗАВДАННЯ 1: Парні елементи в діапазоні індексів

def count_and_sum_even_in_range(arr, start_index, end_index):
    """Пораховує кількість та суму парних елементів у заданому діапазоні індексів."""
    start = max(0, start_index)
    end = min(len(arr) - 1, end_index)

    evens = [arr[i] for i in range(start, end + 1) if arr[i] % 2 == 0]
    return len(evens), sum(evens)



# ЗАВДАННЯ 2: Середнє арифметичне та більші елементи

def average_and_count_greater(arr):
    """Визначає середнє арифметичне та кількість елементів, більших за нього."""
    if not arr:
        return 0.0, 0

    average = sum(arr) / len(arr)
    count_greater = sum(1 for item in arr if item > average)
    return average, count_greater


# ЗАВДАННЯ 3: Попарна сума двох масивів

def pairwise_sum(arr1, arr2):
    """Створює третій масив як попарну суму двох масивів однакової довжини."""
    if len(arr1) != len(arr2):
        raise ValueError("Масиви повинні бути однакової довжини.")

    return [x + y for x, y in zip(arr1, arr2)]


# ЗАВДАННЯ 4: Конкатенація двох масивів

def concatenate_arrays(arr1, arr2):
    """Утворює третій масив як конкатенацію двох масивів."""
    return arr1 + arr2



# ЗАВДАННЯ 5: Обмін місцями максимуму та мінімуму

def swap_min_max(arr):
    """Міняє місцями перші знайдені максимум та мінімум у масиві."""
    if len(arr) <= 1:
        return arr.copy()

    result = arr.copy()
    min_idx = result.index(min(result))
    max_idx = result.index(max(result))

    result[min_idx], result[max_idx] = result[max_idx], result[min_idx]
    return result



# ЗАВДАННЯ 6: Поділ на додатні та від’ємні елементи

def split_positive_negative(arr):
    """Поділяє масив на два: з додатних та з від’ємних елементів."""
    positive = [x for x in arr if x > 0]
    negative = [x for x in arr if x < 0]
    return positive, negative


# ЗАВДАННЯ 7: Видалення дублікатів максимума та мінімума

def remove_min_max_duplicates(arr):
    """Видаляє з масиву повторні дублікати максимумів і мінімумів (залишає лише перші)."""
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)

    min_seen = False
    max_seen = False
    result = []

    for item in arr:
        if item == min_val:
            if not min_seen:
                result.append(item)
                min_seen = True
        elif item == max_val:
            if not max_seen:
                result.append(item)
                max_seen = True
        else:
            result.append(item)

    return result



# ЗАВДАННЯ 8: Елементи у межах між середніми арифметичними

def elements_between_averages(arr1, arr2):
    """Створює масив з елементів двох масивів, що знаходяться між значеннями їх середніх арифметичних."""
    avg1 = sum(arr1) / len(arr1) if arr1 else 0
    avg2 = sum(arr2) / len(arr2) if arr2 else 0

    min_avg = min(avg1, avg2)
    max_avg = max(avg1, avg2)

    combined = arr1 + arr2
    return [x for x in combined if min_avg <= x <= max_avg]



# ДОДАТКОВЕ ЗАВДАННЯ: Симуляція ігрового інвентарю

class Inventory:
    """Клас RPG інвентарю на 10 слотів."""

    def __init__(self):
        self.slots = ["Empty"] * 10

    def add_item(self, item):
        """Додавання предмета у першу вільну комірку."""
        if "Empty" in self.slots:
            empty_idx = self.slots.index("Empty")
            self.slots[empty_idx] = item
            return True
        return False

    def remove_item(self, item):
        """Видалення предмета за назвою."""
        for i, slot in enumerate(self.slots):
            if slot.lower() == item.lower():
                self.slots[i] = "Empty"
                return True
        return False

    def compact(self):
        """Ущільнення інвентарю (переміщення предметів на початок)."""
        filled = [slot for slot in self.slots if slot != "Empty"]
        self.slots = filled + ["Empty"] * (10 - len(filled))

    def display(self):
        """Виведення інвентарю на екран."""
        print("Інвентар:", self.slots)


# ==========================================
# ДЕМОНСТРАЦІЯ РОБОТИ ТА КОНТРОЛЬНІ ПИТАННЯ
# ==========================================
if __name__ == "__main__":
    print("=== ПІДГОТОВКА ===")
    arr_main = generate_random_array(10, -10, 10)
    print("Згенерований масив:", arr_main)

    print("\n=== ЗАВДАННЯ 1 ===")
    count_even, sum_even = count_and_sum_even_in_range(arr_main, 2, 7)
    print(f"Парних елементів з індексу 2 по 7: кількість = {count_even}, сума = {sum_even}")

    print("\n=== ЗАВДАННЯ 2 ===")
    avg, count_greater = average_and_count_greater(arr_main)
    print(f"Середнє арифметичне = {avg:.2f}, елементів більших за середнє = {count_greater}")

    print("\n=== ЗАВДАННЯ 3 ===")
    a1 = generate_random_array(5, 1, 10)
    a2 = generate_random_array(5, 1, 10)
    print("Масив 1:", a1)
    print("Масив 2:", a2)
    print("Попарна сума:", pairwise_sum(a1, a2))

    print("\n=== ЗАВДАННЯ 4 ===")
    b1 = [1, 2, 3]
    b2 = [4, 5, 6, 7]
    print("Конкатенація масивів:", concatenate_arrays(b1, b2))

    print("\n=== ЗАВДАННЯ 5 ===")
    sample_arr = [3, 1, 8, -5, 8, -5]
    print("Вхідний масив:", sample_arr)
    print("Після обміну max та min:", swap_min_max(sample_arr))

    print("\n=== ЗАВДАННЯ 6 ===")
    pos, neg = split_positive_negative(arr_main)
    print("Додатні елементи:", pos)
    print("Від'ємні елементи:", neg)

    print("\n=== ЗАВДАННЯ 7 ===")
    dups_arr = [10, 2, 10, -4, 5, -4, 10]
    print("Вхідний масив з дублікатами min/max:", dups_arr)
    print("Без дублікатів min/max:", remove_min_max_duplicates(dups_arr))

    print("\n=== ЗАВДАННЯ 8 ===")
    arr_a = [1, 5, 10]  # avg = 5.33
    arr_b = [15, 20, 25]  # avg = 20.0
    print("Масив A:", arr_a)
    print("Масив B:", arr_b)
    print("Елементи в межах середніх (5.33 ... 20.0):", elements_between_averages(arr_a, arr_b))

    print("\n=== ДОДАТКОВЕ ЗАВДАННЯ: СИМУЛЯЦІЯ ІНВЕНТАРЮ ===")
    inv = Inventory()
    inv.add_item("Меч")
    inv.add_item("Зілля здоров'я")
    inv.add_item("Щит")
    inv.display()

    print("Видаляємо 'Зілля здоров'я':")
    inv.remove_item("Зілля здоров'я")
    inv.display()

    print("Ущільнюємо інвентар:")
    inv.compact()
    inv.display()

    print("\n=== ВІДПОВІДІ НА КОНТРОЛЬНІ ПИТАННЯ ===")
    print("""
1. Способи визначення парності:
   - Операція залишку від ділення: `num % 2 == 0`
   - Побітова операція `&`: `(num & 1) == 0`
   - Перевірка за допомогою `divmod(num, 2)[1] == 0`

2. Повернення більше ніж одного результату з методу:
   - У Python використовуються кортежі (tuples), наприклад: `return val1, val2`.
   - Також можна повертати словник `{"res1": val1, "res2": val2}` або клас/dataclass.

3. Якщо у завданні 3 вхідні масиви будуть різної довжини:
   - Якщо стоїть перевірка `len(arr1) != len(arr2)`, програма згенерує помилку `ValueError`.
   - Без перевірки стандартний `zip()` обріже обробку до довжини коротшого масиву.

4. Якщо у завданні 4 один чи обидва масиви порожні:
   - Якщо один порожній — буде створено копію другого (непорожнього) масиву.
   - Якщо обидва порожні — повернеться новий порожній список `[]`.
   - Помилок не виникне в обох випадках.

5. Поведінка програми (завдання 5) для [1, 1, 1, 5, 5]:
   - Метод `index()` знайде перші входження мінімуму (індекс 0) та максимуму (індекс 3).
   - Місцями поміняються лише елементи з індексами 0 та 3. Результат: [5, 1, 1, 1, 5].
""")
