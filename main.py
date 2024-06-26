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

