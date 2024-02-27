numbers = []
count = 1
n = int(input("Insira um numero "))

while(count < n):
    if ((n % count) == 0):
        numbers.append(count)
    count += 1

if (sum(numbers) == n):
    print("perfeito")
else:
    print("imperfeito")