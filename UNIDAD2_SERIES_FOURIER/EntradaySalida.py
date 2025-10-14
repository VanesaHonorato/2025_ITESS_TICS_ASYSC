
"""
FECHA:14/10/25
NOMBRE: Vanesa Gonzalez Honorato
MATERIA: Analisis de señales y comunicacion
ITESS TICS 501
vanegoho@gmail.com
"""
print("Uso de repr() y str()")
s = 'Hola mundo'
print(str(s))   # Muestra el texto normal
print(repr(s))  # Muestra el texto con comillas y caracteres especiales


print("Rellenar cadenas con ceros zfill()")
print('12'.zfill(5))
print('-3.14'.zfill(7))

print("Formateo con variables nombradas")
print('Esta {comida} es {adjetivo}.'.format(comida='pizza', adjetivo='deliciosa'))


print("Lectura y escritura de archivos")
f = open('ejemplo.txt', 'w')
f.write('Hola, este es un texto de prueba\n')
f.close()

f = open('ejemplo.txt', 'r')
print(f.read())
f.close()


print("Guardar datos con json")
import json
datos = {'nombre': 'Vanesa', 'edad': 20, 'activo': True}
with open('datos.json', 'w') as f:
    json.dump(datos, f)

with open('datos.json', 'r') as f:
    datos_leidos = json.load(f)
print(datos_leidos)
