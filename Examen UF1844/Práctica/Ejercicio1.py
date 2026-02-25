# Escribe un programa que:
# Pida al usuario su nombre completo
nombre = input("Introduce tu nombre completo: ")

# Muestra:
# El nombre en mayúsculas
print("Mayúsculas:", nombre.upper())

# El nombre en minúsculas
print("Minúsculas:", nombre.lower())

# El número total de caracteres (incluyendo espacios)
print("Número de caracteres:", len(nombre))

# El nombre sin espacios al inicio ni al final
print("Sin espacios al inicio y final:", nombre.strip())