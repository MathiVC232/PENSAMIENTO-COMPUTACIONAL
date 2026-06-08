# Cadena original
texto = "   ¡Hola, Mundo! Bienvenidos a Python.   "

# Limpiar (quitar espacios al inicio y final)
limpio = texto.strip()
print("Limpio:", limpio)

# Dividir la cadena en palabras
palabras = limpio.split()  # usa el espacio como separador
print("Palabras:", palabras)

# Unir las palabras con un guion
unido = "-".join(palabras)
print("Unido:", unido)

# Formateo con f-string
nombre = "Estudiante"
saludo = f"Bienvenido, {nombre}! Tu mensaje es: '{unido}'"
print(saludo)

# Convertir caracteres a números (ejemplo)
primer_caracter = limpio[0]
codigo_ascii = ord(primer_caracter)
print("Código ASCII del primer carácter:", codigo_ascii)

# Convertir código a carácter (ejemplo inverso)
caracter_invertido = chr(codigo_ascii)
print("Carácter invertido:", caracter_invertido)

# Imprimir usando la función print
print("Impresión final:", limpio.upper())