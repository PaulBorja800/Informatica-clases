"""Paúl Borja
Diploma 1 A
20-04-2026
Evaluación"""

# ========== Parte A ==========
#Respuesta 1:
nombre = "Lucía" 
edad = 16 
promedio = 9.75 
cursos = ["Python", "HTML", "CSS"] 
print(type(nombre)) 
print(type(edad)) 
print(type(promedio)) 
print(type(cursos)) 
print(len(nombre)) 
"""Responde: 
a) Indica el tipo de dato de cada variable:
nombre = str
edad = int
promedio = float
cursos = list
b) Escribe qué mostraría el programa en pantalla:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'list'>
5
c) Explica qué hace len(nombre):
Escribe el número de caracteres que tiene el valor de la variable
"""
#Resuesta 2:
"""Responde con tus palabras: 
a) ¿Qué diferencia hay entre print() e input()?:
Print escribe en pantalla el valor de una variable, pero input pide que el usuario escriba el valor de la variable
b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?:
Porque si el dato ingresado no es del mismo tipo que los otros datos, no se pueden hacer operaciones de calculo
c) Explica la diferencia entre /, // y %:
/ es una division normal, // es una division que mostrara solo el resultado entero, y % mostrara solo el residuo de la divison
d) Escribe una instrucción que permita comprobar la versión de Python que se está usando:
print(python --version)
e) Escribe una instrucción que permita consultar las palabras reservadas de Python:
print(help"keywords")
"""
#...

# ========== PARTE B ==========
"""ancho = input("Ingrese el ancho del terreno: ") 
largo = input("Ingrese el largo del terreno: ") 
precio = input("Ingrese el precio por metro cuadrado: ") 
area = ancho * largo 
costo = area * precio 
print("Área total: " + area) 
print("Costo estimado: " + costo) 
"""
# Código corregido 
ancho = int(input("Ingrese el ancho del terreno:", ))
largo = int(input("Ingrese el largo del terreno: ", ))
precio = int(input("Ingrese el precio por metro cuadrado: ", ))
area = ancho * largo 
costo = area * precio 
print("Área total: ", area) 
print("Costo estimado: ", costo) 

"""Luego responde: 
a) ¿Cuáles eran los errores principales?
Los principales errores eran, en las variables no se establecia que tipo de dato era, y no se daba el espacio para responder.
Mientras en os print, no se debia poner "+", sino solo una coma, porque son 2 tipos de datos diferentes
b) ¿Por qué tu corrección sí permite obtener resultados válidos?
porque al estar definiendo que datos son (int), sí se pueden hacer la operaciones matemáticas, y las comas en el print hacen que se puedan escribir las variables, y no sumarlas
"""
# ... 

# ========== PARTE C ========== 
# Programa integrador 
# ... 
