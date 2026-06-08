# Crear un diccionario
estudiante = {
    "nombre": "Mathias",
    "edad": 18,
    "carrera": "Software"
}

# Mostrar todo el diccionario
print(estudiante)

# Acceder a un valor mediante una clave
print(estudiante["nombre"])

# Actualizar un valor
estudiante["edad"] = 19

# Agregar una nueva clave y valor
estudiante["universidad"] = "PUCE"

print(estudiante)

# Mostrar todas las claves
print(estudiante.keys())

# Mostrar todos los valores
print(estudiante.values())

# Mostrar todos los pares clave-valor
print(estudiante.items())