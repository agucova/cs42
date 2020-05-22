import check50

@check50.check()
def triangulo_1():
    """triangulo_1"""
    check50.run("python3 hipotenusa.py").stdin("3\n4", prompt=False).stdout("Hipotenusa: 5", regex=False).exit(0)

@check50.check()
def triangulo_2():
    """triangulo_2"""
    check50.run("python3 hipotenusa.py").stdin("6\n8", prompt=False).stdout("Hipotenusa: 10", regex=False).exit(0)

@check50.check()
def triangulo_3():
    """triangulo_3"""
    check50.run("python3 hipotenusa.py").stdin("5\n12", prompt=False).stdout("Hipotenusa: 13", regex=False).exit(0)

@check50.check()
def triangulo_4():
    """triangulo_4"""
    check50.run("python3 hipotenusa.py").stdin("120\n209", prompt=False).stdout("Hipotenusa: 241", regex=False).exit(0)

@check50.check()
def triangulo_5():
    """triangulo_5"""
    check50.run("python3 hipotenusa.py").stdin("32\n255", prompt=False).stdout("Hipotenusa: 257", regex=False).exit(0)

@check50.check()
def triangulo_6():
    """triangulo_6"""
    check50.run("python3 hipotenusa.py").stdin("160\n231", prompt=False).stdout("Hipotenusa: 281", regex=False).exit(0)

@check50.check()
def triangulo_7():
    """triangulo_7"""
    check50.run("python3 hipotenusa.py").stdin("68\n285", prompt=False).stdout("Hipotenusa: 293", regex=False).exit(0)

@check50.check()
def triangulo_8():
    """triangulo_8"""
    check50.run("python3 hipotenusa.py").stdin("115\n252", prompt=False).stdout("Hipotenusa: 277", regex=False).exit(0)