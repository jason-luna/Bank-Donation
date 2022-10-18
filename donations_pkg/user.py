def login(database, username, password):
    if username in database.keys() and password == database[username]:
        print("\nWelcome", username + "!")
        return username
    elif username in database.keys() and not password == database[username]:
        print("Incorrect password")
        return ""
    else:
        print("\nUser not found")
        return ""


def register(database, username, password):
    if username in database.keys():
        print("\nUsername already registered")
        return ""
    elif len(username) > 10:
        print("\nUsername cannot be over 10 characters")
        return ""
    elif len(password) < 5:
        print("\nPassword must be at least 5 characters")
        return ""
    elif len(username) < 10 and len(password) >= 5:
        print(f"\n{username} has been registered")
        return username
    else:
        print("\nUsername must be 1-10 characters long and password must contain at least 5 characters")
        return ""
