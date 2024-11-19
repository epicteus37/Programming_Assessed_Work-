def find_maximum_difference(a, b):
    # code implementation here...
    min_a, max_a = min(a), max(a)
    min_b, max_b = min(b), max(b)
    
    # This will calculate the possible maxium differences
    maximum = max(abs(max_a - min_b), abs (max_b - min_a))
   
    return maximum

#a = [1, 5, 600]
#b = [100, 7, 3, 29, 39]

# print(find_maximum_difference(a, b))

