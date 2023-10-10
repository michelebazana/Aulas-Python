# arquivo = open("aula_arquivo.txt", "w")
# arquivo.write("Primeira aula de arquivo de texto.")
# arquivo.close()

# with open("aula_arquivo.txt","w") as arquivo:
#     arquivo.write("Hoje vai chover.")

# arquivo = open("aula_arquivo.txt", "r")
# print(arquivo.read())
# arquivo.close()

# with open("aula_arquivo.txt", "r") as arquivo:
#     print(arquivo.read())

# with open("aula_arquivo.txt", "a") as arquivo:
#     arquivo.write("Amanhã fará sol.")

# with open("aula_arquivo.txt", "a") as arquivo:
#     arquivo.write("\nAmanhã fará sol.")

# with open("aula_arquivo.txt", "r") as arquivo:
#     print(arquivo.readline())
#     print(arquivo.readline())

with open("aula_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
