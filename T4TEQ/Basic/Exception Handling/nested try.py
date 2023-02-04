try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    try:
        result = num1 / num2
        print(f"Result is {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
except ValueError:
    print("Invalid input. Enter a valid number")
