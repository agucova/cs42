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


# En este caso usé una forma relativamente compleja de solucionarlo, a través de recursión (una función que se llama a si mismo), pero también se podía resolver con un loop o un while True.

def pythonesco(x):
    # Determina la suma de los cuadrados de los digitos. Por cada digito, toma la cifra, saca su cuadrado, y sumalo al contador de suma_cuadrado.
    suma_cuadrados = 0
    for enesimo_digito in range(largo(x)):
        cifra = digito(x, enesimo_digito)
        suma_cuadrados += cifra ** 2

    # Si tenemos un número de un digito, y este es 1 o 7, devuelve True! Si no tiene 1 o 7, devuelve False. Si tenemos un número de más de 1 digito, corre esta misma función de nuevo (recursión).
    if largo(suma_cuadrados) == 1:
        if suma_cuadrados in (1, 7):
            return True
        else:
            return False
    else:
        return suma(suma_cuadrados)


# Esto maneja el input y el output.
num = int(input())
res = pythonesco(num)
print(res)
