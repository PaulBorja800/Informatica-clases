#Paúl Borja 08-04-2026
#Muchas variables en una misma linea
primer_nombre, primer_apellido, pais, edad, esta_casado = "Paúl", "Borja", "Ecuador", 16, False
print(primer_nombre, primer_apellido, pais, edad, esta_casado)
print("Primer nombre: ", primer_nombre)
print("Primer apellido: ", primer_apellido)
print("País: ", pais)
print("Edad: ", edad)
print("Esta casado?: ", esta_casado)

#Tarea

"""Nombre: Paúl Borja
Fecha: 12-04-2026
Titulo: Tarea variables
"""
#Nivel 1
#variables separadas
nombre = "Paúl"
apellido = "Borja"
nombreCompleto = "Paúl Borja"
pais = "Ecuador"
ciudad = "Quito"
edad = 16
año = 2026
estaCasado = False
esVerdadero = True
luzEncendida = True
#Varias variables en una sola linea
nombre, apellido, nombreCompleto, pais, ciudad, edad, año, estaCasado, esVerdadero, luzEncendida = "Paúl", "Borja", "Paúl Borja", "Ecuador", "Quito", 16, 2026, False, True, True

#Nivel 2
#Funcion type
type(nombre)
type(apellido)
type(nombreCompleto)
type(pais)
type(ciudad)
type(edad)
type(año)
type(estaCasado)
type(esVerdadero)
type(luzEncendida)
#Funcion len
len(nombre)
len(apellido)
print("La diferencia de carácteres entre mi nombre y apellido son: ", len(apellido)-len(nombre))
#Declarar más variables
numeroUno = 5
numeroDos = 4
total = numeroUno + numeroDos
diferencia = numeroUno - numeroDos
producto = numeroUno * numeroDos
division = numeroUno / numeroDos
residuo = numeroDos % numeroUno
potencia = numeroUno ** numeroDos
divisionEntera = numeroUno // numeroDos
#Circulo
radioCirculo = 30
areaCirculo = 3.14159*(30**2)
circunferenciaCirculo = 2*(3.14159*30)
#Circulo del usuario
radio = input()
area = 3.14159*(radio**2)
#Funcion input
usuarioNombre, usuarioApellido, usuarioPais, usuarioEdad = input(), input(), input(), input()
#Comprobar palabras reservadas
help("keywords")
