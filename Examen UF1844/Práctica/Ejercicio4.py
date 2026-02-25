# Define una función llamada area_rectangulo(base, altura) que devuelva el área.
def area_rectangulo(base, altura):
    return base * altura

# Pide al usuario base y altura.
while True:
    try:
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))

        # Para validar que los valores sean positivos.
        if base > 0 and altura > 0:
            break
        else:
            print("Los valores deben ser positivos.")

    except:
        print("Introduce valores numéricos válidos.")

# Muestra el resultado llamando a la función.
resultado = area_rectangulo(base, altura)
print("El área del rectángulo es:", resultado)