print("\nRecorrer una lista de frutas")
a, b = 1, 1  
frutas = ['manzana', 'uva', 'mango', 'sandía']
for f in frutas:
    print(f, len(f))


print("\nmodificar la lista mientras se recorre (haciendo una copia)")
palabras = ['gato', 'ventana', 'mariposa']
for p in palabras[:]:
    if len(p) > 6:
        palabras.insert(0, p)
print(palabras)


