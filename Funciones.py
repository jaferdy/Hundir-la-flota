### Funciones###
import random
import numpy as np


def crear_tablero(tamaño):
    return np.full((tamaño,tamaño), " ")

def crear_barco_random(eslora, tamaño):
    barco_random = []
    fila_random = random.randint(0,9)
    columna_random = random.randint(0,9)
    barco_random.append((fila_random,columna_random))
    orient = random.choice(["N","S","E","O"])

    while len(barco_random) < eslora:
        if orient == "O":
            columna_random = columna_random - 1 
        elif orient == "E":
            columna_random = columna_random + 1
        elif orient == "N":
            fila_random = fila_random - 1
        elif orient == "S":
            fila_random = fila_random + 1

        if fila_random not in range(tamaño) or columna_random not in range(tamaño):
            fila_random = random.randint(0,9)
            columna_random = random.randint(0,9)
            barco_random = []
            barco_random.append((fila_random,columna_random))
        else:
            barco_random.append((fila_random,columna_random))
            
    return barco_random
def colocar_barco(barco, tablero):
    for casilla in barco:
        if tablero[casilla] == " ":
            tablero[casilla] = "O"
        elif tablero[casilla] == "O":
            barco = crear_barco_random(len(barco),10)

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        tablero[casilla] = "X"
        print("Tocado")
    else:
        tablero[casilla] = "-"
        print("Agua")
    return tablero

def disparojug1(casilla, tablero):
        import Variables
        if tablero[casilla] == "O":
            Variables.tablerodisparos1[casilla] = "X"
            print(f"Tocado. Dispara otra vez {Variables.jugador1}")
        else:
            import main
            Variables.tablerodisparos1[casilla] = "-"
            Variables.vidasjugador1 = Variables.vidasjugador1 - 1 
            print(f"Agua. El número de vidas restantes es de {Variables.vidasjugador1}. Turno de {Variables.jugador2}")
            main.turno_jugador1 = False
        return  print(f"Los disparos efectuados por {Variables.jugador1} han sido los siguientes: ", Variables.tablerodisparos1)

def disparojug2(casilla, tablero):
    import Variables
    casillax = random.randint(0,9)
    casillay = random.randint(0,9)
    casilla = [(casillax,casillay)]
    if tablero[casilla] == "O":
        Variables.tablerodisparos2[casilla] = "X"
        print(f"Tocado. Dispara otra vez {Variables.jugador2}")
    else:
        import main
        Variables.tablerodisparos2[casilla] = "-"
        Variables.vidasjugador2 = Variables.vidasjugador2 - 1 
        print(f"Agua. El número de vidas restantes es de {Variables.vidasjugador2}. {Variables.jugador1}")
        main.turno_jugador1 = True
        Variables.vidasjugador2 = Variables.vidasjugador2 - 1 
    return  print(f"Los disparos efectuados por {Variables.jugador2} han sido los siguientes: ", Variables.tablerodisparos2)



