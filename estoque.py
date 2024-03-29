estoque = {"Audi Q3": [2, 150000], "BMW": [3, 200000],
           "Mercedes": [1, 230000]}
venda = [["Audi Q3", 1], ["BMW", 2]]

total = 0
for carro, quantidade in venda:
    preco = estoque[carro][1]
    custo = preco * quantidade
    print(f"{carro}: {quantidade} x R${preco:.2f} = R${custo:.2f}")
    estoque[carro][0] -= quantidade
    total += custo

print(f"\nCusto total = R${total:.2f}\n")

for chave, valores in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", valores[0])
    print(f"Preço:R${valores[1]:.2f}\n")
