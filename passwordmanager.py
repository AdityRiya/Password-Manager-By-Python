pwd = input("What is the master password? ")


while True:
    mode = input("Would you like to add a new password or view existing ones (view or add)? ").lower()

    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid Mode.")