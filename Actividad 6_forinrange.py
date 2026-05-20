"""Paúl Borja
Diploma 1A
20-05-2026"""

#For in range
# Tabla de multiplicar
print("------- Ejercicio 1 -------")
numero = int(input("Ingresa un número: " ))
num = int(input("¿Hasta qué número quieres ver?: " ))
for i in range (2, num+1, 2):
    print(f"{numero}{"x"}{i}{"="}{i*numero}")

#Ejercicio 2
print("------- Ejercicio 2 -------")
notas = [5, 8, 9, 7, 10]
suma = 0
for i in range (1, 4):
    suma = suma + notas[i]
promedio = suma/3
print(promedio)

#Ejercicio 3
print("------- Ejercicio 3 -------")
estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofía", "Mateo"]
parejas = ""
for i in range (0,6,2):
    parejas = estudiantes[i], estudiantes[i+1]
    print(f"{"Pareja "}{int(i/2+1)} {"= "}{parejas}")

#Ejercicio 4
print("------- Ejercicio 4 -------")
for vidas in range (3,0,-1):
    print(f"{"Te quedan "}{vidas}{" vidas"}")
print("Game over")

#For anidado
print("------- Ejercicio 5 -------")
for fila in range (1, 4):
    for computadora in range (1, 5):
        nombre = input("Ingrese el nombre del estudiante: " )
        print(f"{nombre}{" asignado a la fila: "}{fila}{" - Computadora: "}{computadora}")
    print(f"{"Fin de la fila "}{fila}")