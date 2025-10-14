
"""
FECHA:14/10/25
NOMBRE: Vanesa Gonzalez Honorato
MATERIA: Analisis de señales y comunicacion
ITESS TICS 501
vanegoho@gmail.com
"""


print("Crear conjunto y eliminar duplicados")
frutas = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana'}
print(frutas)  # Muestra los elementos sin repetir

print("Verificar pertenencia")
frutas = {'manzana', 'mango', 'pera', 'banana'}
print('mango' in frutas)  # Devuelve True si está en el conjunto
print('sandía' in frutas)   # Devuelve False si no está


print("Operaciones entre conjuntos")
a = set('abracadabra')
b = set('alacazam')

print(a - b)  # Diferencia letras en A pero no en B
print(a | b)  # Unión letras en A o en B
print(a & b)  # Intersección letras comunes
print(a ^ b)  # Diferencia simétrica letras en uno u otro, pero no en ambos

print("Comprension en conjuntos")
a = {x for x in 'Vanesa' if x not in 'ans'}
print(a)  # Crea un conjunto con letras que no están en ans







