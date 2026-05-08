"""Paúl Borja, Paúl Zurita
Dipoma 1 A
08-05-2026"""
#Ejercicios while
#Ejercicio 1: Suma acumulativa
num = int(input("Ingresa un número entero positivo: " ))
control = 1
sum = 1
while num > 0:
    while num > control:
        control = control + 1
        sum = sum + control
    else:
        print("La suma de todos los enteros es: ", sum)
else:
    print("Número inválido, ingresar un positivo")
# Ejercicio 2: Control de presupuesto
