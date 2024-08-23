"""26 Invertir un string, sin usar la biblioteca que lo haga automáticamente."""

a = "inteligencia"

def invertir(a):
    b=""
    for i in range((len(a)-1) , -1, -1): # for(int i = (a.leng -1); i >= 0; i-- ) en este caso puse -1 en el segundo parametro en el de python porque si pongo hasta 0 no incluye el 0, asi que pongo -1 asi va de la ultima posicion hasta la 0 
        b = b + a[i]
    return b

print("Palabra invertida: " + invertir(a))

"""27 Escribir una función que reciba un string y lo devuelva invertido. Por ejemplo: invertirCadena("Hola"),retorna "aloH". 
Reutilice la función implementada para decir si una palabra es o no, un palíndromo.
esPalindromo("neuquen") devuelve true."""

def es_palindromo (a):

    # llamamos a todos los metodos necesarios
    c = minusculas(a)
    c = sin_espacios(c)
    c = sin_puntuacion(c)
    c = sin_acentos(c)

    #invertimos la palabra con la funcion del ejercico anterior
    d = invertir(c)

    if c == d:
        return True
    else:
        return False

#hacemos todos los metodos necesarios:
def minusculas(a):
    b = a.lower()
    return b

def sin_espacios(a):
    b = ""
    for i in range(0, len(a), 1):
        if a[i] == " ":
            b = b + ""
        else:
            b = b + a[i]
    return b

def sin_puntuacion(a):
    b = ""
    for i in range(0, len(a), 1):
        if a[i] == "." or a[i] == ";" or a[i] == "," or a[i] == "_" or a[i] == "-" or a[i] == ":":
            b = b + ""
        else:
            b = b +  a[i]
    return b

def sin_acentos(a):
    b = ""
    for i in range(0, len(a), 1):
        if a[i] == "á":
            b = b + "a"
        elif a[i] == "é":
            b = b + "e"
        elif a[i] == "í":
            b = b + "i"
        elif a[i] == "ó":
            b = b + "o"
        elif a[i] == "ú":
            b = b + "u"
        else:
            b = b + a[i]
    return b



#probamos los metodos
print("\n-------PROBANDO LAS FUNCIONES--------------")
print(minusculas("SAAAAASASASAS"))

print(sin_espacios("sddd sdsds jjjjj"))

print(sin_puntuacion("hola juan, todo. -  _bien;"))

print(sin_acentos("función última"))

#llamamos a la funcion palindromo 
print("\n-----------EJECUTANDO LA FUNCION PALINDROMO----------------")
print(es_palindromo("Dábale arroz a la zorra,  el abad.")) #como vemos aqui devuelve true ya que es un palindromo
print(es_palindromo("Dábale arroz con leche a la zorra el abad")) #como vemos aqui devuelve false ya que no es un palindromo