def main():
    # User input
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    login_name = input("Enter your login name: ")
    password = input("Enter your password: ")
    repeat_password = input("Repeat your password: ")

    # Checking if passwords match
    if password != repeat_password:
        print("Incorrect password.")
    else:
        print(f"Welcome {name} {surname} in our team!")

if __name__ == "__main__":
    main()