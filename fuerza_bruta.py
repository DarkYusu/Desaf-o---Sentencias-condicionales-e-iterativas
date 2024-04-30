# Importamos el alfabeto en minúsculas desde la biblioteca string
from string import ascii_lowercase

# Definimos una función llamada fuerza_bruta que recibe la contraseña como argumento
def fuerza_bruta(password):
    # Inicializamos el contador de intentos
    intentos = 0
    # Iteramos sobre todas las letras en el alfabeto
    for letra in ascii_lowercase:
        # Incrementamos el contador de intentos en 1 en cada iteración
        intentos += 1
        # Si la letra actual es igual a la primera letra de la contraseña, terminamos el bucle
        if letra == password[0]:
            break
    # Iteramos sobre las letras restantes en la contraseña (a partir de la segunda letra)
    for letra in password[1:]:
        # Iteramos sobre todas las letras en el alfabeto
        for i in ascii_lowercase:
            # Incrementamos el contador de intentos en 1 en cada iteración
            intentos += 1
            # Si la letra actual es igual a la letra de la contraseña actual, terminamos el bucle
            if i == letra:
                break
    # Retornamos el número total de intentos
    return intentos

# Solicitamos al usuario que ingrese la contraseña y la convertimos a minúsculas
password = input("Ingrese la contraseña: ").lower()
# Llamamos a la función fuerza_bruta para determinar el número de intentos necesarios
intentos = fuerza_bruta(password)
# Imprimimos el resultado
print(f"La contraseña fue forzada en {intentos} intentos")