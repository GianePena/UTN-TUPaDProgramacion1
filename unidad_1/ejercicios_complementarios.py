
#1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección.

numero_1=15
print(f"Nuemero entero {numero_1}")

# 2. No borres la variable número uno y crea una variable llamada "numero2" asignándole
# un número decimal de tu elección.

numero_2=10.5
print(f"Nuemero decimal {numero_2}")

# 3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".

suma=numero_1+numero_2
print(f"Suma: {numero_1} + {numero_2} = {suma}")

# 4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para
# multiplicación y otra para división. Imprime estas variables.

resta=numero_1-numero_2
multiplicacion=numero_1*numero_2
division=numero_1/numero_2
print(f"Resta: {numero_1} - {numero_2} = {resta}")
print(f"Multiplicacion: {numero_1} x {numero_2} = {multiplicacion}")
print(f"Division: {numero_1} / {numero_2} = {division}")

# 5. Crea una variable llamada "nombre" y asígnale tu nombre como valor.

nombre="Gianella"
print(f"Nombre: {nombre}")

# 6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el
# precio de un artículo ficticio.

precio=1800
print(f"Precio inicial ${precio}")

# 7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
# un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le
# quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al
# 100% y el valor 0 al 0%.

descuento=0.20
print(f"Descuento %{0.20*100}")

# 8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y
# almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que
# aplicar la lógica de matemáticas.

precio_final=precio-(precio*descuento)
print(f"Precio final con descuento ${precio_final}")

# 9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu
# elección. Qué sea un string.

cadena="Algoritmo es un conjunto de pasos ordenados y finitos que permiten resolver un problema"

# 10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas
# a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de
# Python.

longitud=len(cadena)
print(f"Longitud de cadena: {longitud}")

# 11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
# conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo
# mismo.

precio_2=300.50
precio_entero=int(precio_2)
print(f"Precio entero: {precio_entero}")

# 12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
# en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
# espacio entre medio. Puedes usar libremente la forma de concatenación que quieras.

nombre="Gianella"
apellido="Peña"
nombre_completo=nombre + " " + apellido
print(nombre_completo)

# 13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.

edad=23
incremento=edad+5
print(f"Incremento 5 la edad: {incremento}")
decremento=edad-10
print(f"Decremento 10 la edad: {decremento}")

# 14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
# centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3.

altura=1.78
mutiplicar_altura=altura*4
print(f"Altura multiplicada por 4: {altura} x 4 = {mutiplicar_altura}")
dividir_altura=altura/3
print(f"Altura dividida en 3: {altura} / 3 = {dividir_altura}")

# 15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después
# transfórmalo todo en minúsculas con algún método o función de Python.

nombre_en_mayuscula=nombre.upper()
nombre_en_minuscula=nombre.lower()
print(f"Nombre en mayuscula: {nombre_en_mayuscula}")
print(f"Nombre en minuscula: {nombre_en_minuscula}")

# 16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
# para que se transforme todo en minúsculas excepto la primera letra.

nombre_primera_letra_mayuscula=nombre.capitalize()
print(nombre_primera_letra_mayuscula)