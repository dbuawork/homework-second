# Вводимо 3 числа з яких нам потрібно знайти максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

# # Знаходимо найбільше із трьох
if n1 >= n2 and n1 >= n3:
    print(f"Найбільше число: {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"Найбільше число: {n2}")
elif n3 >= n1 and n3 >= n1:
    print(f"Найбільше число: {n3}")
else:
    print(f"equals")


