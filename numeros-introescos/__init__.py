import check50

@check50.check()
def numero_0():
    """numero_0"""
    check50.run("python3 numeros_introescos.py").stdin("1100\n1150", prompt=False).stdout("1103\n1130\n2", regex=False).exit(0)

@check50.check()
def numero_1():
    """numero_1"""
    check50.run("python3 numeros_introescos.py").stdin("1101\n1160", prompt=False).stdout("1103\n1130\n2", regex=False).exit(0)

@check50.check()
def numero_2():
    """numero_2"""
    check50.run("python3 numeros_introescos.py").stdin("1\n10", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def numero_3():
    """numero_3"""
    check50.run("python3 numeros_introescos.py").stdin("999\n1000", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def numero_4():
    """numero_4"""
    check50.run("python3 numeros_introescos.py").stdin("9000\n15000", prompt=False).stdout("10013\n10031\n10103\n10113\n10123\n10130\n10131\n10132\n10133\n10134\n10135\n10136\n10137\n10138\n10139\n10143\n10153\n10163\n10173\n10183\n10193\n10213\n10231\n10301\n10310\n10311\n10312\n10313\n10314\n10315\n10316\n10317\n10318\n10319\n10321\n10331\n10341\n10351\n10361\n10371\n10381\n10391\n10413\n10431\n10513\n10531\n10613\n10631\n10713\n10731\n10813\n10831\n10913\n10931\n11003\n11013\n11023\n11030\n11031\n11032\n11033\n11034\n11035\n11036\n11037\n11038\n11039\n11043\n11053\n11063\n11073\n11083\n11093\n11103\n11130\n11203\n11230\n11300\n11301\n11302\n11303\n11304\n11305\n11306\n11307\n11308\n11309\n11310\n11320\n11330\n11340\n11350\n11360\n11370\n11380\n11390\n11403\n11430\n11503\n11530\n11603\n11630\n11703\n11730\n11803\n11830\n11903\n11930\n12013\n12031\n12103\n12130\n12301\n12310\n13001\n13010\n13011\n13012\n13013\n13014\n13015\n13016\n13017\n13018\n13019\n13021\n13031\n13041\n13051\n13061\n13071\n13081\n13091\n13100\n13101\n13102\n13103\n13104\n13105\n13106\n13107\n13108\n13109\n13110\n13120\n13130\n13140\n13150\n13160\n13170\n13180\n13190\n13201\n13210\n13301\n13310\n13401\n13410\n13501\n13510\n13601\n13610\n13701\n13710\n13801\n13810\n13901\n13910\n14013\n14031\n14103\n14130\n14301\n14310\n174", regex=False).exit(0)

@check50.check()
def numero_5():
    """numero_5"""
    check50.run("python3 numeros_introescos.py").stdin("16000\n17000", prompt=False).stdout("16013\n16031\n16103\n16130\n16301\n16310\n6", regex=False).exit(0)

@check50.check()
def numero_6():
    """numero_6"""
    check50.run("python3 numeros_introescos.py").stdin("1103\n1104", prompt=False).stdout("1103\n1", regex=False).exit(0)

@check50.check()
def numero_7():
    """numero_7"""
    check50.run("python3 numeros_introescos.py").stdin("1100\n1103", prompt=False).stdout("1103\n1", regex=False).exit(0)

@check50.check()
def numero_8():
    """numero_8"""
    check50.run("python3 numeros_introescos.py").stdin("999\n1104", prompt=False).stdout("1013\n1031\n1103\n3", regex=False).exit(0)

@check50.check()
def numero_9():
    """numero_9"""
    check50.run("python3 numeros_introescos.py").stdin("3000\n3113", prompt=False).stdout("3011\n3101\n3110\n3", regex=False).exit(0)

@check50.check()
def numero_10():
    """numero_10"""
    check50.run("python3 numeros_introescos.py").stdin("1\n2000", prompt=False).stdout("1013\n1031\n1103\n1130\n1301\n1310\n6", regex=False).exit(0)

@check50.check()
def numero_11():
    """numero_11"""
    check50.run("python3 numeros_introescos.py").stdin("11111111\n11111200", prompt=False).stdout("11111130\n1", regex=False).exit(0)

@check50.check()
def numero_12():
    """numero_12"""
    check50.run("python3 numeros_introescos.py").stdin("333333333\n333333999", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def numero_13():
    """numero_13"""
    check50.run("python3 numeros_introescos.py").stdin("2222222\n2225000", prompt=False).stdout("2223011\n2223101\n2223110\n3", regex=False).exit(0)

@check50.check()
def numero_14():
    """numero_14"""
    check50.run("python3 numeros_introescos.py").stdin("10000\n30000", prompt=False).stdout("10013\n10031\n10103\n10113\n10123\n10130\n10131\n10132\n10133\n10134\n10135\n10136\n10137\n10138\n10139\n10143\n10153\n10163\n10173\n10183\n10193\n10213\n10231\n10301\n10310\n10311\n10312\n10313\n10314\n10315\n10316\n10317\n10318\n10319\n10321\n10331\n10341\n10351\n10361\n10371\n10381\n10391\n10413\n10431\n10513\n10531\n10613\n10631\n10713\n10731\n10813\n10831\n10913\n10931\n11003\n11013\n11023\n11030\n11031\n11032\n11033\n11034\n11035\n11036\n11037\n11038\n11039\n11043\n11053\n11063\n11073\n11083\n11093\n11103\n11130\n11203\n11230\n11300\n11301\n11302\n11303\n11304\n11305\n11306\n11307\n11308\n11309\n11310\n11320\n11330\n11340\n11350\n11360\n11370\n11380\n11390\n11403\n11430\n11503\n11530\n11603\n11630\n11703\n11730\n11803\n11830\n11903\n11930\n12013\n12031\n12103\n12130\n12301\n12310\n13001\n13010\n13011\n13012\n13013\n13014\n13015\n13016\n13017\n13018\n13019\n13021\n13031\n13041\n13051\n13061\n13071\n13081\n13091\n13100\n13101\n13102\n13103\n13104\n13105\n13106\n13107\n13108\n13109\n13110\n13120\n13130\n13140\n13150\n13160\n13170\n13180\n13190\n13201\n13210\n13301\n13310\n13401\n13410\n13501\n13510\n13601\n13610\n13701\n13710\n13801\n13810\n13901\n13910\n14013\n14031\n14103\n14130\n14301\n14310\n15013\n15031\n15103\n15130\n15301\n15310\n16013\n16031\n16103\n16130\n16301\n16310\n17013\n17031\n17103\n17130\n17301\n17310\n18013\n18031\n18103\n18130\n18301\n18310\n19013\n19031\n19103\n19130\n19301\n19310\n20113\n20131\n20311\n21013\n21031\n21103\n21130\n21301\n21310\n23011\n23101\n23110\n216", regex=False).exit(0)

@check50.check()
def numero_15():
    """numero_15"""
    check50.run("python3 numeros_introescos.py").stdin("33110\n36110", prompt=False).stdout("33110\n34011\n34101\n34110\n35011\n35101\n35110\n36011\n36101\n36110\n10", regex=False).exit(0)

@check50.check()
def numero_16():
    """numero_16"""
    check50.run("python3 numeros_introescos.py").stdin("10000\n10001", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def numero_17():
    """numero_17"""
    check50.run("python3 numeros_introescos.py").stdin("100\n300", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def numero_18():
    """numero_18"""
    check50.run("python3 numeros_introescos.py").stdin("871013\n899999", prompt=False).stdout("871013\n871031\n871103\n871130\n871301\n871310\n873011\n873101\n873110\n880113\n880131\n880311\n881013\n881031\n881103\n881130\n881301\n881310\n883011\n883101\n883110\n890113\n890131\n890311\n891013\n891031\n891103\n891130\n891301\n891310\n893011\n893101\n893110\n33", regex=False).exit(0)

@check50.check()
def numero_19():
    """numero_19"""
    check50.run("python3 numeros_introescos.py").stdin("881310\n889999", prompt=False).stdout("881310\n883011\n883101\n883110\n4", regex=False).exit(0)

@check50.check()
def numero_20():
    """numero_20"""
    check50.run("python3 numeros_introescos.py").stdin("1234\n1999", prompt=False).stdout("1301\n1310\n2", regex=False).exit(0)

@check50.check()
def numero_21():
    """numero_21"""
    check50.run("python3 numeros_introescos.py").stdin("1235\n2000", prompt=False).stdout("1301\n1310\n2", regex=False).exit(0)

@check50.check()
def numero_22():
    """numero_22"""
    check50.run("python3 numeros_introescos.py").stdin("11031103\n11031130", prompt=False).stdout("11031103\n11031104\n11031105\n11031106\n11031107\n11031108\n11031109\n11031110\n11031111\n11031112\n11031113\n11031114\n11031115\n11031116\n11031117\n11031118\n11031119\n11031120\n11031121\n11031122\n11031123\n11031124\n11031125\n11031126\n11031127\n11031128\n11031129\n11031130\n28", regex=False).exit(0)

@check50.check()
def numero_23():
    """numero_23"""
    check50.run("python3 numeros_introescos.py").stdin("11031119\n11031122", prompt=False).stdout("11031119\n11031120\n11031121\n11031122\n4", regex=False).exit(0)

@check50.check()
def numero_24():
    """numero_24"""
    check50.run("python3 numeros_introescos.py").stdin("1\n1015", prompt=False).stdout("1013\n1", regex=False).exit(0)

@check50.check()
def numero_25():
    """numero_25"""
    check50.run("python3 numeros_introescos.py").stdin("2\n1234", prompt=False).stdout("1013\n1031\n1103\n1130\n4", regex=False).exit(0)

@check50.check()
def numero_26():
    """numero_26"""
    check50.run("python3 numeros_introescos.py").stdin("1111\n1111", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def numero_27():
    """numero_27"""
    check50.run("python3 numeros_introescos.py").stdin("9999\n9999", prompt=False).stdout("0", regex=False).exit(0)

@check50.check()
def numero_28():
    """numero_28"""
    check50.run("python3 numeros_introescos.py").stdin("1000\n10000", prompt=False).stdout("1013\n1031\n1103\n1130\n1301\n1310\n3011\n3101\n3110\n9", regex=False).exit(0)

@check50.check()
def numero_29():
    """numero_29"""
    check50.run("python3 numeros_introescos.py").stdin("1000\n25000", prompt=False).stdout("1013\n1031\n1103\n1130\n1301\n1310\n3011\n3101\n3110\n10013\n10031\n10103\n10113\n10123\n10130\n10131\n10132\n10133\n10134\n10135\n10136\n10137\n10138\n10139\n10143\n10153\n10163\n10173\n10183\n10193\n10213\n10231\n10301\n10310\n10311\n10312\n10313\n10314\n10315\n10316\n10317\n10318\n10319\n10321\n10331\n10341\n10351\n10361\n10371\n10381\n10391\n10413\n10431\n10513\n10531\n10613\n10631\n10713\n10731\n10813\n10831\n10913\n10931\n11003\n11013\n11023\n11030\n11031\n11032\n11033\n11034\n11035\n11036\n11037\n11038\n11039\n11043\n11053\n11063\n11073\n11083\n11093\n11103\n11130\n11203\n11230\n11300\n11301\n11302\n11303\n11304\n11305\n11306\n11307\n11308\n11309\n11310\n11320\n11330\n11340\n11350\n11360\n11370\n11380\n11390\n11403\n11430\n11503\n11530\n11603\n11630\n11703\n11730\n11803\n11830\n11903\n11930\n12013\n12031\n12103\n12130\n12301\n12310\n13001\n13010\n13011\n13012\n13013\n13014\n13015\n13016\n13017\n13018\n13019\n13021\n13031\n13041\n13051\n13061\n13071\n13081\n13091\n13100\n13101\n13102\n13103\n13104\n13105\n13106\n13107\n13108\n13109\n13110\n13120\n13130\n13140\n13150\n13160\n13170\n13180\n13190\n13201\n13210\n13301\n13310\n13401\n13410\n13501\n13510\n13601\n13610\n13701\n13710\n13801\n13810\n13901\n13910\n14013\n14031\n14103\n14130\n14301\n14310\n15013\n15031\n15103\n15130\n15301\n15310\n16013\n16031\n16103\n16130\n16301\n16310\n17013\n17031\n17103\n17130\n17301\n17310\n18013\n18031\n18103\n18130\n18301\n18310\n19013\n19031\n19103\n19130\n19301\n19310\n20113\n20131\n20311\n21013\n21031\n21103\n21130\n21301\n21310\n23011\n23101\n23110\n225", regex=False).exit()