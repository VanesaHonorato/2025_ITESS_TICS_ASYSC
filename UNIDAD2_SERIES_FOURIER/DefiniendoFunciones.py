
"""
FECHA:13/10/25
NOMBRE: Vanesa Gonzalez Honorato
MATERIA: Analisis de señales y comunicacion
ITESS TICS 501
vanegoho@gmail.com
"""

print("\nEscribe la serie de Fibonacci hasta n")
def fib(n):
    """Escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(500)

print("\nSerie de Fibonacci (devuelve los números en una lista)")
def fib2(n):
    """Devuelve una lista conteniendo la serie de Fibonacci hasta n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f300 = fib2(300)
print(f300)


print("\nRenombrando funciones")
def fib(n):
    """Escribe la serie de Fibonacci hasta n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Guardamos la función en otra variable
serie = fib
# Llamada con el nuevo nombre
serie(150)

