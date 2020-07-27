def ciegos(m, k):
    assert isinstance(k, int)

    tramos = []
    tramo = 0
    for char in m:
        if char != "V":
            tramo += 1
        else:
            tramos.append(tramo)
            tramo = 0
    suma = 0
    for t in tramos:
        if t >= k:
            dif = t - k
            suma += dif + 1

    return suma


m = input()
k = int(input())
p = ciegos(m, k)
print(p)
