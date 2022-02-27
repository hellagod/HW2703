import task2
import task3

password = task2.generate_password()
print(password)
i = 1
while task3.check_password(password):
    password = task2.generate_password()
    print(password)
    i += 1

print(i)
