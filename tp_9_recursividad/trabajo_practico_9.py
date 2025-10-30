
# #Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def ejercicio1():
    try:
        numero = int(input("Ingrese un numero entero positivo: "))
        if numero < 1:
            print("El número debe ser mayor o igual a 1")
            return
        for i in range(1, numero + 1):
            print(f"Factorial de {i} = {factorial(i)}")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")


ejercicio1()

# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def ejercicio2():
    try:
        posicion = int(input("Ingrese la posición hasta donde mostrar la serie: "))
        if posicion < 0:
            print("La posición debe ser mayor o igual a 0")
            return
        print("Fibonacci: ")
        for i in range(posicion + 1):
            print(fibonacci(i), end=" ")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

ejercicio2()

#  Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
# . Prueba esta función en un algoritmo general

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def ejercicio3():
    try:
        base = int(input("Ingrese la base: "))
        exponente = int(input("Ingrese un exponente entero no negativo: "))
        
        if exponente < 0:
            print("El exponente debe ser mayor o igual a 0")
            return
        
        resultado = potencia(base, exponente)
        print(f"{base}^{exponente} = {resultado}")
    except ValueError:
        print("Error: Debe ingresar números enteros válidos")


ejercicio3()

# Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    return decimal_a_binario(n // 2) + str(n % 2)

def ejercicio4():
    try:
        numero = int(input("Ingrese un numero decimal positivo: "))
        if numero < 0:
            print("El numero debe ser positivo")
            return
        
        if numero == 0:
            binario = "0"
        else:
            binario = decimal_a_binario(numero)
        
        print(f"{numero} en binario es {binario}")
    except ValueError:
        print("Error: Debe ingresar un numero entero valido")


ejercicio4()

# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]: #ver si el ultimo y elprimer caracter son iguales
        return False
    return es_palindromo(palabra[1:-1])

def ejercicio5():
    palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
    if es_palindromo(palabra):
        print(f"{palabra} ES un palindromo")
    else:
        print(f"{palabra} NO es un palindromo")

ejercicio5()

# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

def ejercicio6():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("El número debe ser positivo")
            return
        
        resultado = suma_digitos(numero)
        print(f"La suma de los digitos de {numero} es: {resultado}")
    except ValueError:
        print("Error: Debe ingresar un numero entero valido")

ejercicio6()

# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def ejercicio7():
    try:
        nivel_base = int(input("Ingrese el número de bloques en el nivel más bajo: "))
        if nivel_base < 1:
            print("El número debe ser mayor o igual a 1")
            return
        
        total = contar_bloques(nivel_base)
        print(f"\nTotal de bloques en la pirámide: {total}")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

ejercicio7()

# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10 # para obtener el último dígito
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

def ejercicio8():
    try:
        numero = int(input("Ingrese un numero entero positivo: "))
        digito = int(input("Ingrese el digito a buscar (0-9): "))
        
        if numero < 0:
            print("El numero debe ser positivo")
            return
        
        if digito < 0 or digito > 9:
            print("El digito debe estar entre 0 y 9")
            return
        
        cantidad = contar_digito(numero, digito)
        print(f"El digito {digito} aparece {cantidad} veces en {numero}")
    except ValueError:
        print("Error: Debe ingresar numeros enteros validos")

ejercicio8()