def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero!"
    else:
        return x / y

def calculator():
    print("Welcome to Simple Calculator App")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == '+':
                print("Result:", add(num1, num2))
            elif operation == '-':
                print("Result:", subtract(num1, num2))
            elif operation == '*':
                print("Result:", multiply(num1, num2))
            elif operation == '/':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid operation! Please try again.")
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print("An error occurred:", str(e))

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            break

    print("Thank you for using Simple Calculator App")

if __name__ == "__main__":
    calculator()
