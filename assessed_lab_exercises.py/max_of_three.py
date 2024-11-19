def max_of_three(num1, num2, num3):
   
    maximum = num1

    if num2 > maximum:
        maximum = num2

    if num3 > maximum:
        maximum = num3

    return maximum

# Example usage:
# maximum = max_of_three(10, 20, 30)
# print(maximum, "is the maximum")