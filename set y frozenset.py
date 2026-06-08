# Crear un set con algunos elementos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# Unión de conjuntos
union = conjunto_a | conjunto_b
print("Unión:", union)

# Intersección de conjuntos
interseccion = conjunto_a & conjunto_b
print("Intersección:", interseccion)

# Diferencia de conjuntos (a - b)
diferencia = conjunto_a - conjunto_b
print("Diferencia (a - b):", diferencia)

# Diferencia simétrica (elementos en a o b, pero no en ambos)
simetrica = conjunto_a ^ conjunto_b
print("Diferencia simétrica:", simetrica)

# Verificar si a es subconjunto de b
es_subconjunto = conjunto_a.issubset(conjunto_b)
print("a es subconjunto de b:", es_subconjunto)

# Crear un frozenset a partir de un set
frozen_conjunto = frozenset(conjunto_a)
print("Frozenset:", frozen_conjunto)

# Intento de modificar frozenset (esto genera un error)
try:
    frozen_conjunto.add(7)  # No se puede, ya que es inmutable
except AttributeError as e:
    print("Error al modificar frozenset:", e)