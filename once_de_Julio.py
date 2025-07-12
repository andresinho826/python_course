"""
0
1
2
3
4
5
6


ciclos for y while

Imprimir los números pares del 2 al 50.
for numero in range(2,51,2):
    print(numero)

en el rango empezamos desde le numero indicado = 2
y el final seria el 51
range(inicio, fin, paso)

-> Simular un semáforo que cambie de color automáticamente entre "verde", "amarillo" y "rojo" con una pausa entre ellos.
"""

import time
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

colores = ["verde","amarillo","rojo"]

duracion = [5,2,4]


while True:
    for i in range(len(colores)):
        limpiar_pantalla()
        print(" semaforo:")
        print(f" {colores[i]}")
        time.sleep(duracion[i])
    break
    

