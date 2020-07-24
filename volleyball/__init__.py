import check50

@check50.check()
def partida_0():
    """partida_0"""
    check50.run("python3 volleyball.py").stdin("A\nB\nA\nA\nA\nB\nB\nA\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA B\nA 3 B 0\nSACA B\nGANA B\nA 3 B 1\nSACA B\nGANA A\nA 3 B 1\nSACA A\nGANA A\nA 4 B 1\nSACA A\nGANA A\nA 5 B 1\nFINAL", regex=False).exit(0)

@check50.check()
def partida_1():
    """partida_1"""
    check50.run("python3 volleyball.py").stdin("A\nA\nA\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA A\nA 4 B 0\nSACA A\nGANA A\nA 5 B 0\nFINAL", regex=False).exit(0)

@check50.check()
def partida_2():
    """partida_2"""
    check50.run("python3 volleyball.py").stdin("A\nB\nB\nB\nB\nB\nA\nA\nA\nA\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA B\nA 1 B 1\nSACA B\nGANA B\nA 1 B 2\nSACA B\nGANA B\nA 1 B 3\nSACA B\nGANA B\nA 1 B 4\nSACA B\nGANA A\nA 1 B 4\nSACA A\nGANA A\nA 2 B 4\nSACA A\nGANA A\nA 3 B 4\nSACA A\nGANA A\nA 4 B 4\nSACA A\nGANA A\nA 5 B 4\nSACA A\nGANA A\nA 6 B 4\nFINAL", regex=False).exit(0)

@check50.check()
def partida_3():
    """partida_3"""
    check50.run("python3 volleyball.py").stdin("A\nA\nA\nA\nB\nB\nB\nB\nB\nB\nA\nB\nA\nA\nA\nB\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA A\nA 4 B 0\nSACA A\nGANA B\nA 4 B 0\nSACA B\nGANA B\nA 4 B 1\nSACA B\nGANA B\nA 4 B 2\nSACA B\nGANA B\nA 4 B 3\nSACA B\nGANA B\nA 4 B 4\nSACA B\nGANA B\nA 4 B 5\nSACA B\nGANA A\nA 4 B 5\nSACA A\nGANA B\nA 4 B 5\nSACA B\nGANA A\nA 4 B 5\nSACA A\nGANA A\nA 5 B 5\nSACA A\nGANA A\nA 6 B 5\nSACA A\nGANA B\nA 6 B 5\nSACA B\nGANA A\nA 6 B 5\nSACA A\nGANA A\nA 7 B 5\nFINAL", regex=False).exit(0)

@check50.check()
def partida_4():
    """partida_4"""
    check50.run("python3 volleyball.py").stdin("B\nA\nB\nB\nA\nA\nA\nA\nA\nB\nB\nB\nB\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA A\nA 0 B 0\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA A\nA 0 B 1\nSACA A\nGANA A\nA 1 B 1\nSACA A\nGANA A\nA 2 B 1\nSACA A\nGANA A\nA 3 B 1\nSACA A\nGANA A\nA 4 B 1\nSACA A\nGANA B\nA 4 B 1\nSACA B\nGANA B\nA 4 B 2\nSACA B\nGANA B\nA 4 B 3\nSACA B\nGANA B\nA 4 B 4\nSACA B\nGANA B\nA 4 B 5\nSACA B\nGANA B\nA 4 B 6\nFINAL", regex=False).exit(0)

@check50.check()
def partida_5():
    """partida_5"""
    check50.run("python3 volleyball.py").stdin("B\nB\nA\nA\nB\nA\nB\nB\nA\nB\nA\nB\nA\nA\nB\nB\nA\nB\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA A\nA 0 B 1\nSACA A\nGANA A\nA 1 B 1\nSACA A\nGANA B\nA 1 B 1\nSACA B\nGANA A\nA 1 B 1\nSACA A\nGANA B\nA 1 B 1\nSACA B\nGANA B\nA 1 B 2\nSACA B\nGANA A\nA 1 B 2\nSACA A\nGANA B\nA 1 B 2\nSACA B\nGANA A\nA 1 B 2\nSACA A\nGANA B\nA 1 B 2\nSACA B\nGANA A\nA 1 B 2\nSACA A\nGANA A\nA 2 B 2\nSACA A\nGANA B\nA 2 B 2\nSACA B\nGANA B\nA 2 B 3\nSACA B\nGANA A\nA 2 B 3\nSACA A\nGANA B\nA 2 B 3\nSACA B\nGANA B\nA 2 B 4\nSACA B\nGANA B\nA 2 B 5\nFINAL", regex=False).exit(0)

