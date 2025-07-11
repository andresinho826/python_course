# python_course

## 📌 Descripción del Repositorio

Este repositorio tiene como objetivo **aprender y consolidar conocimientos fundamentales sobre el lenguaje de programación Python**, desde lo más básico hasta conceptos más avanzados. Aquí encontrarás explicaciones claras, ejemplos prácticos, estructuras de datos, buenas prácticas y ejercicios que te ayudarán a desarrollar tus habilidades paso a paso.

Ya sea que estés dando tus primeros pasos o quieras reforzar lo que ya sabes, este repositorio está pensado para ser tu guía de estudio y referencia personal en el mundo de Python.




---------------------------------------------------------------------------------------------------------------------------------------------------

# 🐍 Introducción a Python

## ¿Qué es Python y para qué sirve?

Python es un lenguaje de programación interpretado, de alto nivel y con una sintaxis sencilla y clara. Es uno de los lenguajes más populares en la actualidad debido a su versatilidad y facilidad de aprendizaje.

**¿Para qué sirve?**

Python se puede usar para:

* Desarrollo web (con frameworks como Django, Flask)
* Análisis de datos y ciencia de datos
* Automatización de tareas
* Desarrollo de videojuegos
* Inteligencia artificial y aprendizaje automático
* Aplicaciones de escritorio
* Scripts y tareas de administración de sistemas

---

## 🔧 Instalación de Python

