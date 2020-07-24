import check50

@check50.check()
def muro_0():
    """muro_0"""
    check50.run("python3 ciegos.py").stdin("V--V----V--P--VV---V------V--P--V--V\n5", prompt=False).stdout("4", regex=False).exit(0)

@check50.check()
def muro_1():
    """muro_1"""
    check50.run("python3 ciegos.py").stdin("V--V----V--P--VV---V------V--P--V--V\n6", prompt=False).stdout("1", regex=False).exit(0)

@check50.check()
def muro_2():
    """muro_2"""
    check50.run("python3 ciegos.py").stdin("V--V----V--P--VV---V------V--P--V--V\n7", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def muro_3():
    """muro_3"""
    check50.run("python3 ciegos.py").stdin("V--V----V--P--VV---V-----V--P--V--V\n5", prompt=False).stdout("3", regex=False).exit(0)

@check50.check()
def muro_4():
    """muro_4"""
    check50.run("python3 ciegos.py").stdin("V--V--V\n2", prompt=False).stdout("2", regex=False).exit(0)

@check50.check()
def muro_5():
    """muro_5"""
    check50.run("python3 ciegos.py").stdin("V--V--V--P-V\n2", prompt=False).stdout("5", regex=False).exit(0)

@check50.check()
def muro_6():
    """muro_6"""
    check50.run("python3 ciegos.py").stdin("V-P-V-P-V\n3", prompt=False).stdout("2", regex=False).exit(0)

@check50.check()
def muro_7():
    """muro_7"""
    check50.run("python3 ciegos.py").stdin("VP-VP-V--V--VPPV\n2", prompt=False).stdout("5", regex=False).exit(0)

@check50.check()
def muro_8():
    """muro_8"""
    check50.run("python3 ciegos.py").stdin("VPPPVPPV--V--VPPV\n3", prompt=False).stdout("1", regex=False).exit(0)

@check50.check()
def muro_9():
    """muro_9"""
    check50.run("python3 ciegos.py").stdin("VPPPVPPPV----V\n4", prompt=False).stdout("1", regex=False).exit(0)

@check50.check()
def muro_10():
    """muro_10"""
    check50.run("python3 ciegos.py").stdin("VPPPP-V-----VP-P-PV\n5", prompt=False).stdout("3", regex=False).exit(0)

@check50.check()
def muro_11():
    """muro_11"""
    check50.run("python3 ciegos.py").stdin("VPPPVPPPVPPPPV\n3", prompt=False).stdout("4", regex=False).exit(0)

@check50.check()
def muro_12():
    """muro_12"""
    check50.run("python3 ciegos.py").stdin("VPP--VPP--V\n4", prompt=False).stdout("2", regex=False).exit(0)

@check50.check()
def muro_13():
    """muro_13"""
    check50.run("python3 ciegos.py").stdin("VVV-P-VVPPPV--PV\n3", prompt=False).stdout("3", regex=False).exit(0)

@check50.check()
def muro_14():
    """muro_14"""
    check50.run("python3 ciegos.py").stdin("VVVP-V-P-VV---VPPV\n3", prompt=False).stdout("2", regex=False).exit(0)

@check50.check()
def muro_15():
    """muro_15"""
    check50.run("python3 ciegos.py").stdin("VVV--PPV-P-PVPP--V\n4", prompt=False).stdout("3", regex=False).exit(0)

@check50.check()
def muro_16():
    """muro_16"""
    check50.run("python3 ciegos.py").stdin("VVV--PPV-P-PVPP--VPPPV----V--VPPV\n4", prompt=False).stdout("4", regex=False).exit(0)

@check50.check()
def muro_17():
    """muro_17"""
    check50.run("python3 ciegos.py").stdin("VVV--PPV-P-PVPPV-VPPPV-V--V--VPPV\n5", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def muro_18():
    """muro_18"""
    check50.run("python3 ciegos.py").stdin("VVVP-V-P-VV----VPPV\n4", prompt=False).stdout("1", regex=False).exit(0)

@check50.check()
def muro_19():
    """muro_19"""
    check50.run("python3 ciegos.py").stdin("VVVP-V-P-VV----VPPV\n5", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def muro_20():
    """muro_20"""
    check50.run("python3 ciegos.py").stdin("VVV--PPV-P-PVPP--V\n5", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def muro_21():
    """muro_21"""
    check50.run("python3 ciegos.py").stdin("VVV--VVPPPV--V\n3", prompt=False).stdout("1", regex=False).exit(0)

@check50.check()
def muro_22():
    """muro_22"""
    check50.run("python3 ciegos.py").stdin("VVV--VVPPPV--PV\n3", prompt=False).stdout("2", regex=False).exit(0)

@check50.check()
def muro_23():
    """muro_23"""
    check50.run("python3 ciegos.py").stdin("VVV-P-VVPPPV--PV\n3", prompt=False).stdout("3", regex=False).exit(0)

@check50.check()
def muro_24():
    """muro_24"""
    check50.run("python3 ciegos.py").stdin("VVV-P-VVPPPV--PV\n4", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def muro_25():
    """muro_25"""
    check50.run("python3 ciegos.py").stdin("VVV-P-VVPP--PV--PV\n5", prompt=False).stdout("1", regex=False).exit(0)

@check50.check()
def muro_26():
    """muro_26"""
    check50.run("python3 ciegos.py").stdin("VVV-P-VVPP--PV--PV\n6", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def muro_27():
    """muro_27"""
    check50.run("python3 ciegos.py").stdin("VVV-P-PVVPP--PV--PV\n4", prompt=False).stdout("3", regex=False).exit(0)

@check50.check()
def muro_28():
    """muro_28"""
    check50.run("python3 ciegos.py").stdin("VVVPPPPP-V\n6", prompt=False).stdout("1", regex=False).exit(0)

@check50.check()
def muro_29():
    """muro_29"""
    check50.run("python3 ciegos.py").stdin("VVVPPPPPP-V\n6", prompt=False).stdout("2", regex=False).exit()