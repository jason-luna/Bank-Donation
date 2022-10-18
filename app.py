from donations_pkg import homepage, user

database = {"admin": "password123"}
donations = []
donation_amt_list = []
authorized_user = ""

while True:
    homepage.show_homepage()
    if len(authorized_user) == 0:
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)
    user_input = input("Choose an option: ")
    if user_input == "1":
        username = (input("\nEnter username: ").lower())
        password = input("Enter password: ")
        authorized_user = user.login(database, username, password)
    elif user_input == "2":
        username = (input("\nEnter username: ").lower())
        password = input("Enter password: ")
        authorized_user = user.register(database, username, password)
        if len(authorized_user) != 0:
            database[username] = password
    elif user_input == "3":
        if len(authorized_user) == 0:
            print("\nYou are not logged in!")
        else:
            donation_string, donation_amt = homepage.donate(authorized_user)
            donations.append(donation_string)
            donation_amt_list.append(donation_amt)
    elif user_input == "4":
        homepage.show_donations(donations, donation_amt_list)
    elif user_input == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Choose an option from the menu")
