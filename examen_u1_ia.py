#author: Uc Nicoli

# Teniendo en cuenta que la clave es “@finalPrograma”, elaborar un programa que nos pida una clave. 
# Solo tenemos 3 intentos para acertar, si fallamos los 3 intentos nos mostrara un mensaje indicándonos que hemos agotado esos 3 intentos. 
# Si acertamos la clave deberá de mostrar un mensaje de Bienvenida y deberá de mostrar en un menú opciones 
#1. Promedio (Calcular el promedio de 5 calificaciones) , 2. Ejecutar Aplicaciones (Word, Excel, PowerPoint), 
# 3. Detector de vocal o consonante (introducir una letra y mostrar si es vocal o consonante).

# Autor: Uc Nicoli

#uso de librerias
import subprocess
import getpass

# Definir cual es la clave para que podamos acceder al programa
clave_correcta = "@finalPrograma"

# Iniciar una variable para el contador de los intentos que hara el programa.
intentos = 0

# Pedimos la contraseña y se ciclara si la clave es incorrecta en el while hasta que ocurra el 3er intento
while intentos < 3:
    # lib para que no se vea la contraseña que se esta tecleando
    clave = getpass.getpass("Bienvenido!\nPor favor, introduzca la contraseña: ") 

    if clave == clave_correcta:
        print("=== Contraseña Correcta! ===\n\n=====    BIENVENIDO!    =====")
        break  # Salimos del bucle si la clave es correcta continuando con el menú
    else:
        intentos += 1
        print("Clave incorrecta!\nIntentenlo de nuevo!\n\n      Intento {} de 3!".format(intentos))

# Determina si agotamos los 3 intentos y sale del programa.
if intentos == 3:
    print("Has agotado tus 3 intentos. Programa bloqueado.")
else:
    while True:
        print("\nSeleccione alguna de las siguientes opciones: ")
        print("1. Promedio de 5 calificaciones)")
        print("2. Ejecutar Word, Excel y PowerPoint")
        print("3. Detectar una vocal o consonante")
        print("4. Salir del programa")
        opcion = input()

        if opcion == "1":
            # Calculo de promedio
            calificaciones = []
            for i in range(5):
                calificacion = float(input("Ingrese la {}° calificacion: ".format(i + 1)))
                calificaciones.append(calificacion)
            promedio = sum(calificaciones) / len(calificaciones)
            print("El promedio es: {:.2f}".format(promedio))

        elif opcion == "2":
               # Ejecución de las aplicaciones en segundo plano utilizando el shell
                try:
                    subprocess.Popen(["start", "winword.exe"], shell=True)
                    subprocess.Popen(["start", "excel.exe"], shell=True)
                    subprocess.Popen(["start", "powerpnt.exe"], shell=True)
                except Exception as e:
                    print("Error al abrir las aplicaciones:", str(e))
                    
        elif opcion == "3":
            # Detector si es que es una vocal o consonante
            letra = input("Ingrese una letra: ").lower()
            if letra.isalpha() and len(letra) == 1:
                if letra in "aeiou":
                    print("La letra '{}' es una vocal.".format(letra))
                else:
                    print("La letra '{}' es una consonante.".format(letra))
            else:
                print("Por favor, ingrese una única letra válida!") # Por si se introduce mas de 1 una letar o se introduzca un numero

        elif opcion == "4":
            # Salir del programa
            print("\n¡Hasta luego!")
            break

        else:
            #finaliza el programa si es que la persona se equivoco en introducir la contraseña mas de 3 veces al sistema
            print("\nTu opcion no es valida!\nPor favor, seleccione una opción válida del menú.")
