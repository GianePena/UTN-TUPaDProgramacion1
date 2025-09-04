import random
from statistics import mode, median, mean 

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad=int(input("Ingrese edad: ")) 

print("Edad: ", edad)
if edad<=0 or edad>110:
    print("Ingrese un valor valido")
elif edad>=18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota=int(input("Ingrese su nota: "))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par".

numero=int(input("Ingrese un numero entero: "))

if numero%2==0:
    print("Ha ingresado un numero par")
else: 
    print("Por favor, ingrese un número par")



# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:

edad_usuario=int(input("Ingrese su edad: "))

# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30
#Adulto/a: mayor o igual que 30
if edad_usuario<0 or edad_usuario>110:
    print("Ingrese un valor valido")
elif edad_usuario<12:
    print("Niño/a")
elif edad_usuario<18: 
    print("Adolescente")
elif edad_usuario<30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 

contraseña=input("Contraseña: ")
if len(contraseña)<8 or len(contraseña)>14:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else:
    print("Ha ingresado una contraseña correcta") 

#6)escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

lista_numerica= [random.randint(1, 100) for i in range(50)]

moda=mode(lista_numerica)
print("moda: ", moda)
mediana=median(lista_numerica)
print("mediana: ",mediana)
media=mean(lista_numerica)
print("media: ",media)

# Sesgo positivo= media>mediana and  mediana>moda
# sesgo negativo: media<mediana and mediana<moda
# sin sesgo: media=mediana=moda
if media>mediana and mediana>moda:
    print("Sesgo positivo")
elif media<mediana and mediana<moda:
    print("Sesgo negativo")
elif media==mediana==moda:
    print("No hay sesgo")
else:
    print("Otro caso de sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

texto=input("Igrese un texto(frase, parrafo, etc): ").lower()

#temine en vocal + signo ! --> imprimir el string+!
#si no termina con vocal --> imprime sin cambios
if texto[-1] in ["a", "e", "i", "o", "u"]:
    texto=texto+"!"
    print(texto)
else:
    print(texto)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas
# 2. Si quiere su nombre en minúsculas
# 3. Si quiere su nombre con la primera letra mayúscula
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada 

nombre=input("Ingrese su nombre: ")
numero_elegido=int(input("Ingrese un numero: 1)MAYUSCULA, 2)minuscula y 3)Nombre: "))
if len(nombre)!=0 :
    if numero_elegido==1:
        print(nombre.upper())
    elif numero_elegido==2:
        print(nombre.lower())
    elif numero_elegido==3:
        print(nombre.title())
    else:
        print("Ingrese un numero valido")
else:
    print("Error en lo datos ingresados: nombre incorrecto")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

escala_terremoto=float(input("Ingrese la magnitud de un terremoto: "))

if escala_terremoto<0 or escala_terremoto>11:
    print("Ingrese una escala real")
elif escala_terremoto<3:
    print("Clasificacion: Muy leve (imperceptible)")
elif escala_terremoto<4:
    print("Clasificacion: Leve (ligeramente perceptible)")
elif escala_terremoto<5:
    print("Clasificacion: Moderado (sentido por personas, pero generalmente no causa daños)")
elif escala_terremoto<6:
    print("Clasificacion: Fuerte (puede causar daños en estructuras débiles)")
elif escala_terremoto<7:
    print("Clasificacion: Muy fuerte (puede causar daños significativos)")
elif escala_terremoto>=7:
    print("Clasificacion: Extremo (puede causar graves daños a gran escala)")


#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.


hemisferio=input("Hemisferio en que se encuentra: S(sur) | N(norte): ").upper()
fecha_actual=input("Ingrese fecha actual en el siguiente formato (ej: 15 de mayo): nº de dia de mes actual: ")
fecha_cortada=fecha_actual.split("de")
dia_actual=int(fecha_cortada[0])
mes_actual=fecha_cortada[1].strip().lower()

if hemisferio=="N":
    if (mes_actual=="diciembre" and dia_actual>=21) or mes_actual in ["enero", "febrero"] or (mes_actual=="marzo"and dia_actual<=20):
        estacion="INVIERNO"

    elif (mes_actual=="marzo" and dia_actual>=21) or mes_actual in ["abril", "mayo"] or (mes_actual=="junio"and dia_actual<=20):
        estacion="PRIMAVERA"
        
    elif (mes_actual=="junio" and dia_actual>=21) or mes_actual in ["julio", "agosto"] or (mes_actual=="septiembre"and dia_actual<=20):
        estacion="VERANO"
    elif (mes_actual=="septiembre" and dia_actual>=21) or mes_actual in ["octubre", "noviembre"] or (mes_actual=="diciembre"and dia_actual<=20):
        estacion="OTOÑO"
elif hemisferio=="S":
    if (mes_actual=="diciembre" and dia_actual>=21) or mes_actual in ["enero", "febrero"] or (mes_actual=="marzo"and dia_actual<=20):
        estacion="VERANO"
    elif (mes_actual=="marzo" and dia_actual>=21) or mes_actual in ["abril", "mayo"] or (mes_actual=="junio"and dia_actual<=20):
        estacion="OTOÑO"
    elif (mes_actual=="junio" and dia_actual>=21) or mes_actual in ["julio", "agosto"] or (mes_actual=="septiembre"and dia_actual<=20):
        estacion="INVIERNO"
    elif (mes_actual=="septiembre" and dia_actual>=21) or mes_actual in ["octubre", "noviembre"] or (mes_actual=="diciembre"and dia_actual<=20):
        estacion="PRIMAVERA"
else:
    print("Hemisferio no válido. Ingrese N o S")

print(f"{fecha_actual} en el {'Sur' if (hemisferio=='S') else 'Norte'} es {estacion}")
