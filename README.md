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

> Quando começamos a executar o ***for***, temos **i** igual ao primeiro elemento da lista, no caso **Renault Duster Intense**, ou seja, carros_suv[0]. Imprimimos **Renault Duster Intense** e a execução do programa volta para o for e **i** passa a valer **Citroen C4 Cactus Live**, ou seja, carros_suv[1]. Na próxima repetição **i** valerá **Peugeot 2008 Allure**, ou seja carros_suv[2]. Depois de imprimir o último elemento, a repetição é concluída. 

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
