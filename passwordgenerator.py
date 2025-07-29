import string
import random
import secrets

def generate_password(min,num=True,sp=True):
    letters = string.ascii_letters
    digits=string.digits
    special=string.punctuation
    characters=letters
    if num:
        characters+=digits
    if sp:
        characters+=special
    passw="" 
    mec=False
    hn=False
    hassp=False
    while not mec or len(passw)<min:
        new_char=random.choice(characters)
        passw+=new_char
        if new_char in digits:
            hn=True
        elif new_char in special:
            hassp = True
        mec=True
        if num:
            mec=hn

        if sp:
            mec=mec and hassp
    return passw
def estimate_strength(password):
    l=len(password)
    has_upper = any(c.isupper()
for c in password)
    has_lower=any(c.islower()for c in password)
    has_symbol=any(c in string.punctuation for c in password)
    has_digits=any(c.isdigit()for c in password)
    score=sum([has_upper,has_lower,has_digits,has_symbol])
    if l>=12 and score==4:
        return"strong"
    elif l>=8 and score>=3:
        return "medium"
    else:
        return"weak"

min_length=int(input("enter minimum length:"))
has_number=input("do you want to have number(y/n)?").lower()=="y"
has_special=input("dp you want to add special char(y/n)?").lower()=="y"
pwd=generate_password(min_length,has_number,has_special)
print("Password:",pwd)
print("Strength:",estimate_strength(pwd))
