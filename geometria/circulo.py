"""Class Circulo"""

import math
import punto


class Circulo:
    """Modela un circulo a partir de su radio y su centro"""

    def __init__(self, radio, x_centro, y_centro):
        if radio <= 0:
            raise ValueError("El radio debe ser positivo")
        self.__radio = radio
        self.__centro = punto.Punto(x_centro, y_centro)

    def get_centro(self):
        """Devuelve un Punto que es el centro del circulo"""
        return self.__centro

    def get_radio(self):
        """Devuelve el radio del circulo"""
        return self.__radio

    def set_radio(self, r):
        "Establece el radio r"
        self.__radio = r

    def get_diametro(self):
        """Devuelve el diametro del circulo"""
        return 2 * self.get_radio()

    def set_diametro(self, d):
        """Establece el diametro en el valor d pasado como parametro"""
        self.set_radio(d / 2)

    def get_perimetro(self):
        """Devuelve la logitud de circunferencia
        del circulo o su perimetro"""
        return math.pi * self.get_diametro()

    def set_perimetro(self, p):
        """Establece el valor del perimetro p"""
        self.set_radio(p / (2 * math.pi))

    def get_area(self):
        """Devuelve el area del circulo"""
        return math.pi * math.pow(self.get_radio(), 2)

    def set_area(self, a):
        "Establece el valor del perimetro a"
        self.set_radio(math.sqrt(a/math.pi))
