def is_golden_number(n):
#     # function implementation ...
    for a in range(1, n):
        b = n - a 
        if (a * b) % 1000 == 0:      #This wil check if a * b is a divisble by 1000
         return True
    return False

# print(is_golden_number(65))
# print(is_golden_number(70))
# print(is_golden_number(62))