cont = 1
soma = 0

while cont <= 10:
    num = float(input(f"Digite o {cont}º número: "))
    soma += num
    cont += 1

print(f"A soma dos 10 números é igual a {soma:.2f}.")
print(f"A média dos 10 números é igual a {soma/10:.2f}.")
print(f"A média dos 10 números é igual a {soma/(cont-1):.2f}.")
