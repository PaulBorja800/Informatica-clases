"""Paúl Borja
Diploma 1 A
23-04-2026"""

#Nivel 1
#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    años_faltantes = 18 - edad
    print("Necesitas", años_faltantes, "años más para aprender a conducir.")
#Ejercicio 2
mi_edad = 25  # puedes cambiar este valor
tu_edad = int(input("Ingrese su edad: "))
if tu_edad > mi_edad:
    diferencia = tu_edad - mi_edad
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print("Eres", diferencia, "años mayor que yo.")
elif tu_edad < mi_edad:
    diferencia = mi_edad - tu_edad
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print("Soy", diferencia, "años mayor que tú.")
else:
    print("Tenemos la misma edad.")
#Ejercico 3
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
if numero1 > numero2:
    print(numero1, "es mayor que", numero2)
elif numero1 < numero2:
    print(numero1, "es menor que", numero2)
else:
    print(numero1, "es igual a", numero2)

#Nivel 2
#Ejercicio 4
puntaje = int(input("Ingrese su puntaje: "))
if puntaje >= 90 and puntaje <= 100:
    print("A")
elif puntaje >= 80:
    print("B")
elif puntaje >= 70:
    print("C")
elif puntaje >= 60:
    print("D")
elif puntaje >= 0:
    print("F")
else:
    print("Puntaje inválido")
#Ejercicio 5
mes = input("Ingrese el mes: ").lower()
if mes == "septiembre" or mes == "octubre" or mes == "noviembre":
    print("Otoño")
elif mes == "diciembre" or mes == "enero" or mes == "febrero":
    print("Invierno")
elif mes == "marzo" or mes == "abril" or mes == "mayo":
    print("Primavera")
elif mes == "junio" or mes == "julio" or mes == "agosto":
    print("Verano")
else:
    print("Mes inválido")
#Ejercico 6
frutas = ['banana', 'orange', 'mango', 'lemon']
fruta_usuario = input("Ingrese una fruta: ").lower()
if fruta_usuario in frutas:
    print("Esa fruta ya existe en la lista")
else:
    frutas.append(fruta_usuario)
    print("Fruta agregada. Lista actual:", frutas)