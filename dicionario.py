# cadastro = {"6342764273": ["Michele", 1978, "São José do Rio Pardo", "SP"],
#             "8724390750": ["Jennyfer", 2005,"São Paulo", "SP"]}
# print(cadastro)
#
# print(cadastro["6342764273"])
#
# cadastro["8724390750"][0] = "Jennifer"
#
# print(cadastro["8724390750"])
#
# del cadastro["6342764273"]
#
# print(cadastro)
#
# print("4839573483" in cadastro)
# print("8724390750" in cadastro)
#
# print(cadastro.keys())
# print(cadastro.values())

cadastro = {"6342764273": ["Michele", 1978, "São José do Rio Pardo", "SP"],
            "8724390750": ["Jennyfer", 2005,"São Paulo", "SP"],
            "8978973985": ["Amaury", 1994, "Varzelândia", "MG"]}

for chave, valores in cadastro.items():
    print("Nome:", valores[0])
    print("CPF:", chave)
    print("Ano de nascimento:", valores[1])
    print(f"Cidade e estado de nascimento: {valores[2]}/{valores[3]}\n")

while True:
    cpf = input("Digite o CPF ou fim para sair: ").lower()
    if cpf == "fim":
        break
    if cpf in cadastro:
        print(f"Nome: {cadastro[cpf][0]}")
    else: print("CPF não encontrado!")