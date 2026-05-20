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
