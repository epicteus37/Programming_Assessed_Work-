def winning_numbers(user_list, winning_list):


    matches = len(set(user_list) & set(winning_list))
    if matches == 3:
        prize = "First"
    elif matches == 2:
        prize = "Second"
    elif matches == 1:
        prize = "Third"
    else:
        prize = "No"
    # Print the result
    print(f"Congratulations, you won {prize} prize!")
    return prize

# winning_list = [5, 14, 17]
# user_list = [5, 14, 17]
# result = winning_numbers(user_list, winning_list)