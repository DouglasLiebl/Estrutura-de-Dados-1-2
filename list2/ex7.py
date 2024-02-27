import random

p1 = 100
p2 = 100

while (True):
    p1 -= random.randint(0, 15)
    p2 -= random.randint(0, 15)

    if (p1 <= 0): 
        print("p2 win")
        break
    if (p2 <= 0): 
        print("p1 win")
        break
