import csv

def leer_csv():
    productos = [] 
    try: 
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, delimiter=";")
            total = 0
            for fila in lector:
                print(f"{fila['producto']} $ {fila['precio']}")
                total += int(fila['precio'])
                productos.append(fila)
            print("Precio total acumulado:", total)
        return productos
    except FileNotFoundError:
        print("Error: archivo csv no encontrado")
        print("Creando archivo productos.csv")
        with open(RUTA_ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
            campos = ["producto", "precio"]
            escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=";")
            escritor.writeheader()  
            escritor.writerows([
                {"producto": "Laptop HP", "precio": "850000"},
                {"producto": "Mouse Logitech", "precio": "15000"},
                {"producto": "Teclado Mecánico", "precio": "32000"}
            ])
        return []


def agregar_producto(ruta_archivo):
    with open(ruta_archivo, "a", encoding="utf-8", newline="") as archivo:
        campos = ["producto", "precio"]
        escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=";")
        producto = ingresar_producto()
        precio = ingresar_precio()
        escritor.writerow({"producto": producto.capitalize(), "precio": precio})
        print(f"\nProducto '{producto}' agregado exitosamente!")


def ingresar_precio():
    while True:
        try: 
            precio = input("Precio: $")
            if not precio.isdigit():
                raise ValueError("Ingrese un valor numérico")
            precio = int(precio)
            if precio <= 0:
                raise ValueError("Ingrese un precio mayor a 0")
            return precio
        except ValueError as e:
            print("Error:", e)


def ingresar_producto():
    while True:
        try: 
            producto = input("Ingresar nombre de producto: ").capitalize()
            if producto == "":
                raise ValueError("Campo vacío. Ingrese un nombre para el producto")
            if producto.isnumeric():
                raise ValueError("Ingrese un nombre de un producto, No un numero")
            return producto
        except ValueError as e:
            print("Error:", e)


def eliminar_producto(ruta_archivo):
    try:
        while True:
            producto_a_eliminar = ingresar_producto()
            encontrado = False
            productos_actualizados = []
            #busco el producto en el csv
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo, delimiter=";")
                for fila in lector:
                    #guardo todos los elementos del csv menos el ingresado en una lista
                    if fila["producto"].lower() == producto_a_eliminar.lower():
                        encontrado = True
                    else:
                        if fila["producto"].strip() and fila["precio"].strip():
                            productos_actualizados.append(fila)
            if not encontrado:
                print(f"Producto '{producto_a_eliminar}' no encontrado\n")
                continue
        
            # Para modificar el csv se debe reescribir todo csv. Se gaurda la lista en csv
            with open(ruta_archivo, "w", encoding="utf-8", newline="") as archivo:
                campos = ["producto", "precio"]
                escritor = csv.DictWriter(archivo, fieldnames=campos, delimiter=";")
                escritor.writeheader()
                escritor.writerows(productos_actualizados)#se ecrinben todos menos el eliminado
        
            print(f"Producto '{producto_a_eliminar}' eliminado exitosamente!")
            
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no existe")
    except Exception as e:
        print(f"Error al eliminar producto: {e}\n")


RUTA_ARCHIVO="trabajo_en_clase/manejo_de_archivos/productos.csv"

while True:
    try:
        print("======MENU:SISTEMA PRODUCTOS CON CVS=====")
        print("1. Mostar listado de productos")
        print("2. Agregar un nuevo proucto al cvs")
        print("3. Eliminar producto del cvs")
        print("4. Salir del sistema")
        opcion=input("Ingrese una accion a ejecutar: ")
        if not opcion.isnumeric():
            raise ValueError("Opcion invalida. Ingrese un numero entero positivo")
        opcion=int(opcion)
        match opcion:
            case 1:#mostrar productos
                print("-----Listado de productos-----")
                leer_csv()
            case 2:#agregar un nuevo producto
                agregar_producto(RUTA_ARCHIVO)
            case 3:#eliminar un produco
                eliminar_producto(RUTA_ARCHIVO)
            case 4:#salir del sistema
                print("Salida del sistema de manejo de productos!!!")
                break
            case _:
                raise ValueError("Opcion invalida")
    except ValueError as e:
        print("Error: ", e)