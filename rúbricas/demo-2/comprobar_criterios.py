import spacex

veredicto = "proseguir"

for numero, criterio in enumerate(spacex.criterios):
    respuesta = spacex.preguntar(criterio)
    if respuesta == "no":
        if numero <= 8:
            veredicto = "detener"
        elif numero >= 9:
            veredicto = "retrasar"
        break

print("Veredicto:", veredicto)