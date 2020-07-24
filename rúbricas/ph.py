while True:
    while True:
        try:
            ph = float(input("Ingrese un pH: ").strip())
        except TypeError:
            print("Valor inválido")
        else:
            if not 0 <= ph <= 14:
                print("Valor inválido.")
            else:
                break
    if ph < 7:
        print("pH ácido")
    elif ph == 7:
        print("pH neutro")
    elif ph > 6:
        print("pH básico")
