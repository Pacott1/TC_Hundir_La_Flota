# **Team Challenge Sprint 3 Grupo 4 (Mañana)**
- [**Introducción**](#introducción)
- [**Resumen del juego**](#resumen-del-juego)
- [**Desarrollo del juego**](#desarrollo-del-juego)

## **Introducción**
---

Como Team Challenge del Sprint 3 hemos creado nuestra propia versión del juego de **Hundir la flota** en Python. 

Enlace al repositorio del TC: https://github.com/Carlos72293/Team_Challenge_Hundir_La_Flota_Team_M_4  

Formamos parte del grupo 4 del turno de mañana, compuesto por: 
- Lucas Cavalcante Balaguer
- Francisco de las Cuevas
- Eric Calvo Díaz
- Elena Acosta Hernández
- Carlos D'Olhaberriague Fernández
- Qamar Bahra Al-Borghli


## **Resumen del juego**
---
1. Hay dos jugadores: tú y la máquina
2. Un **tablero de 10 x 10** posiciones donde irán los barcos
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. Ahora bien, puedes empezar colocando los barcos en unas posiciones fijas, que no cambien con cada partida, y después implementarlo aleatoriamente, ya que es más complejo. Los barcos son:**
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora

4. Tanto tú, como la máquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
5. Funciona por turnos y empiezas tú.
6. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.
7. En los turnos de la máquina, si acerta también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.
8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.


## **Desarrollo del juego**
---
Tendrás que desarrollar lo siguiente:
1. Necesitarás un conjunto de **constantes**, donde tengas inventariados los barcos del juego, dimensiones y demás variables que no vayan a cambiar que tendréis definidas en archivo de **variables.py**

2. Tendrás que construir **una clase Tablero**. Para facilitar el desarrollo, la mejor opción es desarrollar una clase tablero donde implementes las siguientes funcionalidades:
    * Cuando se inicialice deberás asignar
        * Un id de jugador, para saber de quién es el tablero.
        * Unas dimensiones de tablero, que en el fondo serán tus constantes 10 x 10.
        * Unos barcos. Los que hayas definido como constantes. Aqui simplemente puedes pasar, por ejemplo, un diccionario donde especifiques el nombre de tus barcos, y la eslora de cada uno. Luego ya los colocarás en el tablero.
        * **Un tablero sin barcos, que será un array de `numpy`** donde posicionarás los barcos. Este tablero está vacío, por lo que lo puedes rellenar de 0s, 1s, o el caracter que consideres.
        * Adicionalmente la clase tablero necesitará otro array de `numpy`, ¿por qué? porque el tablero de la maquina tendrá internamente un array con sus barcos (lo que no vemos) y hará falta otro array (que sí veremos nosotros) con los disparos efectuados, para saber dónde tenemos que disparar.
    * **Inicializar el tablero**, es decir, colocar los barcos. Puedes pasar por alto el hecho de que tengan que tener espacios entre ellos pero si los colocas aleatoriamente, mucho cuidado aquí de poner los barcos dentro del tablero, y de no colocar unos barcos encima de otros :)
    * Necesitarás un método de **disparo coordenada**. Cuando hay un disparo de un jugador en ese tablero, tendrás que comprobar si ahi había un barco, o simplemente agua. Acuérdate de marcar en el tablero, tanto si hay un impacto, como si dio agua.
    * NO te ciñas a los métodos que te acabo de mencionar, crea todos los que necesites, introduce en el constructor lo que quieras y desarrolla las funciones que consideres oportunas para facilitarte el desarrollo.

3. Una vez ya tienes modelizado tu tablero, hay que montar el programa que se ejecutara desde un **main.py**:
    * El programa no es más que el **típico `while true: `, con una serie de inputs del usuario**. Se está ejecutando constantemente y le pide al usuario coordenadas para comprobar si impacta.
    * Cuando arranque el programa, primero pon algún mensaje de bienvenida y las instrucciones del juego.
    * A continuación **inicializa los tableros de ambos jugadores** con los barcos. Estas dos primeras acciones solo se ejecutan una vez!! Que es el comienzo del juego.
    * Después de eso ya comienza el juego. Básicamente **se irá ejecutando iterativamente en el `while`, y le irá preguntando coordenadas al usuario.**
    * Recoges coordenadas, compruebas en el tablero de la máquina si habia barco.
        * Hay barco: marca en el tablero de la maquina el impacto y le vuelve a tocar al usuario
        * No hay barco: le toca a la maquina. O lo que es lo mismo, escoge una coordenada aleatoria, y comprueba en el tablero del usuario si habia barco.
    * **Así hasta que uno de los dos jugadores se quede sin barcos, y termina el juego.**
    * Cuando empiece tu turno deberías imprimir por pantalla tu tablero, para ver cuántos impactos te ha hecho la máquina, así como el tablero con los impactos que has hecho tu en el adversario, de manera que te sirva de ayuda para el siguiente disparo.
    * Todas aquellas funciones que puedas construir para la ejecución de este programa deberán estar definidas en un script que se llame **funciones.py**.
