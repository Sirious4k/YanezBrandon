import random
import math
import statistics
import csv
from functools import reduce

# Variables
# Diccionario de usuarios
usuarios = {
    "Juan": {"saldo": 0, "categoria": ""},
    "Leo": {"saldo": 0, "categoria": ""},
    "Maria": {"saldo": 0, "categoria": ""},
    "Jorge": {"saldo": 0, "categoria": ""},
    "Brandon": {"saldo": 0, "categoria": ""},
    "Ana": {"saldo": 0, "categoria": ""},
    "Pablo": {"saldo": 0, "categoria": ""},
    "Ron": {"saldo": 0, "categoria": ""},
    "Luis": {"saldo": 0, "categoria": ""},
    "Jose": {"saldo": 0, "categoria": ""}
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

# Función para generar el reporte y exportar a CSV
def generarReporte(usuarios):
    # Definir conceptos de deducción y porcentaje de cada uno
    conceptos_deduccion = {
        "Impuesto": 0.1,
        "Comisión bancaria": 0.05,
        "Seguro": 0.02
    }

    # Abrir archivo CSV para escritura
    with open('YanezBrandon.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
    # Escribir encabezados
        writer.writerow(['Usuario', 'Saldo inicial', 'Deducciones', 'Saldo neto'])
        
    # Calcular y escribir cada línea de datos
        for usuario, detalles in usuarios.items():
            saldo_inicial = detalles["saldo"]
            
            # Calcular deducciones
            deducciones_total = sum(saldo_inicial * porcentaje for concepto, porcentaje in conceptos_deduccion.items())
            saldo_neto = saldo_inicial - deducciones_total
            
            # Escribir en el archivo CSV
            writer.writerow([usuario, saldo_inicial, deducciones_total, saldo_neto])
            

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
                print("------------------------------------------------")
                generarReporte(usuarios)
                print("Se generó el reporte y se exportó a 'YanezBrandon.csv'.")
                print("------------------------------------------------")
            elif opcion == 5:
                print("------------------------------------------------")
                print("Gracias por usar el banco")
                print("------------------------------------------------")
                break

# Función para recorrer y mostrar los valores del diccionario
def recorrerValores():
    for usuario in usuarios:
        print(f"{usuario}: ${usuarios[usuario]['saldo']} - Categoría {usuarios[usuario]['categoria']}")

# Llamar al menú principal
menu()