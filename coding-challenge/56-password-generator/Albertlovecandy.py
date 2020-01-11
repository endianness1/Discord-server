import random
import string

def split(word):
    return [char for char in word]
charset = split(string.ascii_letters + string.digits)

def random_character():
    random_char = charset[random.randint(0,55)]
    return random_char
password = ""
i = 0
x = 0
#while i < 10:
   #password = random_char + password
   #i += 1
#print(password)
while i < 10:
    password = password + random_character()
    i += 1
    x = 1
while len(password) == 10 and x == 1:
    print(password)
    x = 0
