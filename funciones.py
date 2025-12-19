# Aquí irán las funciones
import numpy as np
import random
from variables import *
import numpy as np




def crear_tablero(filas=10, columnas=10):
  
    # Crea un tablero vacío usando NumPy.
    # Cada casilla empieza como AGUA (0).
 
    return np.full((filas, columnas), AGUA)

def colocar_barco_jugador(tablero, longitud, nombre_barco, simbolo):
    filas, columnas = tablero.shape
    

    while True:
        print(f"\nColocando {nombre_barco} (tamaño {longitud})")

        # ---------------------------
        # PEDIR COORDENADAS INICIALES
        # ---------------------------
        try:
            fila = int(input("Fila inicial: "))
            columna = int(input("Columna inicial: "))
        except ValueError:
            print("❌ Introduce números enteros.")
            continue

        # Validar límites
        if not (0 <= fila < filas and 0 <= columna < columnas):
            print("❌ Esa casilla está fuera del tablero.")
            continue

        # ---------------------------
        # ORIENTACIÓN
        # ---------------------------
        if longitud == 1:
            orientacion = "H"     # Da igual para barcos de 1 casilla
        else:
            orientacion = input("Orientación (H horizontal / V vertical): ").upper()
            if orientacion not in ("H", "V"):
                print("❌ Orientación incorrecta.")
                continue

        # ---------------------------
        # CALCULAR TODAS LAS CASILLAS
        # ---------------------------
        coords = []

        try:
            for d in range(longitud):
                r = fila + d if orientacion == "V" else fila
                c = columna + d if orientacion == "H" else columna

                # comprobar límites
                if not (0 <= r < filas and 0 <= c < columnas):
                    raise ValueError("El barco se sale del tablero.")

                # comprobar ocupación
                if tablero[r, c] != AGUA:
                    raise ValueError("Casilla ocupada por otro barco.")

                coords.append((r, c))

        except ValueError as e:
            print(f"❌ {e}")
            print("Intenta colocar de nuevo este barco.")
            continue

        # ---------------------------
        # COLOCAR BARCO EN EL TABLERO
        # ---------------------------
        for (r, c) in coords:
            tablero[r, c] = simbolo

        print(f"✅ {nombre_barco} colocado en {coords}")
        
        return coords




def calcular_estadisticas(tablero):
   
    # Calcula estadísticas básicas del tablero:
        # - total_disparos
        # - impactos (IMPACTO)
        # - fallos (FALLO)
        # - precision (impactos / total_disparos)
        # - casillas_barco (total de celdas con BARCO o IMPACTO)
   
    impactos = np.count_nonzero(tablero == IMPACTO)
    fallos = np.count_nonzero(tablero == FALLO)
    total_disparos = impactos + fallos

    # Barcos aún enteros + barcos impactados
    casillas_barco = np.count_nonzero((tablero == BARCO) | (tablero == IMPACTO))

    precision = impactos / total_disparos if total_disparos > 0 else 0.0

    return {
        "total_disparos": total_disparos,
        "impactos": impactos,
        "fallos": fallos,
        "precision": precision,
        "casillas_barco_totales": casillas_barco,
    }


def mostrar_tablero(tablero, titulo="Tablero"):
    print(f"\n=== {titulo} ===")
    
    # Encabezado de columnas
    print("    " + " ".join([str(i) for i in range(tablero.shape[1])]))
    
    # Filas del tablero
    for i in range(tablero.shape[0]):
        print(f"{i:2}  " + " ".join(tablero[i]))



def disparar(tablero_rival, tablero_rival_2, fila, col):
    # Devuelve True si acierta, False si falla, None si ya disparó ahí.
    if tablero_rival[fila, col] == BARCO:
        tablero_rival[fila, col] = IMPACTO
        tablero_rival_2[fila, col] = IMPACTO
        print(f"¡Impacto en ({fila}, {col})!")
        print(tablero_rival_2)
        return True
    elif tablero_rival[fila, col] == AGUA:
        tablero_rival[fila, col] = FALLO
        tablero_rival_2[fila, col] = FALLO
        print(f"Agua en ({fila}, {col}).")
        print(tablero_rival_2)
        return False
    else:
        print(f"Ya se disparó en ({fila}, {col}).")
        return None

