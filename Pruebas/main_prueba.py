# Importar archivos
from variables import *
from clases import *
import numpy as np
import random
from funciones import *



# ==============================
# PROGRAMA PRINCIPAL
# ==============================
while True:
    print("=== ¡Bienvenido a Hundir la Flota! ===")
    print("Reglas básicas:")
    print("- Tablero de 10x10.")
    print("- Dispara introduciendo fila y columna (0–9).")
    print("- Si aciertas, vuelves a disparar. Si fallas, dispara la máquina.\n")
    
    nombre = input("Introduce tu nombre: ")

    # Crear tableros (de variables.py)
    tablero_jugador = crear_tablero()
    tablero_rival = crear_tablero()
    tablero_rival_visible = crear_tablero()

    # ==============================
    # COLOCAR BARCOS DEL JUGADOR
    # ==============================
    print(f"\nHola {nombre}, coloca tus barcos en el tablero.")
    print("Tienes:")
    print("- 4 barcos de 1 posición")
    print("- 3 barcos de 2 posiciones")
    print("- 2 barcos de 3 posiciones")
    print("- 1 barco de 4 posiciones")

    flota_jugador = []

    # 4 barcos pequeños
    for i in range(4):
        coords = colocar_barco_jugador(tablero_jugador, 1, "barco pequeño", BARCO)
        flota_jugador.append(coords)
        print(tablero_jugador)
    # 3 barcos medianos
    for i in range(3):
        coords = colocar_barco_jugador(tablero_jugador, 2, "barco mediano",BARCO)
        flota_jugador.append(coords)
        print(tablero_jugador)

    # 2 barcos grandes
    for i in range(2):
        coords = colocar_barco_jugador(tablero_jugador, 3, "barco grande", BARCO)
        flota_jugador.append(coords)
        print(tablero_jugador)

    # 1 barco gigante
    coords = colocar_barco_jugador(tablero_jugador, 4, "barco gigante", BARCO)
    flota_jugador.append(coords)
    

        
    # ==============================
    # COLOCAR BARCOS DEL RIVAL
    # ==============================
    print("\nColocando barcos del rival aleatoriamente...")

    flota_peq, tablero_rival = flota_peq_aleatorio(tablero_rival)
    flota_med, tablero_rival = flota_med_aleatoria(tablero_rival, flota_peq)
    flota_grand, tablero_rival = flota_grand_aleatoria(tablero_rival, flota_peq, flota_med)
    flota_gigante, tablero_rival = flota_enorme_aleatoria(tablero_rival, flota_peq, flota_med, flota_grand)

    
    turno_jugador = True

    # ==============================
    # BUCLE DE PARTIDA
    # ==============================
    while True:
         # Tu tablero con todos tus barcos visibles
        print("\nTu tablero:")
        mostrar_tablero(tablero_jugador)

        # Tablero enemigo: sin mostrar barcos, solo X y O
        print("\nTablero enemigo visible:")
        mostrar_tablero(tablero_rival_visible)

        if turno_jugador:
            print(f"\nTurno de {nombre}:")
            try:
                fila, col = map(int, input("Introduce las coordenadas para disparar (fila,col): ").split(","))
            except:
                print("Formato incorrecto. Usa fila,col (ejemplo: 3,5).")
                continue

            resultado = disparar(tablero_rival, tablero_rival_visible, fila, col)

            if resultado is True:
                print("🎯 ¡Has acertado! Vuelves a disparar.")
            elif resultado is False:
                print("🌊 Has fallado. Le toca a la máquina.")
                turno_jugador = False
            else:
                print("⚠️ Esa posición ya fue atacada, el turno pasa igualmente.")
                turno_jugador = False

            if comprobar_derrota(tablero_rival):
                print(f"🎉 ¡{nombre} ha ganado! Todos los barcos enemigos han sido hundidos.")
                break

        else:
            print("\nTurno de la máquina:")
            resultado = disparo_rival(tablero_jugador)

            if resultado:
                print("💥 La máquina ha acertado y repite turno.")
                turno_jugador = False
            else:
                print("💧 La máquina ha fallado. Te toca a ti.")
                turno_jugador = True

            if comprobar_derrota(tablero_jugador):
                print("💀 ¡La máquina ha ganado! Todos tus barcos han sido hundidos.")
                break

    # ==============================
    # FIN DE PARTIDA / REINICIO
    # ==============================
    print("\nPartida terminada.")
    calcular_estadisticas(tablero_jugador)
    calcular_estadisticas(tablero_rival)

    opcion = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if opcion != "s":
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    else:
        print("\nReiniciando partida...\n")

