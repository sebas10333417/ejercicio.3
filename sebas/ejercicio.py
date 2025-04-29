print("!!! Bienvenido a la lista de libros!!!")

libro = []
libro1 = []
continuar = True

while continuar:
    print("\n Por favor ingresa los siguientes datos: ")
    print("\n por favor ingresa ID del libro: ")
    id = input()
    print("\n por favor ingresa el Titulo del libro: ")
    Titulo = input()
    print("\n por favor ingresa el nombre del Autor del libro: ")
    Autor = input()
    print("\n por favor ingresa el Año de publicacion del libro: ")
    año_de_publicacion = input()
    libro.append(id)
    libro.append(Titulo)
    libro.append(Autor)
    libro.append(año_de_publicacion)
    
    libros = { "ID": id,
                "Nombre": Titulo,
                "Nombre Autor": Autor,
                  "Año de publicacion": año_de_publicacion
        }
    libro.append(libros)

    salir = input("Deseas registra un nuevo libro: \n si no, dar No para salir: ").lower()
    if salir == "no":
        continuar = False
        print(libros)


# for p in libros: 
#     print(f"\n ID: {p["id"]}")
#     print(f"\n Nombre: {p["Titulo"]}")
#     print(f"\n Nombre autor: {p["Autor"]} ")
#     print(f"\n Año de publicacion: {p["año_de_publicacion"]}")
        
#     print("Libros ingresados: ")
#     print(libros)   

   