import random
import math
import statistics

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
    saldos = random.randint(100000, 2000000)
    return saldos

# Asignación de saldos a usuarios
def asignacionesSaldos(usuarios):
    for usuario in usuarios:
        usuarios[usuario] = saldoRandom()
        # Categorías
        if 100000 <= usuarios[usuario] <= 900000:
            usuarios[usuario] = {
                "saldo": usuarios[usuario],
                "categoria": "bronce"
            }
        elif 900000 < usuarios[usuario] <= 1200000:
            usuarios[usuario] = {
                "saldo": usuarios[usuario],
                "categoria": "plata"
            }
        elif 1200000 < usuarios[usuario] <= 2000000:
            usuarios[usuario] = {
                "saldo": usuarios[usuario],
                "categoria": "oro"
            }
            

# Valores del diccionario
def recorrerValores():
    for i in usuarios:
        print(f"{i}: ${usuarios[i]["saldo"]} - Categoría {usuarios[i]["categoria"]}")

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
                print("------------------------------------------------")
                print("Se asignaron los siguientes saldos: ")
                asignacionesSaldos(usuarios)
                print(recorrerValores())
                print("------------------------------------------------")
            elif (opcion == 2):
                print("------------------------------------------------")
                print("Categorías de usuarios...")
                for i in usuarios:
                    print(f"{i}: {usuarios[i]["categoria"]}")
                print("------------------------------------------------")
            elif (opcion == 3):
                print("Opción 3")
            elif (opcion == 4):
                print("Opción 4")
            elif (opcion == 5):
                print("Gracias por usar el banco")
                break



menu()