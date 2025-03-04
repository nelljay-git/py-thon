first_value = float(input("Enter first value: "))
second_value = float(input("Enter second value: "))
operator = input("Select operator: +, -, /, *")

if operator == "+":
    print(first_value + second_value)
elif operator == "-":
    print(first_value - second_value)
elif operator == "/":
    if second_value == 0:
        print("Error: Division by zero is not allowed")
    else:
        print(first_value - second_value)
elif operator == "*":
    print(first_value * second_value)
else:
    print("Invalid operator")
    