@check50.check()
def partida_6():
    """partida_6"""
    check50.run("python3 volleyball.py").stdin("A\nA\nB\nB\nA\nA\nB\nA\nA\nB\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA B\nA 2 B 0\nSACA B\nGANA B\nA 2 B 1\nSACA B\nGANA A\nA 2 B 1\nSACA A\nGANA A\nA 3 B 1\nSACA A\nGANA B\nA 3 B 1\nSACA B\nGANA A\nA 3 B 1\nSACA A\nGANA A\nA 4 B 1\nSACA A\nGANA B\nA 4 B 1\nSACA B\nGANA A\nA 4 B 1\nSACA A\nGANA A\nA 5 B 1\nFINAL", regex=False).exit(0)

@check50.check()
def partida_7():
    """partida_7"""
    check50.run("python3 volleyball.py").stdin("A\nA\nA\nB\nA\nB\nA\nA\nB\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA B\nA 3 B 0\nSACA B\nGANA A\nA 3 B 0\nSACA A\nGANA B\nA 3 B 0\nSACA B\nGANA A\nA 3 B 0\nSACA A\nGANA A\nA 4 B 0\nSACA A\nGANA B\nA 4 B 0\nSACA B\nGANA A\nA 4 B 0\nSACA A\nGANA A\nA 5 B 0\nFINAL", regex=False).exit(0)

@check50.check()
def partida_8():
    """partida_8"""
    check50.run("python3 volleyball.py").stdin("B\nB\nB\nA\nA\nB\nB\nA\nB\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA B\nA 0 B 2\nSACA B\nGANA A\nA 0 B 2\nSACA A\nGANA A\nA 1 B 2\nSACA A\nGANA B\nA 1 B 2\nSACA B\nGANA B\nA 1 B 3\nSACA B\nGANA A\nA 1 B 3\nSACA A\nGANA B\nA 1 B 3\nSACA B\nGANA B\nA 1 B 4\nSACA B\nGANA B\nA 1 B 5\nFINAL", regex=False).exit(0)

@check50.check()
def partida_9():
    """partida_9"""
    check50.run("python3 volleyball.py").stdin("B\nB\nA\nB\nB\nB\nB\nA\nA\nA\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA A\nA 0 B 1\nSACA A\nGANA B\nA 0 B 1\nSACA B\nGANA B\nA 0 B 2\nSACA B\nGANA B\nA 0 B 3\nSACA B\nGANA B\nA 0 B 4\nSACA B\nGANA A\nA 0 B 4\nSACA A\nGANA A\nA 1 B 4\nSACA A\nGANA A\nA 2 B 4\nSACA A\nGANA B\nA 2 B 4\nSACA B\nGANA B\nA 2 B 5\nFINAL", regex=False).exit(0)

@check50.check()
def partida_10():
    """partida_10"""
    check50.run("python3 volleyball.py").stdin("A\nB\nB\nB\nB\nB\nA\nA\nA\nA\nB\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA B\nA 1 B 1\nSACA B\nGANA B\nA 1 B 2\nSACA B\nGANA B\nA 1 B 3\nSACA B\nGANA B\nA 1 B 4\nSACA B\nGANA A\nA 1 B 4\nSACA A\nGANA A\nA 2 B 4\nSACA A\nGANA A\nA 3 B 4\nSACA A\nGANA A\nA 4 B 4\nSACA A\nGANA B\nA 4 B 4\nSACA B\nGANA B\nA 4 B 5\nSACA B\nGANA B\nA 4 B 6\nFINAL", regex=False).exit(0)

@check50.check()
def partida_11():
    """partida_11"""
    check50.run("python3 volleyball.py").stdin("A\nA\nA\nA\nB\nB\nB\nB\nB\nB\nA\nA\nA\nB\nB\nB\nA\nA\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA A\nA 4 B 0\nSACA A\nGANA B\nA 4 B 0\nSACA B\nGANA B\nA 4 B 1\nSACA B\nGANA B\nA 4 B 2\nSACA B\nGANA B\nA 4 B 3\nSACA B\nGANA B\nA 4 B 4\nSACA B\nGANA B\nA 4 B 5\nSACA B\nGANA A\nA 4 B 5\nSACA A\nGANA A\nA 5 B 5\nSACA A\nGANA A\nA 6 B 5\nSACA A\nGANA B\nA 6 B 5\nSACA B\nGANA B\nA 6 B 6\nSACA B\nGANA B\nA 6 B 7\nSACA B\nGANA A\nA 6 B 7\nSACA A\nGANA A\nA 7 B 7\nSACA A\nGANA A\nA 8 B 7\nSACA A\nGANA A\nA 9 B 7\nFINAL", regex=False).exit(0)

