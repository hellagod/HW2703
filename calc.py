def calc(a, b, operation):
    try:
        print(eval(f'{a}{operation}{b}'))
    except ZeroDivisionError:
        print('Ошибка деления на ноль')
    except NameError:
        print('Ошибка преобразования типов')


a, b, c = input().split(' ')
calc(a, b, c)