def disparo_rival(tablero):
    filas, cols = tablero.shape
    while True:
        fila = random.randint(0, filas - 1)
        col = random.randint(0, cols - 1)

        if tablero[fila, col] in [BARCO,AGUA]:
            if tablero[fila, col] == BARCO:
                tablero[fila, col] = IMPACTO
                print(f"¡Impacto en ({fila}, {col})!")
                print(tablero)
                return True
            else:
                tablero[fila, col] = AGUA
                print(f"Agua en ({fila}, {col}).")
                print(tablero)
                return False
            
def comprobar_derrota(tablero):                                     
    """Devuelve True si no quedan barcos en el tablero."""
    return not np.any(tablero == BARCO)



def flota_peq_aleatorio(tablero):
    # Dimensiones de tablero:
    filas_totales = tablero.shape[0]
    columnas_totales = tablero.shape[1] 
    # Fijamos unos numeros random que tendrá la computadora.
    random.seed(42)

    flota_peq = [] 
    ocupadas = set() # Set para guardar las posiciones y que nos servira a futuro de comprobar que no estemos poniendo en la misma posicion 2 barcos.

    for barco in range(4):
        while True:
            fila = random.randint(0,filas_totales-1)
            columna = random.randint(0,columnas_totales-1)
            primera_pieza = (fila,columna)

            if primera_pieza in ocupadas:
                continue

            flota_peq.append(primera_pieza)
            ocupadas.add(primera_pieza)
            tablero[primera_pieza] = BARCO

            break

    return flota_peq, tablero






def flota_med_aleatoria(tablero, flota_peq):
    filas_totales = tablero.shape[0]
    columnas_totales = tablero.shape[1] 
    
    ocupadas = set(flota_peq)
    flota_med=[]
    random.seed(42)
    for barco in range(3):
        while True:
        # Primera pieza:
            fila = random.randint(0,filas_totales-1)
            columna = random.randint(0,columnas_totales-1)
            primera_pieza = (fila,columna)
        # Si la primera pieza es una de las ocupadas, vuelve a sacar una primera pieza
            if primera_pieza in ocupadas:
                continue
        # Elegimos orientacion, para asegurarnos que esten juntas las coordenadas de los barcos medianos.            
            orientacion = random.choice(['N','S','O','E'])

            fila2,columna2 = fila,columna # Muy importante ya que le decimos que la fila y columna de la segunda pieza en principio sea igual que la primera pieza y en funcion de la coordenad, sumamos o restamos columna o fila.

            match orientacion:
                case 'N':
                    fila2 = fila - 1
                                
                case 'S':
                    fila2 = fila + 1
                   
                case 'O':
                   columna2 = columna - 1
                    
                case 'E':
                    columna2 = columna + 1
                   
            if not (0 <= fila2 < filas_totales and 0 <= columna2 < columnas_totales):
                continue # Si la fila y columna no es mayor que las totlas y no son menores que 0, agregala a la variable segunda_pieza
            
            segunda_pieza = (fila2,columna2)

            if segunda_pieza in ocupadas:
                continue

            flota_med.append([primera_pieza,segunda_pieza])
            ocupadas.add(primera_pieza)
            ocupadas.add(segunda_pieza)

            tablero[primera_pieza] = BARCO
            tablero[segunda_pieza] = BARCO



            break
    return flota_med,tablero




def flota_grand_aleatoria(tablero, flota_peq,flota_med):
    filas_totales = tablero.shape[0]
    columnas_totales = tablero.shape[1] 

    ocupadas = set(flota_peq) 
    for barco in flota_med:
        for pieza in barco:
            ocupadas.add(pieza)
    flota_grand = []
    random.seed(42)
    for barco in range(2):
        while True:
        # Primera pieza:
            fila = random.randint(0,filas_totales-1)
            columna = random.randint(0,columnas_totales-1)
            primera_pieza = (fila,columna)
        # Si la primera pieza es una de las ocupadas, vuelve a sacar una primera pieza
            if primera_pieza in ocupadas:
                continue
        # Elegimos orientacion, para asegurarnos que esten juntas las coordenadas de los barcos medianos.            
            orientacion = random.choice(['N','S','O','E'])

            fila2,columna2 = fila,columna
            fila3,columna3 = fila,columna  # Muy importante ya que le decimos que la fila y columna de la segunda pieza en principio sea igual que la primera pieza y en funcion de la coordenad, sumamos o restamos columna o fila.
            
            match orientacion:
                case 'N':
                    fila2 = fila -1 
                    fila3 = fila -2            
                case 'S':
                   fila2 = fila + 1
                   fila3 = fila + 2
                case 'O':
                   columna2 = columna - 1
                   columna3 = columna - 2
                case 'E':
                    columna2 = columna + 1
                    columna3 = columna + 2


            if not (0 <= fila2 < filas_totales and 0 <= columna2 < columnas_totales):
                continue # Si la fila y columna no es mayor que las totlas y no son menores que 0, agregala a la variable segunda_pieza

            if not (0 <= fila3 < filas_totales and 0 <= columna3 < columnas_totales):
                continue # Si la fila y columna no es mayor que las totaless y no son menores que 0, agregala a la variable tercera_pieza
            segunda_pieza = (fila2,columna2)
            tercera_pieza = (fila3,columna3)

            if segunda_pieza in ocupadas:
                continue
            
            if tercera_pieza in ocupadas: # Compruebo que la tercera pieza no este ocupada antes.
                continue

            flota_grand.append([primera_pieza,segunda_pieza,tercera_pieza])
            ocupadas.add(primera_pieza)
            ocupadas.add(segunda_pieza)
            ocupadas.add(tercera_pieza)

            tablero[primera_pieza] = BARCO
            tablero[segunda_pieza] = BARCO
            tablero[tercera_pieza] = BARCO


            break
    return flota_grand,tablero





