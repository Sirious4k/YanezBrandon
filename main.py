import random
import math
import statistics

# Funciones
# Saldos randomizados entre 100.000 y 2.000.000
def saldoRandom():
    saldos = random.randint(100000, 2000000)
    return saldos

# Asignación de saldos a usuarios
def asignacionesSaldos():
    for i in usuarios:
        usuarios[i] = saldoRandom()
        return usuarios[i]

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
    print("Bienvenido al banco")
    print("1. Asignar saldos")
    print("2. Clasificar saldos")
    print("3. Consultar estadísticas de saldos")
    print("4. Reporte de saldos")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion < 1 and opcion > 5:
        print("Opción inválida")
        menu()
