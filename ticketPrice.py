while True:
    try:
        age = int(input("Enter your age (or type '0' to exit): "))

        if age == 0:
            print("Exiting the program.")
            break

        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 15
        else:
            ticket_price = 20

        print(f"The cost of your movie ticket is {ticket_price}\n")

    except ValueError:
        print("Invalid input. Please enter a valid age or '0' to exit.\n")
