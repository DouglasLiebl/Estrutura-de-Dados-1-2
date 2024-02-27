letters = ["a", "e", "i", "o", "u"]
count = 0

word = input("Insira uma palavra: ")
for i in word:
    if (i in letters):
        count += 1

print("Numero de vogais:", count)