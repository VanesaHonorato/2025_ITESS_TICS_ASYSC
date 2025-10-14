
print("\nMétodos básicos de listas")
numeros = [12.5, 200, 200, 7, 999.9]
print(numeros.count(200), numeros.count(12.5), numeros.count(50))
numeros.insert(1, -5)
numeros.append(300)
print(numeros)
numeros.remove(200)
numeros.reverse()
numeros.sort()
print(numeros)
numeros.pop()
print(numeros)


print("\nLista como pila")
pila = [10, 20, 30]
pila.append(40)
pila.append(50)
print(pila)
pila.pop()
pila.pop()
print(pila)


print("\nLista como cola")
from collections import deque
cola = deque(["Vanesa", "Sandra", "Brendy"])
cola.append("Cristian")
cola.append("Daniel")
cola.popleft()
cola.popleft()
print(cola)

print("\nComprensión de listas simple")
cubos = [n**3 for n in range(8)]
print(cubos)

print("\nComprensión de listas anidada")
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transpuesta = [[fila[i] for fila in matriz] for i in range(4)]
print(transpuesta)



