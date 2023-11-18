password = input("Enter password: ")
while len(password) >= 0:
    if len(password) > 0:
        print('*' * len(password))
        break
    password = input("Enter password: ")
