# Господа, эта программа поможет вам в вычислениях

print("\nВас приветствует интерактивная программа-калькулятор!\nЗдесь вы можете упростить свою жизнь и избавиться от необходимости самому выполнять вычисления\n")

import math
continued = 1

note = input("Вызвать справку?\nspace - нет, другой ввод - да ")
print()
if note != ' ':
    print("                 +    сложение - последовательно указываются 2 слагаемых;\n")
    print("                 -    вычитание - сначала указывается уменьшаемое, затем вычитаемое;\n")
    print("                 *    умножение - последовательно указывается 2 множителя;\n")
    print("                 /    деление - сначала указывается делимое, затем делитель;\n")
    print("                 ^    возведение в степень - первым вводится основание, вторым - показатель степени\n                      (для нахождения корня используйте рациональный показатель степени);\n")
    print("                 =    возвращает значение 'True' если первое число равно второму или 'False' - если не равно;\n")
    print("                //    деление без дробного остатка - сначала указывается делимое, затем делитель;\n")
    print("               log    логарифм - первым вводится число под логарифмом, вторым - основание;\n")
    print("               deg    переводит указанное количество радиан в градусы (вторым значением служит любой ввод);\n")
    print("               rad    переводит указанное количество градусов в радианы (вторым значением служит любой ввод);\n")
    print("     sin, cos, tan    синус, косинус, тангенс, указанного угла в градусах - первым значением служит любой ввод,\n                      далее по порядку вводится оператор и количество градусов;\n")
    print("  asin, acos, atan    возвращает значение арксинуса, арккосинуса или арктангенса в градусах - первым значением служит любой ввод,\n                      далее по порядку вводится оператор и второе значение\n")

while continued != ' ':

    user_check_one = 'false'
    user_check_two = 'false'
    user_check_three = 'false'
    convert = 0
    
    while user_check_one == 'false':    # Проверка первого числа
        try:
            user_num_one = float(input("Введите первое значение: "))
        except ValueError:
            print("Ошибка ввода")
        else:
            user_check_one = 'true'

    while convert == 0:     # Проверка оператора
        operator = input("Введите оператор: ")
        if operator == '+':     # Со строками логика работать не хочет, поэтому приходится делать так
            convert = 1
        elif operator == '-':
            convert = 2
        elif operator == '*':
            convert = 3
        elif operator == '/':
            convert = 4
        elif operator == '^':
            convert = 5
        elif operator == '=':
            convert = 6
        elif operator == '//':
            convert = 7
        elif operator == 'log':
            convert = 8
        elif operator == 'deg':
            convert = 9
        elif operator == 'rad':
            convert = 10
        elif operator == 'sin':
            convert = 11
        elif operator == 'cos':
            convert = 12
        elif operator == 'tan':
            convert = 13
        elif operator == 'asin':
            convert = 14
        elif operator == 'acos':
            convert = 15
        elif operator == 'atan':
            convert = 16
        else:
            convert = 0
            print("Ошибка ввода")

    while user_check_two == 'false':    # Проверка второго числа
        while user_check_three == 'false':
            try:
                user_num_two = float(input("Введите второе значение: "))
            except ValueError:
                print("Ошибка ввода")
            else:
                user_check_three = 'true'
        if user_num_two == 0 and operator == '/':   # Проверка деления на ноль
            print("На ноль делить нельзя!")
            user_check_three = 'false'
        elif (user_num_two <= 0 or user_num_two == 1) and operator == 'log':     # Проверка области определения основания логарифма
                    print("основание логарифма должно быть больше нуля и не равно 1")
                    user_check_three = 'false'
        elif (user_num_two < -1 or user_num_two > 1) and operator == 'asin':     # Проверка области определения арксинуса
            print("значение арксинуса должно принадлежать интервалу от -1 до 1")
            user_check_three = 'false'
        elif (user_num_two < -1 or user_num_two > 1) and operator == 'acos':     # Проверка области определения арккосинуса
            print("значение арккосинуса должно принадлежать интервалу от -1 до 1")
            user_check_three = 'false'
        else:
            user_check_two = 'true'

    if operator == '+':     # Выполняем вычисления
        result = user_num_one + user_num_two
    elif operator == '-':
        result = user_num_one - user_num_two
    elif operator == '*':
        result = user_num_one * user_num_two
    elif operator == '/':
        result = user_num_one / user_num_two
    elif operator == '^':
        result = user_num_one ** user_num_two
    elif operator == '//':
        result = user_num_one // user_num_two
    elif operator == 'log':
        try:
            result = math.log(user_num_one, user_num_two)       # Проверка области определения числа под логарифмом
        except ValueError:
            print("Число под логарифмом должно быть больше нуля!")
            result ='not defined'
    elif operator == 'rad':
        result = math.radians(user_num_one)
    elif operator == 'deg':
        result = math.degrees(user_num_one)     
    elif operator == 'sin':
        result = math.sin(math.radians(user_num_two))
    elif operator == 'cos':
        result = math.cos(math.radians(user_num_two))
    elif operator == 'tan':
        result = math.tan(math.radians(user_num_two))
    elif operator == 'asin':
        result = math.degrees(math.asin(user_num_two))
    elif operator == 'acos':
        result = math.degrees(math.acos(user_num_two))
    elif operator == 'atan':
        result = math.degrees(math.atan(user_num_two))
    else:
        if user_num_one == user_num_two:
            result = 'True'
        else:
            result = 'False' 

    if type(result) == float:   # отсеивает переменные типа 'float' от остальных
        check_result = result - int(result)     # Эта конструкция позволяет избавиться от нуля в конечном результате при получении целого числа
        if check_result == 0:
            final_result = int(result)
        else:
            final_result = result
    else:
        final_result = result
        
    print("\nРезультат: ", final_result, "\n")
    print("Продолжить? ")
    continued = input("space - нет, другой ввод - да ")
    print()
