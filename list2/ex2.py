numbers = []
while (True):
    n = float(input("Insira um numerno: "))
    if (n >= 0):
        numbers.append(n)
        continue
    
    print(f"sum: {sum(numbers)}, media {sum(numbers) / len(numbers)}")
    break