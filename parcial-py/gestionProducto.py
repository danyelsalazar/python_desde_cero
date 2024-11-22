class Producto:
    def __init__(self,descripcion, categoria, precio, stock):
        self.__dezscripcion = descripcion
        self.__categoria = categoria
        self.__precio = precio
        self.__stock = stock
    
    def getCategoria(self):
        return self.__categoria

    def __str__(self):
        return self.__dezscripcion + ", " + str(self.__precio) + ", " +  str(self.__stock) 

class GestionProductos():

    def __init__(self):
        self.__lista = []

    def llenarLista(self, archivo):
        with open(archivo,"r") as file:
            for linea in file:
                datos = linea.split(",")
                descripcion = datos[0]
                categoria = datos[1]
                precio = float(datos[2])
                stock = int(datos[3])
                self.__lista.append(Producto(descripcion,categoria,precio,stock))
                           
    def cargarMapa(self):
        mapa = {}
        for producto in self.__lista:
            li = mapa.get(producto.getCategoria(), [])
            li.append(producto)
            mapa.update({producto.getCategoria(): li})

        return mapa
    
class main:
    gestion = GestionProductos()
    gestion.llenarLista("producto.csv")
    mapa = gestion.cargarMapa()

    for categoria,productos in mapa.items():
        print("---------\n" + categoria + "\n--------------")
        for producto in productos:
            print(str(producto))