def flota_enorme_aleatoria(tablero, flota_peq,flota_med,flota_grand):
    filas_totales = tablero.shape[0]
    columnas_totales = tablero.shape[1] 

    ocupadas = set(flota_peq) 
    for barco in flota_med:
        for pieza in barco:
            ocupadas.add(pieza)
    for barco in flota_grand:
        for pieza in barco:
            ocupadas.add(pieza)
    flota_enorme = []
    random.seed(42)
    for barco in range(1):
        while True:
        # Primera pieza:
            fila = random.randint(0,filas_totales-1)
            columna = random.randint(0,columnas_totales-1)
            primera_pieza = (fila,columna)
        # Si la primera pieza es una de las ocupadas, vuelve a sacar una primera pieza
            if primera_pieza in ocupadas:
                continue
        # Elegimos orientacion, para asegurarnos que esten juntas las coordenadas de los barcos medianos.            
            orientacion = random.choice(['N','S','O','E'])

            fila2,columna2 = fila,columna # Muy importante ya que le decimos que la fila y columna de la segunda pieza en principio sea igual que la primera pieza y en funcion de la coordenad, sumamos o restamos columna o fila.
            fila3,columna3 = fila,columna
            fila4,columna4 = fila,columna
            match orientacion:
                case 'N':
                    fila2 = fila - 1
                    fila3 = fila - 2 
                    fila4 = fila - 3           
                case 'S':
                   fila2 = fila + 1
                   fila3 = fila + 2
                   fila4 = fila + 3
                case 'O':
                   columna2 = columna - 1
                   columna3 = columna - 2
                   columna4 = columna - 3
                case 'E':
                    columna2 = columna + 1
                    columna3 = columna + 2
                    columna4 = columna + 3

            if not (0 <= fila2 < filas_totales and 0 <= columna2 < columnas_totales):
                continue # Si la fila y columna no es mayor que las totaless y no son menores que 0, agregala a la variable segunda_pieza
            if not (0 <= fila3 < filas_totales and 0 <= columna3 < columnas_totales):
                continue # Si la fila y columna no es mayor que las totaless y no son menores que 0, agregala a la variable tercera_pieza
            if not (0 <= fila4 < filas_totales and 0 <= columna4 < columnas_totales):
                continue # Si la fila y columna no es mayor que las totaless y no son menores que 0, agregala a la variable tercera_pieza


            segunda_pieza = (fila2,columna2)
            tercera_pieza = (fila3,columna3)
            cuarta_pieza = (fila4,columna4)


            if segunda_pieza in ocupadas:
                continue
            if tercera_pieza in ocupadas: # Compruebo que la tercera pieza no este ocupada antes.
                continue
            if cuarta_pieza in ocupadas: # Compruebo que la tercera pieza no este ocupada antes.
                continue

            

            flota_enorme.append([primera_pieza,segunda_pieza,tercera_pieza,cuarta_pieza])
            ocupadas.add(primera_pieza)
            ocupadas.add(segunda_pieza)
            ocupadas.add(tercera_pieza)
            ocupadas.add(cuarta_pieza)

            tablero[primera_pieza] = BARCO
            tablero[segunda_pieza] = BARCO
            tablero[tercera_pieza] = BARCO
            tablero[cuarta_pieza] = BARCO


            break
    return flota_med,tablero




