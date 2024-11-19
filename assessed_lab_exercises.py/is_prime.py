def is_prime(num):

    # Function implementation here ...
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# Run code example
# boolean = is_prime(5)   # returns True
# print(boolean)
  