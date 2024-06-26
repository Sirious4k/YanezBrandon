import random
import math
import statistics

def saldoRandom():
    saldos = random.randint(100000, 2000000)
    return saldos

usuarios = {
    "Juan": 0,
    "Leo": 0,
    "Maria": 0,
    "Jorge": 0,
    "Brandon": 0,
    "Ana": 0
}

def asignacionesSaldos():
    for i in usuarios:
        usuarios[i] = saldoRandom()
        return usuarios[i]
