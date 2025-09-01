import random #ejrcicio pridra, papepl o tijera



corrimiento=int(input("Ingrese corrimiento: "))


abecedario=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#Pedir 5 mensajes y cifrarlos segun el numero ingresado
for oficial in range(5):
    jugador=1
    mensaje_encriptado=""
    mensaje_original=input("Ingrese mensaje: ").upper()
    for letra in mensaje_original:
        if letra in abecedario:
            index = abecedario.index(letra)
            nuevo_index = (index + corrimiento) % len(abecedario)
            mensaje_encriptado += abecedario[nuevo_index]
        else:
            mensaje_encriptado+=letra
    print(f"Mensaje jugador {jugador}: {mensaje_encriptado}")
    jugador+1





#PIEDRA, PAPEL O TIJERA --> con bucle while
opciones={
    1:"Piedra",
    2:"Papel",
    3:"Tijera"
}


ganado=False

while ganado==False:
    eleccion=input("Ingrese: piedra, papel o tijera: ").upper()
    if eleccion not in ["PIEDRA", "PAPEL", "TIJERA"]: 
        print("Error: Ingrese piedra, papel o tijera")
        continue
    secreto=opciones[random.randint(1,3)].upper()
    if (secreto=="PIEDRA" and eleccion=="PAPEL") or (secreto=="TIJERA" and eleccion=="PIEDRA") or (secreto=="PAPEL"and eleccion=="TIJERA"):
        print(f"Ganasta: {eleccion} gana a la {secreto}")
        ganado=True
    elif secreto==eleccion:
        print("Empate: ")
    else:
        ganado=False
        print("Perdiste: Otro intento")