@check50.check()
def partida_12():
    """partida_12"""
    check50.run("python3 volleyball.py").stdin("B\nB\nB\nB\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA B\nA 0 B 2\nSACA B\nGANA B\nA 0 B 3\nSACA B\nGANA B\nA 0 B 4\nSACA B\nGANA B\nA 0 B 5\nFINAL", regex=False).exit(0)

@check50.check()
def partida_13():
    """partida_13"""
    check50.run("python3 volleyball.py").stdin("B\nA\nB\nA\nA\nA\nA\nB\nA\nA\nB\nA\nB\nB\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA A\nA 0 B 0\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA A\nA 0 B 0\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA B\nA 3 B 0\nSACA B\nGANA A\nA 3 B 0\nSACA A\nGANA A\nA 4 B 0\nSACA A\nGANA B\nA 4 B 0\nSACA B\nGANA A\nA 4 B 0\nSACA A\nGANA B\nA 4 B 0\nSACA B\nGANA B\nA 4 B 1\nSACA B\nGANA A\nA 4 B 1\nSACA A\nGANA A\nA 5 B 1\nFINAL", regex=False).exit(0)

@check50.check()
def partida_14():
    """partida_14"""
    check50.run("python3 volleyball.py").stdin("A\nB\nB\nA\nA\nA\nB\nA\nB\nB\nA\nB\nB\nB\nA\nB\nA\nB\nA\nA\nB\nA\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA B\nA 1 B 1\nSACA B\nGANA A\nA 1 B 1\nSACA A\nGANA A\nA 2 B 1\nSACA A\nGANA A\nA 3 B 1\nSACA A\nGANA B\nA 3 B 1\nSACA B\nGANA A\nA 3 B 1\nSACA A\nGANA B\nA 3 B 1\nSACA B\nGANA B\nA 3 B 2\nSACA B\nGANA A\nA 3 B 2\nSACA A\nGANA B\nA 3 B 2\nSACA B\nGANA B\nA 3 B 3\nSACA B\nGANA B\nA 3 B 4\nSACA B\nGANA A\nA 3 B 4\nSACA A\nGANA B\nA 3 B 4\nSACA B\nGANA A\nA 3 B 4\nSACA A\nGANA B\nA 3 B 4\nSACA B\nGANA A\nA 3 B 4\nSACA A\nGANA A\nA 4 B 4\nSACA A\nGANA B\nA 4 B 4\nSACA B\nGANA A\nA 4 B 4\nSACA A\nGANA A\nA 5 B 4\nSACA A\nGANA A\nA 6 B 4\nFINAL", regex=False).exit(0)

@check50.check()
def partida_15():
    """partida_15"""
    check50.run("python3 volleyball.py").stdin("B\nB\nB\nA\nB\nA\nB\nA\nA\nB\nA\nA\nA\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA B\nA 0 B 2\nSACA B\nGANA A\nA 0 B 2\nSACA A\nGANA B\nA 0 B 2\nSACA B\nGANA A\nA 0 B 2\nSACA A\nGANA B\nA 0 B 2\nSACA B\nGANA A\nA 0 B 2\nSACA A\nGANA A\nA 1 B 2\nSACA A\nGANA B\nA 1 B 2\nSACA B\nGANA A\nA 1 B 2\nSACA A\nGANA A\nA 2 B 2\nSACA A\nGANA A\nA 3 B 2\nSACA A\nGANA A\nA 4 B 2\nSACA A\nGANA A\nA 5 B 2\nFINAL", regex=False).exit(0)

@check50.check()
def partida_16():
    """partida_16"""
    check50.run("python3 volleyball.py").stdin("A\nB\nB\nB\nB\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA B\nA 1 B 1\nSACA B\nGANA B\nA 1 B 2\nSACA B\nGANA B\nA 1 B 3\nSACA B\nGANA B\nA 1 B 4\nSACA B\nGANA B\nA 1 B 5\nFINAL", regex=False).exit(0)

