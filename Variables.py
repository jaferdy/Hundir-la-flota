### Variables###
import Funciones

jugador1 = input("Introduce tu nombre ")
jugador2 = "La Máquina"
vidasjugador1 = 30
vidasjugador2 = 30

tablerojug1 = Funciones.crear_tablero(10)
tablerojug2 = Funciones.crear_tablero(10)
tablerodisparos1 = Funciones.crear_tablero(10)
tablerodisparos2 = Funciones.crear_tablero(10)


barco_1_jugador1 = Funciones.crear_barco_random(1, 10)
barco_2_jugador1 = Funciones.crear_barco_random(1, 10)
barco_3_jugador1 = Funciones.crear_barco_random(1, 10)
barco_4_jugador1 = Funciones.crear_barco_random(1, 10)
barco_5_jugador1 = Funciones.crear_barco_random(2, 10)
barco_6_jugador1 = Funciones.crear_barco_random(2, 10)
barco_7_jugador1 = Funciones.crear_barco_random(2, 10)
barco_8_jugador1 = Funciones.crear_barco_random(3, 10)
barco_9_jugador1 = Funciones.crear_barco_random(3, 10)
barco_10_jugador1 = Funciones.crear_barco_random(4, 10)

barco_1_jugador2 = Funciones.crear_barco_random(1, 10)
barco_2_jugador2 = Funciones.crear_barco_random(1, 10)
barco_3_jugador2 = Funciones.crear_barco_random(1, 10)
barco_4_jugador2 = Funciones.crear_barco_random(1, 10)
barco_5_jugador2 = Funciones.crear_barco_random(2, 10)
barco_6_jugador2 = Funciones.crear_barco_random(2, 10)
barco_7_jugador2 = Funciones.crear_barco_random(2, 10)
barco_8_jugador2 = Funciones.crear_barco_random(3, 10)
barco_9_jugador2 = Funciones.crear_barco_random(3, 10)
barco_10_jugador2 = Funciones.crear_barco_random(4, 10)

Funciones.colocar_barco(barco_1_jugador1,tablerojug1) 
Funciones.colocar_barco(barco_2_jugador1,tablerojug1)
Funciones.colocar_barco(barco_3_jugador1,tablerojug1) 
Funciones.colocar_barco(barco_4_jugador1,tablerojug1) 
Funciones.colocar_barco(barco_5_jugador1,tablerojug1) 
Funciones.colocar_barco(barco_6_jugador1,tablerojug1) 
Funciones.colocar_barco(barco_7_jugador1,tablerojug1) 
Funciones.colocar_barco(barco_8_jugador1,tablerojug1) 
Funciones.colocar_barco(barco_9_jugador1,tablerojug1) 
Funciones.colocar_barco(barco_10_jugador1,tablerojug1) 

Funciones.colocar_barco(barco_1_jugador2,tablerojug2) 
Funciones.colocar_barco(barco_2_jugador2,tablerojug2) 
Funciones.colocar_barco(barco_3_jugador2,tablerojug2) 
Funciones.colocar_barco(barco_4_jugador2,tablerojug2) 
Funciones.colocar_barco(barco_5_jugador2,tablerojug2) 
Funciones.colocar_barco(barco_6_jugador2,tablerojug2) 
Funciones.colocar_barco(barco_7_jugador2,tablerojug2) 
Funciones.colocar_barco(barco_8_jugador2,tablerojug2) 
Funciones.colocar_barco(barco_9_jugador2,tablerojug2) 
Funciones.colocar_barco(barco_10_jugador2,tablerojug2) 


