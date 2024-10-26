a = [23, 45, 7, -1, 89, 9]

"""for each"""
for cada_uno in a:
    print(cada_uno)

"""for normal"""

print("------------------------")
for i in range(len(a)):
    print(a[i])

a.append("Hola") #asi agregamos un elemento a la lista

print("------------------------")
for i in range(len(a)):
    print(a[i])