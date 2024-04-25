# Define a function to perform basic arithmetic operations
def simple_calculator():
    # Prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user for an operation choice
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation based on the operation choice
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation."

    # Display the result
    print(f"The result is: {result}")

# Call the simple_calculator function
simple_calculator()
