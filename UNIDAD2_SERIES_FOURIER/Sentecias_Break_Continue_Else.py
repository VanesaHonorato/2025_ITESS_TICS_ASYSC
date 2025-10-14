"""
FECHA:13/10/25
NOMBRE: Vanesa Gonzalez Honorato
MATERIA: Analisis de señales y comunicacion
ITESS TICS 501
vanegoho@gmail.com
"""


print("\nDetener el ciclo cuando se encuentra el número 5")
for num in range(1, 10):
    if num == 5:
        print("Se encontró el numero 5")
        break
    print("Numero", num)


print("\nSaltar los numeros pares")
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print("Numero impar ", num)


print("\nBuscar un numero en una lista")
numeros = [2, 4, 6, 8, 10]
for n in numeros:
    if n == 5:
        print("Encontrado", n)
        break
else:
    print("No se encontró el número 5")


print("\nBuscar el primer número divisible entre 3")
for n in range(1, 10):
    if n % 2 == 0:
        continue  # salta los pares
    if n % 3 == 0:
        print("El primer número divisible entre 3 es ", n)
        break
else:
    print("No se encontró ninguno")




