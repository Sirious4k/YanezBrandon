import random
import math
import statistics
import csv
from functools import reduce

# Variables
# Diccionario de usuarios
usuarios = {
    "Juan": {},
    "Leo": {},
    "Maria": {},
    "Jorge": {},
    "Brandon": {},
    "Ana": {},
    "Pablo": {},
    "Ron": {},
    "Luis": {},
    "Jose": {}
}

# Funciones
# Saldos randomizados entre 100.000 y 2.000.000
def saldoRandom():
    return random.randint(100000, 2000000)

# Asignación de saldos a usuarios
def asignacionesSaldos(usuarios):
    for usuario, detalles in usuarios.items():
        saldo = saldoRandom()
        detalles["saldo"] = saldo
        # Categorías
        if 100000 <= saldo <= 900000:
            detalles["categoria"] = "bronce"
        elif 900000 < saldo <= 1200000:
            detalles["categoria"] = "plata"
        elif 1200000 < saldo <= 2000000:
            detalles["categoria"] = "oro"

# Función para calcular la media geométrica
def mediaGeometrica(saldos):
    producto = reduce(lambda x, y: x * y, saldos)
    media_geo = producto ** (1 / len(saldos))
    return media_geo

# Menú
def menu():
    while True:
        print("Bienvenido al banco")
        print("1. Asignar saldos")
        print("2. Clasificar saldos")
        print("3. Consultar estadísticas de saldos")
        print("4. Reporte de saldos")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion < 1 or opcion > 5:
            print("------------------------------------------------")
            print("Seleccione una opción válida")
            print("------------------------------------------------")
        
        else:
            if opcion == 1:
                print("------------------------------------------------")
                print("Se asignaron los siguientes saldos: ")
                asignacionesSaldos(usuarios)
                print("Saldos asignados:")
                recorrerValores()
                print("------------------------------------------------")
            elif opcion == 2:
                print("------------------------------------------------")
                print("Categorías de usuarios...")
                for usuario in usuarios:
                    print(f"{usuario}: {usuarios[usuario]['categoria']}")
                print("------------------------------------------------")
            elif opcion == 3:
                print("------------------------------------------------")
                saldos = [usuarios[usuario]['saldo'] for usuario in usuarios]
                if saldos:
                    print(f"Saldo mayor: ${max(saldos)}")
                    print(f"Saldo menor: ${min(saldos)}")
                    print(f"Promedio de saldos: ${sum(saldos) / len(saldos)}")
                    print(f"Media geométrica de saldos: {mediaGeometrica(saldos)}")
                else:
                    print("No hay saldos asignados aún.")
                print("------------------------------------------------")
            elif opcion == 4:
                print("Opción 4")
            elif opcion == 5:
                print("Gracias por usar el banco")
                break

# Función para recorrer y mostrar los valores del diccionario
def recorrerValores():
    for usuario in usuarios:
        print(f"{usuario}: ${usuarios[usuario]['saldo']} - Categoría {usuarios[usuario]['categoria']}")

# Llamar al menú principal
menu()