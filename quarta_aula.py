'''print(1)
print(2)
print(3)
print()
x = 1
print(x)
x = 2
print(x)
x = 3
print(x)
print()
x = 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)

x = 1
while x <= 3:
    print(x)
    #x = x + 1
    x += 1

x = 0
while x < 3:
    x += 1
    print(x)

#name GitHub = michelebazana
from time import sleep

x = 10
while x >= 0:
    print(x)
    sleep(1)
    x -= 1

print("Fogo!")

import time

x = 10
while x >= 0:
    print(x)
    time.sleep(1)
    x -= 1

print("Fogo!")

inicio = int(input("Entre com o primeiro número: "))
fim = int(input("Entre com o último número: "))

while inicio <= fim:
    print(inicio)
    inicio += 1

fim = int(input("Entre com o último número: "))
x = 0
while x <= fim:
    print(x)
    x += 2'''

num = int(input("Entre com a tabuada de: "))

x = 1
while x <= 10:
    print(num * x)
    x += 1
