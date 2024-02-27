money = []
price = 25
print(f"Price: {price}")
while (sum(money) < price):
    n = float(input(f"Insert money: "))
    money.append(n)
    if (sum(money) == price):
        print("Paid")
    elif ((price - sum(money)) < 0):
        print(f"You cannot insert more than the price.")
        money.pop()
    else:
        print("Remaing:", price - sum(money))
