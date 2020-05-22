import check50

@check50.check()
def el_programa_dice_hola_mundo():
    """el programa dice hola mundo"""
    check50.run("python3 hola.py").stdout("Hola, mundo!", regex=False).exit(0)