1. Ve a [https://www.python.org](https://www.python.org) y descarga la versión recomendada para tu sistema operativo.
2. Durante la instalación, **asegúrate de marcar la opción "Add Python to PATH"**.
3. Verifica que la instalación fue exitosa:

   ```bash
   python --version
   ```

---

## 🖥️ Tu primer programa en Python

Crea un archivo llamado `hola_mundo.py` con el siguiente contenido:

```python
print("¡Hola, mundo!")
```

Luego ejecútalo desde la terminal:

```bash
python hola_mundo.py
```

---

## 🔤 Tipos de datos y variables en Python

### 1. Números (`int`, `float`, `complex`)

Python maneja diferentes tipos numéricos:

```python
entero = 5           # int
decimal = 6.5        # float
complejo = 5j        # complex
```

### 2. Cadenas de texto (`str`)

Son secuencias de caracteres encerradas entre comillas simples o dobles:

```python
nombre = "Kathe"
apellido = "Camilo"
mensaje = "Cualquier cosa"
```

### 3. Booleanos (`bool`)

Representan valores de verdadero o falso:

```python
activo = True
es_mayor = False
```

---

## 📦 Estructuras de datos en Python

Python tiene estructuras muy útiles para agrupar y organizar datos:

### 1. Lista (`list`)

Una colección ordenada y mutable:

```python
mi_lista = ["Andres", "Aaron"]
```

### 2. Tupla (`tuple`)

Colección ordenada pero **inmutable** (no se puede modificar):

```python
mi_tupla = ("Andres", "Aaron")
```

### 3. Diccionario (`dict`)

Colección de pares clave-valor:

```python
mi_diccionario = {
    "Andres": "Aaron",
    "Prueba": "Cualquier cosa"
}
```

### 4. Conjunto (`set`)

Colección **no ordenada** de elementos únicos:

```python
mi_set = {"Andres", "Aaron"}
```

---

## 🧠 Notas adicionales

* Python es **tipado dinámicamente**, lo que significa que no necesitas declarar el tipo de dato de una variable.
* Las estructuras como listas y diccionarios son fundamentales para manejar datos en Python y son ampliamente usadas en proyectos reales.
* Para trabajar con arreglos más potentes (como en matemáticas o ciencia de datos), puedes usar la librería `NumPy`.

---

## 📁 ¿Qué sigue?

Puedes ampliar tu conocimiento con estos temas:

* Condicionales (`if`, `else`, `elif`)
* Ciclos (`for`, `while`)
* Funciones y módulos
* Manejo de errores (`try`, `except`)
* Lectura y escritura de archivos

---------------------------------------------------------------------------------------------------------------------------------------------------



## ⚙️ Operadores y Condicionales en Python

### 🧮 Operadores Matemáticos

Los operadores matemáticos (también llamados *aritméticos*) se usan para realizar operaciones básicas como suma, resta, multiplicación, etc.

| Operador | Descripción      | Ejemplo  | Resultado |
| -------- | ---------------- | -------- | --------- |
| `+`      | Suma             | `5 + 3`  | `8`       |
| `-`      | Resta            | `5 - 3`  | `2`       |
| `*`      | Multiplicación   | `5 * 3`  | `15`      |
| `/`      | División         | `5 / 2`  | `2.5`     |
| `//`     | División entera  | `5 // 2` | `2`       |
| `%`      | Módulo (residuo) | `5 % 2`  | `1`       |
| `**`     | Potencia         | `2 ** 3` | `8`       |

---

### 🔍 Operadores Lógicos

Se utilizan para combinar condiciones. Devuelven un valor booleano (`True` o `False`).

| Operador | Significado | Ejemplo          | Resultado |
| -------- | ----------- | ---------------- | --------- |
| `and`    | Y lógico    | `True and False` | `False`   |
| `or`     | O lógico    | `True or False`  | `True`    |
| `not`    | Negación    | `not True`       | `False`   |

---

### 🔗 Operadores de Comparación

Se utilizan para comparar valores. Siempre devuelven `True` o `False`.

| Operador | Significado       | Ejemplo  | Resultado |
| -------- | ----------------- | -------- | --------- |
| `==`     | Igual a           | `5 == 5` | `True`    |
| `!=`     | Diferente de      | `5 != 3` | `True`    |
| `>`      | Mayor que         | `5 > 3`  | `True`    |
| `<`      | Menor que         | `5 < 3`  | `False`   |
| `>=`     | Mayor o igual que | `5 >= 5` | `True`    |
| `<=`     | Menor o igual que | `3 <= 5` | `True`    |

---

### 🧠 Condicionales (`if`, `elif`, `else`)

Las estructuras condicionales permiten que un programa **tome decisiones** dependiendo de ciertas condiciones. Se usan junto con los operadores anteriores para ejecutar diferentes bloques de código.

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

**Explicación:**

* `if`: Se ejecuta si la condición es verdadera.
* `elif`: Se evalúa si la primera condición no se cumple.
* `else`: Se ejecuta si ninguna condición anterior fue verdadera.



---------------------------------------------------------------------------------------------------------------------------------------------------


## 🔁 Ciclos en Python

Un **ciclo** (o bucle) en programación es como decirle a la computadora:

> “Haz esto una y otra vez… hasta que te diga que pares.”

Se utilizan cuando necesitamos **repetir instrucciones** múltiples veces, ya sea una cantidad conocida o mientras se cumpla una condición.

---

### 🔄 Tipos de ciclos en Python

#### ✅ `for` – Ciclo para

Se utiliza cuando sabemos **cuántas veces** queremos repetir algo, por ejemplo, recorrer una lista o repetir una acción un número definido de veces.

```python
for dia in range(1, 6):
    print(f"Vamos al colegio el día {dia}")
```

📌 `range()` genera una secuencia de números. En este caso, del 1 al 5.

---

#### 🔁 `while` – Ciclo mientras

Se utiliza cuando **no sabemos cuántas veces** se repetirá una acción, pero sí sabemos una condición que debe cumplirse.

```python
dia = 1
meta = 5

while dia <= meta:
    print(f"Día {dia}: Vamos al colegio")
    dia += 1
```

Este ciclo se repetirá **mientras** el valor de `dia` sea menor o igual que `meta`.

---

### 🔧 Palabras clave especiales

* **`break`**: Finaliza el ciclo inmediatamente, incluso si la condición todavía es verdadera.

  ```python
  for i in range(1, 10):
      if i == 5:
          break
      print(i)
  # Resultado: 1, 2, 3, 4
  ```

* **`continue`**: Salta la iteración actual y pasa a la siguiente.

  ```python
  for i in range(1, 6):
      if i == 3:
          continue
      print(i)
  # Resultado: 1, 2, 4, 5
  ```

---

### 🧠 Ejemplo ilustrativo

```python
# Meta: llegar al día 365
dia = 360
meta = 365

while dia <= meta:
    print(f"Hoy es el día {dia}")
    dia += 1
```

En este ejemplo, la computadora imprimirá el día actual hasta que llegue al 365, simulando una meta diaria.

---------------------------------------------------------------------------------------------------------------------------------------------------