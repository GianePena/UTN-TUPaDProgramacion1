# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola, Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. --> “Hola Marcos!”

nombre_usuario=input("Ingrese su nombre: ")
print(f"Hola {nombre_usuario}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. --> “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”


nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
lugar_de_residencia=input("Ingrese lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {lugar_de_residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio=input("Ingrese radio de un circulo: ")
PI=3.14
area=PI*(float(radio)**2)
print(f"El area de un circulo de radio {radio} es {area}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos= int(input("Cantidad de segundos: "))
horas=segundos/3600
print(f"{segundos} segundos  son {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

multiplicando=int(input("Ingrese un numero: "))

print(f"{multiplicando}x1={multiplicando*1}")
print(f"{multiplicando}x2={multiplicando*2}")
print(f"{multiplicando}x3={multiplicando*3}")
print(f"{multiplicando}x4={multiplicando*4}")
print(f"{multiplicando}x5={multiplicando*5}")
print(f"{multiplicando}x6={multiplicando*6}")
print(f"{multiplicando}x7={multiplicando*7}")
print(f"{multiplicando}x8={multiplicando*8}")
print(f"{multiplicando}x9={multiplicando*9}")
print(f"{multiplicando}x9={multiplicando*10}")


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_entero1=float(input("Ingrese un numero entero distinto a 0 "))
numero_entero2=float(input("Ingrese otro numero entero distinto a 0 "))

suma=numero_entero1+numero_entero2
resta=numero_entero1-numero_entero2
multiplicacion=numero_entero1*numero_entero2
division=numero_entero1/numero_entero2
print(f"Suma: {numero_entero1} + {numero_entero2}= {suma}")
print(f"Resta: {numero_entero1} - {numero_entero2}= {resta}")
print(f"Multiplicacion: {numero_entero1} x {numero_entero2}= {multiplicacion}")
print(f"Division: {numero_entero1} / {numero_entero2}= {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. 

altura_paciente=float(input("Altura del paciente en metros: "))
peso_paciente=float(input("Peso del paciente en kg: "))
IMC=peso_paciente/(altura_paciente**2)
print("IMC: ", IMC)

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

temperatura_celcius=float(input("Ingrese temperatura actual en grados celcius: "))
FAHRENHEIT=(9/5*temperatura_celcius)+32
print(f"{temperatura_celcius}° Celcius es igual a {FAHRENHEIT} Fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

print("Ingrese 3 numeros")
numero1=float(input("Numero 1: "))
numero2=float(input("Numero 2: "))
numero3=float(input("Numero 3: "))
promedio=(numero1+numero2+numero3)/3
print(f"El promedio de {numero1}, {numero2} y {numero3} es de {promedio}")