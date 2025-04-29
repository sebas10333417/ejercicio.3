print("!!! Bienvenido al sistemas de la Biblioteca!!! \n")

libro = []
libro1 = []
contiuar = True

print("Por favor ingresa los siguientes datos: \n ")
print("Por favor ingresa el ID del libro: ")
id = input()
print("Por favor ingresa el titulo del libro: ")
Titulo = input ()
print("Por favor ingresa el nombre del autor: ")
Nombre = input()
print("Por favor ingresa el año de publicacion: ")
año_publicacion = input()

libro.append (id)
libro.append (Titulo)
libro.append (Nombre)
libro.append (año_publicacion)

print ("!!! Los datos ingresados fueron: !!! ")
print ("ID --", id)
print ("TITULO --", Titulo)
print ("NOMBRE --",Nombre)
print ("AÑO PUBLICACION -- ",  año_publicacion)

salir = input("Deseas ingresar oto libro? \n si no ingresa NO para salir: ").lower
if salir == "no":
    contiuar = False
    print(libro)
else:
    print
("Por favor ingresa los siguientes datos: \n ")
print("Por favor ingresa el ID del libro: ")
id = input()
print("Por favor ingresa el titulo del libro: ")
Titulo = input ()
print("Por favor ingresa el nombre del autor: ")
Nombre = input()
print("Por favor ingresa el año de publicacion: ")
año_publicacion = input()

libro1.append (id)
libro1.append (Titulo)
libro1.append (Nombre)
libro1.append (año_publicacion)

print ("!!! Los datos ingresados fueron: !!! ")
print ("ID --", id)
print ("TITULO --", Titulo)
print ("NOMBRE --",Nombre)
print ("AÑO PUBLICACION -- ",  año_publicacion)

salir = input("Deseas ingresar oto libro? \n si no ingresa NO para salir: ").lower
if salir == "no":
    contiuar = False
    print(libro)
else:
    print(libro)
    print(libro1)






