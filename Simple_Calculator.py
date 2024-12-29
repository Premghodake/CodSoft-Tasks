def show_menu():
    print("\nSimple Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (^)")
    print("7. Exit")

def perform_calculation(choice, num1, num2):
    if choice == "1":
        return num1 + num2
    elif choice == "2":
        return num1 - num2
    elif choice == "3":
        return num1 * num2
    elif choice == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed!"
    elif choice == "5":
        if num2 != 0:
            return num1 % num2
        else:
            return "Error: Modulus by zero is not allowed!"
    elif choice == "6":
        return num1 ** num2
    else:
        return "Invalid operation!"

while True:
    show_menu()
    user_choice = input("\nEnter your choice (1-7): ").strip()

    if user_choice == "7":
        print("Exiting the calculator. Goodbye!")
        break

    if user_choice in ["1", "2", "3", "4", "5", "6"]:
        try:
            number1 = float(input("\nEnter the first number: "))
            number2 = float(input("Enter the second number: "))
            result = perform_calculation(user_choice, number1, number2)
            print(f"\nResult: {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice! Please select a valid option.")
