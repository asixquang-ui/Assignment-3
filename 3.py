numbers = []

while True:
    user_input = input("Enter a number (empty to quit): ")

    if user_input == "":
        break

    numbers.append(int(user_input))

if numbers:
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))
else:
    print("No numbers entered.")