@check50.check()
def partida_17():
    """partida_17"""
    check50.run("python3 volleyball.py").stdin("A\nA\nA\nB\nB\nA\nB\nA\nB\nB\nB\nA\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA B\nA 3 B 0\nSACA B\nGANA B\nA 3 B 1\nSACA B\nGANA A\nA 3 B 1\nSACA A\nGANA B\nA 3 B 1\nSACA B\nGANA A\nA 3 B 1\nSACA A\nGANA B\nA 3 B 1\nSACA B\nGANA B\nA 3 B 2\nSACA B\nGANA B\nA 3 B 3\nSACA B\nGANA A\nA 3 B 3\nSACA A\nGANA A\nA 4 B 3\nSACA A\nGANA A\nA 5 B 3\nFINAL", regex=False).exit(0)

@check50.check()
def partida_18():
    """partida_18"""
    check50.run("python3 volleyball.py").stdin("A\nB\nA\nB\nA\nB\nA\nA\nA\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA A\nA 4 B 0\nSACA A\nGANA A\nA 5 B 0\nFINAL", regex=False).exit(0)

@check50.check()
def partida_19():
    """partida_19"""
    check50.run("python3 volleyball.py").stdin("A\nA\nA\nB\nB\nB\nA\nB\nA\nA\nB\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA B\nA 3 B 0\nSACA B\nGANA B\nA 3 B 1\nSACA B\nGANA B\nA 3 B 2\nSACA B\nGANA A\nA 3 B 2\nSACA A\nGANA B\nA 3 B 2\nSACA B\nGANA A\nA 3 B 2\nSACA A\nGANA A\nA 4 B 2\nSACA A\nGANA B\nA 4 B 2\nSACA B\nGANA A\nA 4 B 2\nSACA A\nGANA A\nA 5 B 2\nFINAL", regex=False).exit(0)

@check50.check()
def partida_20():
    """partida_20"""
    check50.run("python3 volleyball.py").stdin("B\nA\nB\nB\nA\nA\nB\nA\nA\nB\nA\nB\nA\nB\nA\nB\nA\nB\nB\nB\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA A\nA 0 B 0\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA A\nA 0 B 1\nSACA A\nGANA A\nA 1 B 1\nSACA A\nGANA B\nA 1 B 1\nSACA B\nGANA A\nA 1 B 1\nSACA A\nGANA A\nA 2 B 1\nSACA A\nGANA B\nA 2 B 1\nSACA B\nGANA A\nA 2 B 1\nSACA A\nGANA B\nA 2 B 1\nSACA B\nGANA A\nA 2 B 1\nSACA A\nGANA B\nA 2 B 1\nSACA B\nGANA A\nA 2 B 1\nSACA A\nGANA B\nA 2 B 1\nSACA B\nGANA A\nA 2 B 1\nSACA A\nGANA B\nA 2 B 1\nSACA B\nGANA B\nA 2 B 2\nSACA B\nGANA B\nA 2 B 3\nSACA B\nGANA B\nA 2 B 4\nSACA B\nGANA B\nA 2 B 5\nFINAL", regex=False).exit(0)

@check50.check()
def partida_21():
    """partida_21"""
    check50.run("python3 volleyball.py").stdin("B\nA\nA\nB\nA\nB\nA\nA\nB\nB\nA\nB\nA\nA\nA\nB\nA\nB\nA\nB\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA A\nA 0 B 0\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA B\nA 2 B 0\nSACA B\nGANA B\nA 2 B 1\nSACA B\nGANA A\nA 2 B 1\nSACA A\nGANA B\nA 2 B 1\nSACA B\nGANA A\nA 2 B 1\nSACA A\nGANA A\nA 3 B 1\nSACA A\nGANA A\nA 4 B 1\nSACA A\nGANA B\nA 4 B 1\nSACA B\nGANA A\nA 4 B 1\nSACA A\nGANA B\nA 4 B 1\nSACA B\nGANA A\nA 4 B 1\nSACA A\nGANA B\nA 4 B 1\nSACA B\nGANA A\nA 4 B 1\nSACA A\nGANA A\nA 5 B 1\nFINAL", regex=False).exit(0)

