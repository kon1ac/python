import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, n):
    return a ** n

def square_root(a):
    return math.sqrt(a)

def percent(a):
    return a / 100

def factorial(a):
    result = 1
    for i in range(1, a+1):
        result *= i
    return result

while True:
    print("Выберите операцию:")
    print("1. Сложить два числа")
    print("2. Вычесть первое число из второго")
    print("3. Перемножить два числа")
    print("4. Разделить первое число на второе")
    print("5. Возвести первое число в степень")
    print("6. Найти квадратный корень из числа")
    print("7. Найти факториал числа")
    print("8. Выйти из программы")

    choice = input("Введите номер операции: ")

    if choice == "8":
        break

    num1 = float(input("Введите первое число: "))

    if choice != "5" and choice != "6" and choice != "7":
        num2 = float(input("Введите второе число: "))

    if choice == "1":
        result = add(num1, num2)
        print("Результат:", result)
    elif choice == "2":
        result = subtract(num1, num2)
        print("Результат:", result)
    elif choice == "3":
        result = multiply(num1, num2)
        print("Результат:", result)
    elif choice == "4":
        result = divide(num1, num2)
        print("Результат:", result)
    elif choice == "5":
        n = int(input("Введите степень: "))
        result = power(num1, n)
        print("Результат:", result)
    elif choice == "6":
        result = square_root(num1)
        print("Результат:", result)
    elif choice == "7":
        result = factorial(int(num1))
        print("Результат:", result)
    else:
        print("Некорректный ввод операции")
