"""Modelamos una caja de ahorro"""

class CajaDeAhorro:

    #constructor , para crear los atributos privados pones self.__atributo
    #con el __init__() signifia que ese sera el constructor
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0
    
    def obtener_titular(self):
        return self.__titular

    def obtener_saldo(self):
        return self.__saldo
    
    def depositar(self, monto):
        if monto <= 0 :
            raise ValueError("El monto debe ser positivo")
        self.__saldo += monto
    
    def extraer(self, monto):
        if monto <= 0 :
            raise ValueError("El monto debe ser positivo")
        if self.hay_saldo_suficiente(monto):
            self.__saldo -= monto
    
    def transferir(self, destino, monto):
        if self.hay_saldo_suficiente(monto):
            self.extraer(monto)
            destino.depositar(monto)

    
    def hay_saldo_suficiente(self, monto) -> bool: #con el -> bool es como para guiarmne y recordar que devuelve un boleano
        return self.__saldo >= monto
    
