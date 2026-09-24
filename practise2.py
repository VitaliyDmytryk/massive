import random



def generate_matrix(m, n, min_val, max_val):
    """Генерує двовимірний масив (матрицю) m x n випадкових цілих чисел."""
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(m)]


def print_matrix(matrix, title="Матриця:"):
    """Виводить матрицю у відформатованому вигляді з заголовками рядків та стовпців."""
    print(f"\n{title}")
    if not matrix or not matrix[0]:
        print("Порожня матриця")
        return

    m = len(matrix)
    n = len(matrix[0])


    header = "\t" + "\t".join([f"стовпець {j + 1}" for j in range(n)])
    print(header)


    for i in range(m):
        row_values = []
        for val in matrix[i]:
            if isinstance(val, float):
                row_values.append(f"{val:6.2f}")
            else:
                row_values.append(f"{val:9}")
        row_str = f"рядок {i + 1}\t" + "\t".join(row_values)
        print(row_str)



# ОСНОВНІ ЗАВДАННЯ


# 1. Відняти від елементів кожного рядка матриці його середнє арифметичне
def subtract_row_average(matrix):
    """Створює нову матрицю, де від кожного елемента віднято середнє арифметичне відповідного рядка."""
    result = []
    for row in matrix:
        avg = sum(row) / len(row)
        new_row = [round(x - avg, 2) for x in row]
        result.append(new_row)
    return result


# 2. Циклічний зсув матриці на k позицій вправо та на k догори
def cyclic_shift(matrix, k):
    """Виконує циклічний зсув матриці на k позицій вправо та на k позицій догори."""
    if not matrix or not matrix[0]:
        return matrix

    m = len(matrix)
    n = len(matrix[0])

    k_right = k % n
    k_up = k % m

    shifted_right = [
        row[-k_right:] + row[:-k_right] if k_right != 0 else row[:]
        for row in matrix
    ]

   
    shifted_final = shifted_right[k_up:] + shifted_right[:k_up]
    return shifted_final


# 3. Знайти максимальні елементи та видалити відповідні рядки і стовпці
def remove_max_rows_and_cols(matrix):
    """Знаходить максимальні елементи та видаляє з матриці всі рядки і стовпці, що їх містять."""
    if not matrix or not matrix[0]:
        return [], None

    m = len(matrix)
    n = len(matrix[0])

    max_val = max(max(row) for row in matrix)

    rows_to_remove = set()
    cols_to_remove = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == max_val:
                rows_to_remove.add(i)
                cols_to_remove.add(j)

    new_matrix = []
    for i in range(m):
        if i in rows_to_remove:
            continue
        new_row = [matrix[i][j] for j in range(n) if j not in cols_to_remove]
        new_matrix.append(new_row)

    return new_matrix, max_val


# 4. Обертання квадратної матриці на 90 градусів за годинниковою стрілкою in-place
def rotate_matrix_90_clockwise(matrix):
    """Обертає квадратну матрицю n x n на 90 градусів за годинниковою стрілкою (in-place)."""
    n = len(matrix)

    
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

   
    for i in range(n):
        matrix[i].reverse()



# ДОДАТКОВЕ ЗАВДАННЯ: РОЗКЛАД СТУДЕНТІВ (3D-МАСИВ)


DAYS = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]
GROUPS = ["Група 1", "Група 2", "Група 3"]


def create_sample_schedule():
    """
    Створює розклад розмірністю [3][5][4] (Групи x Дні x Пари).
    Заповнено тестовими даними.
    """
    EMPTY = "Вільне вікно"
    schedule = [
        # Група 1
        [
            ["Вища математика", "Фізика", EMPTY, "Програмування"],       # Пн (є вікно на 3 парі)
            ["Англійська мова", "Вища математика", EMPTY, EMPTY],         # Вт
            ["Фізика", "Історія", "Програмування", "Фізкультура"],         # Ср (найбільше навантаження: 4 пари)
            [EMPTY, "Фізкультура", EMPTY, EMPTY],                         # Чт
            ["Програмування", "Вища математика", EMPTY, EMPTY]            # Пт
        ],
        # Група 2
        [
            ["Вища математика", "Філософія", "Програмування", EMPTY],    # Пн (потік з Гр1 та Гр3 на 1 парі)
            ["Фізика", "Англійська мова", EMPTY, EMPTY],                  # Вт
            [EMPTY, "Історія", "Програмування", EMPTY],                   # Ср
            ["Фізкультура", EMPTY, "Фізика", EMPTY],                     # Чт (є вікно)
            ["Вища математика", EMPTY, EMPTY, EMPTY]                      # Пт
        ],
        # Група 3
        [
            ["Вища математика", EMPTY, "Фізика", EMPTY],                  # Пн (є вікно)
            [EMPTY, "Програмування", "Англійська мова", EMPTY],            # Вт
            ["Філософія", "Філософія", EMPTY, EMPTY],                     # Ср
            ["Історія", "Історія", "Фізкультура", EMPTY],                 # Чт
            [EMPTY, EMPTY, "Вища математика", EMPTY]                      # Пт
        ]
    ]
    return schedule


