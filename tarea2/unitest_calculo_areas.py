import unittest
import math 

from calculo_areas import area_triangulo, area_cuadrado, area_rectangulo, area_circulo, area_trapecio, area_rombo


class pruebaAreas(unittest.TestCase):
    
    # ---------- TRIÁNGULO ----------
    def test_area_triangulo_valido(self):
        resultado = area_triangulo(10, 5)
        self.assertEqual(resultado, 25)

    def test_area_triangulo_dato_negativo(self):
        resultado = area_triangulo(-10, 20)
        self.assertEqual(
            resultado,
            "Error: los valores deben ser numeros mayores a cero."
        )
    def test_area_triangulo_dato_incorrecto(self):
        resultado = area_triangulo("base", "altura")
        self.assertEqual(
            resultado,
            "Error: los valores deben ser numeros mayores a cero."
        )
        
    # ---------- CUADRADO ----------
    def test_area_cuadrado_valido(self):
        resultado = area_cuadrado(4)
        self.assertEqual(resultado, 16)

    def test_area_cuadrado_negativo(self):
        resultado = area_cuadrado(-3)
        self.assertEqual(
            resultado,
            "Error: el lado debe ser un número mayor a cero."
        )
    def test_area_cuadrado_incorrecto(self):
        resultado = area_cuadrado("lado")
        self.assertEqual(
            resultado,
            "Error: el lado debe ser un número mayor a cero."
        )
    
    # ---------- RECTÁNGULO ----------
    def test_area_rectangulo_valido(self):
        resultado = area_rectangulo(8, 5)
        self.assertEqual(resultado, 40)

    def test_area_rectangulo_negativo(self):
        resultado = area_rectangulo(8, -5)
        self.assertEqual(
            resultado,
            "Error: los valores deben ser numeros mayores a cero."
        )
    def test_area_rectangulo_incorrecto(self):
        resultado = area_rectangulo("base", "altura")
        self.assertEqual(
            resultado,
            "Error: los valores deben ser numeros mayores a cero."
        )

    # ----------  CÍRCULO ----------
    def test_area_circulo_valido(self):
        resultado = area_circulo(2)
        real = math.pi * (2 ** 2)
        self.assertEqual(resultado, real)

    def test_area_circulo_negativo(self):
        resultado = area_circulo(-6)
        self.assertEqual(
            resultado,
            "Error: el radio debe ser un número mayor a cero.")
        
    def test_area_circulo_incorrecto(self):
        self.assertEqual(
            area_circulo(0),
            "Error: el radio debe ser un número mayor a cero."
        )

    # ---------- TRAPECIO ----------
    def test_area_trapecio_valido(self):
        resultado = area_trapecio(10, 6, 4)
        self.assertEqual(resultado, 32)

    def test_area_trapecio_negativo(self):
        resultado =area_trapecio(10, -6, 4)
        self.assertEqual(
            resultado,
            "Error: todos los valores deben ser números mayores a cero."
        )
    def test_area_trapecio_incorrecto(self):
        resultado = area_trapecio("base mayor", "base menor", "altura")
        self.assertEqual(
            resultado,
            "Error: todos los valores deben ser números mayores a cero."
        )

    # ---------- ROMBO ----------
    def test_area_rombo_valido(self):
        resultado = area_rombo(10, 8)
        self.assertEqual(resultado, 40)

    def test_area_rombo_negativo(self):
        resultado = area_rombo(-10, 8)
        self.assertEqual(
            resultado,
            "Error: las diagonales deben números mayores a cero."
        )
        
    def test_area_rombo_incorrecto(self):
        resultado = area_rombo("diagonal 1", 8)
        self.assertEqual(
            area_rombo("diagonal 1", 8),
            "Error: las diagonales deben números mayores a cero."
        )

if __name__ == '__main__':
    unittest.main()