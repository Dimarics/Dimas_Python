# Господа, эта программа предназначена для выполнения вычислений

print("Вас приветствует интерактивная программа-калькулятор")
print("Здесь вы можете упростить свою жизнь и избавиться от необходимости самому выполнять вычисления") 

continued = 1

while continued != 'n':

    user_check_one = 'false'
    user_check_two = 'false'
    convert = 0
    
    while user_check_one == 'false':    # Проверка первого числа
        try:
            user_num_one = float(input("Введите первое число "))
        except ValueError:
            print("Ошибка ввода")
        else:
            user_check_one = 'true'

    while convert == 0:     # Проверка оператора
        operator = str(input("Введите оператор "))
        if operator == '+':     # Со строками логика работать не хочет, поэтому приходится делать так
            convert = 1
        elif operator == '-':
            convert = 1
        elif operator == '*':
            convert = 1
        elif operator == '/':
            convert = 1
        else:
            convert = 0
            print("Ошибка ввода")

    while user_check_two == 'false':    # Проверка второго числа
        try:
            user_num_two = float(input("Введите второе число "))
        except ValueError:
            print("Ошибка ввода")
        else:
            user_check_two = 'true'

    if operator == '+':     # Выполняем вычисления
        result = user_num_one + user_num_two
    elif operator == '-':
        result = user_num_one - user_num_two
    elif operator == '*':
        result = user_num_one * user_num_two
    else:
        result = user_num_one / user_num_two

    print()
    print("Результат: ", result)
    print()
    print("Продолжить? ")
    continued = str(input("Любой ввод - да, n - нет "))
