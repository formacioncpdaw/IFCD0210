# Crear una lista con 5 números introducidos por el usuario.
numeros = []

for i in range(5):
    num = int(input(f"Introduce el número {i+1}: "))
    numeros.append(num)

# Muestra:
# La lista completa.
print("Lista completa:", numeros)

# El número mayor.
print("Número mayor:", max(numeros))

# El número menor.
print("Número menor:", min(numeros))

# La suma total de los números.
print("Suma total:", sum(numeros))