def check_age():
    age = int(input("age:"))

    if age < 18:
        print("You're not old enough to be here")
        quit()
    elif age >= 18:
        print("OK")

check_age()