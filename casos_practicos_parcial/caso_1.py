# 🧪 Práctica Evaluativa –Parcial I
# Asignatura: Programación I
# Tema: Estructuras Repetitivas con Listas

# Caso 1 — Biblioteca escolar — Préstamos de libros

# Caso 1 – Biblioteca escolar – Préstamos de libros
# Enunciado / Descripción
# La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que utilice listas paralelas (una para títulos[] y otra para ejemplares[]). Cada título debe estar vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas. Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario elija salir.

# Ejemplo:
# 	•	títulos[] = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
# 	•	ejemplares[] = [5, 3, 7]
# En este ejemplo, "El Señor de los Anillos" tiene 5 copias, "Orgullo y Prejuicio" tiene 3 copias, y "Matar un Ruiseñor" tiene 7 copias.
# Opciones del Menú
# 	•	Ingresar lista de títulos:
# titulo_ingresado=input("Ingrese titulo del libro: ").lower()

# 	•	Permite al usuario introducir los títulos de los libros en la biblioteca.
# 	•	Ejemplo: El usuario introduce "1984", "Rebelión en la Granja".
# 	•	Ingresar lista de ejemplares disponibles (por título):
# 	•	Permite al usuario introducir el número de copias disponibles para cada título de libro.
# 	•	Ejemplo: Si el título es "1984", el usuario podría introducir "4" (lo que significa que hay 4 copias).
# 	•	Mostrar catálogo con stock:
# 	•	Muestra una lista de todos los títulos y el número de copias disponibles para cada uno.
# 	•	Ejemplo de salida:
# 	•	"El Señor de los Anillos: 5 copias"
# 	•	"Orgullo y Prejuicio: 3 copias"
# 	•	"Matar un Ruiseñor: 7 copias"
# 	•	Consultar disponibilidad de un título específico:
# 	•	Permite al usuario introducir un título y ver cuántas copias están disponibles.
# 	•	Ejemplo: El usuario introduce "Orgullo y Prejuicio", y el programa muestra "3 copias disponibles".
# 	•	Listar agotados (0 ejemplares):
# 	•	Muestra una lista de todos los títulos que tienen 0 copias disponibles.
# 	•	Agregar título:
# 	•	Permite al usuario añadir un nuevo título al catálogo y especificar el número inicial de copias.
# 	•	Ver títulos agotados:
# 	•	Muestra una lista de los títulos con cero copias disponibles.
# 	•	Actualizar ejemplares (préstamo/devolución):
# 	•	Permite al usuario actualizar el número de copias cuando un libro es prestado (préstamo) o devuelto (devolución).
# 	•	Ejemplo: Si alguien toma prestada una copia de "El Señor de los Anillos", el usuario puede actualizar el conteo de 5 a 4.
# 	•	Ver catálogo:
# 	•	Muestra el catálogo entero de los títulos de libros.
# 	•	Salir:
# 	•	Sale del programa.


titulos=[]
cantidad_de_ejemplares=[]

opcion=1
while opcion:
    print("MENU: 1.Ingresar libro/s || 2.Mostrar libros disponibles || 3.Consultar dispoibilidad || 4.Mostrar libros no disponibles || 5.Actualizar ejemplares ||6. Mostrar catalogo || 7.Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1: #Ingresar lista de libros y sus cantidades
        cantidad_de_libros = int(input("Número de libros a ingresar: ")) #cantidad de libros a ingresar
        for i in range(cantidad_de_libros):
            titulo = input("Título del libro: ").lower()
            cantidad = int(input("Cantidad de ejemplares: "))
            if cantidad<0:
                print("Error numero invalido: Ingrese un numero entero positivo")
                cantidad=0
            if titulo in titulos:
                index = titulos.index(titulo)
                cantidad_de_ejemplares[index] += cantidad
            else:
                titulos.append(titulo)
                cantidad_de_ejemplares.append(cantidad)
    elif opcion==2: #mostrar todo el catalogo de libros 
        print("CATALOGO DE LIBROS DISPONIBLES: ")
        for libro, stock in zip(titulos, cantidad_de_ejemplares): 
            if stock>0: print(f"Titulo: {libro}: - cantidad en stock: {stock} copias disponibles")
        
    elif opcion==3: #buscar diponibilidad ingresando el titulo
        print("BUSCAR DISPONIBILIDAD")
        buscar_titulo= input("Titulo del libro: ").lower()
        if buscar_titulo not in titulos:
            print("Error libro no encontrado")
        else: 
            index=titulos.index(buscar_titulo)  
            print(f"{buscar_titulo}: {cantidad_de_ejemplares[index]} copias disponibles")
    elif opcion==4: #Lista de libros agotados
        print("LIBROS AGOTADOS")
        for libro, stock in zip(titulos, cantidad_de_ejemplares):
            if stock==0:
                print(f"Titulo: {libro}")
    elif opcion==5:# prestar o devolver libros 
        print("PRESTAR O DEVOLVER LIBROS")
        estado_del_libro=input("¿Que desea hacer? Prestar - Devolver (ingrese la palabra correspindiente a la accion) ").lower()
        libro_buscado= input("Titulo del libro: ").lower()
        if estado_del_libro=="prestar":
            if libro_buscado not in titulos:
                print("Error titulo no encontrado")
                continue
            else: 
                index= titulos.index(libro_buscado)
                if cantidad_de_ejemplares[index]>0:
                    cantidad_de_ejemplares[index]-=1
                else:
                    print("Error libro no disponible")
        elif estado_del_libro=="devolver":
            if libro_buscado not in titulos:
                print("Error titulo no encontrado")
                continue
            else: 
                index= titulos.index(titulo)
                cantidad_de_ejemplares[index]+=1
        else:
            print("Opcion ingresada incorrecta")
            continue
        print("CATALOGO ACTUALIZADO:")
        for libro, stock in zip(titulos, cantidad_de_ejemplares):
            print(f"Titulo:{libro} - cantidad en stock: {stock} ")
    elif opcion==6:
        print("CATALOGO COMPLETO: ")
        for libro, stock in zip(titulos, cantidad_de_ejemplares):
            print(f"Titulo:{libro} - cantidad en stock: {stock} ")
    elif opcion==7:
        print("Saludos!")
        break
    else: 
        print("Opcion incorrecta")
        continue

