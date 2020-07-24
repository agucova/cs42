# Definimos una función que maneje la lógica de nuestro programa
def sepuede(m, i):
    # assert comprueba de que efectivamente m sea un str e i un int. Si es falso, tira un error
    assert isinstance(m, str) and isinstance(i, int)

    # Acá envolvemos el código en un try/except porque no estaba del todo especificado si podian chocar bordes, aunque es innecesario.
    try:
        # si la posicion en i es una pared, al igual que la anterior y la subsecuente
        if m[i] == "-" and m[i - 1] == "-" and m[i + 1] == "-":
            return True
        else:
            return False
    except IndexError:
        return False
        # por si choca un borde

# Recibe ambas variables del input y da el output
m = input()
i = int(input())
p = sepuede(m, i)
print(p)
