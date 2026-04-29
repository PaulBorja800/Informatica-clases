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
print("Participante: ", nombre.upper())
print("Caracteres del nombre: ", len(nombre))
#Promedio:
promedio = (puntaje + asistencia)/2
print("Promedio general: ", promedio)
#Ingresar al evento:
if edad >= 14:
    if promedio >= 80:
        if codigoInvitacion == "PYTHON2026":
            print("Resultado: Acceso VIP")
        else:
            print("Resultado: Acceso general")
    elif 60 < promedio < 79:
        print("Resultado: Acceso con observación")
    elif promedio < 60:
        print("Resultado: No se puede ingresar por bajo rendimiento")
else:
    if codigoInvitacion == "PYTHON2026":
        print("Resultado: Acceso especial con acompañante")
    else:
        print("Resultado: No cumple con la edad mínima")
#Puntaje adicional:
if puntaje >= 90 and asistencia >= 90:
    print("Mensaje adicional: Candidato destacado")
elif puntaje < 50 or asistencia < 50:
    print("Mensaje adicional: Requiere refuerzo previo")
