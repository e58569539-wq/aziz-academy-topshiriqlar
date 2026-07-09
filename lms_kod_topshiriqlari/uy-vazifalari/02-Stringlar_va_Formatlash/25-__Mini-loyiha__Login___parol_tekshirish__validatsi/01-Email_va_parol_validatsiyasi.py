email = input()
password = input()

is_valid_email = ("@" in email) and ("." in email) and (email == email.lower())

print(is_valid_email and is_valid_email)