name = input("Insira o seu nome: ")
price = float(input("Insira o preco do produto: "))
quantity = int(input("Insira a quantidade comprada: "))

total = (quantity * price) * 0.90 if quantity > 10 else quantity * price

print(f"Usuario: {name} \nPreco unitario: {price} \nQuantidade: {quantity} \nValor total: {total}")