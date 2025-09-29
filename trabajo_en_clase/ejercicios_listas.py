# Bingo
# 1. Generá un cartón 5x5 con números aleatorios entre 1 y 50, sin repetirse.
# 2. Mostrá el cartón al jugador en forma de matriz.
# 3. El programa debe sortear números al azar entre 1 y 50, uno por uno.
# 4. Cada vez que salga un número:
# o Si está en el cartón, reemplazarlo por un 0.
# o Si no está, avisar que no aparece.
# o Mostrar el cartón actualizado después de cada sorteo.
# 5. El juego termina cuando el cartón completo queda en 0 (¡Bingo!).
# Desafío extra: Validar cuando haya una línea completa (una fila llena de ceros) y mostrar el
# mensaje "¡Línea!".
# Sugerencias para resolverlo
# • Usar random.sample(range(1,51), 25) para obtener 25 números únicos y luego
# acomodarlos en la matriz.
# • Representar el cartón como una lista anidada de 5x5.
# • Recorrer la matriz con bucles anidados para marcar los números.
# • Usar un while que termine cuando todos los valores de la matriz sean 0.
import random

numeros=random.sample(range(1,51), 25)
carton=[numeros[i:i+5] for i in range(0,25,5)]
for fila in carton:
    print(fila)

numeros_salidos=[]

carton_lleno=False
while len(numeros_salidos)<50 and carton_lleno==False:
    numero_salido=random.randint(1, 50)
    if numero_salido in numeros_salidos:
        continue
    print("Numero sorteado: ", numero_salido)
    numeros_salidos.append(numero_salido)
    numero_encontrado=False
    #COLOCAR 0 EN EL NUMEOR EN EL CARTON
    for i in range(5):
        for j in range(5):
            if carton[i][j]==numero_salido:
                numero_encontrado=True
                carton[i][j]=0
    #MOSTRAR MENSAJE SI EL NUM ESTA O NO DENTRO DEL CARTON O NO
    if numero_encontrado:
        print(f"El numero {numero_salido} aparece en el carton")
    else:
        print(f"El numero {numero_salido} no aparece en el carton")
    #MOSTRAR ANTE CADA JUGADA LA EVOLUCION DEL CARTON
    for fila in carton:
        print(fila)
    #CORROBORAR QUE EL CARTON ESTE LLENO--> TODOS LOS CAMPOS 0
    carton_lleno=True
    for i in range(5):
        for j in range(5):
            if carton[i][j] != 0:
                carton_lleno = False
                break
        if carton_lleno==False:
            break
    #CICLO PARA MOSTRAR EL CARTON SI ESTA LLENO
    if carton_lleno:
        print("¡BINGO!")


