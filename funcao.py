def soma(a, b):
    print(a + b)

soma(1, 1)
soma(2, 4)

def ehpar(x):
    return x % 2 == 0

print(ehpar(2))
print(ehpar(3))

def parouimpar(x):
    if ehpar(x):
        return "par"
    else:
        return "impar"

print(parouimpar(2))
print(parouimpar(3))

def maior(a,b):
    if a > b:
        return a
    else:
        return b

print(maior(5, 10))

def maior_max(a, b):
    num = [a, b]
    return max(num)

print(maior_max(5, 10))

def valida_num(num, min, max):
    return num >= min and num <= max

print(valida_num(5, 5, 10))
print(valida_num(1, 5, 10))

def valida_string(s, min, max):
    tamanho = len(s)
    return min <= tamanho <= max

print(valida_string("michele", 7, 10))
print(valida_string("michele", 8, 11))

def barra():
    return print("*" * 40)

barra()

def barra_op(n=40, caractere="*"):
    return print(n * caractere)

barra_op()
barra_op(80, "_")

def soma(a, b, imprime=True):
    s = a + b
    if imprime:
        print(s)
    return s

print(soma(1, 2))
print(soma(3, 4, False))

def soma(a, b):
    print(a + b)

lista = [9, 10]
soma(*lista)

print(sum(lista))

v = lambda r, i: r * i
print(f"V = {v(100, 1)}V")
