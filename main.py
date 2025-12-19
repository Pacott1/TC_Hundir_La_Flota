# MAIN
from variables import *
from clases import Tablero
from funciones import *
import numpy as np
import random

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

    # ====== Crear tableros ======
    tablero_jugador = Tablero()
    tablero_rival = Tablero()
    tablero_rival_visible = Tablero()

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

    # Barcos tamaño 1
    for _ in range(4):
        coords = tablero_jugador.colocar_barco_jugador(1, "barco pequeño")
        flota_jugador.append(coords)
        tablero_jugador.mostrar("Tu tablero")

    # Barcos tamaño 2
    for _ in range(3):
        coords = tablero_jugador.colocar_barco_jugador(2, "barco mediano")
        flota_jugador.append(coords)
        tablero_jugador.mostrar("Tu tablero")

    # Barcos tamaño 3
    for _ in range(2):
        coords = tablero_jugador.colocar_barco_jugador(3, "barco grande")
        flota_jugador.append(coords)
        tablero_jugador.mostrar("Tu tablero")

    # Barco tamaño 4
    coords = tablero_jugador.colocar_barco_jugador(4, "barco gigante")
    flota_jugador.append(coords)

    # ==============================
    # COLOCAR BARCOS DEL RIVAL
    # ==============================
    print("\nColocando barcos del rival aleatoriamente...")

    flota_peq, tablero_rival.matriz = flota_peq_aleatorio(tablero_rival.matriz)
    flota_med, tablero_rival.matriz = flota_med_aleatoria(tablero_rival.matriz, flota_peq)
    flota_grand, tablero_rival.matriz = flota_grand_aleatoria(tablero_rival.matriz, flota_peq, flota_med)
    flota_gigante, tablero_rival.matriz = flota_enorme_aleatoria(tablero_rival.matriz, flota_peq, flota_med, flota_grand)

    turno_jugador = True

    # ==============================
    # BUCLE DE PARTIDA
    # ==============================
    while True:
        print("\nTu tablero:")
        tablero_jugador.mostrar("Jugador")

        print("\nTablero enemigo visible:")
        tablero_rival_visible.mostrar("Enemigo (visible)")

        if turno_jugador:
            print(f"\nTurno de {nombre}:")
            try:
                fila, col = map(int, input("Introduce las coordenadas (fila,col): ").split(","))
            except:
                print("Formato incorrecto. Usa fila,col (ejemplo: 3,5).")
                continue

            resultado = tablero_rival.disparar(fila, col)

            # Reflejar en tablero visible
            if resultado is True:
                tablero_rival_visible.matriz[fila, col] = IMPACTO
                print("🎯 ¡Has acertado! Vuelves a disparar.")
            elif resultado is False:
                tablero_rival_visible.matriz[fila, col] = FALLO
                print("🌊 Has fallado. Le toca a la máquina.")
                turno_jugador = False
            else:
                print("⚠️ Ya habías disparado ahí.")
                turno_jugador = False

            if tablero_rival.derrota():
                print(f"🎉 ¡{nombre} ha ganado! Todos los barcos enemigos han sido hundidos.")
                break

        else:
            print("\nTurno de la máquina:")
            resultado = disparo_rival(tablero_jugador.matriz)

            if resultado:
                print("💥 La máquina ha acertado y repite turno.")
                turno_jugador = False
            else:
                print("💧 La máquina ha fallado. Te toca a ti.")
                turno_jugador = True

            if tablero_jugador.derrota():
                print("💀 ¡La máquina ha ganado! Todos tus barcos han sido hundidos.")
                break

    # ==============================
    # FIN DE PARTIDA
    # ==============================
    print("\nPartida terminada.")
    # print("Estadísticas jugador:", tablero_jugador.estadisticas())
    # print("Estadísticas rival:", tablero_rival.estadisticas())

    opcion = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if opcion != "s":
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    else:
        print("\nReiniciando partida...\n")
