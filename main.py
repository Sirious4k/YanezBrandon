import random
import math
import statistics

# Funciones
# Saldos randomizados entre 100.000 y 2.000.000
def saldoRandom():
    saldos = random.randint(100000, 2000000)

# Asignación de saldos a usuarios
def asignacionesSaldos():
    for usuario in usuarios:
        usuarios[usuario] = saldoRandom()

# Variables
# Diccionario de usuarios
usuarios = {
    "Juan": 0,
    "Leo": 0,
    "Maria": 0,
    "Jorge": 0,
    "Brandon": 0,
    "Ana": 0,
    "Pablo": 0,
    "Ron": 0,
    "Luis": 0,
    "Jose": 0
}

# Menú
def menu():
    while(True):
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
            if (opcion == 1):
                print("Se asignaron los siguientes saldos: ")
                asignacionesSaldos()
                print(usuarios)
            elif (opcion == 2):
                print("Opción 2")
            elif (opcion == 3):
                print("Opción 3")
            elif (opcion == 4):
                print("Opción 4")
            elif (opcion == 5):
                print("Gracias por usar el banco")
                break



menu()