# num1 = 5
# num2 = 8.5
# print(num1 + num2)
# print(type(num1))
# print(type(num2))

# pi = 3.1415
# print(f"O número pi com duas casas decimais é {pi:.2f}.")

# d = True
# e = False
# print(type(d))
# print(type(e))

# nota = 6
# media = 7
# aprovado = nota >= media
# print(aprovado)

media_final = float(input("Média final da disciplina de 0 a 10 = "))
frequencia = int(input("Frequência da disciplina em porcentagem = "))

if media_final >= 6 and frequencia >= 75:
    print("Aprovado!")
else:
    print("Reprovado!")
