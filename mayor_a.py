import sys

# Diccionario de balances de la empresa
ventas = {
    "Enero": 15000, "Febrero": 22000, "Marzo": 12000, "Abril": 17000,
    "Mayo": 81000, "Junio": 13000, "Julio": 21000, "Agosto": 41200,
    "Septiembre": 25000, "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000,
}

# Obtener el umbral de ventas desde la línea de comandos
umbral = int(sys.argv[1])

# Filtrar las ventas que superan el umbral dado utilizando una comprensión de diccionario
ventas_filtradas = {mes: monto for mes, monto in ventas.items() if monto > umbral}

# Imprimir el informe resumido
print(ventas_filtradas)