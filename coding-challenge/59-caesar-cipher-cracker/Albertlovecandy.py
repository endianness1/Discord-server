import os
choice = int(input("Do you want to (1) Encrypt or (2) Decrypt"))
key = int(input("Enter key:"))
converted_text = ""

if choice == 1:
    plaintext = input("Enter plaintext:")
    chars = [char for char in plaintext]
    for char in chars:
       ch = chr(ord(char)+key)
       converted_text = converted_text + ch
    print(converted_text)
elif choice == 2:
    ciphertext = input("Enter ciphertext:")
    chars = [char for char in ciphertext]
    for char in chars:
       ch = chr(ord(char)-key)
       converted_text = converted_text + ch
    print(converted_text)
else:
    print("Incorrect choice")
    os.exit()
