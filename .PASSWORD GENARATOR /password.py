import random as r 
password_length = int(input("Enter the length of the password: "))
characters = "syam143"
password = ''.join(r.choice(characters) for _ in range(password_length))
print("Generated password:", password)

