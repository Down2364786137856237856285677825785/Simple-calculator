import time

# Variables for language detection
Russian_Language = ['Русский', 'русский', 'РУССКИЙ', '1']
English_Language = ['English', 'english', 'ENGLISH', '2']

while True:
    Select_Language = input("""
Выберите язык/Select language:

Русский
English 
""")

# language definition
    if Select_Language in Russian_Language:
        language = 'ru'
        break
    elif Select_Language in English_Language:
        language = 'en'
        break
    else:
        print("Неверный выбор, попробуйте снова.")
        time.sleep(1)

# Launching the calculator in Russian
while True:
    if language == 'ru':
        try:
            num1 = float(input("Введите первое число: "))
            time.sleep(0.5)
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Это не число")
            continue
        
        operators2 = input("""Введите оператор:
+ = Плюс
- = Минус
* = Умножение
/ = Деление\n """)
        
        if operators2 == '+':
            total = num1 + num2
            print(f"{num1} {operators2} {num2} = {total}")
        elif operators2 == '-':
            total = num1 - num2
            print(f"{num1} {operators2} {num2} = {total}")
        elif operators2 == '*':
            total = num1 * num2
            print(f"{num1} {operators2} {num2} = {total}")
        elif operators2 == '/':
            if num2 == 0:
                print("Нельзя поделить на ноль")
                time.sleep(1.5)
                continue
            total = num1 / num2
            print(f"{num1} {operators2} {num2} = {total}")
        else:
            print("Неизвестный оператор!")
        time.sleep(2)
      
    # Launching the calculator in English
    elif language == 'en':
        try:
            num1 = float(input("Enter the first number: "))
            time.sleep(0.5)
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("This is not a number\nPlease try again")
            time.sleep(2)
            continue

        operators2 = input("""Enter the operator:
+ = Plus
- = Minus
* = Multiplication
/ = Division\n """)
        
        if operators2 == '+':
            total = num1 + num2
            print(f"{num1} {operators2} {num2} = {total}")
        elif operators2 == '-':
            total = num1 - num2
            print(f"{num1} {operators2} {num2} = {total}")
        elif operators2 == '*':
            total = num1 * num2
            print(f"{num1} {operators2} {num2} = {total}")
        elif operators2 == '/':
            if num2 == 0:
                print("You can't divide by zero\nPlease try again")
                time.sleep(2)
                continue
            total = num1 / num2
            print(f"{num1} {operators2} {num2} = {total}")
        else:
            print("Unknown operator!\nPlease try again")
        time.sleep(2)
        
