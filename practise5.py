import random
import time
import sys

# Збільшуємо ліміт рекурсії для QuickSort на великих масивах (100_000 елементів)
sys.setrecursionlimit(200000)

def generate_array(length: int, start: int = 1, end: int = 100, use_floats: bool = False) -> list:
    """Генерує масив випадкових чисел (цілих або дробових)."""
    if use_floats:
        return [round(random.uniform(start, end), 2) for _ in range(length)]
    return [random.randint(start, end) for _ in range(length)]

def print_array(arr: list) -> str:
    formatted_elements = [f"[cell - {i}, value - {val}]" for i, val in enumerate(arr)]
    result_str = "{" + ", ".join(formatted_elements) + "}"
    print(result_str)
    return result_str

# ==========================================
# АЛГОРИТМИ З ПРАКТИЧНОЇ РОБОТИ №3
# ==========================================

def bubble_sort(arr: list, ascending: bool = True) -> list:
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            should_swap = (a[j] > a[j + 1]) if ascending else (a[j] < a[j + 1])
            if should_swap:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def insertion_sort(arr: list, ascending: bool = True) -> list:
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and ((a[j] > key) if ascending else (a[j] < key)):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def selection_sort(arr: list, ascending: bool = True) -> list:
    a = arr.copy()
    n = len(a)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            should_update = (a[j] < a[target_idx]) if ascending else (a[j] > a[target_idx])
            if should_update:
                target_idx = j
        a[i], a[target_idx] = a[target_idx], a[i]
    return a

# ==========================================
# ПРАКТИЧНА РОБОТА №5: QUICKSORT ТА ПЕРЕВІРКА
# ==========================================

def _partition(arr: list, low: int, high: int, ascending: bool) -> int:
    """Вибір півоти та партиціонування (кроки 1-2)."""
    pivot = arr[high] # Півотою обираємо останній елемент
    i = low - 1       # Індекс меншого елемента
    
    for j in range(low, high):
        # Перевірка умови залежно від напрямку сортування
        condition = (arr[j] <= pivot) if ascending else (arr[j] >= pivot)
        if condition:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Ставимо півоту на правильне місце
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def _quick_sort_recursive(arr: list, low: int, high: int, ascending: bool):
    """Рекурсивне застосування алгоритму до підмасивів (крок 3)."""
    if low < high:
        pi = _partition(arr, low, high, ascending)
        _quick_sort_recursive(arr, low, pi - 1, ascending)
        _quick_sort_recursive(arr, pi + 1, high, ascending)

def quick_sort(arr: list, ascending: bool = True) -> list:
    """Головний метод сортування QuickSort."""
    a = arr.copy()
    _quick_sort_recursive(a, 0, len(a) - 1, ascending)
    return a

def is_sorted(arr: list, ascending: bool = True) -> bool:
    """Перевіряє, чи відсортований масив у заданому напрямку."""
    for i in range(len(arr) - 1):
        if ascending:
            if arr[i] > arr[i + 1]:
                return False
        else:
            if arr[i] < arr[i + 1]:
                return False
    return True

# ==========================================
# ТЕСТУВАННЯ ТА ПОРІВНЯННЯ ПРОДУКТИВНОСТІ
# ==========================================

def compare_performance():
    sizes = [1_000, 10_000, 100_000]
    algorithms = {
        "Quick Sort": quick_sort,
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort
    }
    
    print(f"{'Розмір':<10} | {'Алгоритм':<18} | {'Час (сек)':<10} | {'Відсортовано (True/False)'}")
    print("-" * 65)
    
    for size in sizes:
        # Використовуємо масив дробових чисел, як вимагалося в завданні
        test_array = generate_array(size, 1, 1000, use_floats=True)
        
        for name, func in algorithms.items():
            # Повільні алгоритми пропускаємо для 100_000, щоб не чекати годинами
            if size > 10_000 and name != "Quick Sort":
                print(f"{size:<10} | {name:<18} | {'Пропущено (>10к)':<10} | -")
                continue
                
            start_time = time.perf_counter()
            sorted_arr = func(test_array, ascending=True)
            end_time = time.perf_counter()
            
            elapsed_time = end_time - start_time
            valid = is_sorted(sorted_arr, ascending=True)
            
            print(f"{size:<10} | {name:<18} | {elapsed_time:<10.5f} | {valid}")
        print("-" * 65)


if __name__ == "__main__":
    # Демонстрація роботи QuickSort на малому масиві (з дробовими числами)
    array_length = 6
    original_array = generate_array(array_length, 1, 50, use_floats=True)
    
    print("=== ВИХІДНИЙ МАСИВ (ДРОБОВІ ЧИСЛА) ===")
    print_array(original_array)
    print()

    print("=== QUICK SORT ===")
    
    sorted_asc = quick_sort(original_array, True)
    print("Прямий порядок (ascending = True):")
    print_array(sorted_asc)
    print(f"Масив впорядковано за зростанням? {is_sorted(sorted_asc, True)}\n")
    
    sorted_desc = quick_sort(original_array, False)
    print("Зворотний порядок (ascending = False):")
    print_array(sorted_desc)
    print(f"Масив впорядковано за спаданням? {is_sorted(sorted_desc, False)}\n")
    
    print("\n=== ПОРІВНЯННЯ ПРОДУКТИВНОСТІ АЛГОРИТМІВ ===")
    compare_performance()
