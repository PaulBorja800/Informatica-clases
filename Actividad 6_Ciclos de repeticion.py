"""Paúl Borja
Diploma 1A
04-05-2026"""
#Ciclos de repetición
#Variables de control
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(f"Se dieron {count} vueltas .Ciclo terminado")
#Ingresar clave
clave = ""
while clave != "Python":
    clave = str(input("Ingrese la clave: " ))
else:
    print("Acceso permitido")
