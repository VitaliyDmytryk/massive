import random

def generate_array(length: int, start: int = 1, end: int = 100) -> list[int]:
   
    return [random.randint(start, end) for _ in range(length)]


def print_array(arr: list[int]) -> str:
    
    formatted_elements = [f"[cell - {i}, value - {val}]" for i, val in enumerate(arr)]
    result_str = "{" + ", ".join(formatted_elements) + "}"
    print(result_str)
    return result_str


def bubble_sort(arr: list[int], ascending: bool = True) -> list[int]:
   
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            should_swap = (a[j] > a[j + 1]) if ascending else (a[j] < a[j + 1])
            if should_swap:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr: list[int], ascending: bool = True) -> list[int]:
    
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and ((a[j] > key) if ascending else (a[j] < key)):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(arr: list[int], ascending: bool = True) -> list[int]:
    """
    Сортування вибором (Selection Sort).
    """
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


if __name__ == "__main__":
    # Генерація вихідного масиву
    array_length = 6
    original_array = generate_array(array_length, 1, 50)
    
    print("=== ВИХІДНИЙ МАСИВ ===")
    print_array(original_array)
    print()

    # 1. Bubble Sort
    print("=== BUBBLE SORT ===")
    print("Прямий порядок (ascending = True):")
    print_array(bubble_sort(original_array, True))
    print("Зворотний порядок (ascending = False):")
    print_array(bubble_sort(original_array, False))
    print()

    # 2. Insertion Sort
    print("=== INSERTION SORT ===")
    print("Прямий порядок (ascending = True):")
    print_array(insertion_sort(original_array, True))
    print("Зворотний порядок (ascending = False):")
    print_array(insertion_sort(original_array, False))
    print()

    # 3. Selection Sort
    print("=== SELECTION SORT ===")
    print("Прямий порядок (ascending = True):")
    print_array(selection_sort(original_array, True))
    print("Зворотний порядок (ascending = False):")
    print_array(selection_sort(original_array, False))
