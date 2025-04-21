list = ["vape", "tech", "fruits", "pendrive"]



def addprod():
    addp = input("What do you wanna add?: ")
    list.append(addp)

def remprod():
    remp = input("What do you wanna remove?: ")
    try:
        list.remove(remp)
    except ValueError:
        print("Sorry, that doesn't exist!")

def showlist():
    print(list)

def howmany():
    print(len(list))

def exit():
    quit()

while True:
    choose = input("What action?: ")
    if choose == "add":
      addprod()
    elif choose == "remove":
       remprod()
    elif choose == "show":
        showlist()
    elif choose == "howmany":
        howmany()
    elif choose == "exit":
        exit()
    else:
        print("That action doesn't exist, try something else!")