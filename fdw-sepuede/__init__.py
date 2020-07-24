import check50

@check50.check()
def muralla_0():
    """muralla_0"""
    check50.run("python3 sepuede.py").stdin("V--V----V--P--VV---V------V--P--V--V\n5", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_1():
    """muralla_1"""
    check50.run("python3 sepuede.py").stdin("V--V----V--P--VV---V------V--P--V--V\n3", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_2():
    """muralla_2"""
    check50.run("python3 sepuede.py").stdin("V--V----V--P--VV---V------V--P--V--V\n4", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_3():
    """muralla_3"""
    check50.run("python3 sepuede.py").stdin("V--V----V--P--VV---V------V--P--V--V\n2", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_4():
    """muralla_4"""
    check50.run("python3 sepuede.py").stdin("V--PP--V---V\n5", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_5():
    """muralla_5"""
    check50.run("python3 sepuede.py").stdin("V-------PP-PPP-VV-----V\n3", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_6():
    """muralla_6"""
    check50.run("python3 sepuede.py").stdin("V-------PP-PPP-VV-----V\n6", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_7():
    """muralla_7"""
    check50.run("python3 sepuede.py").stdin("V-------PP-PPP-VV-----V\n5", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_8():
    """muralla_8"""
    check50.run("python3 sepuede.py").stdin("V-------PP-PPP-VV-----V\n4", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_9():
    """muralla_9"""
    check50.run("python3 sepuede.py").stdin("V-------PP-PPP-VV-----V\n18", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_10():
    """muralla_10"""
    check50.run("python3 sepuede.py").stdin("V-------PP-PPP-VV-----V\n19", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_11():
    """muralla_11"""
    check50.run("python3 sepuede.py").stdin("V-------PP-PPP-VV-----V\n14", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_12():
    """muralla_12"""
    check50.run("python3 sepuede.py").stdin("V-------PP-PPP-VV-----V\n13", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_13():
    """muralla_13"""
    check50.run("python3 sepuede.py").stdin("V---V--V-PP-PPP-V\n2", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_14():
    """muralla_14"""
    check50.run("python3 sepuede.py").stdin("V---V--V-PP-PPP-V\n3", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_15():
    """muralla_15"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n5", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_16():
    """muralla_16"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n6", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_17():
    """muralla_17"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n4", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_18():
    """muralla_18"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n7", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_19():
    """muralla_19"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n8", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_20():
    """muralla_20"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n3", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_21():
    """muralla_21"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n9", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_22():
    """muralla_22"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n14", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_23():
    """muralla_23"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n15", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_24():
    """muralla_24"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n16", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_25():
    """muralla_25"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n10", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_26():
    """muralla_26"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n11", prompt=False).stdout("False", regex=False).exit(0)

@check50.check()
def muralla_27():
    """muralla_27"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n23", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_28():
    """muralla_28"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n24", prompt=False).stdout("True", regex=False).exit(0)

@check50.check()
def muralla_29():
    """muralla_29"""
    check50.run("python3 sepuede.py").stdin("VPV------VPPV----VPPPV----VV---VPV\n25", prompt=False).stdout("False", regex=False).exit()