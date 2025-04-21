list = ["tech", "music", "coding"]


def addahobby():
    hobbyadd = input("What do you wanna add?: ")
    list.append(hobbyadd)

def remahobby():
    hobbyrem = input("What do you wanna remove?: ")
    list.remove(hobbyrem)

def printlength():
    print(len(list))

def printlist():
    print(list)

question = input("What do you wanna do?: ")
if question == "add":
    addahobby()
elif question == "remove":
    remahobby()
elif question == "printlen":
    printlength()
elif question == "print":
    printlist()
