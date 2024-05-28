# Aulas de algoritmos em Python 

Aqui você encontrará códigos em Python.

> Vamos lá!
```
aulas iniciadas...
```

## Agora vamos trabalhar com repetições utilizando a instrução ***for***

A instrução ***for*** funciona de forma parecida com o ***while***, mas a cada repetição utiliza um elemento diferente da lista. O ***for*** passa em cada um dos itens que a lista possui.

> Vamos escrever um programa que utilize ***for*** para imprimir todos os elementos de uma lista.

```
carros_suv = ["Renault Duster Intense", "Citroen C4 Cactus Live", "Peugeot 2008 Allure"]
for i in carros_suv:
  print(i)
```  

> Quando começamos a executar o ***for***, temos **i** igual ao primeiro elemento da lista, no caso **Renault Duster Intense**, ou seja, **carros_suv[0]**. Imprimimos **Renault Duster Intense** e a execução do programa volta para o for e **i** passa a valer **Citroen C4 Cactus Live**, ou seja, **carros_suv[1]**. Na próxima repetição **i** valerá **Peugeot 2008 Allure**, ou seja **carros_suv[2]**. Depois de imprimir o último elemento, a repetição é concluída. 

Normalmente utilizamos ***for*** quando quisermos processar elementos de uma lista, um a um. 
A instrução ***break*** também interrompe o ***for***. 

> Vejamos a pesquisa, utilizando o ***for***.

```
carros_suv = ["Renault Duster Intense", "Citroen C4 Cactus Live", "Peugeot 2008 Allure", "Chery Tiggo 5X T", "Nissan Kicks Sense"]
carro = input("Digite um carro SUV a pesquisar na lista: ")
for i in carros_suv:
  if i == carro:
    print("Elemento encontrado!")
    break
else: 
  print("Elemento não encontrado.")
```

Observação: a instrução ***while*** também possui uma cláusula opcional ***else*** que funciona da mesma forma que o ***else*** do ***for***.

Podemos utilizar a função ***range*** para gerar listas simples. A função ***range*** não retorna uma lista propriamente dita, mas um gerador.  

> Vejamos um programa que imprime de 0 a 9 na tela:

```
for i in range(10):
  print(i)
```

> A função ***range*** gerou números de 0 a 9 porque passamos 10 como parâmetro. 

Com a mesma função ***range***, podemos indicar qual é o primeiro número a gerar. 

> Vejamos:

```
for i in range(5, 8):
  print(i)
```

> Usando 5 como início e 8 como fim (não incluso na faixa de valores), vamos imprimi os números 5, 6 e 7.

Podemos acrescentar um terceiro parâmetro à função ***range***, podemos saltar entre os valores gerados. 

> Vejamos um exemplo em que geramos os números pares de 0 e 10:

```
for i in range(0, 11, 2):
  print(t)
```

Podemos percorrer uma lista de forma a verificar o menor e o maior valor. 

> Vejamos:

```
notas = [10, 5, 7, 8]
maximo = notas[0]
for i in notas:
  if i > maximo:
    maximo = i
print(maximo)
```

> Utilizamos um truque, inicializando a variável **maximo** com o valor do primeiro elemento da lista. Precisamos de um valor para **maximo** antes de utilizá-lo no comparação com ***if***.
