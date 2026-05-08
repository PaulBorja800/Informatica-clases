"""Paúl Borja, Paúl Zurita
Dipoma 1 A
08-05-2026"""
# Ejercicios while
# Ejercicio 1: Suma acumulativa
print("------- Ejercicio 1 -------")
num = int(input("Ingresa un número entero positivo: " ))
control = 1
sum = 1
while num > 0:
    while num > control:
        control = control + 1
        sum = sum + control
    else:
        print("La suma de todos los enteros es: ", sum)
        break
else:
    print("Número inválido, ingresar un positivo")

# Ejercicio 2: Control de presupuesto
print("------- Ejercicio 2 -------")
cantidad = 0
sumaTotal = 0
while True:
    compras = int(input("Ingresa el valor de tu compra: $" ))
    if compras <= 0:
        break
    cantidad = cantidad + 1
    sumaTotal = sumaTotal + compras
print("La cantidad de compras fue de: ", cantidad)
print("La suma total de las compras es de: $", sumaTotal)
print("Registro de compras finalizado")

# Ejercicio 3: Filtro de números
print("------- Ejercicio 3 -------")
numero = int(input("Ingresa un número entero positivo: " ))
recorrer = 0
while recorrer < numero:
    recorrer = recorrer + 1
    sigue = recorrer % 5
    if sigue == 0:
        continue
    print(recorrer)
