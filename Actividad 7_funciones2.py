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

#Tarea:
def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3
def nota_mayor(n1, n2, n3):
    return max(n1, n2, n3)
def nota_menor(n1, n2, n3):
    return min(n1, n2, n3)
def estado_estudiante(n1, n2, n3):
    promedio = calcular_promedio(n1, n2, n3)
    if promedio >= 7:
        return "Aprueba"
    else:
        return "Reprueba"
nota1 = float(input("Ingrese la primera calificación: "))
nota2 = float(input("Ingrese la segunda calificación: "))
nota3 = float(input("Ingrese la tercera calificación: "))
print("------- MENÚ DE CALIFICACIONES -------")
print("1. Calcular el promedio")
print("2. Mostrar la nota mayor")
print("3. Mostrar la nota menor")
print("4. Determinar si el estudiante aprueba o reprueba")
opcion = int(input("Seleccione una opción: "))
if opcion == 1:
    promedio = calcular_promedio(nota1, nota2, nota3)
    print(f"El promedio del estudiante es: {promedio:.2f}")
elif opcion == 2:
    mayor = nota_mayor(nota1, nota2, nota3)
    print(f"La nota más alta es: {mayor}")
elif opcion == 3:
    menor = nota_menor(nota1, nota2, nota3)
    print(f"La nota más baja es: {menor}")
elif opcion == 4:
    estado = estado_estudiante(nota1, nota2, nota3)
    print(f"El estudiante: {estado}")
else:
    print(f"La opción {opcion} no es válida.")