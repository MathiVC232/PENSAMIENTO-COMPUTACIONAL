# Definir un literal de bytes
datos = b'Hola Mundo'  # b antes de las comillas indica bytes

print("Literal de bytes:", datos)

# Acceder a un byte específico
primer_byte = datos[0]
print("Primer byte:", primer_byte)

# Crear un bytearray (mutable)
datos_mutables = bytearray(datos)
print("Bytearray original:", datos_mutables)

# Modificar un byte en el bytearray
datos_mutables[0] = ord('h')  # Cambia el primer byte a 'h'
print("Bytearray modificado:", datos_mutables)

# Concatenar bytes (crear bytes desde una cadena con codificación UTF-8)
mas_datos = '¿Cómo están?'.encode('utf-8')
datos_completos = datos + mas_datos
print("Bytes concatenados:", datos_completos)

# Convertir bytes a una cadena
cadena = datos_completos.decode('utf-8')
print("Cadena decodificada:", cadena)