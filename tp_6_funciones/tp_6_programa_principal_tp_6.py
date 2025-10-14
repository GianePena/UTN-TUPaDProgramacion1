import trabajo_practico_6 as tp

#Actividad 1
tp.imprimir_hola_mundo()

#Actividad 2
nombre_del_usuario=input("Ingrese su nombre: ").capitalize()
print(tp.saludar_usuario(nombre_del_usuario))

#Actividad 3
nombre=input("Ingrese su nombre: ").capitalize()
apellido=input("Ingrese su apellido: ").capitalize()
edad=int(input("Ingrese edad: "))
lugar_de_residencia=input("Ingrese lugar de residencia: ").capitalize()
tp.informacion_personal(nombre, apellido, edad, lugar_de_residencia)

#Actividad 4
radio=float(input("Ingrese radio de un circulo: "))
print(f"El area de un circulo de radio= {radio} es {tp.calcular_area_circulo(radio):.2f} y su perimetro {tp.calcular_perimetro_circulo(radio):.2f}")

#Actividad 5
segundos=int(input("Ingrese una cantidad de segundos para transforlas en horas: "))
print(f"{segundos} es igual a {tp.segundos_a_horas(segundos):.2f}: horas")

#Actividad 6
numero=int(input("Ingrese un numero para obtener su tabla de multiplicar: "))
tp.tabla_multiplicar(numero)

#Actividad 7
numero_1=int(input("Ingrese un numero: "))
numero_2=int(input("Ingrese otro numero: "))
resultados=tp.operaciones_basicas(numero_1, numero_2)

print(f"Resultados de las operaciones basicas: {resultados}")
operaciones=["suma", "resta", "multiplicacion", "division"]
for o, total in zip(operaciones, resultados):
    print(f"Operacion {o} : {total}")

#Actividad 8
peso=float(input("Ingrese peso en kg: "))
altura=float(input("Ingrese su altura en metros: "))
print(f"El IMC es de: {tp.calcular_imc(peso, altura):.2f}")


#Actividad 9
grados_celsius=float(input("Ingrese grados celcisus: "))
print(f"{grados_celsius}°C son {tp.celsius_a_fahrenheit(grados_celsius)}°F")

#Actividad 10

numero_1=float(input("Ingrese un numero: "))
numero_2=float(input("Ingrese un numero: "))
numero_3=float(input("Ingrese un numero: "))

print(f"El promedio de: {numero_1}, {numero_2}, {numero_3} es de {tp.calcular_promedio(numero_1, numero_2, numero_3):.2f}")