# ITERABLES E ITERADORES EN PYTHON

# Un iterable (lista)
numeros = [10, 20, 30, 40]

print("=== ITERABLE ===")
print(numeros)

# Crear un iterador a partir del iterable
iterador = iter(numeros)

print("\n=== ITERADOR CON NEXT() ===")
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

# Recorrer un iterable con FOR
print("\n=== FOR SOBRE ITERABLE ===")
for numero in numeros:
    print(numero)

# Enumerate (índice y valor)
print("\n=== ENUMERATE ===")
for indice, numero in enumerate(numeros):
    print("Índice:", indice, "Valor:", numero)

# Zip (unir iterables)
print("\n=== ZIP ===")
nombres = ["Ana", "Luis", "Pedro", "Sofía"]

for nombre, numero in zip(nombres, numeros):
    print(nombre, "-", numero)