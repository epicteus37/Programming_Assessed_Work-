def decrypt_cypher_text(encrypted_text, key):
#     # function implementation here...
     decrypted_text = ""
     for char in encrypted_text:
          ascii_code = ord(char)                       #This converts the characters to ASCII code
          new_ascii_code = ascii_code - key            #This will remove the given key from the ASCII code
          decrypted_ascii_code = new_ascii_code % 256  #This will find the remainder by dividing by 256
          decrypted_char = chr(decrypted_ascii_code)   #This converts the resulting ASCII code back to characters
          decrypted_text += decrypted_char             #This appends the decrypted text to the result string
     
     return decrypted_text

# encrypted_message = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$" # This is the encrypted text
# key = 3
# # print(decrypt_cypher_text(encrypted_message, key))
