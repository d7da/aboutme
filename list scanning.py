import time # imported time for more dramatic experience :)

def show():
  try:
    with open("list.txt", "x") as file:
        file.write("")  # create the file only if it doesnt exist
  except FileExistsError:
    pass  
  with open("list.txt", "r") as file: #opens the file with "reading mode"
    lines = file.read().splitlines() # read the file, the splitlines prints the files in a list
    print(lines) 

def checkports():
  found = False # set flag to false
  try:
    with open("list.txt", "x") as file:
     file.write("")  # create the file only if it doesnt exist
  except FileExistsError:
    pass  
  with open("list.txt", "r") as file:
    lines = file.read().splitlines()
    askrange = input("What's the checking range?: ") # ask for input
    if int(askrange) > 9999: # set a maximum cap, and convert string to int
      time.sleep(0.6)
      print("Maximum limit exceeded")
      return
  for port in range(int(askrange)): # running a loop and checking if the input is in the file converted to an int
    if str(port) in lines:
         found = True # set flag to true
         time.sleep(0.2)
         print(f"Port {port} found")
  if not found:
      time.sleep(0.2)
      print("Port not found!")

def addport():
   try:
    with open("list.txt", "x") as file:
        file.write("")  # create the file only if it doesnt exist
   except FileExistsError:
    pass  
   with open("list.txt", "r") as file:
      lines = file.read().splitlines()
      print(lines)
      askto = input("What port to add?: ")
   if askto in lines: # first check if the port already exists or not
     time.sleep(0.5)
     print("Port already exists")
     return
   if int(askto) > 9999: # set a maximum cap, and convert string to int
     time.sleep(1)
     print("Maximum limit exceeded")
     return
   if askto.isdigit(): # if we pass the first check, proceed to next
       with open("list.txt", "a") as file:
        file.write(askto + "\n") # if we pass both then write to file
        print(f"Port {askto} added")

   else:
     print("That's not a valid number, please add a number")


while True:
 ask = input("What do you wanna do?: ")
 if ask == "add":
   time.sleep(0.3)
   addport()
 elif ask == "check":
   time.sleep(0.3)
   checkports()
 elif ask == "show":
   time.sleep(0.3)
   show()
 else:
  time.sleep(0.3)
  print("Unknown command, use add, check or show")
