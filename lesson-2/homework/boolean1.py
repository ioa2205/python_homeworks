username = input("Enter username: ")
password = input("Enter password: ")
validation = {1:"not empty", 0:"empty"}
print(f"The username is {validation[bool(username)]}, the password is {validation[bool(password)]}")
