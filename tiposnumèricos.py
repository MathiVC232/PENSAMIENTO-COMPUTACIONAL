A = 5
B = 3
suma_enteros = A + B  # 8

C = 5.5
D = 3.2
suma_flotantes = C + D  # 8.7

print(suma_enteros)
print(suma_flotantes)

A = 2 + 3j
B = 1 - 2j
suma_complex = A + B  # (3 + 1j)

print(suma_complex)

x = 5  # 101 en binario
y = 3  # 011 en binario

and_result = x & y   # AND: 001 -> 1
or_result = x | y    # OR: 111 -> 7
xor_result = x ^ y   # XOR: 110 -> 6
shift_left = x << 1  # Desplazamiento a la izquierda: 1010
shift_right = x >> 1 # Desplazamiento a la derecha: 10

print(and_result, or_result, xor_result, shift_left, shift_right)