"""
FECHA:13/10/25
NOMBRE: Vanesa Gonzalez Honorato
MATERIA: Analisis de señales y comunicacion
ITESS TICS 501
vanegoho@gmail.com
"""
print('Crear cadenas con comillas simples y dobles')
print('huevos y pan')
print('doesn\'t')
print("doesn't")
print('"Sí," le dijo.')
print("\"Sí,\" le dijo.")
print('"Isn\'t," she said.')


print('\nMostrar cadenas con print()')
print('"Isn\'t," she said.')


print("\nSaltos de línea")
s = 'Primera línea.\nSegunda línea.'
print(s)


print("\nCadenas crudas")
print('C:\algun\nombre')
print(r'C:\algun\nombre')


print("\nCadenas multilínea (triple comillas)")
print("""\
Uso: algo [OPTIONS]
    -h                        Muestra el mensaje de uso
    -H nombrehost             Nombre del host al cual conectarse
""")


print("\nConcatenar y repetir cadenas")
print(5 * 'va' + 'ne')
print('Py' 'thon')
prefix = 'que dificil es'
print(prefix + 'python')

texto = ('\nPoné muchas cadenas dentro de paréntesis '
         'para que ellas sean unidas juntas')
print(texto)


print("\nÍndices de una cadena")
palabra = 'Vanesa'
print(palabra[0])   # V
print(palabra[5])   # a
print(palabra[-1])  # a
print(palabra[-2])  # s
print(palabra[-6])  # V


print("\nRebanadas (subcadenas)")
print(palabra[0:2])          # Va
print(palabra[2:5])          # nes
print(palabra[:2] + palabra[2:])  # Vanesa
print(palabra[:4] + palabra[4:])  # Vanesa
print(palabra[:2])           # Va
print(palabra[4:])           # sa
print(palabra[-2:])          # sa



print("\nRebanadas fuera de rango (no dan error)")
print(palabra[4:42])  
print(palabra[42:])   # ''


print("\nCrear nuevas cadenas ")
print(':)' + palabra[1:])  
print(palabra[:2] + '<3') 


print("\nLongitud de una cadena")
s = 'VanesaGonzalezHonorato'
print(len(s))
