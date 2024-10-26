from Persona import Persona


class RegistroPersonas:
    

    def get_persona(self, archivo):

        personas = []

        with open(archivo, "r", encoding = "utf-8") as file:
            for cada_linea in file:
                #para cada linea crea un objeto persona y lo agrega a la lista personas
                datos = cada_linea.split(',') #aqui el split sera donde queremos separ cada porcion en este caso separara cuando encuentra una coma y creara un arreglo
                persona = persona = Persona(int(datos[0]), datos[1], int(datos[2]), datos[3])
                personas.append(persona)
        return personas
    
    """este metodo retorna una lista de las personas mayores"""
    def get_personas_mayores(self, lista, edad):
        personas_mayores = []
        for p in lista:
            if(p.get_edad() > edad):
                personas_mayores.append(p)
        return personas_mayores
    
    """este metodo crea un archivo donde escribe los datos de las personas mayores"""   
    def personas_mayores_archivo(self, lista, edad):
        personas_mayores = []
        for p in lista:
            if(p.get_edad() > edad):
                personas_mayores.append(p)
        #creamos un archivo .csv, con write escribe en el archivo
        with open("personas_mayores_de_" + str(edad) + ".csv", "w", encoding="utf-8") as filePeMayo:
            for cada_persona in personas_mayores:
                filePeMayo.write(cada_persona.str())
            #importante saber que with cierra automaticamnete el archivo cuando finaliza su bloque si usaramos otra forma como un Open(...) tendriamos que poner nombreArchivo.close()

    """Este metodo retorna la edad promedio de personas"""
    def edad_promedio(self, lista):

        sum = 0
        for p in lista:
            sum += p.get_edad()
        
        if len(lista) == 0:
            return 0 #si la lista esta vacia entrara aqui y mostrara el 0
        
        return sum//len(lista) #recuerda // es la division entera


    """6 . 1  Agrupar las personas por provincia, o sea, generar un archivo 
    tal que figure en una línea la provincia , y debajo todas las personas
    que viven en esa provincia."""

    def get_personas_por_provincia(self, lista):
        por_provi = {}

        for p in lista:
            provi = p.get_provincia()
            if provi in por_provi:
                por_provi[provi].append(p)
            else:
                por_provi[provi] = [p]  # Inicializa la lista con la primera persona


        return por_provi
    
    def personas_por_provincia_archivo(self, diccionario):
        with open("provincias.txt", "w", encoding="utf-8") as file:
            for provi, per in diccionario:
                file.write("\n" + provi + "\n")
                for p in per:
                    file.write(p.str())


    
rp = RegistroPersonas()
lista_de_personas = rp.get_persona("c:/Users/estudiante/Desktop/Programacion_Universidad/python_desde_cero/ManejoDeArchivos/personas.csv")
#rp.personas_mayores_archivo(lista_de_personas, 37)

# lm = rp.get_personas_mayores(lista_de_personas, 37)
# print(rp.edad_promedio(lm))

# print("Edad promedio de las personas mayores de 37: ",  rp.edad_promedio(lm))


provincias = rp.get_personas_por_provincia(lista_de_personas)

for provi, perso in provincias.items():
    print(provi)
    for p in perso:
        print(p.str())
    print("\n")