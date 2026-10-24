# 1. 
def print_1_to_n(n):
    if n > 1:
        print_1_to_n(n - 1)
    print(n, end=" ")

# 2. 
def print_a_to_b(a, b):
    print(a, end=" ")
    if a < b:
        print_a_to_b(a + 1, b)
    elif a > b:
        print_a_to_b(a - 1, b)

# 3. 
def is_power_of_two(n):
    if n == 1:
        print("YES")
        return
    if n == 0 or n % 2 != 0:
        print("NO")
        return
    is_power_of_two(n // 2)

# 4. 
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

# 5. 
def digits_right_to_left(n):
    print(n % 10, end=" ")
    if n // 10 > 0:
        digits_right_to_left(n // 10)

# 6. 
def digits_left_to_right(n):
    if n // 10 > 0:
        digits_left_to_right(n // 10)
    print(n % 10, end=" ")
