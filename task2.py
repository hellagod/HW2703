from random import randint

generate_password = lambda: "".join([chr(randint(33, 126)) for i in range(randint(7, 10))])

if __name__ == '__main__':
    print(generate_password())
