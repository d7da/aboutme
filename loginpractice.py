username = "4o2"
password = "12345qwert"

retry = 0
def retries():
  global retry
  retry +=1
  if retry > 2:
    print("Too many retries, terminating session...")
    quit()

while True:
    user = input("Username?: ")
    passwordin = input("Password?: ")
    if user == username and passwordin == password:
     print("Logged in as " + username)
     quit()
    else:
     retries()
     print("Username or password incorrect, please try again. Retries: " + str(retry))
     
