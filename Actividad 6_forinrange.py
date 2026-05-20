"""Paúl Borja
Diploma 1A
20-05-2026"""

#For in range
# Tabla de multiplicar
print("------- Ejercicio 1 -------")
numero = int(input("Ingresa un número: " ))
num = int(input("¿Hasta qué número quieres ver?: " ))
for i in range (1, num+1):
    print(f"{numero}{"x"}{i}{"="}{i*numero}")

