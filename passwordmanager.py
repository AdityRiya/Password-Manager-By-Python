pwd = input("What is the master password? ")

def view():
    pass
def add():
    pass

while True:
    mode = input("Would you like to add a new password or view existing ones (view or add) or press 'q' to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid Mode.")
        continue