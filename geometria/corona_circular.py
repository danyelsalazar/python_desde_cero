"""Class Corona Circular"""

import circulo
from python_desde_cero.geometria import punto


class CooronaCircular:
    """Modela una Corona Circular

    pre: ambos radios son mayores que cero y r_g es mayor que r"""

    def __init__(self, r, r_g, x_c, y_c):

        # hacer la verificacion de que radio grande no sea menor que radio chico
        if r_g <= r:
            raise ValueError("El radio grande debe ser mayor que el chico")

        self.__centro = punto.Punto(x_c, y_c)
        self.__circulo_grande = circulo.Circulo(r_g, x_c, y_c)
        self.__circulo_chico = circulo.Circulo(r, x_c, y_c)

    def area(self):
        return self.__circulo_grande.get_area() - self.__circulo_chico.get_area()

    def perimetro(self):
        """pos: devuelve el perimetro de la corona circular"""
        return self.__circulo_chico.get_perimetro() + self.__circulo_grande.get_perimetro()

    def desplazar(self, en_x, en_y):
        self.__centro.desplazar_en_ambas_direcciones(en_x, en_y)
