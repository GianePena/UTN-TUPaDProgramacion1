
import math
# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de- volver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe- dir los datos al usuario y llamar a esta función con los valores in- gresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra- dio como parámetro y devuelva el área del círculo. calcular_peri- metro_circulo(radio) que reciba el radio como parámetro y devuel- va el perímetro del círculo. Solicitar el radio al usuario y llamar am- bas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return math.pi*radio**2
def calcular_perimetro_circulo(radio):
    return 2*(math.pi*radio)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mos- trar el resultado usando esta función.
def segundos_a_horas(seg):
    una_hora=60*60
    return seg/una_hora
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la fun- ción.
def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n}x{i} = {n*i}")


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re- sultados de forma clara.
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def division(a,b):
    return a//b
def multiplicacion(a,b):
    return a*b
def operaciones_basicas(a,b):
    resultado=(suma(a,b), resta(a,b), division(a,b), multiplicacion(a,b))
    return resultado


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun- ción para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return peso/altura**2

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return (celsius*9/5)+32

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def sumar_numeros(num1, num2, num3):
    return num1+num2+num3
def calcular_promedio(num1, num2, num3):
    return sumar_numeros(num1, num2, num3)/3

