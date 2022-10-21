"""Escribir un programa para el manejo de listas el cuál cumplirá los siguientes
requerimientos"""

import random
lista = []
for x in range(1,11):
    lista.append(random.randint(1,11))
print("La lista con valores aleatorios es: {}".format(lista))

lista2 = list(set(lista))
print("La lista con valores no repetidos es: {}".format(lista2))

print("La lista ordenada de menor a mayor es: {}".format(lista2))
lista2.reverse()
print("La lista ordenada de mayor a menor es: {}".format(lista2))

mayor = max(lista2)
print("El número mayor de la lista del ítem 2 es: {}".format(mayor))