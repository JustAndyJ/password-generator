import random
print("Recommended passwords")

cant=int(input("enter the amount of passwors to generate: "))
lengh=int(input("enter the password lengh: "))
letter=("123456789qwertyuiopasdfghjklñzxcvbQWERTYUIOPASDFGHJKLÑZXCnmm#%=@*$")

for x in range (cant):
    password=""
    for x in range (lengh):
        password+=random.choice(letter)
    print(password)    

#11/09/2023


