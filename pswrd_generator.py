import random
import string

from more_itertools import random_combination

spcl_char = ["!", "@", "#", "$", "%", "&", "*"]

def lower():
    random_lower = chr(random.randint(ord("a"),ord("z")))
    return random_lower
def upper():
    random_upper = chr(random.randint(ord("A"),ord("Z")))
    return random_upper
def num():
    random_number = random.randint(1,1000)
    return random_number
def char():
    random_char = random.choice(spcl_char)
    return random_char
# print(random_lower)
# print(random_upper)
# print(random_number)
# print(random_char)

pswrd = []

i = 0
while(i<4):
    a1 = lower()
    i = i+1
    pswrd.append(a1)

i = 0
while(i<4):
    a2 = upper()
    i = i+1
    pswrd.append(a2)

i = 0
while(i<2):
    a3 = num()
    i = i+1
    pswrd.append(a3)

i = 0
while(i<2):
    a4 = char()
    i = i+1
    pswrd.append(a4)

password = "".join(str(i) for i in pswrd)

password_final = "".join(random.sample(password,len(password)))


print(f"Your whole new strong crispy-dispy password is: {password_final}")
