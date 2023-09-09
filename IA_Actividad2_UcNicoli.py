    # autor: Manuel Uc Nicoli

    # PROBLEMA 1 -------------
    # Un obrero necesita calcular su salario semanal, el cual se obtiene de la 
    # siguiente manera: Si trabaja 40 horas o menos se le paga un salario de $16 
    # por hora, si trabaja más de 40 horas se le paga un salario de $16 por cada 
    # una de las primeras 40 horas y un salario de $20 por cada hora extra.
    # ==================================================================
def problema_1():
    # Definir una función llamada calcular_salario_semanal que toma un argumento: horas_trabajadas
    def calcular_salario_semanal(horas_trabajadas):
        # Establecer el salario base por hora en $16
        salario_base = 16
        # Establecer el número máximo de horas normales las cuales son 40 hrs
        horas_normales = 40
        # Establecer el salario por hora extra en $20
        salario_extra = 20

        # Comprobar si las horas trabajadas son iguales o menores a 40 hrs
        if horas_trabajadas <= horas_normales:
            # Calcular el salario multiplicando las horas trabajadas por el salario base
            salario_total = horas_trabajadas * salario_base
        else:
            # Si las horas trabajadas son más de 40, calcular las horas extras
            horas_extras = horas_trabajadas - horas_normales
            # Calcular el salario sumando el salario por horas normales y el salario por horas extras
            salario_total = (horas_normales * salario_base) + (horas_extras * salario_extra)

        # Devolver el salario total calculado
        return salario_total

    # Solicitar al usuario que ingrese la cantidad de horas trabajadas esta semana y almacenarla en la variable horas_trabajadas
    horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas esta semana: "))

    # Calcular el salario llamando a la función calcular_salario_semanal con las horas trabajadas ingresadas y almacenar el resultado en la variable salario
    salario = calcular_salario_semanal(horas_trabajadas)

    # Mostrar el salario semanal calculado formateado con dos decimales (flotante)
    print(f"El salario semanal es: ${salario:.2f}")

    # ==================================================================

    # PROBLEMA 2 -------------
    # En un supermercado se hace una promoción mediante la cual el cliente 
    # obtiene un descuento, el descuento depende de un número de dos digito que 
    # escoja al lazar. Si el número elegido es menor que 74 el descuento es el 15% 
    # sobre el total de compras si es mayor o igual a 74 el descuento es de 20%.
    # Calcula e imprimir el dinero que se le descuenta a un cliente, así como el 
    # momento a pagar.
    # ==================================================================
def problema_2():
    # Solicitar al cliente que ingrese el número de dos dígitos al azar
    numero_elegido = int(input("Ingrese un número de dos dígitos: "))

    # Solicitar al cliente que ingrese el monto total de sus compras
    monto_compras = float(input("Ingrese el monto total de compras: "))

    # Definir una variable para almacenar el porcentaje de descuento inicial que sera por el momento = 0
    porcentaje_descuento = 0

    # Comprobar si el número elegido es menor que 74
    if numero_elegido < 74:
        # Si es menor, se establece el porcentaje de descuento en un 15%
        porcentaje_descuento = 15
    else:
        # Si es mayor o igual a 74, se establece el porcentaje de descuento en un 20%
        porcentaje_descuento = 20

    # Calcular el descuento en función del porcentaje de su descuento
    descuento = (porcentaje_descuento / 100) * monto_compras

    # Calcular el monto a pagar restando el descuento ganado al monto de su total de compras a realizar
    monto_a_pagar = monto_compras - descuento

    # Mostrar el dinero que se le descuenta al cliente al final
    print(f"El descuento aplicado es de: ${descuento:.2f} ")

    # Mostrar el monto a pagar después del descuento realizado
    print(f"Monto total a pagar es de: ${monto_a_pagar:.2f} ")

    # ==================================================================

    # PROBLEMA 3 -------------
    # Realizar un programa que lea un número e imprima el número es positivo, regulativo o neutro
    # ==================================================================
def problema_3():
    # Solicitar al usuario que ingrese un número random
    numero = float(input("Ingrese un número: "))

    # Comprobar si el número es positivo
    if numero > 0:
        # Si es positivo, imprimir que el número es positivo
        print("El número es positivo.")
    # Comprobar si el número es negativo
    elif numero < 0:
        # Si es negativo, imprimir que el número es negativo
        print("El número es negativo.")
    # Si no es ni positivo ni negativo, entonces es neutro (igual a cero)
    else:
        # Imprimir que el número es neutro
        print("El número es neutro (igual a cero).")

    # ==================================================================

    # PROBLEMA 4 -------------
    # Desarrolle un programa que permita leer un valor cualquiera N y escriba si
    # dicho número es par o impar.
    # ==================================================================
