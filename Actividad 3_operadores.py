#Tarea 2
"""Paúl Borja
Diploma 1 A
14-04-2026
"""
#Edad como un entero
edad = int(16)
#Estatura como decimal
estatura = float(1.67)
#Area de un triángulo
base = float(input("Ingresa la base de tu triángulo: "))
altura = float(input("Ingresa la altura de tu triángulo: "))
area = 0.5*base*altura
print("El área del triángulo es: ", area)
#Perímetro de un triángulo
a = float(input("Ingresa el lado a de tu triángulo: "))
b = float(input("Ingresa el lado b de tu triángulo: "))
c = float(input("Ingresa el lado c de tu triángulo: "))
perimetro = a + b + c
print("Perímetro de tu triángulo es: ", perimetro)
#Área y perímetro de un rectángulo
longitud = float(input("Ingresa la longitud del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
areaRectangulo = longitud * ancho
perimetroRectangulo = 2 * (longitud + ancho)
print("El área del rectángulo es:", areaRectangulo)
print("El perímetro del rectángulo es:", perimetroRectangulo)
#Área y circunferencia de un círculo
radio = float(input("Ingresa el radio del círculo: "))
pi = 3.141592
areaCirculo = pi * radio * radio
circunferencia = 2 * pi * radio
print("Área del círculo es:", areaCirculo)
print("La circunferencia del círculo es:", circunferencia)
#Pendiente
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("La pendiente es:", pendiente)
print("La distancia es:", distancia)
#Y en una función
x = int(input("Ingresa el valor de x: "))
y = x**2 + 6*x + 9
print("Valor de y:", y)
for i in range(-5, 1):
    y = i**2 + 6*i + 9
    print("x:", i, "y:", y)
#Longitud de palabras
palabra1 = "python"
palabra2 = "dragon"
print(len(palabra1))
print(len(palabra2))
print(len(palabra1) == len(palabra2))
# Verificar "on"
print("on" in palabra1 and "on" in palabra2)
# Verificar palabra en oración
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
# Comparar int
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
for i in range(2, 6):
    print(i, 1, i, i*i, i*i*i)
