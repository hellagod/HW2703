documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def input_main(n):
    input_dictionary = {0: 'Введите команду:\n',
                        2: 'Введите номер полки:\n',
                        'd': 'Введите номер документа:\n',
                        't': 'Введите тип документа:\n',
                        'n': 'Введите владельца документа:\n',
                        's': 'Введите полку для хранения:\n'
                        }
    return str(input(input_dictionary[n]))


def document_owner(num):
    for doc in documents:
        if doc['number'] == num:
            print('Владелец документа ' + doc['name'])
            return
    print('Документ не найден в базе')


def document_shelf(num):
    n = document_shelf_n(num)
    if n != -1:
        print('Документ хранится на полке: ' + n)
    else:
        print('Документ не найден в базе')


def document_shelf_n(num):
    for key in directories:
        if num in directories[key]:
            return key
    return -1


def documents_inf():
    for doc in documents:
        print(
            f'№: {doc["number"]}, тип: {doc["type"]}, владелец: {doc["name"]}, полка хранения: {document_shelf_n(doc["number"])}')


def add_shelf(n):
    if n in directories:
        print('Такая полка уже существует. ' + shelfs())
    else:
        directories[n] = []
        print('Полка добавлена. ' + shelfs())


def shelfs():
    return f'Текущий перечень полок: {", ".join(directories.keys())}.'


def del_shelf(n):
    if not (n in directories):
        print('Такая полка не существует. ' + shelfs())
    elif directories[n]:
        print('На полке есть документа, удалите их перед удалением полки. ' + shelfs())
    else:
        directories.pop(n)
        print('Полка удалена. ' + shelfs())


def add_doc():
    doc = {'number': input_main('d'), 'type': input_main('t'), 'name': input_main('n')}
    s = input_main('s')
    if s in directories:
        documents.append(doc)
        directories[s].append(doc['number'])
        print('Документ добавлен. Текущий список документов:')
        documents_inf()
    else:
        print('Такой полки не существует. Добавьте полку командой as.')


def del_doc(n):
    for doc in documents:
        if doc['number'] == n:
            directories[document_shelf_n(n)].remove(n)
            documents.remove(doc)
            print('Документ удален. \nТекущий список документов:')
            documents_inf()
            return
    print('Документ не найден в базе. \nТекущий список документов:')
    documents_inf()


def move_doc(n):
    s = input_main('s')
    ln = document_shelf_n(n)
    if ln == -1:
        print('Документ не найден в базе. \nТекущий список документов:')
        documents_inf()
    elif not (s in directories):
        print('Такой полки не существует. ' + shelfs())
    else:
        directories[ln].remove(n)
        directories[s].append(n)
        print('Документ перемещен. \nТекущий список документов:')
        documents_inf()


def start():
    inp = input_main(0)
    while inp != 'q':
        if inp == 'p':
            document_owner(input_main('d'))
        elif inp == 's':
            document_shelf(input_main('d'))
        elif inp == 'l':
            documents_inf()
        elif inp == 'ads':
            add_shelf(input_main(2))
        elif inp == 'ds':
            del_shelf(input_main(2))
        elif inp == 'ad':
            add_doc()
        elif inp == 'd':
            del_doc(input_main('d'))
        elif inp == 'm':
            move_doc(input_main('d'))
        inp = input_main(0)


start()
