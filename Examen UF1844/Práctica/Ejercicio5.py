# Desarrollar un programa que permita gestionar un inventario con los siguientes requisitos:
# El inventario debe almacenarse en un diccionario con la siguiente estructura:
inventario = {
    "manzanas": 10,
    "peras": 5,
    "naranjas": 8
}

# El programa debe mostrar el siguiente menú repetidamente hasta que el usuario decida salir:
while True:

    print("\n1. Mostrar inventario")
    print("2. Añadir producto")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    # 1. Mostrar inventario
    if opcion == "1":
        print("\nInventario:")
        for producto, cantidad in inventario.items():
            print(producto, ":", cantidad)

    # 2. Añadir producto
    elif opcion == "2":
        producto = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        inventario[producto] = cantidad
        print("Producto añadido.")

    # 3. Actualizar cantidad
    elif opcion == "3":
        producto = input("Producto a actualizar: ")
        if producto in inventario:
            cantidad = int(input("Nueva cantidad: "))
            inventario[producto] = cantidad
            print("Cantidad actualizada.")
        else:
            print("El producto no existe.")

    # 4. Eliminar producto
    elif opcion == "4":
        producto = input("Producto a eliminar: ")
        if producto in inventario:
            del inventario[producto]
            print("Producto eliminado.")
        else:
            print("El producto no existe.")

    # 5. Salir
    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")