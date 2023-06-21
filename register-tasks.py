# Definir una lista vacía para almacenar las tareas
tareas = []

# Función para agregar una nueva tarea al registro
def agregar_tarea():
    tarea = input("Ingrese una nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

# Función para mostrar todas las tareas del registro
def mostrar_tareas():
    if len(tareas) == 0:
        print("No hay tareas en el registro.")
    else:
        print("Tareas:")
        for i, tarea in enumerate(tareas):
            print(f"{i+1}. {tarea}")

# Función para eliminar una tarea del registro
def eliminar_tarea():
    mostrar_tareas()
    if len(tareas) == 0:
        return

    numero_tarea = int(input("Ingrese el número de la tarea a eliminar: "))
    if numero_tarea <= 0 or numero_tarea > len(tareas):
        print("Número de tarea inválido.")
    else:
        tarea_eliminada = tareas.pop(numero_tarea - 1)
        print(f"Tarea '{tarea_eliminada}' eliminada con éxito.")

# Menú principal del registro de tareas
def menu():
    while True:
        print("\n-- REGISTRO DE TAREAS --")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

# Ejecutar el programa
menu()
