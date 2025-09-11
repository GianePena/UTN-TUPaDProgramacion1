# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

multiplos_de_cuatro=list(range(4,101,4))
print(multiplos_de_cuatro)


# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

lista_elementos=[12,22,4,15,33]
print(lista_elementos[-2])


# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:

lista_vacia = []
lista_vacia.append("Amarillo")
lista_vacia.append("Rojo")
lista_vacia.append("Azul")
print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”
# ,respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números 
animales=["Perro", "Gato", "Pez", "Tortuga", "Ballena"]
animales[1]="loro"
animales[-1]="oso"

print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
''''
    remove(valor del elemento a eliminar)--> elimina de la lista el elemento que coincida con ese valor
    max(numeros)--> Devuelve el valor maximo de la lista, que seria 22 en este caso
    En el programa remove(max(numeros)) --> elimina 22 (numero maximo de la lista) de la lista numeros [8,15,3,22,7]
    El codigo imprime la lista modificada sin el 22 -->  [8,15,3,7]
'''

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
numeros=list(range(10,31,5))
print(numeros)
print(f"Primer numero de la lista: {numeros[0]}, Segundo numero de la lista: {numeros[1]}")


# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan","polo","suran","gol"]

autos = ["sedan","polo","suran","gol"]
print(autos)
autos[1]="fox"
autos[2]="306"
print(autos)


# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles=[]

for num in range(5,16,5):
    dobles.append(num*2)
print(dobles)

# 9) Dada la lista “compras”
# , cuyos elementos representan los productos comprados por
# diferentes clientes:
#compras = [["pan","leche"], ["arroz","fideos","salsa"],["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras=[["pan", "leche"],["arroz", "fideos", "salsa"], ["agua"]]
print(compras)
compras[2].append("jugo")
print(compras)
compras[1][1]="tallarines"
print(compras)
compras[0].remove("pan")
print(compras)

# 10) Elaborar una lista anidada llamada “lista anidada” que contenga los siguientes elementos:

lista_anidada=[15,True,[25.5,57.9,30.6],False]
print(lista_anidada)