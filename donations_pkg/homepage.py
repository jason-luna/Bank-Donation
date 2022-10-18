def show_homepage():
    print("")
    print("         === DonateMe Homepage ===        ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("------------------------------------------")
    print("|              5.    Exit                |")
    print("------------------------------------------")


def donate(username):
    while True:
        try:
            donation_amt = float(input("Enter amount to donate: "))
        except ValueError:
            print("\nPlease enter a dollar amount to donate")
            continue
        else:
            donation_string = (f"{username} donated ${donation_amt}")
            if donation_amt > 0:
                print("\nThank you for your donation!")
                return donation_string, donation_amt
            else:
                print("\nEnter an amount greater than $0 to donate")


def show_donations(donations, donation_amt_list):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)
        print(f"Total: ${(sum(donation_amt_list))}")