@check50.check()
def partida_22():
    """partida_22"""
    check50.run("python3 volleyball.py").stdin("B\nB\nB\nB\nB\nA\nA\nB\nA\nB\nA\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA B\nA 0 B 2\nSACA B\nGANA B\nA 0 B 3\nSACA B\nGANA B\nA 0 B 4\nSACA B\nGANA A\nA 0 B 4\nSACA A\nGANA A\nA 1 B 4\nSACA A\nGANA B\nA 1 B 4\nSACA B\nGANA A\nA 1 B 4\nSACA A\nGANA B\nA 1 B 4\nSACA B\nGANA A\nA 1 B 4\nSACA A\nGANA B\nA 1 B 4\nSACA B\nGANA B\nA 1 B 5\nFINAL", regex=False).exit(0)

@check50.check()
def partida_23():
    """partida_23"""
    check50.run("python3 volleyball.py").stdin("A\nA\nA\nB\nA\nB\nB\nB\nB\nA\nB\nB\nA\nA\nA\nB\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA B\nA 3 B 0\nSACA B\nGANA A\nA 3 B 0\nSACA A\nGANA B\nA 3 B 0\nSACA B\nGANA B\nA 3 B 1\nSACA B\nGANA B\nA 3 B 2\nSACA B\nGANA B\nA 3 B 3\nSACA B\nGANA A\nA 3 B 3\nSACA A\nGANA B\nA 3 B 3\nSACA B\nGANA B\nA 3 B 4\nSACA B\nGANA A\nA 3 B 4\nSACA A\nGANA A\nA 4 B 4\nSACA A\nGANA A\nA 5 B 4\nSACA A\nGANA B\nA 5 B 4\nSACA B\nGANA A\nA 5 B 4\nSACA A\nGANA A\nA 6 B 4\nFINAL", regex=False).exit(0)

@check50.check()
def partida_24():
    """partida_24"""
    check50.run("python3 volleyball.py").stdin("B\nA\nB\nB\nB\nB\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA A\nA 0 B 0\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA B\nA 0 B 2\nSACA B\nGANA B\nA 0 B 3\nSACA B\nGANA B\nA 0 B 4\nSACA B\nGANA B\nA 0 B 5\nFINAL", regex=False).exit(0)

@check50.check()
def partida_25():
    """partida_25"""
    check50.run("python3 volleyball.py").stdin("A\nA\nA\nB\nB\nB\nA\nA\nB\nB\nB\nB\nA\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA A\nA 2 B 0\nSACA A\nGANA A\nA 3 B 0\nSACA A\nGANA B\nA 3 B 0\nSACA B\nGANA B\nA 3 B 1\nSACA B\nGANA B\nA 3 B 2\nSACA B\nGANA A\nA 3 B 2\nSACA A\nGANA A\nA 4 B 2\nSACA A\nGANA B\nA 4 B 2\nSACA B\nGANA B\nA 4 B 3\nSACA B\nGANA B\nA 4 B 4\nSACA B\nGANA B\nA 4 B 5\nSACA B\nGANA A\nA 4 B 5\nSACA A\nGANA B\nA 4 B 5\nSACA B\nGANA B\nA 4 B 6\nFINAL", regex=False).exit(0)

@check50.check()
def partida_26():
    """partida_26"""
    check50.run("python3 volleyball.py").stdin("B\nA\nB\nB\nB\nA\nA\nA\nB\nA\nB\nA\nA\nB\nB\nB\nA\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA A\nA 0 B 0\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA B\nA 0 B 2\nSACA B\nGANA A\nA 0 B 2\nSACA A\nGANA A\nA 1 B 2\nSACA A\nGANA A\nA 2 B 2\nSACA A\nGANA B\nA 2 B 2\nSACA B\nGANA A\nA 2 B 2\nSACA A\nGANA B\nA 2 B 2\nSACA B\nGANA A\nA 2 B 2\nSACA A\nGANA A\nA 3 B 2\nSACA A\nGANA B\nA 3 B 2\nSACA B\nGANA B\nA 3 B 3\nSACA B\nGANA B\nA 3 B 4\nSACA B\nGANA A\nA 3 B 4\nSACA A\nGANA B\nA 3 B 4\nSACA B\nGANA B\nA 3 B 5\nFINAL", regex=False).exit(0)

