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
#Menu simple
opcion = ""
while opcion != "3":
    print("-------MENU-------")
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("3. Salir")
    opcion = str(input("Ingrese una opción: " ))
    if opcion == "1":
        print("Hola, bienvenido")
    elif opcion == "2":
        print("Estamos aprendiendo ciclos while")
    elif opcion == "3":
        print("Saliendo del programa")
    else:
        print("Opción no válida")
