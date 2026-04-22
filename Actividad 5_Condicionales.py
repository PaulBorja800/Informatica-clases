"""PaúlBorja
Diploma 1 A
22-04-2026"""
#Inicio clase
a = int(input("Ingresa un número: ", ))
if a > 0:
    print('A is a positive number')# A is a positive number
elif a < 0:
    print("A is a negative number")# A is a negative number
elif a/2 == 0:
    print("A is an even number")# A is an even number
elif a/2 != 0:
    print("A is an odd number")# A is an odd number
else:
    print("A is 0")#A is 0
#if anidado
if a > 0:
   if a % 2 == 0:
       print('A is a positive and even integer')
   else:
       print('A is a positive number')
elif a == 0:
   print('A is zero')
else:
   print('A is a negative number')
#Ejercicio sin if anidado
a = int(input("Ingresa un número: ", ))
if a > 0 and a % 2 == 0:
    print("A es positivo y par")
else:
    if a < 0 and a % 2 == 0:
        print("A es negativo par")
    else:
        if a > 0 and a % 2 != 0:
            print("A es positivo impar")
        else:
            if a < 0 and a % 2 != 0:
                print("A es negativo impar")
            else:
                if a == 0:
                    print("A es 0")
