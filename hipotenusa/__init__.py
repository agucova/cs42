import check50

@check50.check()
def triangulo_1():
    """triangulo_1"""
    check50.run("python3 hipotenusa.py").stdin("3\n4", prompt=False).stdout("c: 5", regex=False).exit(0)

@check50.check()
def triangulo_2():
    """triangulo_2"""
    check50.run("python3 hipotenusa.py").stdin("6\n8", prompt=False).stdout("c: 10", regex=False).exit(0)

@check50.check()
def triangulo_3():
    """triangulo_3"""
    check50.run("python3 hipotenusa.py").stdin("5\n12", prompt=False).stdout("c: 13", regex=False).exit(0)

@check50.check()
def triangulo_4():
    """triangulo_4"""
    check50.run("python3 hipotenusa.py").stdin("120\n209", prompt=False).stdout("c: 241", regex=False).exit(0)

@check50.check()
def triangulo_5():
    """triangulo_5"""
    check50.run("python3 hipotenusa.py").stdin("32\n255", prompt=False).stdout("c: 257", regex=False).exit(0)

@check50.check()
def triangulo_6():
    """triangulo_6"""
    check50.run("python3 hipotenusa.py").stdin("160\n231", prompt=False).stdout("c: 281", regex=False).exit(0)

@check50.check()
def triangulo_7():
    """triangulo_7"""
    check50.run("python3 hipotenusa.py").stdin("68\n285", prompt=False).stdout("c: 293", regex=False).exit(0)

@check50.check()
def triangulo_8():
    """triangulo_8"""
    check50.run("python3 hipotenusa.py").stdin("115\n252", prompt=False).stdout("c: 277", regex=False).exit(0)