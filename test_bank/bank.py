def main():
    # Prompt the user for input
    greeting = input("Enter a greeting: ")

    # Call the value function
    amount = value(greeting)

    # Print the amount
    print("Amount:", amount)


def value(greeting):
    # Convert the greeting to lowercase for case-insensitive comparison
    greeting = greeting.lower()

    # Check the conditions and return the corresponding amount
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
