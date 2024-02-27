salary = float(input("Insira o salario: "))
valor_hora = (salary / 20) / 8

horas_trabalhadas = float(input("Insira o numero de horas extras: "))


print(f"Salario neste mes: {((horas_trabalhadas * valor_hora) * 1.50) + salary}")