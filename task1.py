from random import randint

a = input('Введите целое число от 1 до 10: ')
n = randint(1, 10)
while n != int(a):
    a = input(f"Загаданное число {'меньше' if int(a) > n else 'больше'}, попробуй ещё: ")
print('Вы угадали')
