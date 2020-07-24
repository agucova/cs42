while True:
    jugadas = ["piedra", "papel", "tijera"]
    while True:
        jugadaUno = input("Jugador 1: ¿piedra, papel, o tijera? ").strip().lower()
        if any(jugadaUno == jugada for jugada in jugadas):
            break
    while True:
        jugadaDos = input("Jugador 2: ¿piedra, papel, o tijera? ").strip().lower()
        if any(jugadaDos == jugada for jugada in jugadas):
            break
    if jugadaUno == jugadaDos:
        print("empate")
    else:
        if jugadaUno == "piedra" and jugadaDos == "papel":
            print("gana dos")
        elif jugadaUno == "piedra" and jugadaDos == "tijera":
            print("gana uno")
        elif jugadaUno == "papel" and jugadaDos == "tijera":
            print("gana dos")
        elif jugadaUno == "papel" and jugadaDos == "piedra":
            print("gana uno")
        elif jugadaUno == "tijera" and jugadaDos == "piedra":
            print("gana dos")
        elif jugadaUno == "tijera" and jugadaDos == "papel":
            print("gana uno")

    seguir_jugando = input("¿Quieres jugar de nuevo? [sí/no] ").lower().strip()
    opciones_afirmativas = ["si", "sí", "yes", "verdadero"]
    if not any([seguir_jugando == opcion for opcion in opciones_afirmativas]):
        break
