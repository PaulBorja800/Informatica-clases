"""Paúl Borja
Diploma 1A
11-05-2026"""
#Ejemplo
numbers = [ 0, 1, 2, 3]
for iterador in numbers:
    print(iterador)
#Ejemplo 2
notas = [ 8, 7, 9, 10, 6]
suma = 0
for nota in notas:
    suma = suma + nota
promedio = suma / len(notas)
print(promedio)
#Ejemplo 3
palabra = str(input("Ingresa tu nombre y apellido: " ))
for letra in palabra:
    print(letra)
#Ejemplo 4
pal = str(input("Ingresa una palabra: " ))
vocales = 0
consonantes = 0
for let in pal:
    if let == "a" or let == "e" or let == "i" or let == "o" or let == "u":
        vocales = vocales + 1
    else:
        consonantes = consonantes + 1
print("Voclaes: ", vocales, ", Consonantes: ", consonantes)
total = vocales + consonantes
print("El total de letras es: ", total)
#Ejemplo 5
companies = {"Facebook", "Google", "Apple", "Amazon", "Facebook"}
for company in companies:
    print(company)
#Ejemplo 6
num = input("Ingresa un número: " )
lista = {0, 3, 6, 54, 12}
for number in num:
    print(number)
    if number == 3:
        print("ganaste")
        break

#Tarea
#Ejercicio 1: Listas
print("------- Ejercicio 1 -------")
notas = [8.5, 6.0, 9.0, 7.0, 5.5]
suma = 0
aprobados = 0
reprobados = 0
for nota in notas:
    suma = suma + nota
    if nota >= 7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
promedio = suma / len(notas)
print("La suma total de las notas es: ", suma)
print("El promedio del curso es: ", promedio)
print("Cantidad de aprobados: ", aprobados)
print("Cantidad de reprobados: ", reprobados)

#Ejercicio 2: Strings
print("------- Ejercicio 2 -------")
contrasena = "Python2026"
letras = 0
numeros = 0
cantidad_o = 0
for caracter in contrasena:
    if caracter.isalpha():
        letras = letras + 1
    if caracter.isdigit():
        numeros = numeros + 1
    if caracter == "o":
        cantidad_o = cantidad_o + 1
print("Cantidad de letras: ", letras)
print("Cantidad de números: ", numeros)
print("Cantidad de veces que aparece la letra o: ", cantidad_o)

#Ejercico 3: Set
print("------- Ejercicio 3 -------")
productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}
cantidad_productos = 0
mas_de_6 = 0
for producto in productos:
    cantidad_productos = cantidad_productos + 1
    contador_letras = 0
    for letra in producto:
        contador_letras = contador_letras + 1
    if contador_letras > 6:
        mas_de_6 = mas_de_6 + 1
print("Cantidad de productos únicos: ", cantidad_productos)
print("Productos con más de 6 letras: ", mas_de_6)

#Ejercicio 4: Break
print("------- Ejercicio 4 -------")
correo = str(input("Ingrese su correo electrónico: " ))
usuario = ""
for caracter in correo:
    if caracter == "@":
        break
    usuario = usuario + caracter
print("El nombre de usuario es: ", usuario)

#Ejercicio 5: Continue
print("------- Ejercicio 5 -------")
telefono = input("Ingrese su número de teléfono: ")
telefono_limpio = ""
for caracter in telefono:
    if caracter == " " or caracter == "-":
        continue
    telefono_limpio = telefono_limpio + caracter
print("Número limpio: ", telefono_limpio)

#For in range
figura = ""
for i in range(1, 5):
    for j in range(i):
        figura += "*"
    figura += "\n"
print(figura)