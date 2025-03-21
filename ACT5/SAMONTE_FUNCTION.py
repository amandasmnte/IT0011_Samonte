def divide(a, b):
    if b == 0:
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return None
    return a % b

def summation(a, b):
    if b <= a:
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("\nSelect an operation:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting the program.")
            break
        
        if choice in ['D', 'R']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == 'D':
                result = divide(num1, num2)
                if result is None:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The result of {num1} / {num2} is: {result}")
            elif choice == 'R':
                result = remainder(num1, num2)
                if result is None:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The remainder of {num1} % {num2} is: {result}")
        
        elif choice == 'E':
            try:
                num1 = float(input("Enter the base number: "))
                num2 = float(input("Enter the exponent: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            result = exponentiate(num1, num2)
            print(f"The result of {num1} ** {num2} is: {result}")
        
        elif choice == 'F':
            try:
                num1 = int(input("Enter the first number (lower limit): "))
                num2 = int(input("Enter the second number (upper limit): "))
            except ValueError:
                print("Invalid input. Please enter integer values.")
                continue
            
            result = summation(num1, num2)
            if result is None:
                print("Error: The second number must be greater than the first number.")
            else:
                print(f"The summation from {num1} to {num2} is: {result}")
        
        else:
            print("Invalid choice. Please select a valid operation.")


if __name__ == "__main__":
    main()