@check50.check()
def partida_27():
    """partida_27"""
    check50.run("python3 volleyball.py").stdin("A\nB\nB\nA\nA\nA\nB\nA\nB\nA\nA\nB\nB\nA\nB\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA B\nA 1 B 1\nSACA B\nGANA A\nA 1 B 1\nSACA A\nGANA A\nA 2 B 1\nSACA A\nGANA A\nA 3 B 1\nSACA A\nGANA B\nA 3 B 1\nSACA B\nGANA A\nA 3 B 1\nSACA A\nGANA B\nA 3 B 1\nSACA B\nGANA A\nA 3 B 1\nSACA A\nGANA A\nA 4 B 1\nSACA A\nGANA B\nA 4 B 1\nSACA B\nGANA B\nA 4 B 2\nSACA B\nGANA A\nA 4 B 2\nSACA A\nGANA B\nA 4 B 2\nSACA B\nGANA A\nA 4 B 2\nSACA A\nGANA A\nA 5 B 2\nFINAL", regex=False).exit(0)

@check50.check()
def partida_28():
    """partida_28"""
    check50.run("python3 volleyball.py").stdin("A\nB\nA\nB\nB\nA\nB\nA\nB\nB\nB\nA\nB\nA\nA\nA\nA\nB\nA\nA", prompt=False).stdout("EMPIEZA\nSACA A\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA A\nA 1 B 0\nSACA A\nGANA B\nA 1 B 0\nSACA B\nGANA B\nA 1 B 1\nSACA B\nGANA A\nA 1 B 1\nSACA A\nGANA B\nA 1 B 1\nSACA B\nGANA A\nA 1 B 1\nSACA A\nGANA B\nA 1 B 1\nSACA B\nGANA B\nA 1 B 2\nSACA B\nGANA B\nA 1 B 3\nSACA B\nGANA A\nA 1 B 3\nSACA A\nGANA B\nA 1 B 3\nSACA B\nGANA A\nA 1 B 3\nSACA A\nGANA A\nA 2 B 3\nSACA A\nGANA A\nA 3 B 3\nSACA A\nGANA A\nA 4 B 3\nSACA A\nGANA B\nA 4 B 3\nSACA B\nGANA A\nA 4 B 3\nSACA A\nGANA A\nA 5 B 3\nFINAL", regex=False).exit(0)

@check50.check()
def partida_29():
    """partida_29"""
    check50.run("python3 volleyball.py").stdin("B\nB\nA\nB\nA\nA\nA\nB\nA\nB\nA\nB\nB\nA\nB\nB\nA\nB\nA\nB\nB\nA\nA\nA\nA\nB\nB\nB\nA\nA\nA\nB\nB\nB\nB", prompt=False).stdout("EMPIEZA\nSACA A\nGANA B\nA 0 B 0\nSACA B\nGANA B\nA 0 B 1\nSACA B\nGANA A\nA 0 B 1\nSACA A\nGANA B\nA 0 B 1\nSACA B\nGANA A\nA 0 B 1\nSACA A\nGANA A\nA 1 B 1\nSACA A\nGANA A\nA 2 B 1\nSACA A\nGANA B\nA 2 B 1\nSACA B\nGANA A\nA 2 B 1\nSACA A\nGANA B\nA 2 B 1\nSACA B\nGANA A\nA 2 B 1\nSACA A\nGANA B\nA 2 B 1\nSACA B\nGANA B\nA 2 B 2\nSACA B\nGANA A\nA 2 B 2\nSACA A\nGANA B\nA 2 B 2\nSACA B\nGANA B\nA 2 B 3\nSACA B\nGANA A\nA 2 B 3\nSACA A\nGANA B\nA 2 B 3\nSACA B\nGANA A\nA 2 B 3\nSACA A\nGANA B\nA 2 B 3\nSACA B\nGANA B\nA 2 B 4\nSACA B\nGANA A\nA 2 B 4\nSACA A\nGANA A\nA 3 B 4\nSACA A\nGANA A\nA 4 B 4\nSACA A\nGANA A\nA 5 B 4\nSACA A\nGANA B\nA 5 B 4\nSACA B\nGANA B\nA 5 B 5\nSACA B\nGANA B\nA 5 B 6\nSACA B\nGANA A\nA 5 B 6\nSACA A\nGANA A\nA 6 B 6\nSACA A\nGANA A\nA 7 B 6\nSACA A\nGANA B\nA 7 B 6\nSACA B\nGANA B\nA 7 B 7\nSACA B\nGANA B\nA 7 B 8\nSACA B\nGANA B\nA 7 B 9\nFINAL", regex=False).exit()