def find_max_load_day(schedule, group_idx):
    """Знаходить день із найбільшою кількістю пар для обраної групи."""
    max_pairs = -1
    best_day_idx = 0

    for day_idx in range(5):
        active_pairs = sum(1 for subject in schedule[group_idx][day_idx] if subject != "Вільне вікно")
        if active_pairs > max_pairs:
            max_pairs = active_pairs
            best_day_idx = day_idx

    return DAYS[best_day_idx], max_pairs


def find_inconvenient_days(schedule, group_idx):
    """Знаходить дні з «вікнами» (порожніми парами між активними заняттями)."""
    inconvenient_days = []

    for day_idx in range(5):
        day_slots = schedule[group_idx][day_idx]
        active_indices = [i for i, subj in enumerate(day_slots) if subj != "Вільне вікно"]

       
        if len(active_indices) >= 2:
            first_pair = active_indices[0]
            last_pair = active_indices[-1]
            has_window = any(day_slots[i] == "Вільне вікно" for i in range(first_pair, last_pair))
            if has_window:
                inconvenient_days.append(DAYS[day_idx])

    return inconvenient_days


def check_stream_lectures(schedule):
    """Перевіряє наявність потокових занять (однаковий предмет у кількох груп одночасно)."""
    stream_events = []

    for day_idx in range(5):
        for pair_idx in range(4):
            # Збираємо предмет для кожної групи в цей конкретний день і пару
            subjects = [schedule[g_idx][day_idx][pair_idx] for g_idx in range(3)]

            # Перевіряємо, чи є співпадіння предметів (ігноруючи "Вільне вікно")
            subject_counts = {}
            for g_idx, subj in enumerate(subjects):
                if subj != "Вільне вікно":
                    subject_counts.setdefault(subj, []).append(GROUPS[g_idx])

            for subj, groups in subject_counts.items():
                if len(groups) > 1:
                    stream_events.append({
                        "day": DAYS[day_idx],
                        "pair": pair_idx + 1,
                        "subject": subj,
                        "groups": groups
                    })

    return stream_events


==
# ДЕМОНСТРАЦІЯ РОБОТИ

if __name__ == "__main__":
    print("=== ПІДГОТОВКА: Генерація та вивід матриці ===")
    m, n = 3, 4
    matrix = generate_matrix(m, n, 1, 10)
    print_matrix(matrix, "Початкова матриця:")

    print("\n" + "="*50)
    print("=== ЗАВДАННЯ 1: Віднімання середнього арифметичного рядка ===")
    sub_matrix = subtract_row_average(matrix)
    print_matrix(sub_matrix, "Матриця після віднімання середнього рядків:")

    print("\n" + "="*50)
    print("=== ЗАВДАННЯ 2: Циклічний зсув (k=1 вправо, k=1 догори) ===")
    shifted = cyclic_shift(matrix, k=1)
    print_matrix(shifted, "Матриця після зсуву:")

    print("\n" + "="*50)
    print("=== ЗАВДАННЯ 3: Видалення рядків і стовпців з максимумом ===")
    reduced_matrix, max_val = remove_max_rows_and_cols(matrix)
    print(f"Максимальний елемент у матриці: {max_val}")
    print_matrix(reduced_matrix, "Матриця після видалення max елементів:")

    print("\n" + "="*50)
    print("=== ЗАВДАННЯ 4: Обертання квадратної матриці на 90° за годинниковою стрілкою (In-Place) ===")
    sq_matrix = generate_matrix(3, 3, 1, 9)
    print_matrix(sq_matrix, "Початкова квадратна матриця 3x3:")
    rotate_matrix_90_clockwise(sq_matrix)
    print_matrix(sq_matrix, "Матриця після обертання на 90° за годинниковою стрілкою:")

    print("\n" + "="*50)
    print("=== ДОДАТКОВЕ ЗАВДАННЯ: Розклад студентів (3D-масив) ===")
    schedule = create_sample_schedule()

    # 1. Найбільше навантаження для Групи 1 (індекс 0)
    target_group = 0
    max_day, pair_count = find_max_load_day(schedule, target_group)
    print(f"\n1. День з найбільшим навантаженням для '{GROUPS[target_group]}': {max_day} ({pair_count} пари/пари).")

    # 2. Незручний розклад (з «вікнами»)
    inc_days = find_inconvenient_days(schedule, target_group)
    print(f"2. Дні з незручним розкладом («вікнами») для '{GROUPS[target_group]}': {', '.join(inc_days) if inc_days else 'Немає'}")

    # 3. Перевірка на наявність потокових занять
    stream_lectures = check_stream_lectures(schedule)
    print("\n3. Перевірка на потокові заняття (спільні пари у кількох груп):")
    if stream_lectures:
        for event in stream_lectures:
            groups_str = ", ".join(event["groups"])
            print(f" - {event['day']}, пара №{event['pair']}: Предмет '{event['subject']}' у груп: {groups_str}")
    else:
        print(" Потокових занять не знайдено.")
