"""Paúl Borja
Diploma 1 A
03-06-2026
"""
#Funciones
#Ejemplo Básico:
print("------- Ejemplo -------")
def obtenerMensaje(mensaje):
    return mensaje
def GenerarNombreCompleto(nombre, apellido):
    nombreCompleto = (f"{nombre} {apellido}")
    return nombreCompleto
mensaje = input("Ingresa un mensaje: ")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
print(f"{obtenerMensaje(mensaje)}, {GenerarNombreCompleto(nombre, apellido)}")
#Ejercico 2:
#Genere una calculadora con las 4 operaciones básicas ( suma, resta, multiplicación, división) mediante un procedimiento con parámetros para cada operación, el usuario debe ingresar los 2 números por teclado y seleccionar la operación
print("------- Ejercicio 1 -------")
def sumaNumeros(suma):
    return suma
def restaNumeros(resta):
    return resta
def multiplicacionNumeros(multiplicacion):
    return multiplicacion
def divisionNumeros(division):
    return division
print("Calculadora simple, ingresa 2 números y luego elige la operaciíon que quieras realizar")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
while True:
    operacion = int(input("¿Qué operación quieres hacer?(1.Suma, 2.Resta, 3.Multiplicación, 4.División, 5.Salir): "))
    division = num1 / num2
    multiplicacion = num1 * num2
    resta = num1 - num2
    suma = num1 + num2
    if operacion == 1:
        print(f"La respuesta de la suma es: {sumaNumeros(suma)}")
    elif operacion == 2:
        print(f"La respuesta de la resta es: {restaNumeros(resta)}")
    elif operacion == 3:
        print(f"La respuesta de la multiplicación es: {multiplicacionNumeros(multiplicacion)}")
    elif operacion == 4:
        print(f"La respuesta de la división es: {divisionNumeros(division)}")
    elif operacion == 5:
        print("Gracias por utilizar")
        break
    else:
        print("Opción inválida")
