#Aula sobre dicionário

carros ={"Jeep Renegade":['R$90.000,00','2018'],
         "Jeep Compass": 'R$150.000,00',
         "Troller": 'R$200.000,00'}
print(carros)
print(carros["Jeep Renegade"])

carros["Jeep Compass"] = 'R$180.000,00'
print(carros)

carros["Jeep Renegade"][1] = "2016"
print(carros)

del carros["Troller"]
print(carros)

carros["Audi"] = ['R$250.000,00', "2023"]
print(carros)

print("Audi" in carros)
print("BMW" in carros)
