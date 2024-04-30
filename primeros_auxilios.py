# Función para evaluar si la persona responde a estímulos
def evaluar_estimulos():
    # Solicita al usuario que ingrese si la persona responde a estímulos
    respuesta = input("¿Responde a estímulos? (si/no): ")
    # Comprueba si la respuesta es "si"
    if respuesta.lower() == "si":
        # Si la respuesta es "si", muestra un mensaje
        print("Valorar la necesidad de llevarlo al hospital más cercano")
        return True  # Retorna True para indicar que se procedió correctamente
    elif respuesta.lower() == "no":
        # Si la respuesta es "no", llama a la función abrir_via_aerea()
        abrir_via_aerea()
    else:
        # Si la respuesta no es "si" ni "no", muestra un mensaje de error y llama a evaluar_estimulos() nuevamente
        print("Respuesta no válida. Por favor, responda 'si' o 'no'.")
        evaluar_estimulos()

# Función para abrir la vía aérea si la persona no responde a estímulos
def abrir_via_aerea():
    # Muestra un mensaje indicando que se abrirá la vía aérea
    print("Abrir la vía aérea.")
    # Llama a la función respira() para verificar si la persona respira
    respira()

# Función para verificar si la persona respira
def respira():
    # Solicita al usuario que ingrese si la persona respira
    respuesta = input("¿Respira? (si/no): ")
    if respuesta.lower() == "si":
        # Si la respuesta es "si", muestra un mensaje
        print("Permitirle posición de suficiente ventilación")
    elif respuesta.lower() == "no":
        # Si la respuesta es "no", llama a la función administrar_ventilaciones()
        administrar_ventilaciones()
    else:
        # Si la respuesta no es "si" ni "no", muestra un mensaje de error y llama a respira() nuevamente
        print("Respuesta no válida. Por favor, responda 'si' o 'no'.")
        respira()

# Función para administrar ventilaciones si la persona no responde y no respira
def administrar_ventilaciones():
    # Muestra un mensaje indicando que se administrarán ventilaciones y se llamará a la ambulancia
    print("Administrar 5 ventilaciones y llamar a la ambulancia.")
    # Llama a la función signos_vida() para verificar si hay signos de vida
    signos_vida()

# Función para verificar si hay signos de vida
def signos_vida():
    # Solicita al usuario que ingrese si hay signos de vida
    respuesta = input("¿Hay signos de vida? (si/no): ")
    if respuesta.lower() == "si":
        # Si la respuesta es "si", muestra un mensaje y espera a la ambulancia
        print("Reevaluar a la espera de la ambulancia.")
        llegada_ambulancia()
    elif respuesta.lower() == "no":
        # Si la respuesta es "no", muestra un mensaje y llama a llegada_ambulancia()
        print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
        llegada_ambulancia()
    else:
        # Si la respuesta no es "si" ni "no", muestra un mensaje de error y llama a signos_vida() nuevamente
        print("Respuesta no válida. Por favor, responda 'si' o 'no'.")
        signos_vida()

# Función para verificar si ha llegado la ambulancia
def llegada_ambulancia():
    # Solicita al usuario que ingrese si ha llegado la ambulancia
    respuesta = input("¿Ha llegado la ambulancia? (si/no): ")
    if respuesta.lower() == "si":
        # Si la respuesta es "si", muestra un mensaje y finaliza el programa
        print("Fin.")
    elif respuesta.lower() == "no":
        # Si la respuesta es "no", muestra un mensaje y vuelve a verificar los signos de vida
        print("Reevaluar signos de vida.")
        signos_vida()
    else:
        # Si la respuesta no es "si" ni "no", muestra un mensaje de error y llama a llegada_ambulancia() nuevamente
        print("Respuesta no válida. Por favor, responda 'si' o 'no'.")
        llegada_ambulancia()

# Inicio del programa
print("Iniciando evaluación de emergencia:")
evaluar_estimulos()