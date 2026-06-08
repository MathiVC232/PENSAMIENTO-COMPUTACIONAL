# Lista por comprensión
lista = [x for x in range(5)]

# Set por comprensión
conjunto = {x for x in range(5)}

# Diccionario por comprensión
diccionario = {x: x**2 for x in range(5)}

# Expresión generadora
generador = (x for x in range(5))

print("Lista:", lista)
print("Conjunto:", conjunto)
print("Diccionario:", diccionario)

print("\nGenerador:")
for numero in generador:
    print(numero)