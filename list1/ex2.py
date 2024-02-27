pesos = [2, 3, 5]
notas = []

for i in range(0, 3):
  n = float(input(f"Insira a nota {i + 1}: "))
  notas.append(n * pesos[i])

media = sum(notas) / sum(pesos)
print(f"Media: {media}")