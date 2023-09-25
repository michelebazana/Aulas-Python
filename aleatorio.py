
# from random import randint
#
# num_aleatorio = randint(1,5)
#
# chances = 0
# while chances < 3:
#     num_escolha = int(input("Escolha um número inteiro <= 5 e >=1: "))
#     if num_escolha == num_aleatorio:
#         print("Você acertou!")
#     else:
#         print("Você errou!")
#     chances += 1

# from random import choice
#
# frutas = ["uva", "pera", "laranja", "abacaxi"]
# print(choice(frutas))

from random import choice

frutas = ["uva", "pera", "laranja", "abacaxi"]
sorteio = choice(frutas)
escolha = input("Entre com uma fruta: ")

if escolha == sorteio:
    print("Você acertou!")
else:
    print("Você errou!")
