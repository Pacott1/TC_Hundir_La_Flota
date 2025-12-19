# Aquí irán las clases
# clases.py
import numpy as np
from variables import AGUA, BARCO, IMPACTO, FALLO


class Tablero:
    def __init__(self, filas=10, columnas=10):
        self.filas = filas
        self.columnas = columnas
        self.matriz = np.full((filas, columnas), AGUA)

    # ------------------------------------------------------
    def mostrar(self, titulo="Tablero"):
        print(f"\n=== {titulo} ===")
        print("    " + " ".join(str(c) for c in range(self.columnas)))
        for i in range(self.filas):
            print(f"{i:2}  " + " ".join(self.matriz[i]))

    # ------------------------------------------------------
    def colocar_barco_jugador(self, longitud, nombre_barco):
        while True:
            print(f"\nColocando {nombre_barco} (tamaño {longitud})")

            try:
                fila = int(input("Fila inicial: "))
                columna = int(input("Columna inicial: "))
            except ValueError:
                print("❌ Introduce números válidos.")
                continue

            if not (0 <= fila < self.filas and 0 <= columna < self.columnas):
                print("❌ Esa casilla está fuera del tablero.")
                continue

            if longitud == 1:
                orientacion = "H"
            else:
                orientacion = input("Orientación (H/V): ").upper()
                if orientacion not in ("H", "V"):
                    print("❌ Orientación incorrecta.")
                    continue

            coords = []
            try:
                for d in range(longitud):
                    r = fila + (d if orientacion == "V" else 0)
                    c = columna + (d if orientacion == "H" else 0)

                    if not (0 <= r < self.filas and 0 <= c < self.columnas):
                        raise ValueError("El barco se sale del tablero.")

                    if self.matriz[r, c] != AGUA:
                        raise ValueError("Casilla ocupada por otro barco.")

                    coords.append((r, c))

            except ValueError as e:
                print("❌", e)
                continue

            for (r, c) in coords:
                self.matriz[r, c] = BARCO

            print(f"✅ {nombre_barco} colocado en {coords}")
            return coords

    # ------------------------------------------------------
    def disparar(self, fila, col):
        contenido = self.matriz[fila, col]

        if contenido == BARCO:
            self.matriz[fila, col] = IMPACTO
            return True

        elif contenido == AGUA:
            self.matriz[fila, col] = FALLO
            return False

        else:
            return None

    # ------------------------------------------------------
    def derrota(self):
        return not np.any(self.matriz == BARCO)

    # ------------------------------------------------------
    def estadisticas(self):
        impactos = np.count_nonzero(self.matriz == IMPACTO)
        fallos = np.count_nonzero(self.matriz == FALLO)
        total = impactos + fallos
        precision = impactos / total if total > 0 else 0.0

        casillas_barco = np.count_nonzero(
            (self.matriz == BARCO) | (self.matriz == IMPACTO)
        )

        return {
            "total_disparos": total,
            "impactos": impactos,
            "fallos": fallos,
            "precision": precision,
            "casillas_barco_totales": casillas_barco,
        }
