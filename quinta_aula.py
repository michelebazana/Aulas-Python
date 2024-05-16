nomes_alunos = ["Mayene", "Pedro", "André", "Eduardo"]
print(nomes_alunos)
print(nomes_alunos[2])

nomes_alunos[2] = "Arthur"
print(nomes_alunos)

nomes_alunos.sort()
print(nomes_alunos)

idades = [21, 19, 37, 18, 0]
idades.sort()
print(idades)

idades.sort(reverse=True)
print(idades)

idades[4] = 45
print(idades)

nomes_alunos.append("João")
print(nomes_alunos)

idades.append(19)
print(idades)

nomes_alunos.append(["Lucca", "Lucas"])
print(nomes_alunos)
print(nomes_alunos[5])
print(len(nomes_alunos))
print(nomes_alunos[5][0])

nomes_alunos.extend(["Miguel", "Rodrigo"])
print(nomes_alunos)

idades.extend([20, 22])
print(idades)

nomes_alunos.extend(["Emily"])
print(nomes_alunos)
print(idades)
print(idades[3:6])
print(idades[3:7])
print(idades[0:3])
print(idades[:3])
print(idades[:-1])
print(idades[:-2])
print(idades[:-8])
print(idades[:-9])
print(idades[-1])
print(idades[-2])

print(nomes_alunos)

nomes_alunos_back = nomes_alunos
print(nomes_alunos_back)

nomes_alunos.append("Nicolas")
print(nomes_alunos)
print(nomes_alunos_back)

nomes_alunos_back.append("Vinicius")
print(nomes_alunos_back)
print(nomes_alunos)

nomes_alunos_back = nomes_alunos[:]
nomes_alunos.append("Victor")
print(nomes_alunos)
print(nomes_alunos_back)

nomes_alunos_back = nomes_alunos[0:3]
print(nomes_alunos_back)

del nomes_alunos_back[2]
print(nomes_alunos_back)

nomes_alunos += [1, 2, 3]
print(nomes_alunos)

del nomes_alunos[-3:]
print(nomes_alunos)

num = []
num.append(int(input("Digite um número (0 sai): ")))
print(num)
