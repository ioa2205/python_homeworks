def password_checker(password):
    if len(password) < 8:
        print("Password is too short")
    elif not any(char.upper() for char in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")

password = input("Enter a password: ")
password_checker(password)  