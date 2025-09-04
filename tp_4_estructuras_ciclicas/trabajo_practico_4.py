# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(0, 101):
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
numero_ingresado=input("Ingrese un numero: ")
total_digitos=0
for digito in numero_ingresado:
    total_digitos+=1
print(f"El total de digitos de el numero ingresado {numero_ingresado} es de {total_digitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
valor1=int(input("Ingrese un primer numero: "))
valor2=int(input("Ingrese un segundo numero mayor al ingresado anteriormente: "))
total=0
while valor1>=valor2:
    print("Error al ingresar los valores: Reingrese los valores")
    valor1=int(input("Ingrese un primer numero: "))
    valor2=int(input("Ingrese un segundo numero mayor al ingresado anteriormente: "))

for valores_intermedios in range(valor1+1, valor2):
    total+=valores_intermedios
    print(valores_intermedios)
print(f"La suma de todos los valores conprendidos entre {valor1} y {valor2} es de {total}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero=int(input("Ingrese un numero: "))
total_numeros_ingresados=0
numeros=[]
while numero!=0:
    total_numeros_ingresados+=numero
    numeros.append(numero)
    numero=int(input("Ingrese otro un numero: "))
print(f"el total de las suma de los numeros ingresados ({numeros}) es de {total_numeros_ingresados}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_secreto=random.randint(0, 9)
numero_jugador=int(input("Adivine el numero, ingrese un numero del 0 al 9: "))
contador=1
while numero_jugador!=numero_secreto:
    contador+=1
    print("Incorrecto: ")
    numero_jugador=int(input("Adivine el numero, ingrese un numero del 0 al 9: "))

print(f"Felicitaciones!!! Acertaste en numero secreto es {numero_secreto} - Intentos: {contador}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for numero in range(100, -1, -1):
    if numero%2==0:
        print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero_ingresado=int(input("Ingrese un numero: "))
total=0
while numero_ingresado<0:
    print("Error ingrese un numero entero positivo")
    numero_ingresado=int(input("Ingrese un numero: "))
for n in range(0, numero_ingresado):
    total+=n
print(f"Las suma entre todos los numero comprendidos entre 0 y {numero_ingresado} es de {total}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numeros_pares=[]
numeros_impares=[]
cantidad_numeros_positivos=0
cantidad_numeros_negativos=0
for numero in range(100):
    numero_ingresado=int(input("Ingrese numero: "))
    if numero_ingresado%2==0:
        numeros_pares.append(numero_ingresado)
    else: 
        numeros_impares.append(numero_ingresado)

    if  numero_ingresado<0:
        cantidad_numeros_negativos+=1 
    else:
        cantidad_numeros_positivos+=1


print(f"Cantidad de numero positivos = {cantidad_numeros_positivos}, cantidad de numero negativos = {cantidad_numeros_negativos}")
print(f"Numeros pares: {numeros_pares}, Numeros impares:{numeros_impares}")
print(f"Cantidad de numero pares= {len(numeros_pares)}, Cantidad de numero impares= {len(numeros_impares)}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

lista=[]
total=0
media=0

for i in range(100):
    numero=int(input("Ingrese un numero: "))
    total+=numero
    lista.append(numero)
    media=total/(i+1)

print(f"La media de los 100 numeros ingresados es de {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un numero: ")
numero_invertido = ""
for i in range(len(numero) - 1, -1, -1):
    numero_invertido += numero[i]

print(f"El inverso de {numero} es {numero_invertido}")