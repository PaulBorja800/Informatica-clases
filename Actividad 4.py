"""Paúl Borja
Diploma 1 A
15-04-2026
"""
#Actividad 4 (Strings)

#Texto de varias líneas
hola = """hola me llamo paul
soy de diploma 1 
este es el año 2025-2026"""
#Usar con texto
nombre = "Paúl"
apellido = "Borja"
nombreCompleto = nombre + " " + apellido
print(nombreCompleto)
#Secuencias de escape
#Salto de línea
print("Cómo te va? \n Bien, y tu?")
#Backslash
print("Hola, cómo te va? (\\)")
#Cita
print("Dijo \"Hola\"")
#Desempaquetar cadenas
nombreCadena = "Paúl"
print(len(nombreCadena))
a, b, c, d = nombreCadena 
print(a)
print(b)
print(c)
print(d)
#Cortar textos
print(nombreCadena[2:4])
print(nombreCadena[-2:])
print(nombreCadena[0:3:2])
print(nombreCadena[::-1])
