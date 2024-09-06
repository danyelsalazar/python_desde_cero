"""Test unitario Caja Ahorro"""
import caja_ahorro
import unittest

class CajaAhorroTest(unittest.TestCase): #pasamos esos parametros para poder hacer pruebas

    def test_obtener_saldo(self): #siempre poner test_ al inicio del nombre del metodo
        """Testeo para el saldo"""
        c = caja_ahorro.CajaDeAhorro("Pirulo")
        self.assertEqual(0, c.obtener_saldo())

    def test_obtener_Titular(self): 
        """Testeo para el tirular"""
        c = caja_ahorro.CajaDeAhorro("Juan")
        self.assertEqual("Juan", c.obtener_titular())
        

#recuerda agreagr esto al final del archivo unitaria para que se pueda ejecutar 
if __name__ == "__main__":
    unittest.main