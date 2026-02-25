# Crea un programa que:
# Solicite al usuario: Nombre, Edad y Ciudad.
nombre = input("Nombre: ")
edad = input("Edad: ")
ciudad = input("Ciudad: ")

# Guarde los datos en un diccionario.
persona = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad
}

# Muestre un mensaje como: "Juan tiene 25 años y vive en Madrid."
print(f'{persona["nombre"]} tiene {persona["edad"]} años y vive en {persona["ciudad"]}.')