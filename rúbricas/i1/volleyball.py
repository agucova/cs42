# Esta función determina si gana alguien dado un estado del juego.
def comprobar_si_gana(a, b):
    assert a >= 0 and b >= 0
    if (a >= 5) and (a - b) >= 2:
        return "A"
    elif (b >= 5) and (b - a) >= 2:
        return "B"
    return False


# De quien es el turno
quien_saca = "A"
# Ganador de la partida
ganador_partida = False
# Ganador de la jugada
ganador_jugada = False

# Empieza con los puntos en 0
puntos_a, puntos_b = 0, 0

print("EMPIEZA")

# Mientras no haya un ganador, repite
while ganador_partida is False:
    # Esto dice quien saca
    print("SACA", quien_saca)
    # Nos van a dar el ganador en el input
    ganador_jugada = input()
    print("GANA", ganador_jugada)

    # Esto suma puntos a quien gane la jugada, si es que es su turno.
    if ganador_jugada == "A" and quien_saca == "A":
        puntos_a += 1
    elif ganador_jugada == "B" and quien_saca == "B":
        puntos_b += 1
    elif ganador_jugada != quien_saca:
        quien_saca = ganador_jugada

    # Muestra los puntos que cada uno tiene
    print("A", puntos_a, "B", puntos_b)

    # Determina el ganador (si ya ganó alguien), si esto tiene un valor, se rompe la condición del while.
    ganador_partida = comprobar_si_gana(puntos_a, puntos_b)

# Eso es todo, mensaje final.
print("FINAL")
