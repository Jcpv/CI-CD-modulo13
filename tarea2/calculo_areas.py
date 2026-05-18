# *Importar* librería
import math

# Función para validar valores positivos

def validar_valor(valor):

     # Validar que sea un valor numérico positivo - NO texto
    if not isinstance(valor, (int, float)):
        return False

    # Validar que sea un valor positivo
    if valor <= 0:
        return False

    return True

# Área de un triángulo
# Fórmula: (base * altura) / 2

def area_triangulo(base, altura):

    if not validar_valor(base) or not validar_valor(altura):
        return "Error: los valores deben ser numeros mayores a cero."

    return (base * altura) / 2


# Área de un cuadrado
# Fórmula: lado²

def area_cuadrado(lado):

    if not validar_valor(lado):
        return "Error: el lado debe ser un número mayor a cero."

    return lado ** 2


# Área de un rectángulo
# Fórmula: base * altura

def area_rectangulo(base, altura):

    if not validar_valor(base) or not validar_valor(altura):
        return "Error: los valores deben ser numeros mayores a cero."

    return base * altura


# Área de un círculo
# Fórmula: π * radio²
def area_circulo(radio):

    if not validar_valor(radio):
        return "Error: el radio debe ser un número mayor a cero."

    return math.pi * (radio ** 2)


# Área de un trapecio
# Fórmula: ((base mayor + base menor) * altura) / 2

def area_trapecio(base_mayor, base_menor, altura):

    if (not validar_valor(base_mayor) or
        not validar_valor(base_menor) or
        not validar_valor(altura)):

        return "Error: todos los valores deben ser números mayores a cero."

    return ((base_mayor + base_menor) * altura) / 2


# Área de un rombo
# Fórmula: (diagonal mayor * diagonal menor) / 2
def area_rombo(diagonal_mayor, diagonal_menor):

    if (not validar_valor(diagonal_mayor) or
        not validar_valor(diagonal_menor)):

        return "Error: las diagonales deben números mayores a cero."

    return (diagonal_mayor * diagonal_menor) / 2



# Ejemplos
#print("Área del triángulo:", area_triangulo(10, 5))
#print("Área del cuadrado:", area_cuadrado(4))
#print("Área del rectángulo:", area_rectangulo(8, 3))
#print("Área del círculo:", area_circulo(7))
#print("Área del trapecio:", area_trapecio(10, 6, 4))
#print("Área del rombo:", area_rombo(12, 8))

# Pruebas de validación

# print(area_triangulo(-5, 10))
# print(area_circulo("radio"))
# print(area_rectangulo(8, -2))