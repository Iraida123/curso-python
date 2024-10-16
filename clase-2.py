
#creo variables
nombre_usuario = "Juan"
edad_usuario = 30

#OPERADOR DE ASIGNACION ES EL SIGNO DE =

nombre_usuario = "Pedro"       #EN ESTE CASO ESTOY DANDOLE EL VALOR DE PEDRO A LA VARIABLE 
edad_usuario = 25               #REASIGNO VALOR DE 25 A LA VARIABLE

#PYTHON ES SENSIBLE A LAS MAYUSCULAS RECOMENDABLE ESCRIBIR LOS NOMBRES DE LAS VARIABLES EN MINUSCULASY GUION BAJO_

#print( nombre de la variable ) = PERMITE IMPRIMIR POR CONSOLA LO QUE TIENE LA VARIABLE DENTRO
 
nombre_usuario = 44
edad_usuario = "Rojo"
#SI QUIERO VER LO QUE HAY DENTRO DE CADA VARIABLE

print(nombre_usuario)
print(edad_usuario)
# LAS VARIABLES EN PYTHON SON DINAMICAMENTE TIPADAS ( ES DECIR PUEDEN SER DE CUALQUIER GENERO O TIPO)

# TIPOS DE DATOS----->STRING(CADENA DE CARACTERS O TEXTOS, FECHAS, NOMBRES)
nombre_usuario = "Juan"

# INT----> (NUMEROS ENTEROS SIN DECIMALES)
edad_usuario = 25

# FLOAT----> (NUMEROS CON DECIMALES)

nota_usuario = 8.5

# BOOL----> LOGICOS (VERDADERO Y FALSO)
Verdadero = True
Falso = False

# OPERADORES ARITMETICOS ----> SUMA +

suma = 30 + 40
print(suma)
# OTRO EJEMPLO
suma=70+10
print(suma)

# OTRO EJEMPLO
numero_1 = 25
numero_2 = 50
suma = numero_1 + numero_2
print(suma)

#OTRO EJEMPLO

suma= numero_1 + 15
print(suma)

# OTRO EJEMPLO
suma = suma +numero_1
print(suma) #SUMA EL ULTIMO VALOR DE suma + EL VALOR DE  numero_1

# RESTA - (EL PRIMER NUMERO - EL SEGUNDO)

resta = 100-25
print(resta)

# MULTIPLICACION * (primero multiplicado por el segundo)
multi = 40*3
print(multi)

# DIVISION---- / ( EL PRIMERO DIVIDIDO POR EL SEGUNDO)

divi = 50/2
print(divi)


# OBSERVACION ----> EL OPERADOR DE SUMA es un Operador sobrecargado, PUEDE REALIZAR MULTIPLES FUNCIONES, PUEDE SUMAR STRING
# EL OPERADOR DE SUMA AL SUMAR TEXTO LO  QUE HACE ES CONCATENAR UN TEXTO CON EL OTRO 8 pegar uno con otro)
suma= "Juan" + "Lopez"
print(suma)

#  EL OPERADOR SUMA DISTINGUE LOS NUMEROS DEL LOS STRING SI LOS NUMEROS ESTAN DENTRO DE " LOS TOMARA COMO STRING"

suma = "90" + "77"
print(suma)

# NO se pueden sumar un numero + un string- DARIA ERROR
# ERROR
suma = 40 + "Pedro"
print(suma)













