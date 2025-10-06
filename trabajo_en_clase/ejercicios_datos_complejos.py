

def mostar_mochila(mochila):
    for i in range(len(mochila)):
        if mochila[i] == "":
            print("--- vacío ---")
        else:
            print(f"{mochila[i]}")
def ingresar_tamaño_de_mochila():
    while True:
        try:
            tamaño = input("Ingrese el tamaño de la mochila: ")
            if tamaño.strip() == "":
                raise ValueError("No puede estar vacío.")
            tamaño = int(tamaño)
            if tamaño <= 0:
                raise ValueError("No se permiten números negativos.")
        except ValueError as e:
            print("Error:", e)
        else:
            return tamaño


def crear_mochila(tamaño):
    mochila = []
    for _ in range(tamaño):
        mochila.append("")
    return mochila


def guardar_en_mochila(mochila, posicion, nuevo_elemento):
    try:
        if posicion.strip() == "":
            raise IndexError("Posición vacía, ingrese una posición.")
        if not posicion.isnumeric():
            raise ValueError("Ingrese un valor numérico para posición.")
        posicion = int(posicion)
        if posicion > len(mochila) or posicion <= 0:
            raise IndexError("Indice fuera del rango.")
        if nuevo_elemento.strip() == "":
            raise ValueError("Campo vacío, ingrese un elemento nuevo.")
        
        if mochila[posicion-1] == "":
            mochila[posicion-1] = nuevo_elemento
            print(f"Elemento '{nuevo_elemento}' guardado en la posición {posicion}.")
        else:
            print("Esa posición ya está ocupada.")
        return mochila
    except IndexError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)



tamaño = ingresar_tamaño_de_mochila()
nueva_mochila = crear_mochila(tamaño)


while True:
    print("----- MENU DE LA MOCHILA -----")
    print("1. Guardar objeto en mochila")
    print("2. Ver mochila")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    try:
        if opcion == "":
            raise ValueError("Opción ingresada vacía.")
        if not opcion.isnumeric():
            raise ValueError("Ingrese un número.")
        opcion = int(opcion)
        match opcion:
            case 1:
                nuevo_elemento = input("Ingrese un nuevo elemento a incorporar: ")
                posicion = input("Ingrese la posición donde se colocará el elemento: ")
                guardar_en_mochila(nueva_mochila, posicion, nuevo_elemento)
                mostar_mochila(nueva_mochila)
            case 2:
                mostar_mochila(nueva_mochila)
            case 3:
                print("Salida del sistema. ¡Hasta luego!")
                break
            case _:
                raise ValueError("Opción fuera del rango del menú.")
    except ValueError as e:
        print("Error:", e)
