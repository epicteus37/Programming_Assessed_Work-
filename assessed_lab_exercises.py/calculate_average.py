def calculate_average(numbers):
 
    # Function implementation here ...

    total = 0
    count = 0
    for num in numbers:
     total += num
     count += 1

    average = total / count

    return average

# # # Example usage
# numbers = [10, 20, 30, 40, 50]
# print("The average is:", calculate_average(numbers))  # Expected output: The average is: 30.0
