"""Paúl Borja
Diploma 1 A
29-05-2026
"""
#Funciones
# Ejemplo 1(sin parametros):
print("------- Ejemplo 1 -------")
def nombre_completo():
    nombre = "Paúl"
    apellido = "Borja"
    espacio = ""
    nombre_completo = nombre + espacio + apellido
    print(nombre_completo)
nombre_completo() # llama a la variable

# Ejemplo 2(con parametros):
print("------- Ejemplo 2 -------")
def saludar (nombre):
    print(f"Hola, {nombre}!")
saludar ("Paúl")
saludar ("SAntiago")
saludar("Victoria")

# Ejemplo 3(pedir parametros):
print("------- Ejemplo 3 -------")
def estudiante(nombre_estudiante, curso):
    print("=== Datos del estudiante ===")
    print(f"Nombre: {nombre_estudiante}")
    print(f"Curso: {curso}")
pedirNombre = input("Ingrese el nombre del estudiante: ")
pedirCurso = input("Ingrese el curso del estudiante: ")
estudiante(pedirNombre, pedirCurso)
