import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros

class PruebaOperacionesEnteros(unittest.TestCase):
    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        numero1 = 30
        numero2 = 2
        resultadoEsperado = 2
        operacion = OperacionesEnteros([numero1, numero2])

        resultadoActual = operacion.calcularMCD()

        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_tresNumerosPositivos_retornaMCD(self):
        numero1 = 90
        numero2 = 50
        numero3 = 3
        resultadoEsperado = 1
        operacion = OperacionesEnteros([numero1, numero2, numero3])

        resultadoActual = operacion.calcularMCD()

        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_cuatroNumerosPositivos_retornaMCD(self):
        numero1 = 12
        numero2 = 25
        numero3 = 40
        numero4 = 3
        resultadoEsperado = 2
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])

        resultadoActual = operacion.calcularMCD()

        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_cincoNumerosPositivos_retornaMCD(self):
        numero1 = 18
        numero2 = 24
        numero3 = 21
        numero4 = 30
        numero5 = 7
        resultadoEsperado = 1
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4, numero5])

        resultadoActual = operacion.calcularMCD()

        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_unNumeroPositivo_lanzaExcepcion(self):
        numero1 = 13
        operacion = OperacionesEnteros([numero1])

        self.assertTrue(True)
        with self.assertRaises(FaltanParametros):
            operacion.calcularMCD()

    def test_MCD_unaCadena_lanzaExcepcion(self):
        numero1 = "11g"
        numero2 = 12
        operacion = OperacionesEnteros([numero1, numero2])

        self.assertTrue(True)
        with self.assertRaises(ValueError):
            operacion.calcularMCD()
