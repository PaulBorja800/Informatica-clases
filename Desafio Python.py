""" Paúl Borja
Diploma 1 A
29-04-2026"""
#Desafio Python: "Sistema de acceso al club Tecno"
#Variables:
nombre = str(input("Ingrese su nombre: " ))
edad = int(input("Ingrese su edad: " ))
puntaje = int(input("Ingrese su puntaje obtenido: " ))
asistencia = bool(input("¿Asististe a la competencia?(TRUE/FALSE): " ))
codigoInvitacion = str(input("Ingresa tu código de invitación: " ))
#Prints:
print(nombre.upper())
print(nombre())
#Promedio:
promedio = (puntaje + asistencia)/2
#Ingresar al evento:
if edad >= 14:
    if promedio >= 80:
        if codigoInvitacion == "PYTHON2026":
            print("Acceso VIP")
        else:
            print("Acceso general")
    elif 60 < promedio < 79:
        print("Acceso con observación")
    elif promedio < 60:
        print("No se puede ingresar por bajo rendimiento")
else:
    if codigoInvitacion == "PYTHON2026":
        print("Acceso especial con acompañante")
    else:
        print("No cumple con la edad mínima")

