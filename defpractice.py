def login(name, age):
    if age < 18:
        print("Login Denied, Sorry " + name + ".")
    elif age >= 18:
        print("Login successful " + name + "!")

name = input("What's your name?: ")
age = int(input("How old are you?: "))

login(name, age)