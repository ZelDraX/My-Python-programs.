Numeros = [7,6,5,4,3,2,1]
print (f"Lista de números: {Numeros}")
print (f"Posición del número 1: {Numeros.index(1)}")
print (f"Posición del número 3: {Numeros.index(3)}")

Numeros.sort()
print (f"Lista de números de menor a mayor: {Numeros}")
Numeros.sort(reverse = True)
print (f"Lista de números de mayor a menor: {Numeros}")

del Numeros [:]
print (f"Lista de numeros eliminada por completo: {Numeros}")

