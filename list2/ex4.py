import random

numbers = []
for i in range(0, 20):
    numbers.append(random.randint(1, 6))

for i in range(1, 7):
    print(i, " -> ", numbers.count(i))