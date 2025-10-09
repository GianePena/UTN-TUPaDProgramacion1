# #Actididad 1 : añadir frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

def añadir_fruta(nueva_fruta,precio, dict_frutas):
    dict_frutas[nueva_fruta]=precio

añadir_fruta("Naranja", 1200, precios_frutas)
añadir_fruta("Manzana", 1500, precios_frutas)
añadir_fruta("Pera", 2300, precios_frutas)

print(f"Listado de precios: {precios_frutas}")

##Actividad 2: actualizar precios anteriores por los siguientes

def actualizar_precios(dict_frutas, nombre, nuevo_precio):
    dict_frutas[nombre.capitalize()]=nuevo_precio
    return f"Precion {nombre} acutalizado"
actualizar_precios(precios_frutas, "banana", 1330)
actualizar_precios(precios_frutas, "manzana", 1700)
actualizar_precios(precios_frutas, "melón", 2800)

print(f"Listado de precios actualizados: {precios_frutas}")

# #Actividad 3: crearun lista de frutas del punto anterior sin precios

lista_frutas=list(precios_frutas.keys())
print(lista_frutas)


#Actividad 4: Escribí un programa que permita almacenar y consultar números telefónicos
#Permitr cargar 5 contactos con su nombre y numero
#pedir un nombre y mostrar el numero


def añadir_contacto(nombre, numero, agenda):
    if nombre not in agenda.keys():
        agenda[nombre]=numero
        return True
    else:
        return False  

def consultar_numero(agenda, nombre_ingresado):
    try: 
        print(agenda[nombre_ingresado])
    except KeyError: 
        print(f"Error:Contacto {nombre_ingresado} no encontrado ")

agenda={}
contador=1

while contador<5:
    try:
        telefono=input("Ingrese numero telefonico que desea agendar: ")
        if telefono=="":
            raise ValueError("Numero telefonico vacio")
        nombre=input("Nombre del contacto: ").capitalize()
        if nombre=="":
            raise ValueError("Nombre de contacto vacio")
        correcto= añadir_contacto(nombre, telefono, agenda)
        if correcto:
            print("Numero agendado")
            contador+=1
        else:
            print("Error: el nombre de contacto ya existe, ingrese otro contacto")
            continue
    except ValueError as e:
        print("Error: ", e)

consultar_telefono=input("Consultar telefono: Nombre del contacto: ").capitalize()
consultar_numero(agenda, consultar_telefono)
print(agenda)


#Actividad 5:  solicitar una frase e imprimir con un set
#generar un diccionario cn la cantidad de veces que apareca da palabra

def transformar_frase(frase):
    if not frase.split():
        print("Error: Frase vacía")
        return None
    frase=frase.split(" ")
    set_frase=set(frase)
    return set_frase

def contar_palabras(frase, set_frase):
    diccionario={}
    for palabra in set_frase:
        diccionario[palabra]=list(frase).count(palabra)
    return diccionario

frase_ingresada=input("Ingrese una frase: ")

frase_seteada=transformar_frase(frase_ingresada)
print(frase_seteada)

diccionario_de_palabras=contar_palabras(frase_ingresada, frase_seteada)
print(diccionario_de_palabras)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

def ingresar_alumno():
    while True:
        try:
            alumno = input("Nombre alumno: ").strip()
            if alumno == "":
                raise ValueError("Campo nombre incompleto")
            return alumno
        except ValueError as e:
            print("Error:", e)


def ingresar_notas():
    notas = []
    for n in range(3):
        while True:
            try:
                nota = input(f"Ingrese nota nº{n+1}: ").strip()
                if nota == "":
                    raise ValueError("No se puede dejar la nota vacía.")
                nota = int(nota)
                if nota <= 0:
                    raise ValueError("La nota debe ser mayor que 0.")
                notas.append(nota)
                break  
            except ValueError as e:
                print("Error:", e)
    return notas


def principal():
    alumnos = {}
    for _ in range(3):  
        alumno = ingresar_alumno()
        notas = ingresar_notas()
        alumnos[alumno] = tuple(notas)
    for alumno, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{alumno}: Notas {notas} | Promedio: {promedio:.2f}")

principal()

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1,2,3,4,5,8,10}
parcial2 = {1,2,3,4,5,6,7,9,10}

ambos = parcial1 & parcial2
print("Aprobaron ambos:", ambos)

solo_p1 = parcial1 - parcial2
print("Solo parcial 1:", solo_p1)

solo_p2 = parcial2 - parcial1
print("Solo parcial 2:", solo_p2)

uno_o_ambos = parcial1 | parcial2
print("Aprobaron al menos uno:", uno_o_ambos)



# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

def buscar_producto(listado_productos):
    try:
        producto = input("Nombre de producto a consultar: ").strip()
        if producto == "":
            raise ValueError("Campo vacío, ingrese un producto")
        producto_lower = producto.lower()
        existe = producto_lower in listado_productos
        return existe, producto_lower
    except ValueError as e:
        print("Error:", e)
        return False, None

def consultar_stock(listado_productos, existe, producto):
    if existe:
        print(f"Producto: {producto} | Stock: {listado_productos[producto]} disponibles")
    else:
        print("Producto no encontrado")

def agregar_unidad(listado_productos, producto):
    listado_productos[producto] += 1
    print(f"Producto actualizado: {listado_productos[producto]} unidades disponibles")

def agregar_producto(productos, nuevo_producto):
    productos[nuevo_producto] = 0
    print(f"Producto {nuevo_producto} agregado con éxito")

productos={"leche":20, "yogurt":5, "dulce de leche":0, "crema":2, "postre":3}
while True:
    print("1. Consultar sock")
    print("2. Agregar unidad a stock")
    print("3. Agregar un nuevo productos al listado")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese la opción que desea realizar: "))
        match opcion:
            case 1:
                existe, producto = buscar_producto(productos)
                consultar_stock(productos, existe, producto)
            case 2:
                existe, producto = buscar_producto(productos)
                if existe:
                    agregar_unidad(productos, producto)
                else:
                    print("No se puede agregar unidad. Producto no existe.")
            case 3:
                nuevo_producto = input("Ingrese nombre del nuevo producto: ").strip().lower()
                if nuevo_producto in productos:
                    print("El producto ya existe.")
                else:
                    agregar_producto(productos, nuevo_producto)
            case 4:
                print("SALIDA DEL SISTEMA")
                break
            case _:
                print("Opción no válida")
    except ValueError:
        print("Error: Debe ingresar un número válido")


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:
# Permití consultar qué actividad hay en cierto día y hora.

def agregar_evento(dia, horario, evento, agenda):
    if evento.lower() in [e.lower() for e in agenda.keys()]:
        print("Evento ya programado, intente con otro nombre")
        return
    agenda[evento] = (dia, horario)
    print("Evento agregado con éxito")
def buscar_evento(dia, horario, agenda):
    hay_evento=False
    encontrado=""
    for e, h in agenda.items():
        if dia==h[0] and horario==h[1]:
            hay_evento=True
            encontrado=e
            break
    if not hay_evento:
        print("NO hay eventos para esa fecha y horario")
    else:
        print(f"Evento encontrado para el dia {dia} a las {horario}hs: {encontrado}")

agenda={"Concierto":(15, "20:30"), "Partido":(16, "21:00"),"turno medico":(16, "15:20")}
while True:
    try:
        print("SISTEMA DE AGENDA")
        print("Ingrese agregar si dese agendar algun evento")
        print("Ingrese buscar para buscar eventos agendados")
        print("Ingrese ver para observar la agenda completa")
        print("Ingrese salir para salir del sistema")
        opcion = input("Opcion seleccionada: ").lower()
        match opcion:
            case "agregar":
                nuevo_evento=input("Ingrese el nuevo evento: ")
                if nuevo_evento=="":
                    raise ValueError("Campo evento vacio, ingrese el nombre de nuevo evento")
                dia=int(input(f"Ingrese el dia que desea agendar {nuevo_evento}: "))
                if dia<=0:
                    raise ValueError("Ingrese un numero entero para el dia")
                horario=input(f"Ingrese el horario (hr:min) que desea agendar {nuevo_evento} dia {dia} a las : ")
                if horario=="":
                    raise ValueError("Campo horario vacio, ingrese un horario valido")
                agregar_evento(dia, horario, nuevo_evento, agenda)
            case "buscar":
                dia=int(input("Ingrese el dia que desea agendar: "))
                horario=input("Ingrese el horario que desea agendar: ")
                if dia<=0:
                    raise ValueError("Ingrese un numero entero para el dia")
                if horario=="":
                    raise ValueError("Campo horario vacio, ingrese un horario valido")
                buscar_evento(dia, horario, agenda)
            case "ver":
                print(agenda)
            case "salir":
                print("SALIDA DE AGRENDA")
                break
            case _:
                raise ValueError("Opcion ingresada invalida")
    except ValueError as e:
        print("Error: ", e)




# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
original={"Argentina":"Buenos Aires", "Chile":"Santiago"}
invertidos={}
for p,c in original.items():
    invertidos[c]=p

for capital, pais in invertidos.items():
    print(capital,pais)

print(invertidos)
