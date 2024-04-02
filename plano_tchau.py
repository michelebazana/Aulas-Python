print("O seu pacote é o Tchau Pré-pago Prezão 15GB por R$29,99/mês.\n")

plano = input("Você utilizou todo o seu pacote (sim/não): ")

valor_mensal = 29.99

if plano == "sim":
    pacote_adicional = input("Você gostaria de contratar pacotes adicionais? ")
    if pacote_adicional == "sim":
        quant_pacotes = int(input("Quantidade de pacotes de adicional "
                                  "de 300MB = "))
        valor_mensal = 29.99 + quant_pacotes * 7.99

print(f"O valor mensal do plano é R${valor_mensal:.2f}.\n")

teste = input("Aperte o botão ENTER para sair do programa.")
