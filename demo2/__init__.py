import check50

@check50.check()
def lanzamiento_0():
    """lanzamiento_0"""
    check50.run("python3 comprobar_criterios.py").stdin("si\nsi\nno", prompt=False).stdout("Veredicto: detener", regex=False).exit(0)

@check50.check()
def lanzamiento_1():
    """lanzamiento_1"""
    check50.run("python3 comprobar_criterios.py").stdin("si\nsi\nsi\nsi\nsi\nno", prompt=False).stdout("Veredicto: detener", regex=False).exit(0)

@check50.check()
def lanzamiento_2():
    """lanzamiento_2"""
    check50.run("python3 comprobar_criterios.py").stdin("no", prompt=False).stdout("Veredicto: detener", regex=False).exit(0)

@check50.check()
def lanzamiento_3():
    """lanzamiento_3"""
    check50.run("python3 comprobar_criterios.py").stdin("si\nsi\nsi\nsi\nsi\nsi\nsi\nsi\nsi\nno", prompt=False).stdout("Veredicto: retrasar", regex=False).exit(0)

@check50.check()
def lanzamiento_4():
    """lanzamiento_4"""
    check50.run("python3 comprobar_criterios.py").stdin("si\nsi\nsi\nsi\nsi\nsi\nsi\nsi\nsi\nsi\nno", prompt=False).stdout("Veredicto: retrasar", regex=False).exit(0)

@check50.check()
def lanzamiento_5():
    """lanzamiento_5"""
    check50.run("python3 comprobar_criterios.py").stdin("si\nsi\nsi\nsi\nsi\nsi\nsi\nsi\nsi\nsi\nsi", prompt=False).stdout("Veredicto: proseguir", regex=False).exit(0)

@check50.check()
def lanzamiento_6():
    """lanzamiento_6"""
    check50.run("python3 comprobar_criterios.py").stdin("si\nsi\nsi\nsi\nno", prompt=False).stdout("Veredicto: detener", regex=False).exit(0)