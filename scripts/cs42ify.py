padding_check = " " * 4
padding_run = " " * 6
padding_std = " " * 8
padding_line = " " * 10

nombre_archivo = input("nombre_archivo.py: ").strip()
prefix = input("prefix: ").strip()
modo = input("modo (a o w): ").lower().strip()

if modo not in ["a", "w"]:
    raise ValueError

if modo == "a":
    desde = int(input("desde: ").strip())

with open(nombre_archivo + ".cs50.yaml", mode=modo) as checks:
    if modo == "w":
        checks.write("check50:\n")
        checks.write("  files: &check50_files\n")
        checks.write("    - !exclude \"*\"\n")
        checks.write("    - !require " + nombre_archivo + "\n")
        checks.write("  checks:\n")
        check = 0
    else:
        check = desde

    while True:
        check_name = prefix + "_" + str(check)
        checks.write(padding_check + check_name + ":\n")
        checks.write(padding_run + "- run: python3 " + nombre_archivo + "\n")

        # INPUT
        print(check_name, "input:")
        checks.write(padding_std + "stdin:\n")
        linea = True
        while linea:
            linea = input()
            if linea and not linea == "RED":
                checks.write(padding_line + "- " + linea + "\n")
            if linea == "RED":
                break
        if linea == "RED":
            break

        ## OUTPUT
        print(check_name, "output:")
        checks.write(padding_std + "stdout:\n")
        linea = True
        while linea:
            linea = input()
            if linea and not linea == "RED":
                checks.write(padding_line + "- " + linea + "\n")
            if linea == "RED":
                break
        if linea == "RED":
            break

        ## EXIT
        checks.write(padding_std + "exit: 0" + "\n")
        check += 1

    checks.write("submit50:\n")
    checks.write("  files: *check50_files\n")

print("Archivo guardado.")