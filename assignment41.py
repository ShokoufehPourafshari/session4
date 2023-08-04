import random
print("think about a number between 0 and 20")

my_number=random.randint(0,20)
count=1
for i in range (20):
    your_number = int(input("enter your guess: "))
    if your_number == my_number:
        print("yes you got it after", count, "try!")
        break

    if my_number > your_number:
        print("go up")
    if my_number < your_number:
        print("go down")
    count+=1