preco = float(input("Insira o valor do carro: "))
parcelas = int(input("Insira o numero de parcelas: "))
juro = float(input("Insira a porcentagem de juros: "))

total = 0

for i in range(0, parcelas):
  total += (preco / parcelas) * (1 + (juro / 100))

print(f"Valor total: {total:.2f}")