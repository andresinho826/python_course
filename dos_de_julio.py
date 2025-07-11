# operadores matemáticos, operadores lógicos y condicionales (if, else, elif) para que el programa pueda tomar decisiones según ciertas condiciones.
# Se usan para comparar valores y siempre devuelven True o False.




#Verificar si un número es positivo o negativo


# cuando es positivo? = 2    mayor a 0
# cuando es negativo? = -1    

""""
numero = input("ingrese un numero aleatorio")
numero = int(numero)

if numero > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo o cero")

    Clasificar notas **
    Acceso según edad
    Verificar número par o impar **
    Usar operadores lógicos
    """

# maxima 5, menor es 1
nota = input(" ingrese su nota ")
nota = float(nota)

if nota >= 5:
    print("Te fue excelente")
elif nota >= 4 and nota < 5:
    print("Te fue bien")
elif nota >= 3 and nota < 4:
    print("te fue regular")
elif nota >=2 and nota <3:
    print("Debes mejorar")
else:
    print("Perdiste el curso, debes repetir")



