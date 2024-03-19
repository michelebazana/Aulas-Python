'''media_final = int(input("Entre com a sua média final = "))
if media_final >= 60:
    print("Aprovado")
else:
    print("Reprovado")'''

velocidade = int(input("Entre com a sua velocidade em km/h = "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado e o valor da multa é de R$ {multa:.2f}.")
else:
    print("Parabéns você não foi multado!")