def problema_4():
    # Solicitar al usuario que ingrese un número
    numero = float(input("Ingrese un número: "))

    # Comprobar si el número es divisible por 2 (par)
    if numero % 2 == 0:
        # Si el residuo de la división es 0, el número es par
        print(f"El número {numero} es par.")
    else:
        # Si el residuo de la división no es 0, el número es impar
        print(f"El número {numero} es impar.")

    # ==================================================================

    # PROBLEMA 5 -------------
    # Elabora un programa que solicite 3 números y que permita al usuario
    # seleccionar la operación que desea que realice con los dígitos, entre los
    # cuales se encuentra: suma, resta, multiplicación y división. 
    # ==================================================================
def problema_5():
    # Definir una función para realizar las operaciones y que se cicle hasta que de con
    # una opcion que sea valida para el sistema o hasta salir
    def realizar_operacion(numero1, numero2, numero3, opcion):
        if opcion == 1: # Suma
            resultado = numero1 + numero2 + numero3
            print(f"Resultado de la suma es: {resultado}")
        elif opcion == 2: # Resta
            resultado = numero1 - numero2 - numero3
            print(f"Resultado de la resta es: {resultado}")
        elif opcion == 3: # Multiplicacion
            resultado = numero1 * numero2 * numero3
            print(f"Resultado de la multiplicación es: {resultado}")
        elif opcion == 4: # Division y comprobacion
            if numero2 == 0 or numero3 == 0:
                print("No se puede realizar la división debido a un divisor igual a cero!.")
            else:
                resultado = numero1 / numero2 / numero3
                print(f"Resultado de la división es: {resultado}")
        else:
            print("¡Opción no válida. Por favor, seleccione una operación válida!")

    # Solicitar al usuario que ingrese los tres números
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    numero3 = float(input("Ingrese el tercer número: "))

    while True:
        # Mostrar las opciones de operaciones disponibles
        print("Selecciones una opcion de la lista")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        # Solicitar al usuario que elija una opcion
        opcion = int(input())

        # Salir del programa si se selecciona la opción 5
        if opcion == 5: # Finaliza el problema y continua con el otro bloque de lo contrario llama la funcion
            print("¡Hasta luego!")
            break

        # Llamar a la función para realizar la operación
        realizar_operacion(numero1, numero2, numero3, opcion)

    # ==================================================================

    # PROBLEMA 6 -------------
    # Hallar Aumento al Sueldo de un empleado; si el sueldo es mayor a $500.000
    # su aumento será del 12%, pero si su sueldo es menor el aumento será del 15%
    # ==================================================================
def problema_6():
    # Solicitar al usuario que ingrese el sueldo del empleado
    sueldo = float(input("Ingrese el sueldo del empleado: "))

    # Comprobar si el sueldo es mayor a $500,000
    if sueldo > 500000:
        # Calcular el aumento para el sueldo mayor
        aumento = .12 * sueldo
        nuevo_sueldo = sueldo + aumento
        print("El aumento de sueldo es del 12%")
    else:
        # Calcular el aumento para sueldo menor o igual a $500,000
        # Calcular el aumento para el menor
        aumento = .15 * sueldo
        nuevo_sueldo = sueldo + aumento
        print("El aumento de sueldo es del 15%")

    # Mostrar el monto del aumento y el nuevo sueldo en dos decimales
    print(f"Monto del aumento: ${aumento:.2f}")
    print(f"Nuevo sueldo: ${nuevo_sueldo:.2f}")

# ==================================================================

# Menú principal de los problemas
while True:
    print("\nMenú:")
    print("1. Calcular salario semanal de un obrero")
    print("2. Calcular descuento en un supermercado")
    print("3. Determinar si un número es positivo, negativo o neutro")
    print("4. Determinar si un número es par o impar")
    print("5. Realizar operaciones matemáticas con tres números")
    print("6. Aumento de sueldo de un empleado")
    print("7. Salir")

    opcion_menu = int(input())

    if opcion_menu == 1:
        problema_1()
    elif opcion_menu == 2:
        problema_2()
    elif opcion_menu == 3:
        problema_3()
    elif opcion_menu == 4:
        problema_4()
    elif opcion_menu == 5:
        problema_5()
    elif opcion_menu == 6:
        problema_6()   
    elif opcion_menu == 7:
        print("¡Hasta luego :D!")
        break
    else:
        print("¡ Opción no válida. Por favor, seleccione una opción válida :( !")
