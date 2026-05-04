"""Paúl Borja
Diploma 1A
04-05-2026"""
#Ciclos de repetición
# %%
#Variables de control
"""count = 0
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
# %%
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
#%%
#Break
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
    if contador == 3:
        break
print("E ciclo fue interrumpido")
"""
#Contraseña
contraseña = ""
intento = 1
while intento < 4:
    contraseña = str(input("Ingresa la contraseña: " ))
    intento = intento + 1
    if contraseña == "python123":
        print("Acceso permitido")
        break
else:
    print("Cuentas suspendida por muchos intentos")