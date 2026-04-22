"""Paúl Borja
Diploma 1 A
15-04-2026
"""
#Actividad 4 (Strings)
# %%
# Nivel 1
texto = "Programación Para Todos"
# Mostrar contenido
print(texto)
# Cantidad de caracteres
print(len(texto))
# %%
# Nivel 2
# Mayúsculas
print(texto.upper())
# Minúsculas
print(texto.lower())
# Title
print(texto.title())
# Capitalize
print(texto.capitalize())
# %%
# Nivel 3
# Empieza con "Programación"
print(texto.startswith("Programación"))
# Termina con "Todos"
print(texto.endswith("Todos"))
# Posición de "Para"
print(texto.find("Para"))
# Contiene "Python"
print("Python" in texto)
# %%
# Nivel 4
# Reemplazar
nuevo_texto = texto.replace("Programación", "Python")
print(nuevo_texto)
# Dividir en palabras
palabras = texto.split()
print(palabras)
# Unir con " - "
unido = " - ".join(palabras)
print(unido)
# %%
# Nivel 5
# Primer carácter
print(texto[0])
# Último carácter
print(texto[-1])
# Carácter en posición 5
print(texto[5])
# %%
# Nivel 6
# Nombre completo
nombre = "Juan Perez"   # puedes cambiarlo por tu nombre
# Mensaje
print("Hola, mi nombre es {}".format(nombre))
# opción 2
print(f"Hola, mi nombre es {nombre}")
# Acrónimo
partes = nombre.split()
iniciales = partes[0][0] + partes[1][0]
print(iniciales)
