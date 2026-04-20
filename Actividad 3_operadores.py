#Tarea 2
"""Paúl Borja
Diploma 1 A
14-04-2026
"""
#Edad como un entero
edad = int(16)
#Estatura como decimal
estatura = float(1.67)
# Área de un triángulo
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area_triangulo = 0.5 * base * altura
print("Área del triángulo:", area_triangulo)
# Perímetro de un triángulo
a = float(input("Ingresa el lado a: "))
b = float(input("Ingresa el lado b: "))
c = float(input("Ingresa el lado c: "))
perimetro = a + b + c
print("Perímetro del triángulo:", perimetro)
# Rectángulo
longitud = float(input("Ingresa la longitud: "))
ancho = float(input("Ingresa el ancho: "))
area_rect = longitud * ancho
perimetro_rect = 2 * (longitud + ancho)
print("Área del rectángulo:", area_rect)
print("Perímetro del rectángulo:", perimetro_rect)
# Círculo
radio = float(input("Ingresa el radio: "))
pi = 3.14
area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio
print("Área del círculo:", area_circulo)
print("Circunferencia:", circunferencia)
# Pendiente y distancia entre (2,2) y (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Pendiente:", pendiente)
print("Distancia:", distancia)
# Función y = x^2 + 6x + 9
x = int(input("Ingresa un valor de x: "))
y = x**2 + 6*x + 9
print("Valor de y:", y)
# Probando valores
x = -3
y = x**2 + 6*x + 9
print("Cuando x = -3, y =", y)
# Longitud de palabras y comparación
palabra1 = "python"
palabra2 = "dragon"
print("Longitud de python:", len(palabra1))
print("Longitud de dragon:", len(palabra2))
print("¿Son iguales?", len(palabra1) == len(palabra2))
# Verificar "on"
print("on" in palabra1 and "on" in palabra2)
# Verificar palabra
oracion = "Espero que este curso no esté lleno de jerga."
print("jerga" in oracion)
# Igual que 13
print("on" in "python" and "on" in "dragon")
# Convertir tipos
longitud_python = len("python")
valor_float = float(longitud_python)
valor_string = str(valor_float)
print(valor_float)
print(valor_string)
# División entera
print(7 // 3 == int(2.7))
# Comparar tipos
print(type("10") == type(10))
# Comparar conversión
print(int(9.8) == 10)
# Pago total
horas = float(input("Horas trabajadas: "))
tarifa = float(input("Tarifa por hora: "))
pago = horas * tarifa
print("Pago total:", pago)
# Segundos vividos
anios = int(input("Años vividos: "))
segundos = anios * 365 * 24 * 60 * 60
print("Has vivido aproximadamente:", segundos, "segundos")
# Tabla
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
