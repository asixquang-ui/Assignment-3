while True:
    inches = float(input("Enter inches (negative to quit): "))

    if inches < 0:
        print("Program ended.")
        break

    cm = inches * 2.54
    print(f"{inches} inches = {cm:.2f} cm")
