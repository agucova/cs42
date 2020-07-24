# Retorna el i-esimo dígito de x
def digito(x, i):
    contador = largo(x) - 1
    while x != 0:
        if i == contador:
            return x % 10
        contador -= 1
        x = x // 10
    return -1


# Retorna el numero de digitos de x
def largo(x):
    contador = 0
    while x != 0:
        x = x // 10
        contador += 1
    return contador


# Retorna si un numero es introesco o no
def introesco(x):
    c1 = 0
    c3 = 0
    c0 = 0
    c = 0
    while c < largo(x):
        d = digito(x, c)
        if d == 1:
            c1 += 1
        elif d == 3:
            c3 += 1
        elif d == 0:
            c0 += 1
        c += 1
    if c1 >= 2 and c3 >= 1 and c0 >= 1:
        return True
    return False

# Lo envolvemos en un try/except en caso de que nos hayan mentido y no sea un entero, pero la verdad es que es innecesario.
try:
    # Toma los dos números del input
    a, b = int(input()), int(input())
except TypeError:
    print("dijieron enteros :(")

# Revisa que se cumplan las condiciones que nos dijieron, tira un error si no. (Ayuda a saber si entendi bien las condiciones).
assert a >= 0 and a <= b

# Itera a través de todos los números en el rango. Cómo range funciona como [a, b), es necesario sumarle 1 al limite superior. Despues, si el número es introesco, lo imprimimos y le sumamos uno al contador de números.
cantidad_introesca = 0
for numero in range(a, b + 1):
    if introesco(numero):
        print(numero)
        cantidad_introesca += 1
print(cantidad_introesca)
