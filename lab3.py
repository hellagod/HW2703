import json


storage = []

def add():
    s1 = ''
    while not s1:
        s1 = input('Сформулируйте задачу: ')
    s2 = ''
    while not s2:
        s2 = input('Добавьте категорию к задаче: ')
    s3 = ''
    while not (s3 and s3.isnumeric()):
        s3 = input('Добавьте время к задаче: ')
    storage.append({'Задача': s1, 'Категория': s2, 'Дата': s3})
    todo()


def out():
    for el in storage:
        print(f'Задача: {el["Задача"]} Категория: {el["Категория"]} Дата: {el["Дата"]}')
    todo()


def save():
    with open('todo.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(storage))


def todo():
    print('Простой todo: \n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.\n')


if __name__ == '__main__':
    with open('todo.json') as f:
        storage = json.load(f)
    print('текущие задачи из файла:')
    print(storage)
    todo()
    while True:
        inp = input('Укажите число: ')
        if inp == '1':
            add()
        elif inp == '2':
            out()
        elif inp == '3':
            save()
        else:
            print('такой команды нет')
