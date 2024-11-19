def calculator(num1, num2, operator):

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    elif operator == "%":
        if num2 == 0:
            return "Error: Modulus by zero is not allowed."
        else:
            return num1 % num2
    elif operator == ">":
        return num1 > num2
    elif operator == ">=":
        return num1 >= num2
    elif operator == "<":
        return num1 < num2
    elif operator == "<=":
        return num1 <= num2
    else:
        return "Invalid operator"

# Example Usage
#print(calculator(4, 5, "*"))  # Output: The result is: 20
#rint(calculator(10, 2, "/"))  # Output: The result is: 5.0
#print(calculator(7, 7, ">="))  # Output: The comparison result is: True
#print(calculator(10, 0, "/"))  # Output: Error Division by zero is not allowed
#print(calculator(12, 8, "+"))  # Output: The result is: 20
#print(calculator(20, 5, "-"))  # Output: The result is: 15
#print(calculator(10, 3, "%"))  # Output: The result is: 1
  
