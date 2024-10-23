#compras = [1,2,3,4,5]
#print("la cantidad de elemntos de la lista es: ")
#print(compras[0])
#
##agrego un elemnto a la lista ya creada
#print("la cantidad de elemntos de la lista es: ")
#print(compras.count)
#
#print("Imprmimimos la tupla")
#tupla = ("manzanas", "pan", "leche")
#print(tupla)
#tupla[1]="nada"
#print(tupla)

productos = ["manzanas", "pan", "leche"]
print(productos)
print("voy a remover el elemento leche")
#productos.remove("leche")
#productos.remove(input("ingrse el elemento que desea remover:  " ))

print(productos)

print("la cantidad de elementos de la lista es: ")
print(len(productos))

contador=0

print(input("ingrese un atecla").upper())

while contador< len(productos):
    print(productos[contador])
    contador=contador +1


