"""1. Implementar un método getPersonas  de la class 
RegistroPersonas que reciba el nombre de un archivo y
 devuelva una lista de Prsonas con personas que fueron 
 leídas del archivo de texto personas.csv con  formato "dni,apellido,edad,provincia".
"""
class Persona:

    def __init__(self, dni, apellido, edad, provincia):
        self.__dni = dni
        self.__apellido = apellido
        self.__edad = edad
        self.__provincia = provincia

    def str(self): 
        return(str(self.__dni) + "," + self.__apellido + "," + str(self.__edad) + "," +  self.__provincia  )
    
    def get_apellido(self):
        return self.__apellido
    
    def get_dni(self):
        return str(self.__dni)
    def get_edad(self):
        return self.__edad
    def get_provincia(self):
        return self.__provincia