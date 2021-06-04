# Господа, эта программа предназначена для выполнения вычислений

print("Вас приветствует интерактивная программа-калькулятор")
print("Тут вы можете избавить свою ленивую задницу от необходимости самой выполнять вычисления") 

user_num_one = int(input("Введите первое число "))
operator = str(input("Введите оператор "))
user_num_two = int(input("Введите второе число "))
if operator == '+':
    result = user_num_one + user_num_two
    print(result)
elif operator == '-':
    result = user_num_one - user_num_two
    print(result)
elif operator == '*':
    result = user_num_one * user_num_two
    print(result)
elif operator == '/':
    result = user_num_one / user_num_two
    print(result)
else:
    print("Ошибка ввода")
