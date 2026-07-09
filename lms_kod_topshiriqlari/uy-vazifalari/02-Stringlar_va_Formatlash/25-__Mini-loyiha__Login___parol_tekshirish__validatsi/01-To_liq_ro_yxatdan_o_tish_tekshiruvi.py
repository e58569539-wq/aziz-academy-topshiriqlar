login = input()
password = input()

is_valid = (len(login) >= 3) and (len(password) >= 8) and (login != password)

print(is_valid)