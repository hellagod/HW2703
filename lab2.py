def add(surname: str, name: str):
    f = open("students.txt", 'r', encoding='utf-8')
    lines = [line.strip() for line in f.readlines()]
    lines.append(surname.strip() + " " + name.strip())
    lines.sort()
    f = open("students.txt", 'w', encoding='utf-8')
    for line in lines:
        f.write(line + "\n")


def find(surname: str, name: str = "") -> bool:
    f = open("students.txt", 'r', encoding='utf-8')
    i = 0
    for line in f:
        line = line.strip()
        ar = line.split()
        if (name and (surname + " " + name) == line) or ((not name) and surname == ar[0]):
            i += 1
            print(" ".join(ar))
    if i == 0:
        print('Студентов с такой фамилией нет')
        return False
    return True


def edit(old_surname, old_name, new_surname="", new_name=""):
    f = open("students.txt", encoding="utf8")
    lines = f.readlines()
    lines = [line.strip().split() for line in lines]
    i = 0
    for line in lines:
        if old_surname == line[0] and old_name == line[1]:
            i += 1
            if new_surname:
                line[0] = new_surname
            if new_name:
                line[1] = new_name
            break
    if i != 0:
        f = open("students.txt", "w", encoding="utf8")
        lines = list(map(lambda x: " ".join(x), lines))
        lines.sort()
        for line in lines:
            f.write(line + "\n")
    else:
        print('Студентов с такой фамилией нет')


def remove(surname: str, name: str):
    f = open("students.txt", encoding="utf8")
    lines = f.readlines()
    lines = [line.strip().split() for line in lines]
    if name:
        if lines.__contains__([surname, name]):
            i = lines.index([surname, name])
            lines.pop(i)
            f = open("students.txt", "w", encoding="utf8")
            for line in lines:
                f.write(" ".join(line) + "\n")
        else:
            print('Студентов с такой фамилией нет')
    else:
        if find(surname, name):
            name = input("Введите имя студента: \n")
            remove(surname, name)


if __name__ == '__main__':
    while True:
        inp = input()
        if inp == 'add':
            add(*input().split(" "))
        elif inp == 'find':
            find(*input().split(" "))
        elif inp == 'edit':
            edit(*input().split(" "))
        elif inp == 'remove':
            remove(*input().split(" "))
        else:
            print('такой команды нет')
