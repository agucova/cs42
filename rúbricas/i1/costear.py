def costo(m):
    # Un conjunto es apropiado para almacenar el largo del tramo
    tramos = set()
    # El largo de un tramo determinado
    tramo = 0
    # Por cada caracteres en el muro
    for char in m:
        # Si no es un P o V
        if char not in ("P", "V"):
            # Añade uno al contador de longitud
            tramo += 1
        else:
            # Añade el largo del tramo al conjunto
            tramos.add(tramo)
            tramo = 0
    # La función max returna el máximo en una lista o conjunto de números, esto nos permite determinar el tramo mas largo del set.
    mayor_tramo = max(tramos)
    return 10 * mayor_tramo


m = input()
c = costo(m)
print(c)
