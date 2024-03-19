# media_final = int(input("Média final = "))
# if media_final >= 70:
#     print("Aprovado!")
# else:
#     print("Reprovado!")

#exercício 1
vel = int(input("Entre com a velocidade do carro em km/h = "))
if vel > 80:
    print("Você foi multado!")
    multa = (vel - 80) * 5
    print(f"O valor da sua multa é R$ {multa:.2f}.")
