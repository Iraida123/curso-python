# EJERCICIOS

"""  Vamos a escribir un programa que calcule el costo total de una salida a cenar para un grupo
de personas. En el mismo se pide la cantidad de personas, el precio promedio del plato y
una propina fija del 10%. """

# pregunto  cantidad  de personas 
#creo la variable personas

personas= int( input("cuantas personas son?:"))
#creo variable costo plato

costo_plato= float(input("cuanto es el costo del plato: "))
#calculo total sin propina
total_cena= personas*costo_plato
propina= total_cena*0.10
total_a_pagar= total_cena + propina
# mostrar los resultados
print("mostrar total cena sin propina:", total_cena)
print("mostrar propina:",propina)
print("mostrar total a pagar con propina:", total_a_pagar)

