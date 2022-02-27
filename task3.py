check_password = lambda s: len(s) >= 8 and sum(
    set([1 if a.isupper() else (2 if a.islower() else (3 if a.isdigit() else 0)) for a in s])) == 6

if __name__ == '__main__':
    print(check_password(input()))
