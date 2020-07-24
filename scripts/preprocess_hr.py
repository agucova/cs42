nombre_archivo = input("nombre_archivo: ")
nombre_output = input("nombre_out: ")

with open(nombre_archivo, mode="r") as archivo:
    with open(nombre_output, mode="w") as salida:
        for linea in archivo:
            if linea and not "Sample Input" in linea and not "Sample Output" in linea:
                salida.write(linea)
            else:
                salida.write("")