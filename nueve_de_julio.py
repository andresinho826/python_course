
import random

"""
Un ciclo en programación es como decirle a la computadora:
 "Haz esto una y otra vez hasta que yo te diga que pares."

 # vamos al colegio 11

# meta = 365 

# dia ? meta == 365?

# dia == 360


# que dia es? dia == 30??

# dia = 30

# ciclos == repeticion

ciclo for = para
ciclo while = mientras
 range = rango

break: Sale del ciclo.
continue: Salta a la siguiente iteración.


array 0 

#Imprimir los números del 1 al 10:

for numero in range(0, 12, 2):
    print(2)

    range(inicio, fin, paso)
    range(fin)


    total_edad = 0

for index in range(5):
    edad = int(input(f"Ingrese la edad de la persona {index + 1}: "))
    total_edad += edad
promedio = total_edad / 5

print("El promedio de las edades es: ", promedio)
"""



#Juego: Adivina el número (con while):

# true, false

numero_secreto = random.randint(1,20)
intentos = 0

while True:
    adivinando = int(input("Adivina el numero secreto (entre 1 y 20)"))
    intentos += 1
    if adivinando == numero_secreto:
        print(f"Correcto, has adivinado el numero en {intentos} intentos")
        break
    elif adivinando < numero_secreto:
        print("Intenta con un numero mas alto")
    else:
        print("Intenta con un numero mas bajo")

