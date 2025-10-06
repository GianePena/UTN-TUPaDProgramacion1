# #Actididad 1 : añadir frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}

# def añadir_fruta(nueva_fruta,precio, dict_frutas):
#     dict_frutas[nueva_fruta]=precio

# naranja=añadir_fruta("Naranja", 1200, precios_frutas)
# manzana=añadir_fruta("Manzana", 1500, precios_frutas)
# pera=añadir_fruta("Pera", 2300, precios_frutas)

# print(f"Listado de precios: {precios_frutas}")

# #Actividad 2: actualizar precios anteriores por los siguientes


# def actualizar_precios(dict_frutas, nombre, nuevo_precio):
#     dict_frutas[nombre.capitalize()]=nuevo_precio
#     return f"Precion {nombre} acutalizado"
# Banana = actualizar_precios(precios_frutas, "banana", 1330)
# Manzana =actualizar_precios(precios_frutas, "manzana", 1700)
# Melón = actualizar_precios(precios_frutas, "melón", 2800)

# print(f"Listado de precios actualizados: {precios_frutas}")

# #Actividad 3: crearun lista de frutas del punto anterior sin precios

# lista_frutas=list(precios_frutas.keys())
# print(lista_frutas)


#Actividad 4: Escribí un programa que permita almacenar y consultar números telefónicos
#Permitr cargar 5 contactos con su nombre y numero
#pedir un nombre y mostrar el numero

def añadir_contacto(nombre, numero, agenda):
    if nombre not in agenda.keys():
        agenda[nombre]=numero
        return True
    else:
        return False
agenda={}
contador=1
while contador<6:
    telefono=input("Ingrese numero telefonico que desea agendar: ")
    nombre=input("Nombre del contacto: ").capitalize()
    correcto= añadir_contacto(nombre, telefono, agenda)
    if correcto:
        print("Numero agendado")
        contador+=1
    else:
        print("Error: el nombre de contacto ya existe")
        continue

print(agenda)