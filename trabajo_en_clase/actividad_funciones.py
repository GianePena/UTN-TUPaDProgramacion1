import random

palabras_secretas = ["azul", "amarillo", "rojo", "violeta", "magenta", "blanco", "gris", "negro"]


def seleccionar_palabra(palabras):
    aleatorio = random.randint(0, len(palabras) - 1)
    return palabras[aleatorio]

def buscar_letra(letra, palabra):
    return letra.lower() in palabra.lower()

def mostrar_palabra_oculta(palabra, letras_acertadas):
    resultado = ""  
    for l in palabra:
        if l.lower() in letras_acertadas:
            resultado += l
        else:
            resultado += "_"
    return resultado

while True:
    print("---- MENU: INGRESE UNA OPCION ----")
    print("1. Jugar")
    print("2. Salir")
    opcion = input("Desea jugar: ")
    if not opcion.isnumeric():
        print("Error: Ingrese una opcion numerica")
        continue
    opcion = int(opcion)
    match opcion:
        case 1:
            palabra_secreta = seleccionar_palabra(palabras_secretas)
            intentos = 6
            letras_ingresadas = []
            letras_acertadas = []
            while intentos > 0:
                adivinar = mostrar_palabra_oculta(palabra_secreta, letras_acertadas)
                print(f"Palabra: {adivinar}")
                print(f"Intentos restantes: {intentos}")
                print(f"Letras ingresadas: {letras_ingresadas}")
                if "_" not in adivinar:
                    print("¡Ganaste! La palabra era:", palabra_secreta)
                    break
                letra_ingresada = input("Ingrese una letra: ").lower()
                if letra_ingresada in letras_ingresadas:
                    print("Ya ingresaste esa letra, probá con otra.")
                    continue
                letras_ingresadas.append(letra_ingresada)
                if buscar_letra(letra_ingresada, palabra_secreta):
                    letras_acertadas.append(letra_ingresada)
                    print("Adivinaste una letra correctamente.")
                else:
                    intentos -= 1
                    print("Letra no encontrada.")
            if intentos == 0:
                print("Te quedaste sin intentos. La palabra era:", palabra_secreta)
        case 2:
            print("Gracias por jugar")
            break
        case _:
            print("Error: Ingrese una opcion valida. 1 o 2")
