import random

x = int(input("enter x: "))

def the_list(x):
    result = set()
    while len(result) < x:
        result.add(random.randint(1,50))
    return list(result)

print(the_list(x))