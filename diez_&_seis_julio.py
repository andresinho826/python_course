"""
utilizar listas y diccionarios para agrupar datos, acceder a ellos fácilmente y aplicarlos en casos reales.

Una lista es una colección ordenada y modificable que permite almacenar múltiples valores.
 Se define usando corchetes [].

 ejemplos:

 my_lista = ["manzana", "pera", "Mango", "sandia", "fresa", "cualqier cosa"]
print(my_lista)


my_lista.append("ultimo valor")
print(my_lista)

#my_lista.clear
#print(my_lista)

my_lista.remove("pera")
print(my_lista)

ejercicio practico listas

#Para recorrer cada ítem en una lista usamos un bucle for:
my_lista = ["manzana", "pera", "Mango", "sandia", "fresa", "cualqier cosa"]
print(my_lista)

for my_l in my_lista:
    print(my_l)


Un diccionario almacena pares clave: valor.
 Se define usando llaves {}.

 persona ={
    "nombre":"tatiana",
    "edad":"15",
    "ciudad":"Medellin"
}
#print(persona)
print(persona["ciudad"])
print(persona["nombre"])

persona["ciudad"] = "Pereira"
print(persona)

"""


# usar un bucle for con el diccionario

persona ={
    "nombre":"tatiana",
    "edad":"15",
    "ciudad":"Medellin"
}
print(persona)

for clave, valor in persona.items():
    print(clave + ":" + valor)





