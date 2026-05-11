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