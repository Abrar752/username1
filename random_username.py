import random as rand
while True:
    name = input("Enter your name: ")
    if name.isalpha():
        print("Your name is valid ")
        break
    else:
        print("Your name is invalid \n Please enter a valid name")
        continue

lower = name.lower()
name1 = "@" +lower + str(rand.randint(1000, 9999))
print(f"Your random username is: {name1}")