import datetime

#=========  VARIABLES   =========
print("\n=========  VARIABLES   =========\n")

# Problema 1
# Crea una variable que contenga el año actual y muéstralo por pantalla.
anio = datetime.date.today().year
print("El año actual es: ", anio)

# Problema 2
# Crea una variable con el valor de PI (3.14….) e imprímela.
pi = 3.14159265359
print("El valor de PI es: ", pi)

# Problema 3
# Crea una variable con el valor Verdadero (True) e imprímela.
flag_true = True
print("Valor Verdadero:", flag_true)

# Problema 4
# Crea una lista de 5 animales y muéstrala.
animales = ["perro","gato","loro","cocodrilo","pato"]
print("La lista de animales es: ", animales)

# Problema 5
# Crea una lista de 5 frutas y muestra solamente la última fruta.
frutas = ["melon","sandia","manzana","durazno","fresas"]
print("Última Fruta:", frutas[-1])

#=========  OPERACIONES   =========
print("\n=========  OPERACIONES   =========\n")

# Problema 1
# Pedir dos números por teclado e imprimir la suma de ambos
numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
print("La suma de ambos numeros es: ",numero1+numero2)

# Problema 2
# Pedir dos números por teclado e imprimir la media aritmética.
numero3 = float(input("Ingresa el primer numero: "))
numero4 = float(input("Ingresa el segundo numero: "))
print("La media aritmética de ambos numeros es: ",(numero3+numero4)/2)

# Problema 3
# Pedir peso y altura para calcular la masa corporal: mc = peso / altura^2.
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
print("Tu IMC es: ",peso / (altura*2))

# Problema 4
# Pedir radio para calcular la circunferencia de un círculo: C = 2*PI*r.
radio = float(input("Calcular circunferencia, cual es tu radio?\nIngresa el radio: "))
print("La circunferencia es: ",2*pi*radio)

# Problema 5
# Pedir un número en Celsius y convertir a Fahrenheit: F = 1.8*C + 32.
celsius = float(input("Ingresa la temperatura en C°: "))
fahrenheit = float(1.8 * celsius + 32)
print(f"La conversion a Fahrenheit es: {fahrenheit}")

#=========  CONDICIONES   =========
print("\n=========  CONDICIONES   =========\n")

# Problema 1
# Pedir dos números por teclado y decir cuál es mayor.
numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}.")
elif numero1 < numero2:
    print(f"{numero2} es mayor que {numero1}.")
else:
    print("Los números son iguales.")

# Problema 2
# Pedir un número por teclado y decir si es par o impar.
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"El {numero} es un número par.")
else:
    print(f"El {numero} es un número impar.")

# Problema 3
# Pedir tres números por teclado e imprimir el mayor de ellos solamente.
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

maximo = max(numero1, numero2, numero3)
print(f"El número mayor es: {maximo}")

# Problema 4
# Pedir un número por pantalla y decir si está entre 10 y 15 o no.
numero = float(input("Ingrese un número: "))

if 10 <= numero <= 15:
    print(f"{numero} está entre el 10 y 15.")
else:
    print(f"{numero} no está entre el 10 y 15.")

# Problema 5
# Pedir lado y alto de un cuadrilátero y decir si es cuadrado o rectángulo
lado = float(input("Ingrese la longitud del lado: "))
alto = float(input("Ingrese la altura: "))

if lado == alto:
    print("Es un cuadrado.")
else:
    print("Es un rectángulo.")

#=========  BUCLES   =========
print("\n=========  BUCLES   =========\n")

# Problema 1
# Imprimir los 25 primeros números naturales.
for i in range(1, 26): # recordando que comienza con el 0
    print(i)

# Problema 2
# Imprimir los números impares desde el 1 al 25, ambos inclusive.
for i in range(1, 26, 2):
    print(i)

# Problema 3
# Calcula e imprime la suma desde el 14 hasta el 38, ambos inclusive.
suma = 0
for i in range(14, 39):
    suma += i
    print(suma)

print(f"La suma final es: {suma}")

# Problema 4
# Calcula e imprime el producto de la serie 2x4x6x8x … x20.
multiplo = 1
for i in range(2, 21, 2):
    multiplo *= i

print(f"El producto total es: {multiplo}")

# Problema 5
# Calcula e imprime la suma de la serie 50+48+46+ … +20.
suma2 = 0
for i in range(50, 19, -2):
    suma2 += i
    print(suma2)

print(f"La suma final es: {suma2}")

#=========  FUNCIONES   =========
print("\n=========  FUNCIONES   =========\n")

# Problema 1
# Crea una función que reciba un número e imprima si es par o impar.
def par_o_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

# Llamada a la función
numero = int(input("Ingrese un número: "))
par_o_impar(numero)

# Problema 2
# Modifica la función anterior para que en vez de imprimirlo lo devuelva.
def par_o_impar2(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Llamada a la función
numero = int(input("Ingrese un número: "))
resultado = par_o_impar2(numero)
print(f"El número es {resultado}.")

# Problema 3
# Crea una función que reciba 2 números, devuelve el mayor e imprímelo.
def mayor_de_dos(numero1, numero2):
    maximo = max(numero1, numero2)
    print(f"El número mayor es: {maximo}")

# Llamada a la función
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
mayor_de_dos(numero1, numero2)

# Problema 4
# Crea una función que reciba 2 números y devuelva el resto de la división del 
# primer número dividido entre el segundo. Imprime el resultado.
def resto_de_division(numero1, numero2):
    resultado = numero1 % numero2
    print(f"El resto de la división es: {resultado}")

# Llamada a la función
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
resto_de_division(numero1, numero2)

# Problema 5
# Crea una función que reciba la base y la altura de un triángulo y devuelva su 
# área. A = ½ bh.
def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

# Llamada a la función
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = calcular_area_triangulo(base, altura)
print(f"El área del triángulo es: {area}")

# Problema 6
# Crea una función para calcular el IVA de un producto. Deberá recibir un precio y 
# devolver el precio IVA incluido
def calcular_iva(precio):
    iva = precio * 0.16  # Suponiendo un 16% de IVA
    precio_con_iva = precio + iva
    return precio_con_iva

# Llamada a la función
precio = float(input("Ingrese el precio del producto: "))
precio_final = calcular_iva(precio)
print(f"El precio con IVA incluido es: {precio_final}")

# Problema 7
# Crea una función que reciba un número, calcule su factorial, devuelva el 
# resultado e imprímelo.
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Llamada a la función
numero = int(input("Ingrese un número: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

# Problema 8
# Crea una función que reciba un número y calcule si es primo o no.
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Llamada a la función
numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")