import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Solicitar al usuario la longitud de la contraseña deseada
longitud = int(input("Ingresa la longitud deseada para la contraseña: "))

# Generar y mostrar la contraseña
contraseña_generada = generar_contraseña(longitud)
print("Contraseña generada:", contraseña_generada)
