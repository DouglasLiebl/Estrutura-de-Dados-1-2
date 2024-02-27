greater = 0

for i in range(0, 3):
  n = float(input(f"Insira o numero {i + 1}: "))
  if (n > greater): 
    greater = n

print(f"Maior numero: {greater}")