def sum_of_evens(min_value, max_value):

    # Function implementation here ...
    total = 0 
    for number in range(min_value, max_value+1):
        if number %2==0:
            total += number
    return total

# # # Run code example
#min_value = 10
#max_value = 13
#result = sum_of_evens(min_value, max_value) # returns 22
#print(result)