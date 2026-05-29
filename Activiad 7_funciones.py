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