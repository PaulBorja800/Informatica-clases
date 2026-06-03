"""Paúl Borja
Diploma 1 A
03-06-2026
"""
#Funciones
#Ejemplo Básico:
def obtenerMensaje(mensaje):
    return mensaje
def GenerarNombreCompleto(nombre, apellido):
    nombreCompleto = (f"{nombre} {apellido}")
    return nombreCompleto
mensaje = input("Ingresa un mensaje: ")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
print(f"{obtenerMensaje(mensaje)}, {GenerarNombreCompleto(nombre, apellido)}")