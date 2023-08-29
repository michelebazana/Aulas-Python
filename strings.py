frase = "Hello world!"
print(frase)
print(len(frase))
print(frase[0])

a = "Hello"
b = "world"
c = " "
d = "!"
e = a + c + b + d
print(e)
print(a + c + b + d * 3)

frase = "Hello world!"
print(frase[0:5])

nome = "Michele"
idade = 44
altura = 1.58
print(f"A {nome} tem {idade} anos e {altura} m de altura.")

frase = "Hello world!"
#frase[0] = "h"

frase_lista = list("Hello world!")
print(frase_lista)

frase_lista[0] = "h"
print(frase_lista)

frase_inteira = " ".join(frase_lista)
print(frase_inteira)

print(frase.startswith("Hello"))
print(frase.endswith("world"))
print("Hello" in frase)
print("Olá" in frase)

print(frase.count("Hello"))
print(frase.count("l"))

print(frase.find("Hello"))
print(frase.find("o"))

frase = "Hello world!"
print(frase.split())

print(frase.replace("world", "mundo"))
print(frase)

frase = "Hello world!"
print(frase.center(50,"."))

print(frase.rjust(50,"."))
print(frase.ljust(50,"."))

print("Hello","world")
print("Hello","world",sep=" ")
print("Hello","world",sep=", ")

print("Hello","world")
print("Hello","world",end="\n")
print("Hello","world")
print("Hello","world",end="\n\n")
print("Hello","world")
print("Hello","world",sep=", ",end="!")
