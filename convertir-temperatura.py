def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Menú de opciones
while True:
    print("\n--- Convertidor de Temperaturas ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius}°C equivale a {fahrenheit}°F.")
    elif opcion == "2":
        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit}°F equivale a {celsius}°C.")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")
