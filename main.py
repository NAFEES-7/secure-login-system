def register():
    with open("users.txt", "a") as f:
        username = input("Enter username: ")
        password = input("Enter password: ")
        f.write(f"{username},{password}\n")
    print("Registered successfully\n")


def login():
    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        with open("users.txt", "r") as f:
            for line in f:
                user, pwd = line.strip().split(",")
                if username == user and password == pwd:
                    print("Login Successful\n")
                    return

        attempts -= 1
        print(f"Invalid credentials. Attempts left: {attempts}\n")

    print("Account Locked\n")


def main():
    while True:
        print("==== MENU ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    main()
