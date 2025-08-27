# este espacio lo creamos con el objetivo de realizar ejercicios practicos con funciones


"""

# Ejercicio 1: Calcular el área de un triángulo:
#  Crea una función llamada calcular_area_triangulo 
# 
# que reciba como parámetros la base y la altura de un triángulo, 
# y que devuelva el área.
# Luego, pide al usuario los valores y muestra el resultado.



# definimos la funcion para calcular el triangulo
def calcular_area_triangulo(base,altura):
    return base * altura


# solicitamos los valores por consola al usuario
dato1 = float(input(" Ingrese la base del triangulo "))
dato2 = float(input(" Ingrese la altura del triangulo "))

# calcular la funcion con los datos del usuario
area = calcular_area_triangulo(dato1,dato2)

# mostrar el resultado
print(f"El area del trianggulo es: {area}")


---------------------------------------------------------------------------

Ejercicio 2: Verificar si un número es par o impar:
Crea una función llamada es_par que reciba un número y devuelva si es "Par" o "Impar".
Luego, pide un número al usuario y muestra el resultado.


"""


# definir la funcion
def es_par(numero):
    if numero % 2 == 0:
        return "es par"
    else:
        return "es impar"
    

# solicitamos el valor al usuario
usuario = int(input(" Ingresa un numero "))

# llamamos la funcion
resultado = es_par(usuario)

# mostramos el resultado
print(f"el numero ingresado es: {usuario}")
print(f"el numero : {resultado}")

