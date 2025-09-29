
titulos=[]
ejemplares=[]
while True:
    print("-----MENU: SISTEMA DE BIBLIOTECA-----")
    print("1. INGRESE LISTADO DE TITULOS")
    print("2. INGRESE EJEMPLARES PARA TITULOS CARGADOS")
    print("3. MOSTRAR CATALOGO")
    print("4. CONSULTAR DISPONIBILIDAD")
    print("5. LISTAR TITULOS AGOTADOS")
    print("6. AGREGAR UN NUEVO TITULO")
    print("7. ACTUALIZAR EJEMPLARES")
    print("8. SALIR")
    opcion=input("Ingrese una opcion: ")
    if not opcion.isnumeric():
        print("Error: Ingrese una opcion numerica")
        continue
    opcion=int(opcion)
    match opcion:
        case 1:#agregar lista de titulos
            while True:
                cantidad_de_titulos=input("Ingrese la cantidad de titulos que desea ingresar: ")
                if not cantidad_de_titulos.isnumeric():
                    print("Error: Ingrese una cantidad numerica")
                    continue
                cantidad_de_titulos=int(cantidad_de_titulos)
                if int(cantidad_de_titulos)<=0:
                    print("Error: Ingrese una cantidad de titulos mayor a 0")
                    continue
                break
            for i in range(cantidad_de_titulos):
                while True:
                    titulo=input(f"Ingrese el {i+1} titulo: ")
                    if titulo=="":
                        print("Error: campo titulo vacio")
                        continue
                    existe=False
                    for t in titulos:
                        if t.lower()==titulo.lower():
                            existe=True
                            break
                    if existe:
                        print(f"Error: titulo {titulo} ya existe en el sistema")
                        continue
                    titulos.append(titulo)
                    ejemplares.append(0)
                    print("Titulo ingresado con exito")
                    break
        case 2:#ingresar n de ejemplares
            if len(titulos)==0:
                print("Lista de titulos vacia")
                continue
            for i in range(len(titulos)):
                while True: 
                    numero_de_ejemplares=input(f"Ingrese cantidad de ejemplares de {titulos[i]}: ")
                    if not numero_de_ejemplares.isnumeric():
                        print("Error: Ingrese una cantidad numerica")
                        continue
                    numero_de_ejemplares=int(numero_de_ejemplares)
                    ejemplares[i]=numero_de_ejemplares
                    break
        case 3:#mostrar catalogo
            if len(titulos)==0:
                print("Lista de titulos vacia")
                continue
            for titulo, cantidad in zip(titulos, ejemplares):
                print(f"Titulo: {titulo} - Cantidad: {cantidad} disponibles")
        case 4:#mostrar dispinibilidad ingresando un titulo
            while True:
                titulo=input("Ingrese el titulo: ")
                if titulo=="":
                    print("Error: campo titulo vacio")
                    continue
                existe=False
                for i in range(len(titulos)):
                    if titulos[i].lower()==titulo.lower():
                        existe=True
                        print(f"Titulo: {titulo} - Cantidad: {ejemplares[i]} disponibles")
                        break
                if not existe:
                    print(f"Error: titulo {titulo} no existe en el sistema")
                    continue
                break
        case 5:#listar titulos agotados
            if len(titulos)==0:
                print("Lista de tituos vacia")
                continue
            print("-----LISTADO DE LIBORS SIN EJEMPLARES DISPONIBLES-----")
            for titulo, cantidad in zip(titulos, ejemplares):
                if cantidad==0:
                    print(f"Titulo: {titulo} sin disponibilidad")
        case 6:#agregar titulo
            while True:
                titulo=input(f"Ingrese un nuevo titulo: ")
                if titulo=="":
                    print("Error: campo titulo vacio")
                    continue
                existe=False
                for t in titulos:
                    if t.lower()==titulo.lower():
                        existe=True
                        break
                if existe:
                    print(f"Error: titulo {titulo} ya existe en el sistema")
                    continue
                titulos.append(titulo)
                ejemplares.append(0)
                print("Titulo ingresado con exito")
                break
        case 7:#ctualizar ejemplares: prestamo y devolucion
            print("Ingrese el numero de accion que desea ejecutar:: ")
            while True:
                respuesta=input("1. Prestar | 2. Devolver: ")
                if not respuesta.isnumeric():
                    print("Error: Ingrese una cantidad numerica")
                    continue
                respuesta=int(respuesta)
                if respuesta not in (1,2):
                    print("Error: Ingrese una opcion aceptada: 1 y 2")
                    continue
                titulo=input("Ingrese titulo:")
                if titulo=="":
                    print("Error: Campo titulo vacio")
                    continue
                existe=False
                for i in range(len(titulos)):
                    if titulos[i].lower()==titulo.lower():
                        existe=True
                        if respuesta==1: # -1
                            if ejemplares[i]>0:
                                ejemplares[i]-=1
                            else: 
                                print("Error: Cantidad de ejemplares insuficiente")
                        if respuesta==2:#+2
                            ejemplares[i]+=1
                        break
                if not existe:
                    print(f"Error: titulo {titulo} no existe en el sistema")
                    continue
                print("Ejemplar actualizado con exito")
                break
        case 8:
            print("Salida del sistema de bibliotecas!!!")
            break
        case _:
            print("Error: Ingrese una opcion valida del 1 al 9")
            continue