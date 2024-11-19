def are_anagrams(str1, str2):
 
    # Function implementation here ...
    str1 = str1.replace(" ", " ").lower()
    str2 = str2.replace(" ", " ").lower()
 
    return sorted(str1) == sorted(str2)

# ## Example 
# print(are_anagrams("listen", "silent"))  # Expected output: True
# print(are_anagrams("hello", "world"))    # Expected output: False
