import random
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$@'
number=int(input("How many passwords you need? "))
length=int(input("Password Length? "))
for i in range(number):
    password=''
    for y in range(length):
        password += random.choice(chars)
    print(password)
        
