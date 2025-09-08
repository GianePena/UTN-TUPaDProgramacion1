
#FOR

#Desarrollar un algoritmo que permita ingresar un número entero positivo. La computadora debe mostrar la sucesión de número pares desde el numero ingresado hasta el cero, en una sola línea → 15  →   14 12 10 8 6 4 2 0
numero_ingresao=int(input("Ingrese un numero: "))

for i in range(numero_ingresao, 0-1, -1):
    if i%2==0:
        print(i, end=" ")
    print()



# Desarrolla un algoritmo que permita un número entero entre 1 y 10. La computadora debe mostrar la tabla de multiplicar del número ingresado. → tabla del 7 
numero_ingresao=int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(f"{numero_ingresao} x {i} = {numero_ingresao*i}")


#Desarrolla un algoritmo que permita ingresar una cantidad de personas. la computadora debe pedir edad de cada una y finalmente mostrar el porcentaje de personas que es mayor de edad

total_personas=6
total_personas_mayores=0

for personas in range(1, 6+1):
    edad=int(input("Edad: "))
    if edad>=18:
        total_personas_mayores+=1

porcentade_de_mayores=(total_personas_mayores*100)/total_personas
print(f"El total de personas mayores de {porcentade_de_mayores}%")


#WHILE
#Desarrolla un algoritmo que permite ingresar el nombre y edad (por separado) de diferentes personas. La carga termina cuando en el nombre de la proxima persona se ingresa un *.
# La computadora debe mostrar como se llama la persona más joven


nombre_del_menor=""
menor_edad=1000
while True:
    nombre=input("Nombre: ")
    if nombre=="*":
        break
    edad=int(input("Edad: "))
    if edad<menor_edad:
        menor_edad=edad
        nombre_del_menor=nombre

print(f"La persona mas joven es {nombre_del_menor} con {menor_edad} años")


