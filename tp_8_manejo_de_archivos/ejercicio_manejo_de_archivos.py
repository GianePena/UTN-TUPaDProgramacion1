import os

RUTA_ARCHIVO = "tp_8_manejo_de_archivos/productos.txt"
#Actividad 1: Crear archivo inicial con tres productos

def crear_archivo_inicial():
    if os.path.exists(RUTA_ARCHIVO): #os.path.exists verifica que exista el .txt
        print(f"El archivo '{RUTA_ARCHIVO}' existe")
    else:
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            archivo.write("Parlante,850000,20\n")
            archivo.write("Mouse,15000,3\n")
            archivo.write("Teclado,32000,12\n")
        print(f"Archivo '{RUTA_ARCHIVO}' creado con productos iniciales.\n")
#Actividad 2: Leer y mostrar productos con formato específico
def leer_y_mostrar_productos():
    try:
        print("===== LISTADO DE PRODUCTOS =====")
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()  
                if linea:
                    datos = linea.split(",") 
                    nombre = datos[0]
                    precio = datos[1]
                    cantidad = datos[2]
                    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        print()
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe.\n")

#Actividad 3: Agregar nuevo producto sin borrar contenido existente
def agregar_producto_desde_teclado():
    print("===== AGREGAR NUEVO PRODUCTO =====")
    while True:
        nombre = input("Ingrese nombre del producto: ").strip()
        if nombre and not nombre.isdigit():
            break
        print("Error: Ingrese un nombre válido.")
    while True:
        try:
            precio = float(input("Ingrese precio: $"))
            if precio > 0:
                break
            print("Error: El precio debe ser mayor a 0.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad >= 0:
                break
            print("Error: La cantidad debe ser mayor o igual a 0.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")
    with open(RUTA_ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    print(f"Producto '{nombre}' agregado exitosamente!")

#Actividad 4: Cargar productos en lista de diccionarios
def cargar_productos_en_lista():
    productos = []
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    datos = linea.split(",")
                    producto = {
                        "nombre": datos[0],
                        "precio": float(datos[1]),
                        "cantidad": int(datos[2])
                    }
                    productos.append(producto)
        return productos
    except FileNotFoundError:
        print(f"Error: El archivo '{RUTA_ARCHIVO}' no existe")
        return []

#Actividad 5: Buscar producto por nombre
def buscar_producto_por_nombre():
    productos = cargar_productos_en_lista()
    
    if not productos:
        print("No hay productos cargados.\n")
        return
    
    print("===== BUSCAR PRODUCTO =====")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']}")
            print(f"  Cantidad: {producto['cantidad']}\n")
            encontrado = True
            break
    
    if not encontrado:
        print(f"Error: El producto '{nombre_buscar}' no existe.\n")

#Actividad 6: Sobrescribir archivo con productos actualizados
def guardar_productos_actualizados(productos):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Archivo actualizado correctamente.\n")


def menu_principal():
    crear_archivo_inicial()
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Mostrar todos los productos")
        print("2. Agregar nuevo producto")
        print("3. Buscar producto por nombre")
        print("4. Ver productos en lista")
        print("5. Guardar cambios al archivo")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1":
                leer_y_mostrar_productos()
            case "2":
                agregar_producto_desde_teclado()
            case "3":
                buscar_producto_por_nombre()
            case "4":
                productos = cargar_productos_en_lista()
                print("===== PRODUCTOS EN MEMORIA =====")
                for i, prod in enumerate(productos, 1):
                    print(f"{i}. {prod}")
                print()
            case "5":
                productos = cargar_productos_en_lista()
                guardar_productos_actualizados(productos)
            case "6":
                print("Salida del sistema!")
                break
            case _ :
                print("Opción inválida. Intente nuevamente")


menu_principal()