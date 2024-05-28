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
carros_suv = ["Renegade", "HRV", "Peugeot 2008"]
for i in carros_suv:
  print(i)
```  

> Quando começamos a executar o ***for***, temos **i** igual ao primeiro elemento da lista, no caso Renegade, ou seja, carros_suv[0]. Imprimimos **Renegade** e a execução do programa volta para o for e **i** passa a valer **HRV**, ou seja, carros_suv[1]. Na próxima repetição **i** valerá **Peugeot 2008**, ou seja carros_suv[2]. Depois de imprimir o último elemento, a repetição é concluída. 
