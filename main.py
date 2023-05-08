### main ###
import random
import Funciones
import Variables
import numpy as np

print(f"\nBienvenido al juego {Variables.jugador1}.\nVamos a jugar a 'Hundir la flota'.\nTe enfrentarás a {Variables.jugador2}")
print(f"\n{Variables.jugador1} será el primero en participar.\nSi las coordenadas elegidas son correctas, el participante realizará un nuevo intento. En caso contrario, se le restará una vida y pasará el turno a {Variables.jugador2}")

turno_jugador1 = True

condicion1a = np.count_nonzero(Variables.tablerojug2 == 'O')
condicion1b = np.count_nonzero(Variables.tablerodisparos1 == 'O')

condicion2a = np.count_nonzero(Variables.tablerojug1 == 'O')
condicion2b = np.count_nonzero(Variables.tablerodisparos2 == 'O')

while (Variables.vidasjugador1 > 0 and Variables.vidasjugador2 > 0):
    if turno_jugador1:
        print(f"turno de {Variables.jugador1}")
        coordenadai = int(input("Introduzca la cordenada del eje x: "))
        coordenadaj = int(input("Introduzca la cordenada del eje y: "))
        Funciones.disparojug1((coordenadai,coordenadaj), Variables.tablerojug2)
    else:
        print(f"turno de {Variables.jugador2}")
        coordenadai2 = random.randint(0,9)
        coordenadaj2 = random.randint(0,9)
        Funciones.disparojug2((coordenadai2,coordenadaj2), Variables.tablerojug1)
    
    if condicion1a == condicion1b:
        print(f"Enhorabuena {Variables.jugador1}, has ganado")
        break
    
    if condicion2a == condicion2b:
        print(f"Enhorabuena {Variables.jugador2}, has ganado")
        break

print("El juego ha terminado.")
print(f"El tablero inicial de {Variables.jugador1} es :\n", Variables.tablerojug1,f"\nSiendo los disparos de {Variables.jugador2} los siguientes:\n", Variables.tablerodisparos2)
print(f"El tablero inicial de {Variables.jugador2} es :\n", Variables.tablerojug2,f"\nSiendo los disparos de {Variables.jugador1} los siguientes:\n", Variables.tablerodisparos1)
