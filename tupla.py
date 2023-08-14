marca_car = ("Jeep", "Fiat", "Ford", "GM")
print(marca_car)

# não é possível alterar uma tupla
#marca_car[0] = "Tesla"

car1, car2, car3, car4 = marca_car
print(car1)
print(car2)
print(car3)
print(car4)
print(type(marca_car))
print(len(marca_car))

pi = (3.141592,)
print(type(pi))
print(len(pi))

produto = ()
print(type(produto))
print(len(produto))

componentes_lista = ["diodo", "resistor", "capacitor"]
componentes_tupla1 = tuple(componentes_lista)
print(componentes_tupla1)

componentes_tupla2 = ("bateria",)
componentes_tupla3 = componentes_tupla1 + componentes_tupla2
print(componentes_tupla3)

