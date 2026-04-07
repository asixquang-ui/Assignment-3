correct_username = "nigga"
correct_password = "backtowork"

attempts = 0

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Incorrect login.")
        attempts += 1

if attempts == 5:
    print("Access denied")
