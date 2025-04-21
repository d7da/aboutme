import time

username = ["4o2", "vzhqz", "TROLL"]
password = ["12345qwert", "12qwasyx", "qwertzuiop"]

retry = 0
def retries():
    global retry
    retry += 1
    if retry > 2:
        print("Too many retries, terminating session...")
        quit()

while True:
    choice = input("Login, register, exit: ")
    if choice == "register":
        time.sleep(0.4)
        register = input("New username: ")
        createpass = input("Create a password: ")
        username.append(register)
        password.append(createpass)
        time.sleep(0.6)
        print("Added new username: ", register)
        time.sleep(0.4)
        print("New password registered")
        time.sleep(0.7)
    elif choice == "exit":
        quit()
    elif choice == "login":
        login_user = input("Username?: ")
        loginpass = input("Password?: ")
        print("ran till this")
        # i put comments cuz i couldnt fucking debug for 1.5 hours
        # im a dumbass
        # check if the username exists first
        if login_user in username:
            index = username.index(login_user)
            # now check the password
            if loginpass == password[index]:
                time.sleep(0.9)
                print("Logged in as " + str(login_user))
            else:
                retries()
                print("Incorrect password, please try again.")
        else:
            retries()
            print("Username incorrect, please try again.")

    else:
        print("Invalid option. Please choose 'login', 'register', or 'exit'.")
