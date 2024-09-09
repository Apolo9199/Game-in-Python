from random import *
#Cambios hechos en otra plataforma*


def EfectosPorTiempo1 (number):
    if number.efecto1 == 'avida':
        number.maxhealth -= number.efecton1
        number.health -= number.efecton1
        print ('Se te ha acabado tu aumento de vida')

    elif number.efecto1 == 'avidapor':
        number.maxhealth = number.maxhealth - number.maxhealth * number.efecton1 / 100
        number.health = number.health - number.health * number.efecton1 / 100
        print ('Se te ha acabado tu aumento de vida')

    elif number.efecto1 == 'bvida':
        number.maxhealth += number.efecton1
        number.health += number.efecton1
        print ('Se te ha acabado tu reducción de vida')

    elif number.efecto1 == 'bvidapor':
        number.maxhealth = number.maxhealth + number.maxhealth * number.efecton1 / 100
        number.health = number.health + number.health * number.efecton1 / 100
        print ('Se te ha acabado tu reducción de vida')

    elif number.efecto1 == 'cura':
        number.health += number.efecton1
        print ('Se te ha aplicado la curación')

    elif number.efecto1 == 'curapor':
        number.health = number.health + number.health * number.efecton1 / 100
        print ('Se te ha aplicado la curación')

    elif number.efecto1 == 'daño':
        number.health -= number.efecton1
        print ('Se te ha aplicado el daño')

    elif number.efecto1 == 'dañopor':
        number.health = number.health - number.health * number.efecton1 / 100
        print ('Se te ha aplicado el daño')

    elif number.efecto1 == 'adefense':
        number.defense -= number.efecton1
        print ('Se te ha acabado tu aumento de defensa')

    elif number.efecto1 == 'adefensepor':
        number.defense = number.defense - number.defense * number.efecton1 / 100
        print ('Se te ha acabado tu aumento de defensa')

    elif number.efecto1 == 'bdefense':
        number.defense += number.efecton1
        print ('Se te ha acabado tu reducción de defensa')

    elif number.efecto1 == 'bdefensepor':
        number.defense = number.defense + number.defense * number.efecton1 / 100
        print ('Se te ha acabado tu reducción de defensa')

    elif number.efecto1 == 'apower':
        number.power -= number.efecton1
        print ('Se te ha acabado tu aumento de poder')

    elif number.efecto1 == 'apowerpor':
        number.power = number.power - number.power * number.efecton1 / 100
        print ('Se te ha acabado tu aumento de poder')

    elif number.efecto1 == 'bpower':
        number.power += number.efecton1
        print ('Se te ha acabado tu reducción de poder')

    elif number.efecto1 == 'bpowerpor':
        number.power = number.power + number.power * number.efecton1 / 100
        print ('Se te ha acabado tu reducción de poder')

def EfectosPorTiempo2 (number):
    if number.efecto2 == 'avida':
        number.maxhealth -= number.efecton2
        number.health -= number.efecton2
        print ('Se te ha acabado tu aumento de vida')

    elif number.efecto2 == 'avidapor':
        number.maxhealth = number.maxhealth - number.maxhealth * number.efecton2 / 100
        number.health = number.health - number.health * number.efecton2 / 100
        print ('Se te ha acabado tu aumento de vida')

    elif number.efecto2 == 'bvida':
        number.maxhealth += number.efecton2
        number.health += number.efecton2
        print ('Se te ha acabado tu reducción de vida')

    elif number.efecto2 == 'bvidapor':
        number.maxhealth = number.maxhealth + number.maxhealth * number.efecton2 / 100
        number.health = number.health + number.health * number.efecton2 / 100
        print ('Se te ha acabado tu reducción de vida')

    elif number.efecto2 == 'cura':
        number.health += number.efecton2
        print ('Se te ha aplicado la curación')

    elif number.efecto2 == 'curapor':
        number.health = number.health + number.health * number.efecton2 / 100
        print ('Se te ha aplicado la curación')

    elif number.efecto2 == 'daño':
        number.health -= number.efecton2
        print ('Se te ha aplicado el daño')

    elif number.efecto2 == 'dañopor':
        number.health = number.health - number.health * number.efecton2 / 100
        print ('Se te ha aplicado el daño')

    elif number.efecto2 == 'adefense':
        number.defense -= number.efecton2
        print ('Se te ha acabado tu aumento de defensa')

    elif number.efecto2 == 'adefensepor':
        number.defense = number.defense - number.defense * number.efecton2 / 100
        print ('Se te ha acabado tu aumento de defensa')

    elif number.efecto2 == 'bdefense':
        number.defense += number.efecton2
        print ('Se te ha acabado tu reducción de defensa')

    elif number.efecto2 == 'bdefensepor':
        number.defense = number.defense + number.defense * number.efecton2 / 100
        print ('Se te ha acabado tu reducción de defensa')

    elif number.efecto2 == 'apower':
        number.power -= number.efecton2
        print ('Se te ha acabado tu aumento de poder')

    elif number.efecto2 == 'apowerpor':
        number.power = number.power - number.power * number.efecton2 / 100
        print ('Se te ha acabado tu aumento de poder')

    elif number.efecto2 == 'bpower':
        number.power += number.efecton2
        print ('Se te ha acabado tu reducción de poder')

    elif number.efecto2 == 'bpowerpor':
        number.power = number.power + number.power * number.efecton2 / 100
        print ('Se te ha acabado tu reducción de poder')

def EfectosPorTiempo3 (number):
    if number.efecto3 == 'avida':
        number.maxhealth -= number.efecton3
        number.health -= number.efecton3
        print ('Se te ha acabado tu aumento de vida')

    elif number.efecto3 == 'avidapor':
        number.maxhealth = number.maxhealth - number.maxhealth * number.efecton3 / 100
        number.health = number.health - number.health * number.efecton3 / 100
        print ('Se te ha acabado tu aumento de vida')

    elif number.efecto3 == 'bvida':
        number.maxhealth += number.efecton3
        number.health += number.efecton3
        print ('Se te ha acabado tu reducción de vida')

    elif number.efecto3 == 'bvidapor':
        number.maxhealth = number.maxhealth + number.maxhealth * number.efecton3 / 100
        number.health = number.health + number.health * number.efecton3 / 100
        print ('Se te ha acabado tu reducción de vida')

    elif number.efecto3 == 'cura':
        number.health += number.efecton3
        print ('Se te ha aplicado la curación')

    elif number.efecto3 == 'curapor':
        number.health = number.health + number.health * number.efecton3 / 100
        print ('Se te ha aplicado la curación')

    elif number.efecto3 == 'daño':
        number.health -= number.efecton3
        print ('Se te ha aplicado el daño')

    elif number.efecto3 == 'dañopor':
        number.health = number.health - number.health * number.efecton3 / 100
        print ('Se te ha aplicado el daño')

    elif number.efecto3 == 'adefense':
        number.defense -= number.efecton3
        print ('Se te ha acabado tu aumento de defensa')

    elif number.efecto3 == 'adefensepor':
        number.defense = number.defense - number.defense * number.efecton3 / 100
        print ('Se te ha acabado tu aumento de defensa')

    elif number.efecto3 == 'bdefense':
        number.defense += number.efecton3
        print ('Se te ha acabado tu reducción de defensa')

    elif number.efecto3 == 'bdefensepor':
        number.defense = number.defense + number.defense * number.efecton3 / 100
        print ('Se te ha acabado tu reducción de defensa')

    elif number.efecto3 == 'apower':
        number.power -= number.efecton3
        print ('Se te ha acabado tu aumento de poder')

    elif number.efecto3 == 'apowerpor':
        number.power = number.power - number.power * number.efecton3 / 100
        print ('Se te ha acabado tu aumento de poder')

    elif number.efecto3 == 'bpower':
        number.power += number.efecton3
        print ('Se te ha acabado tu reducción de poder')

    elif number.efecto3 == 'bpowerpor':
        number.power = number.power + number.power * number.efecton3 / 100
        print ('Se te ha acabado tu reducción de poder')

def EfectosPorTiempo4 (number):
    if number.efecto4 == 'avida':
        number.maxhealth -= number.efecton4
        number.health -= number.efecton4
        print ('Se te ha acabado tu aumento de vida')

    elif number.efecto4 == 'avidapor':
        number.maxhealth = number.maxhealth - number.maxhealth * number.efecton4 / 100
        number.health = number.health - number.health * number.efecton4 / 100
        print ('Se te ha acabado tu aumento de vida')

    elif number.efecto4 == 'bvida':
        number.maxhealth += number.efecton4
        number.health += number.efecton4
        print ('Se te ha acabado tu reducción de vida')

    elif number.efecto4 == 'bvidapor':
        number.maxhealth = number.maxhealth + number.maxhealth * number.efecton4 / 100
        number.health = number.health + number.health * number.efecton4 / 100
        print ('Se te ha acabado tu reducción de vida')

    elif number.efecto4 == 'cura':
        number.health += number.efecton4
        print ('Se te ha aplicado la curación')

    elif number.efecto4 == 'curapor':
        number.health = number.health + number.health * number.efecton4 / 100
        print ('Se te ha aplicado la curación')

    elif number.efecto4 == 'daño':
        number.health -= number.efecton4
        print ('Se te ha aplicado el daño')

    elif number.efecto4 == 'dañopor':
        number.health = number.health - number.health * number.efecton4 / 100
        print ('Se te ha aplicado el daño')

    elif number.efecto4 == 'adefense':
        number.defense -= number.efecton4
        print ('Se te ha acabado tu aumento de defensa')

    elif number.efecto4 == 'adefensepor':
        number.defense = number.defense - number.defense * number.efecton4 / 100
        print ('Se te ha acabado tu aumento de defensa')

    elif number.efecto4 == 'bdefense':
        number.defense += number.efecton4
        print ('Se te ha acabado tu reducción de defensa')

    elif number.efecto4 == 'bdefensepor':
        number.defense = number.defense + number.defense * number.efecton4 / 100
        print ('Se te ha acabado tu reducción de defensa')

    elif number.efecto4 == 'apower':
        number.power -= number.efecton4
        print ('Se te ha acabado tu aumento de poder')

    elif number.efecto4 == 'apowerpor':
        number.power = number.power - number.power * number.efecton4 / 100
        print ('Se te ha acabado tu aumento de poder')

    elif number.efecto4 == 'bpower':
        number.power += number.efecton4
        print ('Se te ha acabado tu reducción de poder')

    elif number.efecto4 == 'bpowerpor':
        number.power = number.power + number.power * number.efecton4 / 100
        print ('Se te ha acabado tu reducción de poder')
    
def EfectosPorTiempo5 (number):
    if number.efecto1 == 'avida':
        number.maxhealth -= number.efecton5
        number.health -= number.efecton5
        print ('Se te ha acabado tu aumento de vida')

    elif number.efecto5 == 'avidapor':
        number.maxhealth = number.maxhealth - number.maxhealth * number.efecton5 / 100
        number.health = number.health - number.health * number.efecton5 / 100
        print ('Se te ha acabado tu aumento de vida')

    elif number.efecto5 == 'bvida':
        number.maxhealth += number.efecton5
        number.health += number.efecton5
        print ('Se te ha acabado tu reducción de vida')

    elif number.efecto5 == 'bvidapor':
        number.maxhealth = number.maxhealth + number.maxhealth * number.efecton5 / 100
        number.health = number.health + number.health * number.efecton5 / 100
        print ('Se te ha acabado tu reducción de vida')

    elif number.efecto5 == 'cura':
        number.health += number.efecton5
        print ('Se te ha aplicado la curación')

    elif number.efecto5 == 'curapor':
        number.health = number.health + number.health * number.efecton5 / 100
        print ('Se te ha aplicado la curación')

    elif number.efecto5 == 'daño':
        number.health -= number.efecton5
        print ('Se te ha aplicado el daño')

    elif number.efecto5 == 'dañopor':
        number.health = number.health - number.health * number.efecton5 / 100
        print ('Se te ha aplicado el daño')

    elif number.efecto5 == 'adefense':
        number.defense -= number.efecton5
        print ('Se te ha acabado tu aumento de defensa')

    elif number.efecto5 == 'adefensepor':
        number.defense = number.defense - number.defense * number.efecton5 / 100
        print ('Se te ha acabado tu aumento de defensa')

    elif number.efecto5 == 'bdefense':
        number.defense += number.efecton5
        print ('Se te ha acabado tu reducción de defensa')

    elif number.efecto5 == 'bdefensepor':
        number.defense = number.defense + number.defense * number.efecton5 / 100
        print ('Se te ha acabado tu reducción de defensa')

    elif number.efecto5 == 'apower':
        number.power -= number.efecton5
        print ('Se te ha acabado tu aumento de poder')

    elif number.efecto5 == 'apowerpor':
        number.power = number.power - number.power * number.efecton5 / 100
        print ('Se te ha acabado tu aumento de poder')

    elif number.efecto5 == 'bpower':
        number.power += number.efecton5
        print ('Se te ha acabado tu reducción de poder')

    elif number.efecto5 == 'bpowerpor':
        number.power = number.power + number.power * number.efecton5 / 100
        print ('Se te ha acabado tu reducción de poder')

def EfectosPorTiempoComprobando11 ():
    if uno.efecto1 != '':
        if uno.tiempo1 == uno.nturnos:
            EfectosPorTiempo1 (uno)

def EfectosPorTiempoComprobando12 ():
    if uno.efecto2 != '':
        if uno.tiempo2 == uno.nturnos:
            EfectosPorTiempo2 (uno)

def EfectosPorTiempoComprobando13 ():
    if uno.efecto3 != '':
        if uno.tiempo3 == uno.nturnos:
            EfectosPorTiempo3 (uno)

def EfectosPorTiempoComprobando14 ():
    if uno.efecto4 != '':
        if uno.tiempo4 == uno.nturnos:
            EfectosPorTiempo4 (uno)

def EfectosPorTiempoComprobando15 ():
    if uno.efecto5 != '':
        if uno.tiempo5 == uno.nturnos:
            EfectosPorTiempo5 (uno)

def EfectosPorTiempoComprobando21 ():
    if dos.efecto1 != '':
        if dos.tiempo1 == dos.nturnos:
            EfectosPorTiempo1 (dos)

def EfectosPorTiempoComprobando22 ():
    if dos.efecto2 != '':
        if dos.tiempo2 == dos.nturnos:
            EfectosPorTiempo2 (dos)

def EfectosPorTiempoComprobando23 ():
    if dos.efecto3 != '':
        if dos.tiempo3 == dos.nturnos:
            EfectosPorTiempo3 (dos)

def EfectosPorTiempoComprobando24 ():
    if dos.efecto4 != '':
        if dos.tiempo4 == dos.nturnos:
            EfectosPorTiempo4 (dos)

def EfectosPorTiempoComprobando25 ():
    if dos.efecto5 != '':
        if dos.tiempo5 == dos.nturnos:
            EfectosPorTiempo5 (dos)

def EfectosPorTiempoComprobando31 ():
    if tres.efecto1 != '':
        if tres.tiempo1 == tres.nturnos:
            EfectosPorTiempo1 (tres)

def EfectosPorTiempoComprobando32 ():
    if tres.efecto2 != '':
        if tres.tiempo2 == tres.nturnos:
            EfectosPorTiempo2 (tres)

def EfectosPorTiempoComprobando33 ():
    if tres.efecto3 != '':
        if tres.tiempo3 == tres.nturnos:
            EfectosPorTiempo3 (tres)

def EfectosPorTiempoComprobando34 ():
    if tres.efecto4 != '':
        if tres.tiempo4 == tres.nturnos:
            EfectosPorTiempo4 (tres)

def EfectosPorTiempoComprobando35 ():
    if tres.efecto5 != '':
        if tres.tiempo5 == tres.nturnos:
            EfectosPorTiempo5 (tres)

def EfectosPorTiempoComprobando41 ():
    if cuatro.efecto1 != '':
        if cuatro.tiempo1 == cuatro.nturnos:
            EfectosPorTiempo1 (cuatro)

def EfectosPorTiempoComprobando42 ():
    if cuatro.efecto2 != '':
        if cuatro.tiempo2 == cuatro.nturnos:
            EfectosPorTiempo2 (cuatro)

def EfectosPorTiempoComprobando43 ():
    if cuatro.efecto3 != '':
        if cuatro.tiempo3 == cuatro.nturnos:
            EfectosPorTiempo3 (cuatro)

def EfectosPorTiempoComprobando44 ():
    if cuatro.efecto4 != '':
        if cuatro.tiempo4 == cuatro.nturnos:
            EfectosPorTiempo4 (cuatro)

def EfectosPorTiempoComprobando45 ():
    if uno.efecto5 != '':
        if uno.tiempo5 == uno.nturnos:
            EfectosPorTiempo5 (uno)

def EfectosPorTiempoComprobando51 ():
    if cinco.efecto1 != '':
        if cinco.tiempo1 == cinco.nturnos:
            EfectosPorTiempo1 (cinco)

def EfectosPorTiempoComprobando52 ():
    if cinco.efecto2 != '':
        if cinco.tiempo2 == cinco.nturnos:
            EfectosPorTiempo2 (cinco)

def EfectosPorTiempoComprobando53 ():
    if cinco.efecto3 != '':
        if cinco.tiempo3 == cinco.nturnos:
            EfectosPorTiempo3 (cinco)

def EfectosPorTiempoComprobando54 ():
    if cinco.efecto4 != '':
        if cinco.tiempo4 == cinco.nturnos:
            EfectosPorTiempo4 (cinco)

def EfectosPorTiempoComprobando55 ():
    if cinco.efecto5 != '':
        if cinco.tiempo5 == cinco.nturnos:
            EfectosPorTiempo5 (cinco)

def EfectosPorTiempoComprobando61 ():
    if seis.efecto1 != '':
        if seis.tiempo1 == seis.nturnos:
            EfectosPorTiempo1 (seis)

def EfectosPorTiempoComprobando62 ():
    if seis.efecto2 != '':
        if seis.tiempo2 == seis.nturnos:
            EfectosPorTiempo2 (seis)

def EfectosPorTiempoComprobando63 ():
    if seis.efecto3 != '':
        if seis.tiempo3 == seis.nturnos:
            EfectosPorTiempo3 (seis)

def EfectosPorTiempoComprobando64 ():
    if seis.efecto4 != '':
        if seis.tiempo4 == seis.nturnos:
            EfectosPorTiempo4 (seis)

def EfectosPorTiempoComprobando65 ():
    if seis.efecto5 != '':
        if seis.tiempo5 == seis.nturnos:
            EfectosPorTiempo5 (seis)

def EfectosPorTiempoComprobandobb1 ():
    if boxblue.efecto1 != '':
        if boxblue.tiempo1 == boxblue.nturnos:
            EfectosPorTiempo1 (boxblue)

def EfectosPorTiempoComprobandobb2 ():
    if boxblue.efecto2 != '':
        if boxblue.tiempo2 == boxblue.nturnos:
            EfectosPorTiempo2 (boxblue)

def EfectosPorTiempoComprobandobb3 ():
    if boxblue.efecto3 != '':
        if boxblue.tiempo3 == boxblue.nturnos:
            EfectosPorTiempo3 (boxblue)

def EfectosPorTiempoComprobandobb4 ():
    if boxblue.efecto4 != '':
        if boxblue.tiempo4 == boxblue.nturnos:
            EfectosPorTiempo4 (boxblue)

def EfectosPorTiempoComprobandobb5 ():
    if boxblue.efecto5 != '':
        if boxblue.tiempo5 == boxblue.nturnos:
            EfectosPorTiempo5 (boxblue)

def EfectosPorTiempoComprobandobr1 ():
    if boxred.efecto1 != '':
        if boxred.tiempo1 == boxred.nturnos:
            EfectosPorTiempo1 (boxred)

def EfectosPorTiempoComprobandobr2 ():
    if boxred.efecto2 != '':
        if boxred.tiempo2 == boxred.nturnos:
            EfectosPorTiempo2 (boxred)

def EfectosPorTiempoComprobandobr3 ():
    if boxred.efecto3 != '':
        if boxred.tiempo3 == boxred.nturnos:
            EfectosPorTiempo3 (boxred)

def EfectosPorTiempoComprobandobr4 ():
    if boxred.efecto4 != '':
        if boxred.tiempo4 == boxred.nturnos:
            EfectosPorTiempo4 (boxred)

def EfectosPorTiempoComprobandobr5 ():
    if boxred.efecto5 != '':
        if boxred.tiempo5 == boxred.nturnos:
            EfectosPorTiempo5 (boxred)

def tempo1 ():
    EfectosPorTiempoComprobando11()
    EfectosPorTiempoComprobando12()
    EfectosPorTiempoComprobando13()
    EfectosPorTiempoComprobando14()
    EfectosPorTiempoComprobando15()

def tempo2 ():
    EfectosPorTiempoComprobando21()
    EfectosPorTiempoComprobando22()
    EfectosPorTiempoComprobando23()
    EfectosPorTiempoComprobando24()
    EfectosPorTiempoComprobando25()

def tempo3 ():
    EfectosPorTiempoComprobando31()
    EfectosPorTiempoComprobando32()
    EfectosPorTiempoComprobando33()
    EfectosPorTiempoComprobando34()
    EfectosPorTiempoComprobando35()

def tempo4 ():
    EfectosPorTiempoComprobando41()
    EfectosPorTiempoComprobando42()
    EfectosPorTiempoComprobando43()
    EfectosPorTiempoComprobando44()
    EfectosPorTiempoComprobando45()

def tempo5 ():
    EfectosPorTiempoComprobando51()
    EfectosPorTiempoComprobando52()
    EfectosPorTiempoComprobando53()
    EfectosPorTiempoComprobando54()
    EfectosPorTiempoComprobando55()

def tempo6 ():
    EfectosPorTiempoComprobando61()
    EfectosPorTiempoComprobando62()
    EfectosPorTiempoComprobando63()
    EfectosPorTiempoComprobando64()
    EfectosPorTiempoComprobando65()

def tempoboxblue ():
    EfectosPorTiempoComprobandobb1()
    EfectosPorTiempoComprobandobb2()
    EfectosPorTiempoComprobandobb3()
    EfectosPorTiempoComprobandobb4()
    EfectosPorTiempoComprobandobb5()

def tempoboxred ():
    EfectosPorTiempoComprobandobr1()
    EfectosPorTiempoComprobandobr2()
    EfectosPorTiempoComprobandobr3()
    EfectosPorTiempoComprobandobr4()
    EfectosPorTiempoComprobandobr5()

def checar_campos ():
    if campo.lluvia > 0:
        campo.lluvia = 0
        print ('Deja de llover')
    if campo.nevar > 0:
        campo.nevar = 0
        print ('Para de nevar')
    if campo.hierba > 0:
        campo.hierba = 0
        print ('El encantamiento de la hierba pierde su poder')
    if campo.sol > 0:
        campo.sol = 0
        print ('El poder solar se calma')
    if campo.purificador > 0:
        campo.purificador = 0
        print ('Otro campo aparece y sustituye a la purificación')

def refuerzos2 ():
    if uno.tipo == 0:
        print (uno.name, 'saca de la manga 50 de energia')
        uno.energy += 50
    elif uno.tipo == 1:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        uno.defense += 0.25
    elif uno.tipo == 3 or uno.tipo == 4:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        uno.power += 0.25
    elif uno.tipo == 2:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        uno.power += 0.15
        uno.defense += 0.15
    if dos.tipo == 0:
        print (dos.name, 'saca de la manga 50 de energia')
        dos.energy += 50
    elif dos.tipo == 1:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        dos.defense += 0.25
    elif dos.tipo == 3 or dos.tipo == 4:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        dos.power += 0.25
    elif dos.tipo == 2:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        dos.power += 0.15
        dos.defense += 0.15

def refuerzos3 ():
    if uno.tipo == 0:
        print (uno.name, 'saca de la manga 50 de energia')
        uno.energy += 50
    elif uno.tipo == 1:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        uno.defense += 0.25
    elif uno.tipo == 3 or uno.tipo == 4:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        uno.power += 0.25
    elif uno.tipo == 2:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        uno.power += 0.15
        uno.defense += 0.15
    if dos.tipo == 0:
        print (dos.name, 'saca de la manga 50 de energia')
        dos.energy += 50
    elif dos.tipo == 1:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        dos.defense += 0.25
    elif dos.tipo == 3 or dos.tipo == 4:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        dos.defense += 0.25
    elif dos.tipo == 2:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        dos.power += 0.15
        dos.defense += 0.15
    if tres.tipo == 0:
        print (tres.name, 'saca de la manga 50 de energia')
        tres.energy += 50
    elif tres.tipo == 1:
        print ('¡', tres.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        tres.defense += 0.25
    elif tres.tipo == 3 or tres.tipo == 4:
        print ('¡', tres.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        tres.power += 0.25
    elif tres.tipo == 2:
        print ('¡', tres.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        tres.power += 0.15
        tres.defense += 0.15

def refuerzos4 ():
    if uno.tipo == 0:
        print (uno.name, 'saca de la manga 50 de energia')
        uno.energy += 50
    elif uno.tipo == 1:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        uno.defense += 0.25
    elif uno.tipo == 3 or uno.tipo == 4:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        uno.power += 0.25
    elif uno.tipo == 2:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        uno.power += 0.15
        uno.defense += 0.15
    if dos.tipo == 0:
        print (dos.name, 'saca de la manga 50 de energia')
        dos.energy += 50
    elif dos.tipo == 1:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        dos.defense += 0.25
    elif dos.tipo == 3 or dos.tipo == 4:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        dos.defense += 0.25
    elif dos.tipo == 2:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        dos.power += 0.15
        dos.defense += 0.15
    if tres.tipo == 0:
        print (tres.name, 'saca de la manga 50 de energia')
        tres.energy += 50
    elif tres.tipo == 1:
        print ('¡', tres.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        tres.defense += 0.25
    elif tres.tipo == 3 or tres.tipo == 4:
        print ('¡', tres.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        tres.power += 0.25
    elif tres.tipo == 2:
        print ('¡', tres.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        tres.power += 0.15
        tres.defense += 0.15
    if cuatro.tipo == 0:
        print (cuatro.name, 'saca de la manga 50 de energia')
        cuatro.energy += 50
    elif cuatro.tipo == 1:
        print ('¡', cuatro.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        cuatro.defense += 0.25
    elif cuatro.tipo == 3 or cuatro.tipo == 4:
        print ('¡', cuatro.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        cuatro.power += 0.25
    elif cuatro.tipo == 2:
        print ('¡', cuatro.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        cuatro.power += 0.15
        cuatro.defense += 0.15

def refuerzos6 ():
    if uno.tipo == 0:
        print (uno.name, 'saca de la manga 50 de energia')
        uno.energy += 50
    elif uno.tipo == 1:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        uno.defense += 0.25
    elif uno.tipo == 3 or uno.tipo == 4:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        uno.power += 0.25
    elif uno.tipo == 2:
        print ('¡', uno.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        uno.power += 0.15
        uno.defense += 0.15
    if dos.tipo == 0:
        print (dos.name, 'saca de la manga 50 de energia')
        dos.energy += 50
    elif dos.tipo == 1:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        dos.defense += 0.25
    elif dos.tipo == 3 or dos.tipo == 4:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        dos.defense += 0.25
    elif dos.tipo == 2:
        print ('¡', dos.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        dos.power += 0.15
        dos.defense += 0.15
    if tres.tipo == 0:
        print (tres.name, 'saca de la manga 50 de energia')
        tres.energy += 50
    elif tres.tipo == 1:
        print ('¡', tres.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        tres.defense += 0.25
    elif tres.tipo == 3 or tres.tipo == 4:
        print ('¡', tres.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        tres.power += 0.25
    elif tres.tipo == 2:
        print ('¡', tres.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        tres.power += 0.15
        tres.defense += 0.15
    if cuatro.tipo == 0:
        print (cuatro.name, 'saca de la manga 50 de energia')
        cuatro.energy += 50
    elif cuatro.tipo == 1:
        print ('¡', cuatro.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        cuatro.defense += 0.25
    elif cuatro.tipo == 3 or cuatro.tipo == 4:
        print ('¡', cuatro.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        cuatro.power += 0.25
    elif cuatro.tipo == 2:
        print ('¡', cuatro.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        cuatro.power += 0.15
        cuatro.defense += 0.15
    if cinco.tipo == 0:
        print (cinco.name, 'saca de la manga 50 de energia')
        cinco.energy += 50
    elif cinco.tipo == 1:
        print ('¡', cinco.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        cinco.defense += 0.25
    elif cinco.tipo == 3 or cinco.tipo == 4:
        print ('¡', cinco.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        cinco.power += 0.25
    elif cinco.tipo == 2:
        print ('¡', cinco.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        cinco.power += 0.15
        cinco.defense += 0.15
    if seis.tipo == 0:
        print (seis.name, 'saca de la manga 50 de energia')
        seis.energy += 50
    elif seis.tipo == 1:
        print ('¡', seis.name, '!¡Llegan refuerzos! Te equipas con más armadura aumentando tu defensa en 0.25')
        seis.defense += 0.25
    elif seis.tipo == 3 or seis.tipo == 4:
        print ('¡', seis.name, '!¡Llegan refuerzos! Te trajeron un libro de hechizos con el que aumentas tu poder en 0.25')
        seis.power += 0.25
    elif seis.tipo == 2:
        print ('¡', seis.name, '!¡Llegan refuerzos! Te equipas con un artefacto que aumenta tu poder y tu defensa en 0.15')
        seis.power += 0.15
        seis.defense += 0.15

def estampida2 ():
    print ('Una estampida cruza la arena aturdiendo a todos, bajando sus precisiones en 8')
    uno.preci1 -= 8
    uno.preci2 -= 8
    uno.preci3 -= 8
    uno.precicura -= 8
    uno.precienergia -= 8
    dos.preci1 -= 8
    dos.preci2 -= 8
    dos.preci3 -= 8
    dos.precicura -= 8
    dos.precienergia -= 8

def estampida3 ():
    print ('Una estampida cruza la arena aturdiendo a todos, bajando sus precisiones en 8')
    uno.preci1 -= 8
    uno.preci2 -= 8
    uno.preci3 -= 8
    uno.precicura -= 8
    uno.precienergia -= 8
    dos.preci1 -= 8
    dos.preci2 -= 8
    dos.preci3 -= 8
    dos.precicura -= 8
    dos.precienergia -= 8
    tres.preci1 -= 8
    tres.preci2 -= 8
    tres.preci3 -= 8
    tres.precicura -= 8
    tres.precienergia -= 8

def estampida4 ():
    print ('Una estampida cruza la arena aturdiendo a todos, bajando sus precisiones en 8')
    uno.preci1 -= 8
    uno.preci2 -= 8
    uno.preci3 -= 8
    uno.precicura -= 8
    uno.precienergia -= 8
    dos.preci1 -= 8
    dos.preci2 -= 8
    dos.preci3 -= 8
    dos.precicura -= 8
    dos.precienergia -= 8
    tres.preci1 -= 8
    tres.preci2 -= 8
    tres.preci3 -= 8
    tres.precicura -= 8
    tres.precienergia -= 8
    cuatro.preci1 -= 8
    cuatro.preci2 -= 8
    cuatro.preci3 -= 8
    cuatro.precicura -= 8
    cuatro.precienergia -= 8

def estampida6 ():
    print ('Una estampida cruza la arena aturdiendo a todos, bajando sus precisiones en 4')
    uno.preci1 -= 4
    uno.preci2 -= 4
    uno.preci3 -= 4
    uno.precicura -= 4
    uno.precienergia -= 4
    dos.preci1 -= 4
    dos.preci2 -= 4
    dos.preci3 -= 4
    dos.precicura -= 4
    dos.precienergia -= 4
    tres.preci1 -= 4
    tres.preci2 -= 4
    tres.preci3 -= 4
    tres.precicura -= 4
    tres.precienergia -= 4
    cuatro.preci1 -= 4
    cuatro.preci2 -= 4
    cuatro.preci3 -= 4
    cuatro.precicura -= 4
    cuatro.precienergia -= 4
    cinco.preci1 -= 4
    cinco.preci2 -= 4
    cinco.preci3 -= 4
    cinco.precicura -= 4
    cinco.precienergia -= 4
    seis.preci1 -= 4
    seis.preci2 -= 4
    seis.preci3 -= 4
    seis.precicura -= 4
    seis.precienergia -= 4

def eliminar_cargas2 ():
    uno.carga_cura = 0
    uno.carga_hemorragia = 0
    uno.carga_hielo = 0
    uno.carga_maldita = 0
    uno.carga_paralizado = 0
    uno.carga_quemado = 0
    uno.carga_sangrado = 0
    uno.carga_stun = 0
    uno.carga_veneno = 0
    dos.carga_cura = 0
    dos.carga_hemorragia = 0
    dos.carga_hielo = 0
    dos.carga_paralizado = 0
    dos.carga_maldita = 0
    dos.carga_quemado = 0
    dos.carga_sangrado = 0
    dos.carga_stun = 0
    dos.carga_veneno = 0
    print ('Se purifica el ambiente', '\n')

def eliminar_cargas3 ():
    uno.carga_cura = 0
    uno.carga_hemorragia = 0
    uno.carga_hielo = 0
    uno.carga_maldita = 0
    uno.carga_paralizado = 0
    uno.carga_quemado = 0
    uno.carga_sangrado = 0
    uno.carga_stun = 0
    uno.carga_veneno = 0
    dos.carga_cura = 0
    dos.carga_hemorragia = 0
    dos.carga_hielo = 0
    dos.carga_paralizado = 0
    dos.carga_maldita = 0
    dos.carga_quemado = 0
    dos.carga_sangrado = 0
    dos.carga_stun = 0
    dos.carga_veneno = 0
    tres.carga_cura = 0
    tres.carga_hemorragia = 0
    tres.carga_hielo = 0
    tres.carga_maldita = 0
    tres.carga_paralizado = 0
    tres.carga_quemado = 0
    tres.carga_sangrado = 0
    tres.carga_stun = 0
    tres.carga_veneno = 0
    print ('Se purifica el ambiente', '\n')

def eliminar_cargas4 ():
    uno.carga_cura = 0
    uno.carga_hemorragia = 0
    uno.carga_hielo = 0
    uno.carga_maldita = 0
    uno.carga_paralizado = 0
    uno.carga_quemado = 0
    uno.carga_sangrado = 0
    uno.carga_stun = 0
    uno.carga_veneno = 0
    dos.carga_cura = 0
    dos.carga_hemorragia = 0
    dos.carga_hielo = 0
    dos.carga_paralizado = 0
    dos.carga_maldita = 0
    dos.carga_quemado = 0
    dos.carga_sangrado = 0
    dos.carga_stun = 0
    dos.carga_veneno = 0
    tres.carga_cura = 0
    tres.carga_hemorragia = 0
    tres.carga_hielo = 0
    tres.carga_maldita = 0
    tres.carga_paralizado = 0
    tres.carga_quemado = 0
    tres.carga_sangrado = 0
    tres.carga_stun = 0
    tres.carga_veneno = 0
    cuatro.carga_cura = 0
    cuatro.carga_hemorragia = 0
    cuatro.carga_hielo = 0
    cuatro.carga_maldita = 0
    cuatro.carga_paralizado = 0
    cuatro.carga_quemado = 0
    cuatro.carga_sangrado = 0
    cuatro.carga_stun = 0
    cuatro.carga_veneno = 0
    print ('Se purifica el ambiente', '\n')

def eliminar_cargas6 ():
    uno.carga_cura = 0
    uno.carga_hemorragia = 0
    uno.carga_hielo = 0
    uno.carga_maldita = 0
    uno.carga_paralizado = 0
    uno.carga_quemado = 0
    uno.carga_sangrado = 0
    uno.carga_stun = 0
    uno.carga_veneno = 0
    dos.carga_cura = 0
    dos.carga_hemorragia = 0
    dos.carga_hielo = 0
    dos.carga_paralizado = 0
    dos.carga_maldita = 0
    dos.carga_quemado = 0
    dos.carga_sangrado = 0
    dos.carga_stun = 0
    dos.carga_veneno = 0
    tres.carga_cura = 0
    tres.carga_hemorragia = 0
    tres.carga_hielo = 0
    tres.carga_maldita = 0
    tres.carga_paralizado = 0
    tres.carga_quemado = 0
    tres.carga_sangrado = 0
    tres.carga_stun = 0
    tres.carga_veneno = 0
    cuatro.carga_cura = 0
    cuatro.carga_hemorragia = 0
    cuatro.carga_hielo = 0
    cuatro.carga_maldita = 0
    cuatro.carga_paralizado = 0
    cuatro.carga_quemado = 0
    cuatro.carga_sangrado = 0
    cuatro.carga_stun = 0
    cuatro.carga_veneno = 0
    cinco.carga_cura = 0
    cinco.carga_hemorragia = 0
    cinco.carga_hielo = 0
    cinco.carga_maldita = 0
    cinco.carga_paralizado = 0
    cinco.carga_quemado = 0
    cinco.carga_sangrado = 0
    cinco.carga_stun = 0
    cinco.carga_veneno = 0
    seis.carga_cura = 0
    seis.carga_hemorragia = 0
    seis.carga_hielo = 0
    seis.carga_maldita = 0
    seis.carga_paralizado = 0
    seis.carga_quemado = 0
    seis.carga_sangrado = 0
    seis.carga_stun = 0
    seis.carga_veneno = 0
    print ('Se purifica el ambiente', '\n')

def cargas (cargadoo):
    if cargadoo.carga_veneno >= 10 and cargadoo.name != 'Caja Azul' and cargadoo.name != 'Caja Roja':
        print (cargadoo.name, 'está tan lleno de veneno que acaba por morir')
        cargadoo.health = -10000
    if cargadoo.carga_sangrado >= 3:
        print ('Tanto sangrado provoca una hemorragia en', cargadoo.name)
        cargadoo.carga_hemorragia += 1
        cargadoo.carga_sangrado -= 3
    if cargadoo.carga_veneno >= 1:
        print ('El veneno inflige', 5 * cargadoo.carga_veneno, 'a', cargadoo.name)
        cargadoo.health -= 5 * cargadoo.carga_veneno
    if cargadoo.carga_quemado >= 1:
        print ('La quemadura inflige', 46 * cargadoo.carga_quemado, 'a', cargadoo.name)
        cargadoo.health -= 46 * cargadoo.carga_quemado
    if cargadoo.carga_sangrado >= 1:
        print ('El sangrado inflige', 20 * cargadoo.carga_sangrado, 'a', cargadoo.name)
        cargadoo.health -= 20 * cargadoo.carga_sangrado
    if cargadoo.carga_hemorragia >= 1:
        print ('La hemorragia inflige', 80 * cargadoo.carga_hemorragia, 'a', cargadoo.name)
        cargadoo.health -= 80 * cargadoo.carga_hemorragia
    if cargadoo.carga_maldita >= 1:
        print ('La maldición inflige', 32 * cargadoo.carga_maldita, 'a', cargadoo.name)
        cargadoo.health -= 32 * cargadoo.carga_maldita
    if cargadoo.health > 0:
        if cargadoo.carga_cura >= 1:
            print ('Tus cargas te curan', 28 * cargadoo.carga_cura, 'puntos de vida')
            cargadoo.health += 28 * cargadoo.carga_cura

def playone2 ():
    uno.nturnos += 1
    tempo1()
    for turnnn in range (1):
        if uno.health <= 0:
            break
        else:
            if campo.lluvia == 1:
                uno.carga_quemado = 0
                dos.carga_quemado = 0
                print ('La lluvia apaga las quemaduras y los moja')
            if campo.nevar == 1:
                nieve = randint (1, 100)
                if nieve <= 20:
                    uno.carga_hielo += 1
                    print (uno.name, 'se congela durante un turno')
                else:
                    print (uno.name, 'resiste el frío de la nieve')
            if campo.hierba == 1:
                if uno.tipo == 4:
                    cura = uno.maxhealth * 0.8 / 100
                    uno.health += cura 
                    print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
                else:
                    cura = uno.maxhealth * 0.5 / 100
                    uno.health += cura
                    print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            if campo.purificador == 1:
                eliminar_cargas2 ()
            if uno.carga_stun <= 0 and uno.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 1?') ##
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1':
                    objective = uno
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 1?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    campo.trrr = 6
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos2 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida2 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Dos rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
            uno.turno(objective)
            if objective.health <= 0:
                print( uno.name,'mató a', objective.name)
            elif uno.health <= 0:
                print (uno.name, 'murió en su turno')
def playone2random ():
    uno.nturnos += 1
    tempo1()
    for turnnn in range (1):
        if uno.health <= 0:
            break
        else:
            if campo.lluvia == 1:
                uno.carga_quemado = 0
                dos.carga_quemado = 0
                print ('La lluvia apaga las quemaduras y los moja')
            if campo.nevar == 1:
                nieve = randint (1, 100)
                if nieve <= 20:
                    uno.carga_hielo += 1
                    print (uno.name, 'se congela durante un turno')
                else:
                    print (uno.name, 'resiste el frío de la nieve')
            if campo.hierba == 1:
                if uno.tipo == 4:
                    cura = uno.maxhealth * 0.8 / 100
                    uno.health += cura
                    print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
                else:
                    cura = uno.maxhealth * 0.5 / 100
                    uno.health += cura
                    print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            if campo.purificador == 1:
                eliminar_cargas2 ()
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    campo.trrr = 6
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos2 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida2 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Dos rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
            piupiu = randint (1, 2)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            uno.turno(objective)
            if objective.health <= 0:
                print( uno.name,'mató a', objective.name)
            elif uno.health <= 0:
                print (uno.name, 'murió en su turno')
def playtwo2 ():
    dos.nturnos += 1
    tempo2()
    for turnnn in range (1):
        if dos.health <= 0:
            break
        else:
            if campo.lluvia == 1:
                uno.carga_quemado = 0
                dos.carga_quemado = 0
                print ('La lluvia apaga las quemaduras y los moja')
            if campo.nevar == 1:
                nieve = randint (1, 100)
                if nieve <= 20:
                    dos.carga_hielo += 1
                    print (dos.name, 'se congela durante un turno')
                else:
                    print (dos.name, 'resiste el frío de la nieve')
            if campo.hierba == 1:
                if dos.tipo == 4:
                    cura = dos.maxhealth * 0.8 / 100
                    dos.health += cura
                    print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
                else:
                    cura = dos.maxhealth * 0.5 / 100
                    dos.health += cura
                    print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            if campo.purificador == 1:
                eliminar_cargas2 ()
            if dos.carga_stun <= 0 and dos.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 2?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 2?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    campo.trrr = 6
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos2 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida2 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Dos rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
            dos.turno(objective)
            if objective.health <= 0:
                print( dos.name,'mató a', objective.name)
            elif dos.health <= 0:
                print (dos.name, 'murió en su turno')
def playtwo2random ():
    dos.nturnos += 1
    tempo2()
    for turnnn in range (1):
        if dos.health <= 0:
            break
        else:
            if campo.lluvia == 1:
                uno.carga_quemado = 0
                dos.carga_quemado = 0
                print ('La lluvia apaga las quemaduras y los moja')
            if campo.nevar == 1:
                nieve = randint (1, 100)
                if nieve <= 20:
                    dos.carga_hielo += 1
                    print (dos.name, 'se congela durante un turno')
                else:
                    print (dos.name, 'resiste el frío de la nieve')
            if campo.hierba == 1:
                if dos.tipo == 4:
                    cura = dos.maxhealth * 0.8 / 100
                    dos.health += cura
                    print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
                else:
                    cura = dos.maxhealth * 0.5 / 100
                    dos.health += cura
                    print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            if campo.purificador == 1:
                eliminar_cargas2 ()
            piupiu = randint (1, 2)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    campo.trrr = 6
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos2 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida2 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Dos rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
            dos.turno(objective)
            if objective.health <= 0:
                print( dos.name,'mató a', objective.name)
            elif dos.health <= 0:
                print (dos.name, 'murió en su turno')
def playone3 ():
    uno.nturnos += 1
    tempo1()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                uno.carga_hielo += 1
                print (uno.name, 'se congela durante un turno')
            else:
                print (uno.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if uno.tipo == 4:
                cura = uno.maxhealth * 0.8 / 100
                uno.health += cura
                print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = uno.maxhealth * 0.5 / 100
                uno.health += cura
                print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas3 ()
        if uno == serpientero or uno == poker and uno.health <= 0:
            if uno.carga_stun <= 0 and uno.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 1?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 1?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            uno.turno(objective)
            if objective.health <= 0:
                print( uno.name,'mató a', objective.name)
        elif uno.health <= 0:
            break
        else:
            if uno.carga_stun <= 0 and uno.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 1?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 1?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            if objective.health <= 0:
                uno.turno(objective)
                if uno.health <= 0:
                    print (uno.name, 'murió en su turno')
            else:
                uno.turno(objective)
                if objective.health <= 0:
                    print( uno.name,'mató a', objective.name)
                elif uno.health <= 0:
                    print (uno.name, 'murió en su turno')
def playone3random ():
    uno.nturnos += 1
    tempo1()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                uno.carga_hielo += 1
                print (uno.name, 'se congela durante un turno')
            else:
                print (uno.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if uno.tipo == 4:
                cura = uno.maxhealth * 0.8 / 100
                uno.health += cura
                print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = uno.maxhealth * 0.5 / 100
                uno.health += cura
                print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas3 ()
        if uno == serpientero or uno == poker and uno.health <= 0:
            piupiu = randint (1, 3)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            uno.turno(objective)
            if objective.health <= 0:
                print( uno.name,'mató a', objective.name)
        elif uno.health <= 0:
            break
        else:
            piupiu = randint (1, 3)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            if objective.health <= 0:
                uno.turno(objective)
                if uno.health <= 0:
                    print (uno.name, 'murió en su turno')
            else:
                uno.turno(objective)
                if objective.health <= 0:
                    print( uno.name,'mató a', objective.name)
                elif uno.health <= 0:
                    print (uno.name, 'murió en su turno')
def playtwo3 ():
    dos.nturnos += 1
    tempo2()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                dos.carga_hielo += 1
                print (dos.name, 'se congela durante un turno')
            else:
                print (dos.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if dos.tipo == 4:
                cura = dos.maxhealth * 0.8 / 100
                dos.health += cura
                print (dos.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = dos.maxhealth * 0.5 / 100
                dos.health += cura
                print (dos.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas3 ()
        if dos == serpientero or dos == poker and dos.health <= 0:
            if dos.carga_stun <= 0 and dos.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 2?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 2?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            dos.turno(objective)
            if objective.health <= 0:
                print( dos.name,'mató a', objective.name)
        elif dos.health <= 0:
            break
        else:
            if dos.carga_stun <= 0 and dos.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 2?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 2?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            if objective.health <= 0:
                dos.turno(objective)
                if dos.health <= 0:
                    print (dos.name, 'murió en su turno')
            else:
                dos.turno(objective)
                if objective.health <= 0:
                    print( dos.name,'mató a', objective.name)
                elif dos.health <= 0:
                    print (dos.name, 'murió en su turno')
def playtwo3random ():
    dos.nturnos += 1
    tempo2()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                dos.carga_hielo += 1
                print (dos.name, 'se congela durante un turno')
            else:
                print (dos.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if dos.tipo == 4:
                cura = dos.maxhealth * 0.8 / 100
                dos.health += cura
                print (dos.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = dos.maxhealth * 0.5 / 100
                dos.health += cura
                print (dos.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas3 ()
        if dos == serpientero or dos == poker and dos.health <= 0:
            piupiu = randint (1, 3)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            dos.turno(objective)
            if objective.health <= 0:
                print( dos.name,'mató a', objective.name)
        elif dos.health <= 0:
            break
        else:
            piupiu = randint (1, 3)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            if objective.health <= 0:
                dos.turno(objective)
                if dos.health <= 0:
                    print (dos.name, 'murió en su turno')
            else:
                dos.turno(objective)
                if objective.health <= 0:
                    print( dos.name,'mató a', objective.name)
                elif dos.health <= 0:
                    print (dos.name, 'murió en su turno')
def playthree3 ():
    tres.nturnos += 1
    tempo3()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                tres.carga_hielo += 1
                print (tres.name, 'se congela durante un turno')
            else:
                print (tres.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if tres.tipo == 4:
                cura = tres.maxhealth * 0.8 / 100
                tres.health += cura
                print (tres.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = tres.maxhealth * 0.5 / 100
                tres.health += cura
                print (tres.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas3 ()
        if tres == serpientero or tres == poker and tres.health <= 0:
            if tres.carga_stun <= 0 and tres.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 3?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 3?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 1 turno')
                    tres.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 3 turnos')
                    tres.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 2 turnos')
                    tres.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            tres.turno(objective)
            if objective.health <= 0:
                print( tres.name,'mató a', objective.name)
        elif tres.health <= 0:
            break
        else:
            if uno.carga_stun <= 0 and uno.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 3?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 3?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 1 turno')
                    tres.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 3 turnos')
                    tres.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 2 turnos')
                    tres.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            if objective.health <= 0:
                tres.turno(objective)
                if tres.health <= 0:
                    print (tres.name, 'murió en su turno')
            else:
                tres.turno(objective)
                if objective.health <= 0:
                    print( tres.name,'mató a', objective.name)
                elif tres.health <= 0:
                    print (tres.name, 'murió en su turno')
def playthree3random ():
    tres.nturnos += 1
    tempo3()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                tres.carga_hielo += 1
                print (tres.name, 'se congela durante un turno')
            else:
                print (tres.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if tres.tipo == 4:
                cura = tres.maxhealth * 0.8 / 100
                tres.health += cura
                print (tres.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = tres.maxhealth * 0.5 / 100
                tres.health += cura
                print (tres.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas3 ()
        if tres == serpientero or tres == poker and tres.health <= 0:
            piupiu = randint (1, 3)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 1 turno')
                    tres.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 3 turnos')
                    tres.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 2 turnos')
                    tres.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            tres.turno(objective)
            if objective.health <= 0:
                print( tres.name,'mató a', objective.name)
        elif tres.health <= 0:
            break
        else:
            piupiu = randint (1, 3)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    campo.trrr = 9
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos3 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida3 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 1 turno')
                    tres.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 3 turnos')
                    tres.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 2 turnos')
                    tres.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Tres rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
            if objective.health <= 0:
                tres.turno(objective)
                if tres.health <= 0:
                    print (tres.name, 'murió en su turno')
            else:
                tres.turno(objective)
                if objective.health <= 0:
                    print( tres.name,'mató a', objective.name)
                elif tres.health <= 0:
                    print (tres.name, 'murió en su turno')
def playone4 ():
    uno.nturnos += 1
    tempo1()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                uno.carga_hielo += 1
                print (uno.name, 'se congela durante un turno')
            else:
                print (uno.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if uno.tipo == 4:
                cura = uno.maxhealth * 0.8 / 100
                uno.health += cura
                print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = uno.maxhealth * 0.5 / 100
                uno.health += cura
                print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas4 ()
        if uno == serpientero or uno == poker and uno.health <= 0:
            if uno.carga_stun <= 0 and uno.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 1?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 1?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            uno.turno(objective)
            if objective.health <= 0:
                print( uno.name,'mató a', objective.name)
        elif uno.health <= 0:
            break
        else:
            if uno.carga_stun <= 0 and uno.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 1?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 1?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            if objective.health <= 0:
                uno.turno(objective)
                if uno.health <= 0:
                    print (uno.name, 'murió en su turno')
            else:
                uno.turno(objective)
                if objective.health <= 0:
                    print( uno.name,'mató a', objective.name)
                elif uno.health <= 0:
                    print (uno.name, 'murió en su turno')
def playone4random ():
    uno.nturnos += 1
    tempo1()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                uno.carga_hielo += 1
                print (uno.name, 'se congela durante un turno')
            else:
                print (uno.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if uno.tipo == 4:
                cura = uno.maxhealth * 0.8 / 100
                uno.health += cura
                print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = uno.maxhealth * 0.5 / 100
                uno.health += cura
                print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas4 ()
        if uno == serpientero or uno == poker and uno.health <= 0:
            piupiu = randint (1, 4)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            elif piupiu == 4:
                objective = cuatro
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            uno.turno(objective)
            if objective.health <= 0:
                print( uno.name,'mató a', objective.name)
        elif uno.health <= 0:
            break
        else:
            piupiu = randint (1, 4)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            elif piupiu == 4:
                objective = cuatro
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            if objective.health <= 0:
                uno.turno(objective)
                if uno.health <= 0:
                    print (uno.name, 'murió en su turno')
            else:
                uno.turno(objective)
                if objective.health <= 0:
                    print( uno.name,'mató a', objective.name)
                elif uno.health <= 0:
                    print (uno.name, 'murió en su turno')
def playtwo4 ():
    dos.nturnos += 1
    tempo2()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                dos.carga_hielo += 1
                print (dos.name, 'se congela durante un turno')
            else:
                print (dos.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if dos.tipo == 4:
                cura = dos.maxhealth * 0.8 / 100
                dos.health += cura
                print (dos.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = dos.maxhealth * 0.5 / 100
                dos.health += cura
                print (dos.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas4 ()
        if dos == serpientero or dos == poker and dos.health <= 0:
            if dos.carga_stun <= 0 and dos.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 2?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 2?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            dos.turno(objective)
            if objective.health <= 0:
                print( dos.name,'mató a', objective.name)
        elif dos.health <= 0:
            break
        else:
            if dos.carga_stun <= 0 and dos.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 2?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 2?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            if objective.health <= 0:
                dos.turno(objective)
                if dos.health <= 0:
                    print (dos.name, 'murió en su turno')
            else:
                dos.turno(objective)
                if objective.health <= 0:
                    print( dos.name,'mató a', objective.name)
                elif dos.health <= 0:
                    print (dos.name, 'murió en su turno')
def playtwo4random ():
    dos.nturnos += 1
    tempo2()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                dos.carga_hielo += 1
                print (dos.name, 'se congela durante un turno')
            else:
                print (dos.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if dos.tipo == 4:
                cura = dos.maxhealth * 0.8 / 100
                dos.health += cura
                print (dos.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = dos.maxhealth * 0.5 / 100
                dos.health += cura
                print (dos.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas4 ()
        if dos == serpientero or dos == poker and dos.health <= 0:
            piupiu = randint (1, 4)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            elif piupiu == 4:
                objective = cuatro
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            dos.turno(objective)
            if objective.health <= 0:
                print( dos.name,'mató a', objective.name)
        elif dos.health <= 0:
            break
        else:
            piupiu = randint (1, 4)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            elif piupiu == 4:
                objective = cuatro
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            if objective.health <= 0:
                dos.turno(objective)
                if dos.health <= 0:
                    print (dos.name, 'murió en su turno')
            else:
                dos.turno(objective)
                if objective.health <= 0:
                    print( dos.name,'mató a', objective.name)
                elif dos.health <= 0:
                    print (dos.name, 'murió en su turno')
def playthree4 ():
    tres.nturnos += 1
    tempo3()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                tres.carga_hielo += 1
                print (tres.name, 'se congela durante un turno')
            else:
                print (tres.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if tres.tipo == 4:
                cura = tres.maxhealth * 0.8 / 100
                tres.health += cura
                print (tres.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = tres.maxhealth * 0.5 / 100
                tres.health += cura
                print (tres.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas4 ()
        if tres == serpientero or tres == poker and tres.health <= 0:
            if tres.carga_stun <= 0 and tres.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 3?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 3?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 1 turno')
                    tres.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 3 turnos')
                    tres.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 2 turnos')
                    tres.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            tres.turno(objective)
            if objective.health <= 0:
                print( tres.name,'mató a', objective.name)
        elif tres.health <= 0:
            break
        else:
            if tres.carga_stun <= 0 and tres.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 3?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 3?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 1 turno')
                    tres.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 3 turnos')
                    tres.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 2 turnos')
                    tres.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            if objective.health <= 0:
                tres.turno(objective)
                if tres.health <= 0:
                    print (tres.name, 'murió en su turno')
            else:
                tres.turno(objective)
                if objective.health <= 0:
                    print( tres.name,'mató a', objective.name)
                elif tres.health <= 0:
                    print (tres.name, 'murió en su turno')
def playthree4random ():
    tres.nturnos += 1
    tempo3()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                tres.carga_hielo += 1
                print (tres.name, 'se congela durante un turno')
            else:
                print (tres.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if tres.tipo == 4:
                cura = tres.maxhealth * 0.8 / 100
                tres.health += cura
                print (tres.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = tres.maxhealth * 0.5 / 100
                tres.health += cura
                print (tres.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas4 ()
        if tres == serpientero or tres == poker and tres.health <= 0:
            piupiu = randint (1, 4)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            elif piupiu == 4:
                objective = cuatro
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 1 turno')
                    tres.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 3 turnos')
                    tres.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 2 turnos')
                    tres.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            tres.turno(objective)
            if objective.health <= 0:
                print( tres.name,'mató a', objective.name)
        elif tres.health <= 0:
            break
        else:
            piupiu = randint (1, 4)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            elif piupiu == 4:
                objective = cuatro
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 1 turno')
                    tres.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 3 turnos')
                    tres.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 2 turnos')
                    tres.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            if objective.health <= 0:
                tres.turno(objective)
                if tres.health <= 0:
                    print (tres.name, 'murió en su turno')
            else:
                tres.turno(objective)
                if objective.health <= 0:
                    print( tres.name,'mató a', objective.name)
                elif tres.health <= 0:
                    print (tres.name, 'murió en su turno')
def playfour4 ():
    cuatro.nturnos += 1
    tempo4()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                cuatro.carga_hielo += 1
                print (cuatro.name, 'se congela durante un turno')
            else:
                print (cuatro.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if cuatro.tipo == 4:
                cura = uno.maxhealth * 0.8 / 100
                cuatro.health += cura
                print (cuatro.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = cuatro.maxhealth * 0.5 / 100
                cuatro.health += cura
                print (cuatro.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas4 ()
        if cuatro == serpientero or cuatro == poker and cuatro.health <= 0:
            if cuatro.carga_stun <= 0 and cuatro.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 4?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 4?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 1 turno')
                    cuatro.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 3 turnos')
                    cuatro.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 2 turnos')
                    cuatro.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            cuatro.turno(objective)
            if objective.health <= 0:
                print( cuatro.name,'mató a', objective.name)
        elif cuatro.health <= 0:
            break
        else:
            if cuatro.carga_stun <= 0 and cuatro.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 4?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 4?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
            else:
                objective = uno
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 1 turno')
                    cuatro.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 3 turnos')
                    cuatro.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 2 turnos')
                    cuatro.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            if objective.health <= 0:
                cuatro.turno(objective)
                if cuatro.health <= 0:
                    print (cuatro.name, 'murió en su turno')
            else:
                cuatro.turno(objective)
                if objective.health <= 0:
                    print( cuatro.name,'mató a', objective.name)
                elif cuatro.health <= 0:
                    print (cuatro.name, 'murió en su turno')
def playfour4random ():
    cuatro.nturnos += 1
    tempo4()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                cuatro.carga_hielo += 1
                print (cuatro.name, 'se congela durante un turno')
            else:
                print (cuatro.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if cuatro.tipo == 4:
                cura = uno.maxhealth * 0.8 / 100
                cuatro.health += cura
                print (cuatro.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = cuatro.maxhealth * 0.5 / 100
                cuatro.health += cura
                print (cuatro.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas4 ()
        if cuatro == serpientero or cuatro == poker and cuatro.health <= 0:
            piupiu = randint (1, 4)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            elif piupiu == 4:
                objective = cuatro
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 1 turno')
                    cuatro.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 3 turnos')
                    cuatro.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 2 turnos')
                    cuatro.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            cuatro.turno(objective)
            if objective.health <= 0:
                print( cuatro.name,'mató a', objective.name)
        elif cuatro.health <= 0:
            break
        else:
            piupiu = randint (1, 4)
            if piupiu == 2:
                objective = dos
            elif piupiu == 1:
                objective = uno
            elif piupiu == 3:
                objective = tres
            elif piupiu == 4:
                objective = cuatro
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    campo.trrr = 12
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos4 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida4 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 1 turno')
                    cuatro.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 3 turnos')
                    cuatro.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 2 turnos')
                    cuatro.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
            if objective.health <= 0:
                cuatro.turno(objective)
                if cuatro.health <= 0:
                    print (cuatro.name, 'murió en su turno')
            else:
                cuatro.turno(objective)
                if objective.health <= 0:
                    print( cuatro.name,'mató a', objective.name)
                elif cuatro.health <= 0:
                    print (cuatro.name, 'murió en su turno')

def playone6atraco ():
    uno.nturnos += 1
    tempo1()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            cinco.carga_quemado = 0
            seis.carga_quemado = 0
            boxblue.carga_quemado = 0
            boxred.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                uno.carga_hielo += 1
                print (uno.name, 'se congela durante un turno')
            else:
                print (uno.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if uno.tipo == 4:
                cura = uno.maxhealth * 0.8 / 100
                uno.health += cura
                print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = uno.maxhealth * 0.5 / 100
                uno.health += cura
                print (uno.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas6 ()
        if uno.ko == 1:
            print (uno.name, 'se levanta y puede seguir peleando')
            uno.health = uno.maxhealth
            uno.ko = 0
            uno.carga_cura = 0
            uno.carga_hemorragia = 0
            uno.carga_hielo = 0
            uno.carga_maldita = 0
            uno.carga_paralizado = 0
            uno.carga_quemado = 0
            uno.carga_sangrado = 0
            uno.carga_stun = 0
            uno.carga_veneno = 0
        if uno == serpientero or uno == poker and uno.ko > 1:
            if uno.carga_stun <= 0 and uno.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 1?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 1?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective <= 0:
                uno.turno(objective)
            else:
                uno.turno(objective)
                if objective.health <= 0:
                    print( uno.name,'mató a', objective.name)
                    objective.ko = 3
        elif uno.ko > 1:
            print ('Estás noqueado, jugador 1', '\n')
            uno.ko -= 1
        else:
            if uno.carga_stun <= 0 and uno.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 1?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 1?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 1 turno')
                    uno.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 3 turnos')
                    uno.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', uno.name, ',', uno.name, 'se congela 2 turnos')
                    uno.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective.health <= 0:
                uno.turno(objective)
                if uno.health <= 0:
                    print (uno.name, 'murió en su turno')
                    uno.ko = 3
            else:
                uno.turno(objective)
                if objective.health <= 0:
                    print( uno.name,'mató a', objective.name)
                    objective.ko = 3
                elif uno.health <= 0:
                    print (uno.name, 'murió en su turno')
                    uno.ko = 3

def playtwo6atraco ():
    dos.nturnos += 1
    tempo2()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            cinco.carga_quemado = 0
            seis.carga_quemado = 0
            boxblue.carga_quemado = 0
            boxred.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                dos.carga_hielo += 1
                print (dos.name, 'se congela durante un turno')
            else:
                print (dos.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if dos.tipo == 4:
                cura = dos.maxhealth * 0.8 / 100
                dos.health += cura
                print (dos.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = dos.maxhealth * 0.5 / 100
                dos.health += cura
                print (dos.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas6 ()
        if dos.ko == 1:
            print (uno.name, 'se levanta y puede seguir peleando')
            dos.health = dos.maxhealth
            dos.ko = 0
            dos.carga_cura = 0
            dos.carga_hemorragia = 0
            dos.carga_hielo = 0
            dos.carga_paralizado = 0
            dos.carga_maldita = 0
            dos.carga_quemado = 0
            dos.carga_sangrado = 0
            dos.carga_stun = 0
            dos.carga_veneno = 0
        if dos == serpientero or dos == poker and dos.ko > 1:
            if dos.carga_stun <= 0 and dos.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 2?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 2?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective <= 0:
                dos.turno(objective)
            else:
                dos.turno(objective)
                if objective.health <= 0:
                    print( dos.name,'mató a', objective.name)
                    objective.ko = 3
        elif dos.ko > 1:
            print ('Estás noqueado, jugador 2', '\n')
            dos.ko -= 1
        else:
            if dos.carga_stun <= 0 and dos.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 2?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 2?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 1 turno')
                    dos.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 3 turnos')
                    dos.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', dos.name, ',', dos.name, 'se congela 2 turnos')
                    dos.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective.health <= 0:
                dos.turno(objective)
                if dos.health <= 0:
                    print (dos.name, 'murió en su turno')
                    dos.ko = 3
            else:
                dos.turno(objective)
                if objective.health <= 0:
                    print( dos.name,'noqueó a', objective.name)
                    objective.ko = 3
                elif dos.health <= 0:
                    print (dos.name, 'murió en su turno')
                    dos.ko = 3

def playthree6atraco ():
    tres.nturnos += 1
    tempo3()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            cinco.carga_quemado = 0
            seis.carga_quemado = 0
            boxblue.carga_quemado = 0
            boxred.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                tres.carga_hielo += 1
                print (tres.name, 'se congela durante un turno')
            else:
                print (tres.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if tres.tipo == 4:
                cura = tres.maxhealth * 0.8 / 100
                tres.health += cura
                print (tres.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = tres.maxhealth * 0.5 / 100
                tres.health += cura
                print (tres.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas6 ()
        if tres.ko == 1:
            print (tres.name, 'se levanta y puede seguir peleando')
            tres.health = tres.maxhealth
            tres.ko = 0
            tres.carga_cura = 0
            tres.carga_hemorragia = 0
            tres.carga_hielo = 0
            tres.carga_maldita = 0
            tres.carga_paralizado = 0
            tres.carga_quemado = 0
            tres.carga_sangrado = 0
            tres.carga_stun = 0
            tres.carga_veneno = 0
        if tres == serpientero or tres == poker and tres.ko > 1:
            if tres.carga_stun <= 0 and tres.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 3?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'cajaroja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 3?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'cajaroja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 1 turno')
                    tres.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 3 turnos')
                    tres.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 2 turnos')
                    tres.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective <= 0:
                tres.turno(objective)
            else:
                tres.turno(objective)
                if objective.health <= 0:
                    print(tres.name,'noqueó a', objective.name)
                    objective.ko = 3
        elif tres.ko > 0:
            print ('Estás noqueado, jugador 3', '\n')
            tres.ko -= 1
        else:
            if tres.carga_stun <= 0 and tres.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 3?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 3?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 1 turno')
                    tres.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 3 turnos')
                    tres.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', tres.name, ',', tres.name, 'se congela 2 turnos')
                    tres.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective.health <= 0:
                tres.turno(objective)
                if tres.health <= 0:
                    print (tres.name, 'murió en su turno')
                    tres.ko = 3
            else:
                tres.turno(objective)
                if objective.health <= 0:
                    print( tres.name,'mató a', objective.name)
                    objective.ko = 3
                elif tres.health <= 0:
                    print (tres.name, 'murió en su turno')
                    tres.ko = 3

def playfour6atraco ():
    cuatro.nturnos += 1
    tempo3()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            cinco.carga_quemado = 0
            seis.carga_quemado = 0
            boxblue.carga_quemado = 0
            boxred.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                cuatro.carga_hielo += 1
                print (cuatro.name, 'se congela durante un turno')
            else:
                print (cuatro.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if cuatro.tipo == 4:
                cura = cuatro.maxhealth * 0.8 / 100
                cuatro.health += cura
                print (cuatro.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = cuatro.maxhealth * 0.5 / 100
                cuatro.health += cura
                print (cuatro.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas6 ()
        if cuatro.ko == 1:
            print (cuatro.name, 'se levanta y puede seguir peleando')
            cuatro.health = cuatro.maxhealth
            cuatro.ko = 0
            cuatro.carga_cura = 0
            cuatro.carga_hemorragia = 0
            cuatro.carga_hielo = 0
            cuatro.carga_maldita = 0
            cuatro.carga_paralizado = 0
            cuatro.carga_quemado = 0
            cuatro.carga_sangrado = 0
            cuatro.carga_stun = 0
            cuatro.carga_veneno = 0
        if cuatro == serpientero or cuatro == poker and cuatro.ko > 1:
            if cuatro.carga_stun <= 0 and cuatro.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 4?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 4?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 1 turno')
                    cuatro.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 3 turnos')
                    cuatro.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 2 turnos')
                    cuatro.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective <= 0:
                cuatro.turno(objective)
            else:
                cuatro.turno(objective)
                if objective.health <= 0:
                    print( cuatro.name,'noqueó a', objective.name)
                    objective.ko = 3
        elif cuatro.ko > 0:
            print ('Estás noqueado, jugador 4', '\n')
            cuatro.ko -= 1
        else:
            if cuatro.carga_stun <= 0 and cuatro.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 4?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 4?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 1 turno')
                    cuatro.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 3 turnos')
                    cuatro.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', cuatro.name, ',', cuatro.name, 'se congela 2 turnos')
                    cuatro.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective.health <= 0:
                cuatro.turno(objective)
                if cuatro.health <= 0:
                    print (cuatro.name, 'murió en su turno')
                    cuatro.ko = 3
            else:
                cuatro.turno(objective)
                if objective.health <= 0:
                    print( cuatro.name,'noqueó a', objective.name)
                    objective.ko = 3
                elif cuatro.health <= 0:
                    print (cuatro.name, 'murió en su turno')
                    cuatro.ko = 3

def playfive6atraco ():
    cinco.nturnos += 1
    tempo5()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            cinco.carga_quemado = 0
            seis.carga_quemado = 0
            boxblue.carga_quemado = 0
            boxred.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                cinco.carga_hielo += 1
                print (cinco.name, 'se congela durante un turno')
            else:
                print (cinco.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if cinco.tipo == 4:
                cura = cinco.maxhealth * 0.8 / 100
                cinco.health += cura
                print (cinco.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = cinco.maxhealth * 0.5 / 100
                cinco.health += cura
                print (cinco.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas6 ()
        if cinco.ko == 1:
            print (cinco.name, 'se levanta y puede seguir peleando')
            cinco.health = cinco.maxhealth
            cinco.ko = 0
            cinco.carga_hemorragia = 0
            cinco.carga_hielo = 0
            cinco.carga_maldita = 0
            cinco.carga_paralizado = 0
            cinco.carga_quemado = 0
            cinco.carga_sangrado = 0
            cinco.carga_stun = 0
            cinco.carga_veneno = 0
        if cinco == serpientero or cinco == poker and cinco.ko > 1:
            if cinco.carga_stun <= 0 and cinco.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 5?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 5?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', cinco.name, ',', cinco.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', cinco.name, ',', cinco.name, 'se congela 1 turno')
                    cinco.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', cinco.name, ',', cinco.name, 'se congela 3 turnos')
                    cinco.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', cinco.name, ',', cinco.name, 'se congela 2 turnos')
                    cinco.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective <= 0:
                cinco.turno(objective)
            else:
                cinco.turno(objective)
                if objective.health <= 0:
                    print( cinco.name,'mató a', objective.name)
                    objective.ko = 3
        elif cinco.ko > 0:
            print ('Estás noqueado, jugador 5', '\n')
            cinco.ko -= 1
        else:
            if cinco.carga_stun <= 0 and cinco.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 5?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 5?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', cinco.name, ',', cinco.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', cinco.name, ',', cinco.name, 'se congela 1 turno')
                    cinco.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', cinco.name, ',', cinco.name, 'se congela 3 turnos')
                    cinco.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', cinco.name, ',', cinco.name, 'se congela 2 turnos')
                    cinco.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective.health <= 0:
                cinco.turno(objective)
                if cinco.health <= 0:
                    print (cinco.name, 'murió en su turno')
                    cinco.ko = 3
            else:
                cinco.turno(objective)
                if objective.health <= 0:
                    print( cinco.name,'mató a', objective.name)
                    objective.ko = 3
                elif cinco.health <= 0:
                    print (cinco.name, 'murió en su turno')
                    cinco.ko = 3

def playsix6atraco ():
    seis.nturnos += 1
    tempo6()
    for turnnn in range (1):
        if campo.lluvia == 1:
            uno.carga_quemado = 0
            dos.carga_quemado = 0
            tres.carga_quemado = 0
            cuatro.carga_quemado = 0
            cinco.carga_quemado = 0
            seis.carga_quemado = 0
            boxblue.carga_quemado = 0
            boxred.carga_quemado = 0
            print ('La lluvia apaga las quemaduras y los moja')
        elif campo.nevar == 1:
            nieve = randint (1, 100)
            if nieve <= 20:
                seis.carga_hielo += 1
                print (seis.name, 'se congela durante un turno')
            else:
                print (seis.name, 'resiste el frío de la nieve')
        elif campo.hierba == 1:
            if seis.tipo == 4:
                cura = seis.maxhealth * 0.8 / 100
                seis.health += cura
                print (seis.name, 'se cura', cura, 'de vida gracias al pasto sanador')
            else:
                cura = seis.maxhealth * 0.5 / 100
                seis.health += cura
                print (seis.name, 'se cura', cura, 'de vida gracias al pasto sanador')
        elif campo.purificador == 1:
            eliminar_cargas6 ()
        if seis.ko == 1:
            print (seis.name, 'se levanta y puede seguir peleando')
            seis.health = seis.maxhealth
            seis.ko = 0
            seis.carga_cura = 0
            seis.carga_hemorragia = 0
            seis.carga_hielo = 0
            seis.carga_maldita = 0
            seis.carga_paralizado = 0
            seis.carga_quemado = 0
            seis.carga_sangrado = 0
            seis.carga_stun = 0
            seis.carga_veneno = 0
        if seis == serpientero or seis == poker and seis.ko > 1:
            if seis.carga_stun <= 0 and seis.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 6?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 6?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', seis.name, ',', seis.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', seis.name, ',', seis.name, 'se congela 1 turno')
                    seis.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', seis.name, ',', seis.name, 'se congela 3 turnos')
                    seis.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', seis.name, ',', seis.name, 'se congela 2 turnos')
                    seis.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective <= 0:
                seis.turno(objective)
            else:
                seis.turno(objective)
                if objective.health <= 0:
                    print( seis.name,'noqueó a', objective.name)
                    objective.ko = 4
        elif seis.ko > 1:
            print ('Estás noqueado, jugador 6', '\n')
            seis.ko -= 1
        else:
            if seis.carga_stun <= 0 and seis.carga_hielo <= 0:
                who = input ('¿Quién es tu objetivo, jugador 6?') ######
                if who.lower() == 'jugador 2': ####
                    objective = dos
                elif who.lower() == 'jugador 1': ##
                    objective = uno
                elif who.lower() == 'jugador 3':
                    objective = tres
                elif who.lower() == 'jugador 4':
                    objective = cuatro
                elif who.lower() == 'jugador 5':
                    objective = cinco
                elif who.lower() == 'jugador 6':
                    objective = seis
                elif who.lower() == 'caja azul':
                    objective = boxblue
                elif who.lower() == 'caja roja':
                    objective = boxred
                else:
                    print ('mal')
                    who = input ('¿Quién es tu objetivo, jugador 6?')
                    if who.lower() == 'jugador 2': ####
                        objective = dos
                    elif who.lower() == 'jugador 1':
                        objective = uno
                    elif who.lower() == 'jugador 3':
                        objective = tres
                    elif who.lower() == 'jugador 4':
                        objective = cuatro
                    elif who.lower() == 'jugador 5':
                        objective = cinco
                    elif who.lower() == 'jugador 6':
                        objective = seis
                    elif who.lower() == 'caja azul':
                        objective = boxblue
                    elif who.lower() == 'caja roja':
                        objective = boxred
            else:
                objective = dos
            fenomeno = randint (1, 487) #487
            if fenomeno <= 28 :
                if campo.trrr == 0:
                    terremoto = randint (1, 4)
                    print ('Un terremoto sacude la tierra y aturde a todos', terremoto, 'turnos')
                    uno.carga_stun += terremoto
                    dos.carga_stun += terremoto
                    tres.carga_stun += terremoto
                    cuatro.carga_stun += terremoto
                    cinco.carga_stun += terremoto
                    seis.carga_stun += terremoto
                    campo.trrr = 18
                else:
                    campo.trrr -= 1
            elif fenomeno > 128 and fenomeno <= 142:
                refuerzos6 ()
            elif fenomeno > 242 and fenomeno <= 257:
                estampida6 ()
            elif fenomeno > 357 and fenomeno <= 377:
                ventisca = randint (1, 100)
                if ventisca <= 40:
                    print ('Una fuerte ventisca azota a', seis.name, ',', seis.name, 'resiste y no se congela')
                elif ventisca > 40 and ventisca <= 75:
                    print ('Una fuerte ventisca azota a', seis.name, ',', seis.name, 'se congela 1 turno')
                    seis.carga_hielo += 1
                elif ventisca > 95:
                    print ('Una fuerte ventisca azota a', seis.name, ',', seis.name, 'se congela 3 turnos')
                    seis.carga_hielo += 3
                else:
                    print ('Una fuerte ventisca azota a', seis.name, ',', seis.name, 'se congela 2 turnos')
                    seis.carga_hielo += 2
            elif fenomeno > 477 and fenomeno <= 487:
                print ('Cuatro rayos azotan la arena quebrantando la armadura de ambos contrincantes bajando su defensa en 0.1')
                uno.defense -= 0.1
                dos.defense -= 0.1
                tres.defense -= 0.1
                cuatro.defense -= 0.1
                cinco.defense -= 0.1
                seis.defense -= 0.1
                boxblue.defense -= 0.1
                boxred.defense -= 0.1
            if objective.health <= 0:
                seis.turno(objective)
                if seis.health <= 0:
                    print (seis.name, 'murió en su turno')
                    seis.ko = 3
            else:
                seis.turno(objective)
                if objective.health <= 0:
                    print( seis.name,'noqueó a', objective.name)
                    objective.ko = 3
                elif seis.health <= 0:
                    print (seis.name, 'murió en su turno')
                    seis.ko = 3

class Player ():
    def __init__(self, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus):
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
jugador = Player (0, 0, 0, 0, 0, 0, '')

class Warrior ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Guerrero')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "tajo", inflige 10 de daño, cuesta 2 de energía, tiene un', self.preci1,'% precisión y un 70% de probabilidades de infligir un sangrado en su enemigo')
        print ('Ataque 2: "estocada", inflige 101 de daño, cuesta 45 de energía y tiene un', self.preci2,'% precisión')
        print ('Ataque super: "Caballero", aplica un escudo a tu objetivo (puedes autotirartelo) que aumenta tu vida en 120 y tu defensa en 0.2 (no afecta el poder), cuesta 60 de energía, tiene un', self.preci3,'% precisión y 2 turnos de cooldown')
        print ('Vendas: "venda", cura 80 de vida (afecta la mitad del poder), cura 1 sangrado y 1 quemadura, cuesta 70 de energía y tiene un', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y tiene un', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "juicio final", al principio de cada turno aumenta su poder en 0.05')
        print ('(Cada turno recuperas 2 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un valiente guerrero llega a la arena, ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for warriorrr in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del guerrero:')
                    self.power += 0.05
                    if turn.lower() == 'tajo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 2:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unoo = randint (0,100)
                        if unoo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 1
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                sng = randint (0, 100)
                                dano = 10 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('Un potenete tajo le hace una brecha en la piel del enemigo que inflige', dano_total, 'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if sng <= 70:
                                    print (self.name, 'inflige un sangrado en', enemy.name)
                                    enemy.carga_sangrado += 1
                                self.energy -= 2
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    sng = randint (0, 100)
                                    print ('A causa de su locura ', self.name,' se hace un tajo en el brazo que le hece', 10 * self.power / self.defense, 'de daño')
                                    if sng <= 70:
                                        print (self.name, 'se auto-inflige un sangrado en', enemy.name)
                                        enemy.carga_sangrado += 1
                                    self.energy -= 2
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 2
                                else:
                                    sng = randint (0, 100)
                                    dano = 10 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Un potenete tajo le hace una brecha en la piel del enemigo que inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if sng <= 70:
                                        print (self.name, 'inflige un sangrado en', enemy.name)
                                        enemy.carga_sangrado += 1
                                    enemy.health -= 10 * self.power / enemy.defense
                                    self.energy -= 2
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'estocada':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 45:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        doos = randint(0, 100)
                        if doos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 17
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 101 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('Una increíble estocada atraviesa al enemigo y le inflige', dano_total, 'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                self.energy -= 45
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print ('Una terrible locura invade a ', self.name,'lo que lo lleva a atravezarse con su propia espada infligiendose', 101 * self.power / self.defense, 'de daño')
                                    self.health -= 101 * self.power / self.defense
                                    self.energy -= 45
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 2
                                else:
                                    dano = 101 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una increíble estocada atraviesa al enemigo y le inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.energy -= 45
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'caballero':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está stuneado y no llega a coger el escudo')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 60:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        trees = randint(0, 100)
                        if trees > self.preci3: 
                            print ('¡El escudo se estropea!')
                            self.energy -= 30
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        else:
                            print ('Coges un escudo de tu caballo aumentando la vida de', enemy.health ,'en', 120 * self.power, ' y su defensa en 0.2')
                            enemy.health += 120 * self.power
                            enemy.defense += 0.2
                            self.energy -= 60
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        self.cooldown3 = self.nturnos + 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'venda':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        curaa = randint(0, 100)
                        if curaa > self.precicura: 
                            print ('¡Falla la venda!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te pones una venda que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 2
                            elif self.health > self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 2
                            else:
                                print ('Te pones una venda que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaa = randint(0, 100)
                        if energiaa > self.precienergia: 
                            print (self.name, 'falla la canalización!')
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        else:
                            print (self.name, 'canaliza y recupera,', 60 * self.power,'de energía')
                            self.energy += 60 * self.power
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad caballero se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('Estás inmovilizado por', self.inmovilizado, 'turnos')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
guerrero = Warrior ('Kenric', 2500, 2500, 120, 0.95, 1.2, 42, 100, 95, 95, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Magician ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Mago')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "orbe", inflige 72 de daño, cuesta 4 de energía, tiene', self.preci1,'% precisión y un 25% de probabilidades de congelar al enemigo 1 turno')
        print ('Ataque 2: "Fuerza", aumenta tu poder en 0.2 (no afecta el poder) y aumenta tu precición de super en 1%, cuesta 60 de energía y tiene', self.preci2,'% precisión')
        print ('Ataque super: "Tornado fuego", inflige 520 de daño, cuesta 150 de energía, tiene', self.preci3,'% precisión, 4 turnos de cooldown y aplica dos quemaduras en tu enemigo')
        print ('Poción curativa: "cura", cura 80 de vida (afecta la mitad del poder), cura 1 hemorragia y 1 quemadura, cuesta 70 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "frenesí", tiene un 30% de probabilidades de lanzar un segundo ataque 1')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un mago se teletransporta a la arena, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for magiciannn in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del mago:')
                    if turn.lower() == 'orbe':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 4:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unooo = randint(0, 100)
                        if unooo > self.preci1: 
                            print ('¡', self.name, 'falla el golpe!')
                            self.energy -= 2
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            if self.locura == 0:
                                dano = 72 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('Un orbe impacta en el enemigo, inflige', dano_total, 'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                orbeee = randint (1,100)
                                if orbeee <= 25:
                                    print (self.name, 'congela a', enemy.name, '1 turno')
                                    enemy.carga_hielo += 1
                                self.energy -= 4
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                                seconddd = randint (1,100)
                                if seconddd <= 30:
                                    dano = 72 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Un segundo orbe impacta en el enemigo, inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    orbeee = randint (1,100)
                                    if orbeee <= 25:
                                        print (self.name, 'congela a', enemy.name, '1 turno')
                                        enemy.carga_hielo += 1
                                    self.energy -= 4
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print ('Debido a tu locura te lanzas un orbe que te inflige', 72 * self.power / self.defense, 'de daño')
                                    orbeee = randint (1,100)
                                    if orbeee <= 25:
                                        print (self.name, 'se auto-congela 1 turno')
                                        self.carga_hielo += 1
                                    self.health -= 72 * self.power / self.defense
                                    self.energy -= 4
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 4
                                    seconddd = randint (1,100)
                                    if seconddd <= 30:
                                        print ('Un segundo orbe impacta sobre ti, te inflige', 72 * self.power / self.defense, 'de daño')
                                        orbeee = randint (1,100)
                                        if orbeee <= 25:
                                            print (self.name, ' se auto-congela 1 turno')
                                            self.carga_hielo += 1
                                        self.health -= 72 * self.power / self.defense
                                        self.energy -= 4
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                else:
                                    print ('Un orbe impacta en el enemigo, inflige', 72 * self.power / enemy.defense, 'de daño a', enemy.name)
                                    orbeee = randint (1,100)
                                    if orbeee <= 25:
                                        print (self.name, 'congela a', enemy.name, '1 turno')
                                        enemy.carga_hielo += 1
                                    enemy.health -= 72 * self.power / enemy.defense
                                    self.energy -= 4
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 4
                                    seconddd = randint (1,100)
                                    if seconddd <= 30:
                                        print ('Un segundo orbe impacta en el enemigo, inflige', 72 * self.power / enemy.defense, 'de daño a', enemy.name)
                                        orbeee = randint (1,100)
                                        if orbeee <= 25:
                                            print (self.name, 'congela a', enemy.name, '1 turno')
                                            enemy.carga_hielo += 1
                                        enemy.health -= 72 * self.power / enemy.defense
                                        self.energy -= 4
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                            else:
                                print ('ERROR')
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'fuerza':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0: 
                            print (self.name, 'está silenciado y no puede tomarse la poción')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 60:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        dooos = randint(1, 100)
                        if dooos > self.preci2: 
                            print ('¡Se rompe la poción!')
                            self.energy -= 30
                            self.energy += 4
                        else:
                            print (self.name, 'toma un poción que aumenta su poder en 0.2 y la precisión del super en', 1 * self.power)
                            self.preci3 += 1 * self.power
                            self.power += 0.2
                            self.energy -= 60
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'tornado fuego':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 150:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treees = randint(0, 100)
                        if treees > self.preci3: 
                            print ('¡', self.name, 'falla el golpe!')
                            self.energy -= 75
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            if self.locura == 0:
                                dano = 520 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print (self.name, 'usa todas sus fuerzas e invoca un tornado ígneo infligiendo', dano_total, 'de daño a', enemy.name, 'y creandole 2 quemaduras')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                enemy.carga_quemado += 2
                                self.energy -= 150
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print (self.name, 'usa todas sus fuerzas e invoca un tornado ígneo sobre si mismo debido a su locura infligiendose', 520 * self.power / self.defense, 'de daño y creandose 2 quemaduras')
                                    self.health -= 520 * self.power / self.defense
                                    self.carga_quemado += 2
                                    self.energy -= 150
                                    self.energy += 4
                                else:
                                    dano = 520 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (self.name, 'usa todas sus fuerzas e invoca un tornado ígneo infligiendo', dano_total, 'de daño a', enemy.name, 'y creandole 2 quemaduras')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_quemado += 2
                                    self.energy -= 150
                                    self.energy += 4
                            else:
                                print ('ERROR')
                        self.cooldown3 = self.nturnos + 5
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'cura':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        curaaa = randint(0, 100)
                        if curaaa > self.precicura: 
                            print ('Se rompe la poción!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te tomas una poción que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            elif self.health > self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            else:
                                print ('Te tomas una poción que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break 
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaa = randint(0, 100)
                        if energiaaa > self.precienergia: 
                            print ('¡', self.name, 'falla la canalización!')
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            print (self.name, 'canaliza y recupera', 70 * self.power, 'de energía')
                            self.energy += 70 * self.power
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad tornado fuego se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('(Las inmovilizaciones no te afectan)')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
mago = Magician('Gandalf', 1580, 1580, 170, 1, 1, 30, 100, 80, 75, 100, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Hereje ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Ágil')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "flecha", inflige 10 de daño, cuesta 3 de energía, tiene', self.preci1,'% precisión y tiene 20% de probabilidades de infligir una hemorragia en tu enemigo')
        print ('Ataque 2: "flecha vampiro", inflige 40 de daño, te cura 25 de vida (aumentado por la mitad del poder), cuesta 40 de energía,', self.preci2,'% precisión y 1 turno de cooldown')
        print ('Ataque super: "Ira", aumenta tu poder en 1 (no afecta el poder), cuesta 70 de energía, tiene', self.preci3,'% precisión y 1 turno de cooldown')
        print ('Vendas: "venda", cura 80 de vida (no afecta el poder), cura 1 sangrado y 1 quemadura, cuesta 70 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía (afecta la mitad del poder) y', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "frenesí", tiene un 30% de probabilidades de lanzar un segundo ataque 1')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Como caído del cielo aparece un hereje arquero, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for herejeee in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del arquero:')
                    if turn.lower() == 'flecha':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 3:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 1.5
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                dano = 10 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('Una flecha se clava en tu enemigo, le inflige', dano_total ,'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                flechaaa = randint (1, 100)
                                if flechaaa <= 20:
                                    enemy.carga_hemorragia += 1
                                    print ('Tras un fuerte flechazo una peligrosa hemorragia surge en', enemy.name)
                                self.energy -= 3
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                                secondd = randint (1,100)
                                if secondd <= 30:
                                    dano = 10 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una segunda flecha se clava en tu enemigo, le inflige', dano_total ,'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    flechaaaa = randint (1, 100)
                                    if flechaaaa <= 20:
                                        enemy.carga_hemorragia += 1
                                        print ('Tras un fuerte flechazo una peligrosa hemorragia surge en', enemy.name)
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print ('A causa de la locura', self.name,'se clava una flecha en el pie, se inflige', 10 * self.power / self.defense ,'de daño')
                                    self.health -= 10 * self.power / self.defense
                                    flechaaa = randint (1, 100)
                                    if flechaaa <= 20:
                                        self.carga_hemorragia += 1
                                        print ('Tras el fuerte flechazo una peligrosa hemorragia surge en', self.name)
                                    self.energy -= 3
                                    self.energy += 3
                                    secondd = randint (1,100)
                                    if secondd <= 30:
                                        print ('Una segunda flecha se clava en ti infligiendote', 10 * self.power / self.defense ,'de daño')
                                        self.health -= 10 * self.power / self.defense
                                        flechaaaa = randint (1, 100)
                                        if flechaaaa <= 20:
                                            self.carga_hemorragia += 1
                                            print ('Tras el fuerte flechazo una peligrosa hemorragia surge en', self.name)
                                else:
                                    dano = 10 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una flecha se clava en tu enemigo, le inflige', dano_total ,'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    flechaaa = randint (1, 100)
                                    if flechaaa <= 20:
                                        enemy.carga_hemorragia += 1
                                        print ('Tras un fuerte flechazo una peligrosa hemorragia surge en', enemy.name)
                                    self.energy -= 3
                                    self.energy += 3
                                    secondd = randint (1,100)
                                    if secondd <= 30:
                                        dano = 10 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('Una segunda flecha se clava en tu enemigo, le inflige', dano_total ,'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        flechaaaa = randint (1, 100)
                                        if flechaaaa <= 20:
                                            enemy.carga_hemorragia += 1
                                            print ('Tras un fuerte flechazo una peligrosa hemorragia surge en', enemy.name)
                            else:
                                print ('ERROR')
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'flecha vampiro':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 20
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                dano = 40 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('Una flecha se clava en tu enemigo, le inflige', dano_total, 'de daño a', enemy.name, '¡Y te cura', 25 * (self.power / 2) * self.lcura * self.rcura,'de vida!')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                self.health += 25 * (self.power / 2) * self.lcura * self.rcura
                                self.energy -= 40
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print ('A causa de la locura', self.name,'se dispara una flecha en su torso, le inflige', 40 * self.power / self.defense, 'de daño ¡Y te cura', 25 * (self.power / 2) * self.lcura * self.rcura,'de vida!')
                                    self.health -= 40 * self.power / self.defense
                                    self.health += 25 * (self.power / 2) * self.lcura * self.rcura
                                    self.energy -= 40
                                    self.energy += 3
                                else:
                                    dano = 40 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una flecha se clava en tu enemigo, le inflige', dano_total, 'de daño a', enemy.name, '¡Y te cura', 25 * (self.power / 2) * self.lcura * self.rcura,'de vida!')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.health += 25 * (self.power / 2) * self.lcura * self.rcura
                                    self.energy -= 40
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        self.cooldown2 = self.nturnos + 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'ira':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar enfurecerse')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 3
                        else:
                            print (self.name, 'se enfurece y aumenta su poder en uno, ¡', enemy.name, 'apurate en matarlo!!')
                            self.power += 1
                            self.energy -= 70
                            self.energy += 3
                        self.cooldown3 = self.nturnos + 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'venda':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        curaaaaa = randint(0, 100)
                        if curaaaaa > self.precicura: 
                            print ('¡falla la venda!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 3
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te pones una venda que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                            else:
                                print ('Te pones una venda que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaaa = randint(0, 100)
                        if energiaaaa > self.precienergia: 
                            print (self.name, 'falla la canalización!')
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 3
                        else:
                            print (self.name, 'canaliza y recupera', 60 * (self.power / 2), 'de energía')
                            self.energy += 60 * (self.power / 2)
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad ira se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('(Las inmovilizaciones no te afectan)')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
arquero = Hereje('Alaric', 1700, 1700, 145, 0.5, 1, 59, 100, 80, 75, 80, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Maldi ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Mago')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "mal", inflige 22 de daño y aplica una maldición al objetivo (máximo 4) y si tiene quitas una cargas de cura a tu objetivo, cuesta 10 de energía y tiene', self.preci1,'% precisión')
        print ('Ataque 2: "oscuridad", aumenta tu poder en 0,05 | 0,1 | 0,3 | 0,6 | 1, te da más poder dependiento de las maldiciones que tengas TÜ, quita todas las maldiciones que tengas tú, cuesta 55 de energía, tiene', self.preci2,'% precisión y 2 turnos de cooldown')
        print ('Ataque super: "Diablo", inflige 100 | 150 | 250 | 500 | 800 de daño, hace más o menos daño dependiendo de la cantidad de maldiciones que tenga el enemigo, cuesta 80 de energía, quita todas las cargas malditas del enemigo, tiene', self.preci3,'% precisión, 3 turnos de cooldown y quita todas las cargas de cura de tu enemigo')
        print ('Poción curativa: "cura", cura 80 de vida (afecta la mitad del poder), cura 1 hemorragia y 1 quemadura, cuesta 70 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "maestro de pociones" al lanzar un ataque 1 tiene un 50% de posibilidades de envenenar a su objetivo')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Salido de la oscuridad, ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for maldiii in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del mago maldito:')
                    if turn.lower() == 'mal':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unooooo = randint(0, 100)
                        if unooooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 5
                            self.energy += 4
                        else:
                            if self.locura == 0:
                                dano = 22 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('una ola de mal inflige', dano_total, 'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                enemy.carga_maldita += 1
                                if enemy.carga_cura > 0:
                                    enemy.carga_cura -= 1
                                if enemy.carga_maldita >= 5:
                                    enemy.carga_maldita = 4
                                venenoo = randint (1, 100)
                                if venenoo <= 50:
                                    print ('Además', self.name, 'lanza una pocion venenosa a', enemy.name, 'y lo envenena')
                                    enemy.carga_veneno += 1
                                if venenoo == 100:
                                    print ('Además', self.name, 'lanza una pocion venenosa concentrada a', enemy.name, 'y lo envenena (dos carga de veneno)')
                                    enemy.carga_veneno += 2
                                self.energy -= 10
                                self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print ('Una ola de mal inflige', 22 * self.power / self.defense, 'de daño a', self.name, 'debido a su locura')
                                    self.health -= 22 * self.power / self.defense
                                    self.carga_maldita += 1
                                    if self.carga_cura > 0:
                                        self.carga_cura -= 1
                                    if self.carga_maldita >= 5:
                                        self.carga_maldita = 4
                                    venenoo = randint (1, 100)
                                    if venenoo <= 50:
                                        print ('Además', self.name, 'se toma una pocion venenosa debido a su locura y se envenena')
                                        self.carga_veneno += 1
                                    if venenoo == 100:
                                        print ('Además', self.name, 'se toma una pocion venenosa concentrada debido a su locura y se envenena (dos carga de veneno)')
                                        self.carga_veneno += 2
                                    self.energy -= 10
                                    self.energy += 4
                                else:
                                    dano = 22 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('una ola de mal inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_maldita += 1
                                    if enemy.carga_cura > 0:
                                        enemy.carga_cura -= 1
                                    if enemy.carga_maldita >= 5:
                                        enemy.carga_maldita = 4
                                    venenoo = randint (1, 100)
                                    if venenoo <= 50:
                                        print ('Además', self.name, 'lanza una pocion venenosa a', enemy.name, 'y lo envenena')
                                        enemy.carga_veneno += 1
                                    if venenoo == 100:
                                        print ('Además', self.name, 'lanza una pocion venenosa concentrada a', enemy.name, 'y lo envenena (dos carga de veneno)')
                                        enemy.carga_veneno += 2
                                    self.energy -= 10
                                    self.energy += 4
                            else:
                                print ('ERROR')
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'oscuridad':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        dooooos = randint(0, 100)
                        if dooooos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 15
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            print ('Te adentras en la oscuridad y aumentas tu poder')
                            if self.carga_maldita <= 0:
                                self.power += 0.05
                                self.carga_maldita = 0
                            elif self.carga_maldita == 1:
                                self.power += 0.1
                                self.carga_maldita = 0
                            elif self.carga_maldita == 2:
                                self.power += 0.3
                                self.carga_maldita = 0
                            elif self.carga_maldita == 3:
                                self.power += 0.6
                                self.carga_maldita = 0
                            elif self.carga_maldita >= 4:
                                self.power += 1
                                self.carga_maldita = 0
                            self.energy -= 30
                            self.energy += 4
                        self.cooldown2 = self.nturnos + 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'diablo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 80:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treeeees = randint(0, 100)
                        if treeeees > self.preci3:
                            print (self.name, 'falla el golpe!')
                            self.energy -= 40
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                            enemy.carga_maldita == 0
                        else:
                            if self.locura == 0:
                                print (self.name, 'invoca el diablo')
                                if enemy.carga_maldita == 0:
                                    dano = 100 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('El diablo inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')

                                elif enemy.carga_maldita == 1:
                                    dano = 150 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('El diablo inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_maldita -= 1

                                elif enemy.carga_maldita == 2:
                                    dano = 250 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('El diablo inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_maldita -= 2

                                elif enemy.carga_maldita == 3:
                                    dano = 500 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('El diablo inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_maldita -= 3

                                elif enemy.carga_maldita >= 4:
                                    dano = 800 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('El diablo inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_maldita = 0
                                enemy.carga_cura = 0
                                self.energy -= 80
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print (self.name, 'invoca el diablo pero este se vuelve contra él y le inflige daño')
                                    if self.carga_maldita == 0:
                                        self.health -= 100 * self.power / self.defense
                                    elif self.carga_maldita == 1:
                                        self.health -= 150 * self.power / self.defense
                                        self.carga_maldita = 0
                                    elif self.carga_maldita == 2:
                                        self.health -= 250 * self.power / self.defense
                                        self.carga_maldita = 0
                                    elif self.carga_maldita == 3:
                                        self.health -= 500 * self.power / self.defense
                                        self.carga_maldita = 0
                                    elif self.carga_maldita >= 4:
                                        self.health -= 800 * self.power / self.defense
                                        self.carga_maldita = 0
                                    self.carga_cura = 0
                                    self.energy -= 80
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 4
                                else:
                                    print (self.name, 'invoca el diablo')
                                    if enemy.carga_maldita == 0:
                                        dano = 100 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('El diablo inflige', dano_total, 'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')

                                    elif enemy.carga_maldita == 1:
                                        dano = 150 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('El diablo inflige', dano_total, 'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        enemy.carga_maldita -= 1

                                    elif enemy.carga_maldita == 2:
                                        dano = 250 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('El diablo inflige', dano_total, 'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        enemy.carga_maldita -= 2

                                    elif enemy.carga_maldita == 3:
                                        dano = 500 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('El diablo inflige', dano_total, 'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        enemy.carga_maldita -= 3

                                    elif enemy.carga_maldita >= 4:
                                        dano = 800 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('El diablo inflige', dano_total, 'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        enemy.carga_maldita = 0
                                    enemy.carga_cura = 0
                                    self.energy -= 80
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 4
                            else:
                                print ('ERROR')
                        self.cooldown3 = self.nturnos + 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'cura':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        curaaaaa = randint(0, 100)
                        if curaaaaa > self.precicura: 
                            print ('¡falla la poción!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te tomas una poción que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            else:
                                print ('Te tomas una poción que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaaaa = randint(0, 100)
                        if energiaaaaa > self.precienergia: 
                            print (self.name, 'falla la canalización!')
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            print (self.name, 'canaliza y recupera', 80 * self.power ,'de energía')
                            self.energy += 80 * self.power
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad diablo se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('(Las inmovilizaciones no te afectan)')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
maldito = Maldi ('Drago', 1400, 1530, 180, 1, 1, 16, 89, 79, 99, 100, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Thief ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, nturnos, tipo, mundo, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.nturnos = nturnos
        self.tipo = tipo
        self.mundo = mundo
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Ágil')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "daga", golpea un nuemero aleatorio de veces del 0 al 5, 1º golpe hace 45 de daño, 2º golpe roba 5 de vida, 3º golpe aumenta tu poder en 0.1, 4º golpe infliges una carga venenosa, 5º golpe haces 80 de daño extra, cuesta 10 de energía y tiene', self.preci1,'% precisión')
        print ('Ataque 2: "fatiga", disminuye el poder del enemigo en 0.1 (no afecta el poder), su precisión en 4% (no afecta el poder), le quita 2 cargas de cura (no afecta el poder) y le reduce la velocidad en 10 (no afecta el poder), cuesta 20 de energía, tiene', self.preci2,'% precisión y 3 turnos de cooldown')
        print ('Ataque super: "energia para mi", roba 40 de energia al rival (no afecta el poder), cuesta 40 de energía, tiene ', self.preci3,'% precisión y 2 turnos de cooldown (si tras el ataque tu enemigo se queda con energia negativa perderá 400 de vida)')
        print ('Vendas: "venda", cura 80 de vida (afecta la mitad del poder), cura 1 sangrado y 1 quemadura, cuesta 70 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "suerte de principiante", si el primer ataque es "daga" da 5 golpes asegurado')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Con una reluciente daga, el ladrón  ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for thiefff in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del ladrón:')
                    if turn.lower() == 'daga':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unoooooo = randint(0, 100)
                        if unoooooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 5
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                if self.nturnos == 1:
                                    self.power += 0.1
                                    dano = 125 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una daga se clava en', enemy.name, '5 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.health += 5 * self.power * self.lcura * self.rcura
                                    enemy.carga_veneno += 1
                                    self.energy -= 10
                                    self.energy += 3
                                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                                    break
                                dddd = randint (0, 5)
                                if dddd == 0:
                                    print (enemy.name, 'esquiva la daga y sobrevive')
                                
                                elif dddd == 1:
                                    dano = 45 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una daga se clava en', enemy.name, ' 1 vez y le inflijes', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.energy -= 10
                                
                                elif dddd == 2:
                                    dano = 45 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una daga se clava en', enemy.name, ' 2 veces, le inflijes', dano_total, 'de daño y le robas', 5 * self.power * self.lcura * self.rcura, 'de vida')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.health += 5 * self.power * self.lcura * self.rcura
                                    self.energy -= 10
                                    
                                elif dddd == 3:
                                    self.power += 0.1
                                    dano = 45 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una daga se clava en', enemy.name, ' 3 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida y te enfureces aumentando tu poder en 0,1')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.health += 5 * self.power * self.lcura * self.rcura
                                    self.energy -= 10

                                elif dddd == 4:
                                    self.power += 0.1
                                    dano = 45 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una daga se clava en', enemy.name, ' 4 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.health += 5 * self.power * self.lcura * self.rcura
                                    enemy.carga_veneno += 1
                                    self.energy -= 10

                                elif dddd == 5:
                                    self.power += 0.1
                                    dano = 125 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una daga se clava en', enemy.name, ' 5 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.health += 5 * self.power * self.lcura * self.rcura
                                    enemy.carga_veneno += 1
                                    self.energy -= 10
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    if self.nturnos == 1:
                                        self.power += 0.1
                                        print ('La daga de', self.name, 'toma vida propia rebelandose y le apuñala 5 veces, infligiendose', 125 * self.power / self.defense, 'de daño, te robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y te envenenas')
                                        self.health -= 125 * self.power / self.defense
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.carga_veneno += 1
                                        self.energy -= 10
                                        self.energy += 3
                                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                                        break
                                    dddd = randint (0, 5)
                                    if dddd == 0:
                                        print (self.name, 'se vuelve loco y se intenta apuñalar, afortunadamente esquiva la daga y sobrevive')
                                    elif dddd == 1:
                                        print (self.name, 'se vuelve loco y se apuñala con su daga 1 vez y infligiendose', 45 * self.power / self.defense, 'de daño')
                                        self.health -= 45 * self.power / self.defense
                                        self.energy -= 10
                                    elif dddd == 2:
                                        print (self.name, 'se vuelve loco y se apuñala con su daga 2 veces y infligiendose', 45 * self.power / self.defense, 'de daño y se robas', 5 * self.power * self.lcura * self.rcura, 'de vida')
                                        self.health -= 45 * self.power / self.defense
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.energy -= 10
                                    elif dddd == 3:
                                        self.power += 0.1
                                        print (self.name, 'se vuelve loco y se apuñala con su daga 3 veces y infligiendose', 45 * self.power / self.defense, 'de daño, se robas', 5 * self.power * self.lcura * self.rcura, 'de vida y te enfureces aumentando tu poder en 0,1')
                                        self.health -= 45 * self.power / self.defense
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.energy -= 10
                                    elif dddd == 4:
                                        self.power += 0.1
                                        print (self.name, 'se vuelve loco y se apuñala con su daga 4 veces y infligiendose', 45 * self.power / self.defense, 'de daño, se robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y se envenenas')
                                        self.health -= 45 * self.power / self.defense
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.carga_veneno += 1
                                        self.energy -= 10
                                    elif dddd == 5:
                                        self.power += 0.1
                                        print (self.name, 'se vuelve loco y se apuñala con su daga 5 veces y infligiendose', 125 * self.power / self.defense, 'de daño, se robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y se envenenas')
                                        self.health -= 125 * self.power / self.defense
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.carga_veneno += 1
                                        self.energy -= 10
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 3
                                else:
                                    if self.nturnos == 1:
                                        self.power += 0.1
                                        dano = 125 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('Una daga se clava en', enemy.name, '5 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        enemy.carga_veneno += 1
                                        self.energy -= 10
                                        self.energy += 3
                                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                                        break
                                    dddd = randint (0, 5)
                                    if dddd == 0:
                                        print (enemy.name, 'esquiva la daga y sobrevive')
                                    
                                    elif dddd == 1:
                                        dano = 45 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('Una daga se clava en', enemy.name, ' 1 vez y le inflijes', dano_total, 'de daño')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        self.energy -= 10
                                    
                                    elif dddd == 2:
                                        dano = 45 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('Una daga se clava en', enemy.name, ' 2 veces, le inflijes', dano_total, 'de daño y le robas', 5 * self.power * self.lcura * self.rcura, 'de vida')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.energy -= 10
                                    
                                    elif dddd == 3:
                                        self.power += 0.1
                                        dano = 45 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('Una daga se clava en', enemy.name, ' 3 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida y te enfureces aumentando tu poder en 0,1')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        self.energy -= 10

                                    elif dddd == 4:
                                        self.power += 0.1
                                        dano = 45 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('Una daga se clava en', enemy.name, ' 4 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        enemy.carga_veneno += 1
                                        self.energy -= 10

                                    elif dddd == 5:
                                        self.power += 0.1
                                        dano = 125 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('Una daga se clava en', enemy.name, ' 5 veces, le inflijes', dano_total, 'de daño, le robas', 5 * self.power * self.lcura * self.rcura, 'de vida, te enfureces aumentando tu poder en 0,1 y le envenenas')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        self.health += 5 * self.power * self.lcura * self.rcura
                                        enemy.carga_veneno += 1
                                        self.energy -= 10
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 3
                            else:
                                print ('ERROR')

                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'fatiga':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede correr')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 35:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        doooooos = randint(0, 100)
                        if doooooos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 10
                            self.energy += 3
                        else:
                            print ('Haces correr al enemigo por todos lados y le das una fatiga, disminuye su poder en 0.1, su precisión en 4%, se le agotan 2 cargas de cura y pierde 10 de velocidad')
                            enemy.power -= 0.1
                            enemy.preci1 -= 4
                            enemy.preci2 -= 4
                            enemy.preci3 -= 4
                            enemy.precicura -= 4
                            enemy.precienergia -= 4
                            if enemy.carga_cura > 0:
                                enemy.carga_cura -= 2
                                if enemy.carga_cura < 0:
                                    enemy.carga_cura = 0
                            enemy.velocity -= 10
                            self.energy -= 20
                            self.energy += 3
                        self.cooldown2 = self.nturnos + 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia para mi':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar el hechizo')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 20:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treeeeees = randint(0, 100)
                        if treeeeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 20
                            self.energy += 3
                        else:
                            print ('¡',self.name, 'saca algo de su mochila! Saca un libro de encantamientos... (', self.name,': ¡robado!) conjura un hechizo y le roba 40 de energia a', self.name)
                            enemy.energy -= 40
                            self.energy += 40
                            self.energy -= 40
                            if enemy.energy < 0:
                                enemy.health -= 400
                            self.energy += 3
                        self.cooldown3 = self.nturnos + 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'venda':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        curaaaaaa = randint(0, 100)
                        if curaaaaaa > self.precicura: 
                            print ('¡Falla la venda!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 3
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te pones una venda que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                            else:
                                print ('Te pones una venda que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaaaaa = randint(0, 100)
                        if energiaaaaaa > self.precienergia: 
                            print ('¡Falla la canalización!')
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 3
                        else:
                            print (self.name, 'canaliza y recupera', 60 * self.power, 'de energía')
                            self.energy += 60 * self.power
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad energia para mi se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('Estás inmovilizado por', self.inmovilizado, 'turnos')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
robador = Thief('Leoric', 1850, 1850, 160, 1, 1, 65, 120, 85, 70, 80, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Shapeshifter ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci11, preci2, preci22, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, carga_cambiaforma, carga_pantera, pantera, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci11 = preci11
        self.preci22 = preci22
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.carga_cambiaforma = carga_cambiaforma
        self.carga_pantera = carga_pantera
        self.pantera = pantera
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Mago')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "rayo energia"(humano), inflige 80 de daño, cuesta 25 de energía, tiene', self.preci1,'% precisión y te da una carga de cambiaforma (Máx. 5)//"zarpazo" (pantera), inflige 70 de daño, cuesta 30 de energia, tiene', self.preci11,'% de precisión, si tienes una carga de cambiaformas se gasta y te da una carga de pantera, tras tres cargas de pantera infliges 500 de daño')
        print ('Ataque 2: "escudo"(humano), aumenta tu vida en 150 y tu defensa en 0.1 y te da una carga de cambiaforma, cuesta 30 de energía, tiene', self.preci2,'% precisión y 1 turno de cooldown//"salto"(pantera), le inflges 20 de daño, cuesta 40 de energia, tiene', self.preci22,'% de precisión y 2 turnos de cooldown , si tienes una carga de cambiaformas esta se consume y infliges 80 más de daño')
        print ('Ataque super: "transformación", pasa de humano a pantera y viseversa, cuesta 10 de energía, tiene', self.preci3,'% precisión y 2 turnos de cooldown')
        print ('Poción curativa: "cura", cura 80 de vida (afecta la mitad del poder), cura 1 hemorragia y 1 quemadura, cuesta 70 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "Incansable", cuando se transforma recupera su velocidad por defecto')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un cambiaforma se abalanza entre los arboles a la arena, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for shapeshifterrr in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del cambiaformas:')
                    if turn.lower() == 'rayo energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 25:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        if self.pantera == 0:
                            unooooooo = randint(0, 100)
                            if unooooooo > self.preci1: 
                                print ('¡', self.name, 'falla el golpe!')
                                self.energy -= 12.5
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            else:
                                if self.locura == 0:
                                    dano = 80 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Un rayo de energía impacta en el enemigo, inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.carga_cambiaforma += 1
                                    if self.carga_cambiaforma > 5:
                                        self.carga_cambiaforma = 5
                                    self.energy -= 25
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 4
                                elif self.locura > 0 and self.locura <= 100:
                                    locuraaa = randint (1, 100)
                                    if locuraaa > self.locura:
                                        print ('Una gran locura inunde a', self.name, 'y conjura un rayo de energía que impacta en él, se inflige', 80 * self.power / self.defense, 'de daño')
                                        self.health -= 80 * self.power / self.defense
                                        self.carga_cambiaforma += 1
                                        if self.carga_cambiaforma > 5:
                                            self.carga_cambiaforma = 5
                                        self.energy -= 25
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                    else:
                                        dano = 80 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('Un rayo de energía impacta en el enemigo, inflige', dano_total, 'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        self.carga_cambiaforma += 1
                                        if self.carga_cambiaforma > 5:
                                            self.carga_cambiaforma = 5
                                        self.energy -= 25
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                else:
                                    print ('ERROR')
                            print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                            print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                        elif self.pantera == 1:
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                            print ('Estás en forma de pantera, no puedes lanzar este ataque')
                            print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                            print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                            break
                    elif turn.lower() == 'zarpazo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        if self.pantera == 0:
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                            print ('Estas en forma humana, no puedes lanzar este ataque')
                            print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                            print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                        elif self.pantera == 1:
                            unooooooo = randint(0, 100)
                            if unooooooo > self.preci11: 
                                print ('¡', self.name, 'falla el golpe!')
                                self.energy -= 15
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            else:
                                if self.locura == 0:
                                    dano = 70 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Un zarpazo inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if self.carga_cambiaforma > 0:
                                        self.carga_pantera += 1
                                        self.carga_cambiaforma -= 1
                                    if self.carga_pantera >= 3:
                                        dano = 500 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('Un gran zarpazo atraviesa a', enemy.name, 'y le inflige', dano_total, 'de daño')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        self.carga_pantera = 0
                                    self.energy -= 30
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 4
                                elif self.locura > 0 and self.locura <= 100:
                                    locuraaa = randint (1, 100)
                                    if locuraaa > self.locura:
                                        print ('De la locura', self.name, 'se da un zarpazo a si mismo, infligiendose', 70 * self.power / self.defense, 'de daño')
                                        self.health -= 70 * self.power / self.defense
                                        if self.carga_cambiaforma > 0:
                                            self.carga_pantera += 1
                                            self.carga_cambiaforma -= 1
                                        if self.carga_pantera >= 3:
                                            print ('Un gran zarpazo atraviesa a', self.name, 'y le inflige', 500 * self.power / self.defense, 'de daño')
                                            self.health -= 500 * self.power / self.defense
                                            self.carga_pantera = 0
                                        self.energy -= 30
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                    else:
                                        dano = 70 * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print ('Un zarpazo inflige', dano_total, 'de daño a', enemy.name)
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        if self.carga_cambiaforma > 0:
                                            self.carga_pantera += 1
                                            self.carga_cambiaforma -= 1
                                        if self.carga_pantera >= 3:
                                            dano = 500 * self.power / enemy.defense
                                            reflejo = dano * enemy.reflejar 
                                            dano_total = dano - reflejo
                                            enemy.health -= dano_total
                                            self.health -= reflejo
                                            print ('Un gran zarpazo atraviesa a', enemy.name, 'y le inflige', dano_total, 'de daño')
                                            if enemy.reflejar > 0:
                                                print (enemy.name, 'refleja', reflejo, 'de daño')
                                            self.carga_pantera = 0
                                        self.energy -= 30
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                else:
                                    print ('ERROR')
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                    elif turn.lower() == 'escudo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        if self.pantera == 0:
                            dooos = randint(0, 100)
                            if dooos > self.preci2: 
                                print ('¡Fallas!')
                                self.energy -= 15
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            else:
                                print (self.name, 'llama a la naturaleza para aplicarse un escudo que aumenta tu vida en 150 y tu defensa en 0.1, además te da una carga de cambiaforma')
                                self.health += 150
                                self.defense += 0.1
                                self.carga_cambiaforma += 1
                                self.energy -= 30
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                            print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                        elif self.pantera == 1:
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                            print ('Estas en forma de pantera, no puedes lanzar este ataque')
                            print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                            print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                        self.cooldown2 = self.nturnos + 2
                    elif turn.lower() == 'salto':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        if self.pantera == 1:
                            dooos = randint(0, 100)
                            if dooos > self.preci22: 
                                print ('¡Fallas!')
                                self.energy -= 20
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 4
                            else:
                                if self.carga_cambiaforma > 0:
                                    danosalto = 100
                                    self.carga_cambiaforma -= 1
                                elif self.carga_cambiaforma == 0:
                                    danosalto = 20
                                if self.locura == 0:
                                    dano = danosalto * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (self.name, 'se lanza a por', enemy.name, 'infligiendole', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.energy -= 40
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 4
                                elif self.locura > 0 and self.locura <= 100:
                                    locuraaa = randint (1, 100)
                                    if locuraaa > self.locura:
                                        print (self.name, 'se lanza a por', enemy.name, ', pero de la locura lo confunde con un árbol y se choca contra este infligiendose', danosalto *self.power / self.defense, 'de daño')
                                        self.health -= danosalto * self.power / self.defense
                                        self.energy -= 40
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                    else:
                                        dano = danosalto * self.power / enemy.defense
                                        reflejo = dano * enemy.reflejar 
                                        dano_total = dano - reflejo
                                        enemy.health -= dano_total
                                        self.health -= reflejo
                                        print (self.name, 'se lanza a por', enemy.name, 'infligiendole', dano_total, 'de daño')
                                        if enemy.reflejar > 0:
                                            print (enemy.name, 'refleja', reflejo, 'de daño')
                                        self.energy -= 40
                                        if self.energy < 0:
                                            self.health -= 800
                                        self.energy += 4
                                else:
                                    print ('ERROR')
                            print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                            print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                        elif self.pantera == 0:
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                            print ('Estas en forma humana, no puedes lanzar este ataque')
                            print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                            print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                        self.cooldown2 = self.nturnos + 3
                    elif turn.lower() == 'transformacion':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede transformarse')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        trees = randint(1, 100)
                        if trees > self.preci3: 
                            print ('¡', self.name, 'falla el golpe!')
                            self.energy -= 5
                            self.energy += 4
                        else:
                            if self.pantera == 0:
                                print (self.name, 'pasa a ser una pantera')
                                self.pantera += 1
                                self.velocity = 78
                                self.energy -= 10
                                self.energy += 4
                            elif self.pantera == 1:
                                print (self.name, 'pasa a ser un humano')
                                self.pantera -= 1
                                self.carga_pantera = 0
                                self.energy -= 10
                                self.velocity = 32
                                self.energy += 4
                        self.cooldown3 = self.nturnos + 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                    elif turn.lower() == 'cura':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        curaaa = randint(0, 100)
                        if curaaa > self.precicura: 
                            print ('Se rompe la poción!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te tomas una poción que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 2
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 2
                            else:
                                print ('Te tomas una poción que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaa = randint(0, 100)
                        if energiaaa > self.precienergia: 
                            print ('¡', self.name, 'falla la canalización!')
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            print (self.name, 'canaliza y recupera', 80 * self.power, 'de energía')
                            self.energy += 80 * self.power
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados, tienes', self.carga_cambiaforma, 'cargas de cambiaformas', self.carga_pantera, 'cargas de pantera y', self.pantera, '(Si es 0 eres humano y si 1 eres pantera)' ,'\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad transformacion se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('Estás inmovilizado por', self.inmovilizado, 'turnos')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
pantera = Shapeshifter('Hildegund', 2100, 2100, 300, 1, 1, 33, 85, 120, 85, 90, 200, 100, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Healer ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Mago')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "Heal", cura 1 hemorragia y 80 de vida a tu objetivo y lo purificas quitandole 1 maldición, cuesta 40 de energía, tiene', self.preci1,'% precisión')
        print ('Ataque 2: "Bendecir", aplica a tu objetivo 2 cargas de cura (no afecta el poder), cuesta 60 de energía, tiene', self.preci2,'% precisión y 1 turno de cooldown')
        print ('Ataque super: "Proteger", cura a tu objetivo 100 de vida y aumenta su poder y su defensa en 0.1, cuesta 100 de energía, tiene', self.preci3,'% precisión y 2 turnos de cooldown')
        print ('Poción curativa: "cura", cura 80 de vida (afecta la mitad del poder), cura 1 hemorragia y 1 quemadura, cuesta 70 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "Apoyo", puedes dar tu cura a tu objetivo escribiendo "curar", además de poder canalizar para tu objetivo escribiendo "energiar"')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Una curandera aparece en arena, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for healerrr in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno de la curandera:')
                    if turn.lower() == 'heal':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unooo = randint(0, 100)
                        if unooo > self.preci1: 
                            print ('¡', self.name, 'falla la cura!')
                            self.energy -= 20
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            print (self.name, 'cura 1 hemorragia y', 80 * self.power * self.lcura * enemy.rcura, 'de vida a tu objetivo y lo purificas quitandole 1 maldición')
                            enemy.health += 80 * self.power * self.lcura * enemy.rcura
                            if enemy.carga_hemorragia > 0:
                                enemy.carga_hemorragia -= 1
                            if enemy.carga_maldita > 0:
                                enemy.carga_maldita -= 1
                            self.energy -= 40
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'bendecir':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        dooos = randint(0, 100)
                        if dooos > self.preci2: 
                            print (self.name, 'se confunde de hechizo y convierte una hoja de pasto en un gusano')
                            self.energy -= 30
                            self.energy += 4
                        else:
                            if enemy.carga_cura >= 4:
                                print (enemy.name, 'está al límite de cargas de cura')
                                self.energy += 4
                            else:
                                print (self.name, 'bendice a', enemy.name, 'aplicandole 2 cargas de cura')
                                enemy.carga_cura += 2
                                self.energy -= 60
                                self.energy += 4
                        self.cooldown2 = self.nturnos + 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'proteger':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 100:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treees = randint(0, 100)
                        if treees > self.preci3: 
                            print ('¡', self.name, 'se equivoca de hechizo y invoca una arañita inofensiva!')
                            self.energy -= 50
                            self.energy += 4
                        else:
                            print (self.name, 'protege a',enemy.name, 'curandole', 100 * self.power * self.lcura * enemy.rcura, 'de vida y aumentandole el poder y la defensa en 0.1')
                            enemy.health += 100 * self.power * self.lcura * enemy.rcura
                            enemy.power += 0.1
                            enemy.defense += 0.1
                            self.energy -= 100
                            self.energy += 4
                        self.cooldown3 = self.nturnos + 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'cura':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        curaaa = randint(0, 100)
                        if curaaa > self.precicura: 
                            print ('Se rompe la poción!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te tomas una poción que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 2
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 2
                            else:
                                print ('Te tomas una poción que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'curar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede curar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 4
                            break
                        curaaa = randint(0, 100)
                        if curaaa > self.precicura: 
                            print ('Se rompe la poción!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            print ('Le das una poción a', enemy.name, 'que le cura', 80 * (self.power/2) ,'de vida')
                            enemy.health += 80 * (self.power/2)
                            if enemy.carga_hemorragia > 0:
                                enemy.carga_hemorragia -= 1
                            if enemy.carga_quemado > 0:
                                enemy.carga_quemado -= 1
                            self.energy -= 70
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaa = randint(0, 100)
                        if energiaaa > self.precienergia: 
                            print ('¡', self.name, 'falla la canalización!')
                            self.energy += 4
                        else:
                            print (self.name, 'canaliza y recupera', 80 * self.power, 'de energía')
                            self.energy += 80 * self.power
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energiar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaa = randint(0, 100)
                        if energiaaa > self.precienergia: 
                            print ('¡', self.name, 'falla la canalización!')
                            self.energy += 4
                        else:
                            print (self.name, 'canaliza y recupera', 80 * self.power, 'de energía para', enemy.name)
                            enemy.energy += 80 * self.power
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad proteger se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('(Las inmovilizaciones no te afectan)')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
curandera = Healer('Hawise', 1700, 1700, 200, 1, 1, 35, 100, 80, 85, 100, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Mace ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Guerrero')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "Golpe defensivo", haces 20 de daño y aumentas tu defensa en 0.08, cuesta 5 de energía y tiene un', self.preci1,'% precisión')
        print ('Ataque 2: "Agitador de tierra", inflige 240 de daño, cuesta 80 de energía, tiene un', self.preci2,'% precisión y 2 turnos de cooldown')
        print ('Ataque super: "Salto profundo", inflige 150 de daño y aturdes a tu enemigo 2 turnos (no es acumulable), cuesta 100 de energía, tiene un', self.preci3,'% precisión, y 3 turnos de cooldown')
        print ('Vendas: "venda", cura 80 de vida (afecta la mitad del poder), cura 1 sangrado y 1 quemadura, cuesta 70 de energía y tiene un', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y tiene un', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "concentración" en una canalización recuperas el doble de energia')
        print ('(Cada turno recuperas 2 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Un valiente guerrero llega a la arena con una pezada maza, ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for maceee in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del macero:')
                    if turn.lower() == 'golpe defensivo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 5:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unoo = randint (0,100)
                        if unoo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 2.5
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 20 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('Un mazazo le hace un gran golpe en el enemigo que le inflige', dano_total, 'de daño a', enemy.name, ', y aumentas tu propia defensa en 0.08')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                self.defense += 0.08
                                self.energy -= 5
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print ('De la locura te pegas un mazazo que te inflige', 20 * self.power / self.defense, 'de daño, y aumentas tu propia defensa en 0.08')
                                    self.health -= 20 * self.power / self.defense
                                    self.defense += 0.08
                                    self.energy -= 5
                                    self.energy += 2
                                else:
                                    dano = 20 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Un mazazo le hace un gran golpe en el enemigo que le inflige', dano_total, 'de daño a', enemy.name, ', y aumentas tu propia defensa en 0.08')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.defense += 0.08
                                    self.energy -= 5
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'agitador de tierra':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 80:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        doos = randint(0, 100)
                        if doos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 40
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 240 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('Agita la tierra alrededor del enemigo y le inflige', dano_total, 'de daño a', enemy.name)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                self.energy -= 80
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print ('Te vuelves loco y al querer azotar la tierra con tu maza te partes el pie, te infliges', 240 * self.power / self.defense, 'de daño')
                                    self.health -= 240 * self.power / self.defense
                                    self.energy -= 80
                                    self.energy += 2
                                else:
                                    dano = 240 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Agita la tierra alrededor del enemigo y le inflige', dano_total, 'de daño a', enemy.name)
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    self.energy -= 80
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown2 = self.nturnos + 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'salto profundo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este ataque')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 100:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        trees = randint(0, 100)
                        if trees > self.preci3: 
                            print ('¡Fallas!')
                            self.energy -= 50
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 150 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('Saltas sobre tu enemigo infligiendole', dano_total, 'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                if enemy.carga_stun == 0:
                                    enemy.carga_stun += 2
                                    print('Aturdes a', enemy.name, '2 turnos')
                                else:
                                    print(enemy.name, 'ya está stuneado')
                                self.energy -= 100
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print ('Saltas sobre tu enemigo pero de la locura te das con tu propio mazo en toda tu cabeza infligiendote', 150 * self.power / self.defense, 'de daño')
                                    self.health -= 150 * self.power / self.defense
                                    if self.carga_stun == 0:
                                        self.carga_stun += 2
                                        print('Te aturdes 2 turnos')
                                    else:
                                        print('Ya estabas stuneado')
                                    self.energy -= 100
                                    self.energy += 2
                                else:
                                    dano = 150 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Saltas sobre tu enemigo infligiendole', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    if enemy.carga_stun == 0:
                                        enemy.carga_stun += 2
                                        print('Aturdes a', enemy.name, '2 turnos')
                                    else:
                                        print(enemy.name, 'ya está stuneado')
                                    self.energy -= 100
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown3 = self.nturnos + 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'venda':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 8:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 70
                            break
                        curaa = randint(0, 100)
                        if curaa > self.precicura: 
                            print ('¡Falla la venda!')
                            self.energy -= 35
                            self.energy += 2
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te pones una venda que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 2
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 2
                            else:
                                print ('Te pones una venda que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaa = randint(0, 100)
                        if energiaa > self.precienergia: 
                            print (self.name, 'falla la canalización!')
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        else:
                            print (self.name, 'canaliza y recupera,', 120 * self.power,'de energía')
                            self.energy += 120 * self.power
                            self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad salto profundo se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('Estás inmovilizado por', self.inmovilizado, 'turnos')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
maza = Mace ('Björn', 1980, 1980, 220, 1, 1.1, 39, 90, 95, 85, 80, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Fires ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Ágil')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "fuego", aplica 1 quemadura en tu enemigo (afecta tu poder, pero no su defensa), cuesta 30 de energía y tiene', self.preci1,'% precisión')
        print ('Ataque 2: "llamas", aumentas tu defensa en 0.25 (no afecta el poder), cuesta 40 de energía y tiene', self.preci2,'% precisión')
        print ('Ataque super: "Volcan", aplicas 4 quemaduras (afecta tu poder, pero no su defensa), cuesta 120 de energía, tiene', self.preci3,'% precisión y 3 turnos de cooldown')
        print ('Vendas: "venda", cura 80 de vida (no afecta el poder), cura 1 sangrado y 1 quemadura, cuesta 70 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "ignifugo", las quemaduras no te hacen daño')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Como un ave fénix, de entre las llamas, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for firesss in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del ígneo:')
                    if turn.lower() == 'fuego':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 15
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                print ('Quemas a', enemy.name, ',le aplicas', 1 * self.power, 'quemaduras')
                                enemy.carga_quemado += 1 * self.power
                                self.energy -= 30
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print ('Te vuelves loco y te quemas, te aplicas', 1 * self.power, 'quemaduras')
                                    self.carga_quemado += 1 * self.power
                                    self.energy -= 30
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 3
                                else:
                                    print ('Quemas a', enemy.name, ',le aplicas', 1 * self.power, 'quemaduras')
                                    enemy.carga_quemado += 1 * self.power
                                    self.energy -= 30
                                    if self.energy < 0:
                                        self.health -= 800
                                    self.energy += 3
                            else:
                                print ('ERROR')

                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'llamas':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 20
                            self.energy += 3
                        else:
                            print ('Te envuelves en llamas, estas te fortalecen')
                            self.defense += 0.25 
                            self.energy -= 40
                        self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'volcan':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 120:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 60
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                print (self.name, 'invoca la fuerza de un volcán y aplica', 4 * self.power,'quemaduras a', enemy.name)
                                enemy.carga_quemado += 4 * self.power
                                self.energy -= 120
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print (self.name, 'invoca la fuerza de un volcán, pero se vuelve loco y se auto-aplica', 4 * self.power,'quemaduras')
                                    self.carga_quemado += 4 * self.power
                                    self.energy -= 120
                                    self.energy += 3
                                else:
                                    print (self.name, 'invoca la fuerza de un volcán y aplica', 4 * self.power,'quemaduras a', enemy.name)
                                    enemy.carga_quemado += 4 * self.power
                                    self.energy -= 120
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        self.cooldown3 = self.nturnos + 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'venda':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        curaaaaa = randint(0, 100)
                        if curaaaaa > self.precicura: 
                            print ('¡falla la venda!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 3
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te pones una venda que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                            else:
                                print ('Te pones una venda que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                if self.energy < 0:
                                    self.health -= 800
                                self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaaa = randint(0, 100)
                        if energiaaaa > self.precienergia: 
                            print (self.name, 'falla la canalización!')
                            self.energy += 3
                        else:
                            print (self.name, 'canaliza y recupera', 60 * self.power, 'de energía')
                            self.energy += 60 * self.power
                            self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad volcan se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado, 'turnos')
                            print ('(Las inmovilizaciones no te afectan)')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
igneo = Fires('Finnian', 1630, 1630, 130, 1, 1, 64, 80, 90, 100, 80, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Snake_Charmer():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Ágil')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "bocajarro", inflige 5 de daño entre 10 a 50 veces, cuesta 30 de energía, tiene', self.preci1,'% precisión y tiene 20% de probabilidades de infligir un sangrado en tu enemigo')
        print ('Ataque 2: "agil", aumenta la velocidad de tu objetivo en 16 (aumentado por la mitad del poder), cuesta 40 de energía,', self.preci2,'% precisión y 2 turnos de cooldown')
        print ('Ataque super: "serpiente", tu serpiente le inflige tres venenos y lo aturde 1 turno, cuesta 160 de energía, tiene', self.preci3,'% precisión y 2 turnos de cooldown')
        print ('Vendas: "venda", cura 80 de vida (no afecta el poder), cura 1 sangrado y 1 quemadura, cuesta 70 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "amigo", (en caso de un combate de más de dos) mientras estás muerto tu serpiente ataca a tu objetivo')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. ¿De donde sale esa música?, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for snake_charmerrr in range (1):
            if self.health <= 0:
                print ('Sigues muerto')
                print ('Tu serpiente inflige un veneno a', enemy.name)
                enemy.carga_veneno += 1
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del encantador de serpientes:')
                    if turn.lower() == 'bocajarro':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 15
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                bocajarro = randint (10, 50)
                                dano = (5 * self.power / enemy.defense) * bocajarro
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print (self.name, 'le da un bocajarro de', bocajarro, 'golpes a', enemy.name, ', le inflige', dano_total, 'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                punetazooo = randint (1, 100)
                                if punetazooo <= 20:
                                    enemy.carga_sangrado += 1
                                    print ('Tras un fuerte puñetazo un sangrado surge en', enemy.name)
                                self.energy -= 30
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    bocajarro = randint (10, 50)
                                    dano = (5 * self.power / self.defense) * bocajarro
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (self.name, 'se vuelve loco, se da un bocajarro de', bocajarro, 'golpes infligiendose', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    punetazooo = randint (1, 100)
                                    if punetazooo <= 20:
                                        self.carga_sangrado += 1
                                        print ('Tras un fuerte puñetazo un sangrado surge en', self.name)
                                    self.energy -= 30
                                    self.energy += 3
                                else:
                                    bocajarro = randint (10, 50)
                                    dano = (5 * self.power / enemy.defense) * bocajarro
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (self.name, 'le da un bocajarro de', bocajarro, 'golpes a', enemy.name, ', le inflige', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    punetazooo = randint (1, 100)
                                    if punetazooo <= 20:
                                        enemy.carga_sangrado += 1
                                        print ('Tras un fuerte puñetazo un sangrado surge en', enemy.name)
                                    self.energy -= 30
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'agil' or turn.lower() == 'ágil':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 40:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (self.name, 'se tropieza!')
                            self.energy -= 20
                            self.energy += 3
                        else:
                            print ('Aumentas la velocidad de', enemy.name,'en', 16 * (self.power / 2))
                            enemy.velocity += 16 * (self.power / 2)
                            self.energy -= 40
                            self.energy += 3
                        self.cooldown2 += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'serpiente':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print ('La serpiente de', self.name, 'está silenciada')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 160:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 80
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                print (self.name, 'lanza su serpiente a', enemy.name, 'le aplica 3 venenos y lo aturde 1 turno')
                                enemy.carga_veneno += 3
                                enemy.carga_stun += 1
                                self.energy -= 160
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print (self.name, 'lanza su serpiente pero está se vuelve loca y le muerde, aplicandole 3 venenos y aturdiendole 1 turno')
                                    self.carga_veneno += 3
                                    self.carga_stun += 1
                                    self.energy -= 160
                                    self.energy += 3
                                else:
                                    print (self.name, 'lanza su serpiente a', enemy.name, 'le aplica 3 venenos y lo aturde 1 turno')
                                    enemy.carga_veneno += 3
                                    enemy.carga_stun += 1
                                    self.energy -= 160
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        self.cooldown3 = self.nturnos + 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'venda':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 3
                            break
                        curaaaaa = randint(0, 100)
                        if curaaaaa > self.precicura: 
                            print ('¡falla la venda!')
                            self.energy -= 35
                            self.energy += 3
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te pones una venda que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 3
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 3
                            else:
                                print ('Te pones una venda que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaaa = randint(0, 100)
                        if energiaaaa > self.precienergia: 
                            print (self.name, 'falla la canalización!')
                            self.energy += 3
                        else:
                            print (self.name, 'canaliza y recupera', 60 * self.power, 'de energía')
                            self.energy += 60
                            self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad serpiente se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado ,'turnos')
                            print ('Estás inmovilizado por', self.inmovilizado,'turnos')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
serpientero = Snake_Charmer('Rayder', 1900, 1900, 140, 1, 1, 58, 120, 80, 95, 80, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Apostador():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, sombra, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.sombra = sombra
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: ¿¿??')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "apostar", tiene un 20% de probabilidades de infligir 180 de daño, tiene un 20% de probabilidades de curarte 10 de vida, tiene un 20% de probabilidades de aumentar tu poder en 0.1 (no afecta el poder), tiene un 20% de probabilidades de aumentar tu defensa en 0.1 (no afecta el poder) y tiene un 20% de probabilidades de aumentar tu velocidad en 4, cuesta 3 de energía, tiene', self.preci1,'% precisión')
        print ('Ataque 2: "invocar", genera una sombra, cuesta 10 de energía y', self.preci2,'% precisión')
        print ('Ataque super: "bomba", tienes un 40% de probabilidades de infligir a tu enemigo 800 de daño (no afecta la defensa superior a 1), 60% de probabilidades de auto infligirte 600 de daño (no afecta la defensa superior a 1), cuesta 20 de energía, tiene', self.preci3,'% precisión y 1 turno de cooldown')
        print ('Vendas: "venda", cura 80 de vida (no afecta el poder), cura 1 sangrado y 1 quemadura, cuesta 5 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 4 de energía y', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "maleta", tienes dos habilidades pasivas extra')
        print ('Habilidad pasiva: "casinooo", no puedes volverte loco (no más de lo que ya estás)')
        print ('Habilidad pasiva: "amigo", (en caso de un combate de más de dos) mientras estás muerto tus sombras atacan a tu objetivo')
        print ('(Cada turno recuperas 2 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Salido del casino, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for apostadorrr in range (1):
            if self.health <= 0:
                if self.sombra > 0:
                    print ('Sigues muerto')
                    print ('Tus sombras infligen', 40 * self.sombra,'a', enemy.name)
                    enemy.health += 40 * self.sombra
                    break
                else:
                    break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del apostador:')
                    if turn.lower() == 'apostar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 3:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print ('Pierdes la apuesta')
                            self.energy -= 1.5
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        else:
                            cccc = randint (0, 4)
                            if cccc == 0:
                                dano = 180 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('En la apuesta sale que', enemy.name, 'pierde', dano_total)
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                self.energy -= 3
                            elif cccc == 1:
                                print ('En la apuesta sale que', self.name, 'recupera', 10 * self.power * self.lcura * self.rcura, 'de vida')
                                self.health += 10 * self.power  * self.lcura * self.rcura
                                self.energy -= 3
                            elif cccc == 2:
                                print ('En la apuesta sale que', self.name, 'aumenta su poder en 0.1')
                                self.power += 0.1 
                                self.energy -= 3
                            elif cccc == 3:
                                print ('En la apuesta sale que', self.name, 'aumenta su defensa en 0.1')
                                self.defense += 0.1
                                self.energy -= 3
                            elif cccc == 4:
                                self.power += 0.1
                                print ('En la apuesta sale que', self.name, 'aumenta su velocidad en', 4 * self.power)
                                self.velocity += 4 * self.power
                                self.energy -= 3
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'invocar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede invocar sombras')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print ('Salió el sol y no hay sombras!')
                            self.energy -= 5
                            self.energy += 2
                        else:
                            print ('invocas una sombra')
                            self.sombra += 1
                            self.energy -= 10
                            self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas, estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados y tienes', self.sombra, 'sombras', '\n')
                    elif turn.lower() == 'bomba':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede detonar sus bombas')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 20:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print ('La bomba explota en el aire')
                            self.energy -= 10
                            self.energy += 2
                        else:
                            boombaaa = randint (1, 100)
                            if boombaaa <= 50:
                                if enemy.defense > 1:
                                    dano = 800 * self.power
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (self.name, 'lanza una bomba nuclear a', enemy.name, 'y le quita', dano_total, 'de vida')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                else:
                                    dano = 800 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (self.name, 'lanza una bomba nuclear a', enemy.name, 'y le quita', dano_total, 'de vida')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                            elif boombaaa >= 51:
                                if enemy.defense > 1:
                                    print (self.name, 'lanza una bomba nuclear a', enemy.name, ', aunque la bomba se detona antes y, ', self.name, 'se quita 600 de vida')
                                    self.health -= 600 * self.power
                                else:
                                    print (self.name, 'lanza una bomba nuclear a', enemy.name, ', aunque la bomba se detona antes y, ', self.name, 'se quita 600 de vida')
                                    self.health -= 600 * self.power / self.defense
                            self.energy -= 20
                            self.energy += 2
                        self.cooldown3 = self.nturnos + 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'venda':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 5:
                            print (self.name, 'no tiene suficiente energia')
                            self.energy += 2
                            break
                        curaaaaa = randint(0, 100)
                        if curaaaaa > self.precicura: 
                            print ('¡falla la venda!')
                            self.energy -= 2.5
                            self.energy += 2
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te pones una venda que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 5
                                self.energy += 2
                            elif self.health >= 1820:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 0
                                self.energy += 2
                            else:
                                print ('Te pones una venda que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 5
                                self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaaa = randint(0, 100)
                        if energiaaaa > self.precienergia: 
                            print (self.name, 'falla la canalización!')
                            self.energy += 2
                        else:
                            print (self.name, 'canaliza y recupera', 4 * self.power, 'de energía')
                            self.energy += 4
                            self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100')
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado, 'turnos')
                            print ('Las inmovilizaciones no te afectan')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
poker = Apostador('@#-·-#@', 1820, 1820, 10, 1, 1, 29, 300, 300, 300, 80, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Natural ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Natural')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "plantar", aplica 1 carga de cura en tu objetivo (max. 4 y no afecta el poder) y quita 1 quemadura (no afecta el poder), cuesta 8 de energía, tiene', self.preci1,'% precisión')
        print ('Ataque 2: "zarza", hace 120 de daño (si afecta el poder) y aplica 1 sangrado (no afecta el poder), cuesta 60 de energía y tiene', self.preci2,'% precisión')
        print ('Ataque 3: "pasto" encanta el pasto curando a los jugadores 0.5% de su salud máxima y en un 0.8% a los personajes de tipo natural, no cuesta energia')
        print ('Ataque super: "naturaleza", dependiendo de las cargas de cura que tenga el objetivo a curar: 0-80/1-180/2-260/3-390/4+-500 (no afecta el poder), consume las cargas de cura, cuesta 100 de energía, tiene', self.preci3,'% precisión y tiene 2 turnos de cooldown')
        print ('Poción curativa: "cura", cura 80 de vida (afecta la mitad del poder), cura 1 hemorragia y 1 quemadura, cuesta 70 de energía y tiene', self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia,'% precisión')
        print ('Habilidad pasiva: "extra", tienes un ataque tres al que no se puede bajar la precisión')
        print ('(Cada turno recuperas 4 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Una druida aparece de entres los árboles, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for naturalll in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno de la druida:')
                    if turn.lower() == 'plantar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 8:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unooo = randint(0, 100)
                        if unooo > self.preci1: 
                            print ('¡', self.name, 'falla la cura!')
                            self.energy -= 4
                            self.energy += 4
                        else:
                            print (self.name, 'cura 1 quemadura y aplicas una carga curativa a', enemy.name)
                            enemy.carga_cura += 1
                            if enemy.carga_cura >= 4:
                                (enemy.name, 'está al límite de cargas de cura')
                            if enemy.carga_quemado > 0:
                                enemy.carga_quemado -= 1
                            self.energy -= 8
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'zarza':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 60:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        dooos = randint(0, 100)
                        if dooos > self.preci2: 
                            print (self.name, 'se confunde de hechizo y convierte una hoja de pasto en un gusano')
                            self.energy -= 30
                            self.energy += 4
                        else:
                            if self.locura == 0:
                                dano = 120 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print ('Una zarza mágica abraza a', enemy.name, 'infligiendole', dano_total, 'de daño y creandole un sangrado')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                enemy.carga_sangrado += 1
                                self.energy -= 60
                                self.energy += 4
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print (self.name, 'se vuelve loca e invoca unas dagas mágicas que la atacan y le infligen', 120 * self.power / self.defense, 'de daño y creandole un sangrado')
                                    self.health -= 120 * self.power / self.defense
                                    self.carga_sangrado += 1
                                    self.energy -= 60
                                    self.energy += 4
                                else:
                                    dano = 120 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print ('Una zarza mágica abraza a', enemy.name, 'infligiendole', dano_total, 'de daño y creandole un sangrado')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_sangrado += 1
                                    self.energy -= 60
                                    self.energy += 4
                            else:
                                print ('ERROR')
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'pasto':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 0:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        print (self.name, 'encanta el pasto curando a los jugadores 0.5% de su salud máxima y en un 0.8% a los personajes de tipo natural')
                        checar_campos()
                        campo.hierba = 1 
                        self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'naturaleza':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (1, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 100:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treees = randint(0, 100)
                        if treees > self.preci3: 
                            print ('¡', self.name, 'se equivoca de hechizo y invoca una serpiente bebé inofensiva!')
                            self.energy -= 50
                            self.energy += 4
                        else:
                            if enemy.carga_cura == 0:
                                natur = 80 * self.lcura * self.rcura
                            elif enemy.carga_cura == 1:
                                natur = 180 * self.lcura * self.rcura
                            elif enemy.carga_cura == 2:
                                natur = 260 * self.lcura * self.rcura
                            elif enemy.carga_cura == 3:
                                natur = 390 * self.lcura * self.rcura
                            elif enemy.carga_cura == 4:
                                natur = 500 * self.lcura * self.rcura
                            print (self.name, 'invoca el poder de la naturaleza para curar', natur ,'de vida a',enemy.name)
                            enemy.health += natur
                            enemy.carga_cura = 0
                            self.energy -= 100
                            self.energy += 4
                        self.cooldown3 = self.nturnos + 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'cura':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        curaaa = randint(0, 100)
                        if curaaa > self.precicura: 
                            print ('Se rompe la poción!')
                            self.energy -= 35
                            self.energy += 4
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te tomas una poción que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 2
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 2
                            else:
                                print ('Te tomas una poción que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciada y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaa = randint(0, 100)
                        if energiaaa > self.precienergia: 
                            print ('¡', self.name, 'falla la canalización!')
                            self.energy += 4
                        else:
                            print (self.name, 'canaliza y recupera', 80 * self.power, 'de energía')
                            self.energy += 80 * self.power
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100)
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por',self.silenciado,'turnos')
                            print ('Las inmovilizaciones no te afectan')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
natural = Natural ('Groa', 1600, 1600, 220, 1, 1, 37, 100, 90, 120, 100, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Diablillo ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: Ágil')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "llamarada ignea", inflige 100 de daño (si afecta el poder) y le haces 1 quemadura (no afecta el poder), cuesta 30 de energía, tiene', self.preci1,'% precisión y 1 turno de cooldown')
        print ('Ataque 2: "Mordida ignea", inflige 50 de daño (si afecta el poder) y le haces 2 quemadura (no afecta el poder), cuesta 55 de energía y tiene', self.preci2,'% precisión y tiene un cooldown de 1 turno')
        print ('Ataque super: "Rafaga ignea", inflige 300 de daño (si afecta el poder) y le haces 3 quemadura (no afecta el poder), cuesta 180 de energía, tiene', self.preci3,'% precisión y tiene un cooldown de 3 turnos')
        print ('Vendas: "venda", cura 80 de vida (no afecta el poder), cura 1 sangrado y 1 quemadura, cuesta 70 de energía y tiene',self.precicura,'% precisión')
        print ('Canalización: "energia", recupera 60 de energía y',self.precienergia,'% precisión')
        print ('Habilidad pasiva: "Corazon de fuego", se cura 15 de vida y energia (no afecta el poder) al aplicar 1 quemadura (no afecta el poder)')
        print ('(Cada turno recuperas 3 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. No es fuego volador, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for diablillooo in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del diablillo:')
                    if turn.lower() == 'llamarada ignea':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 15
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                dano = 100 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print (self.name, 'quema a', enemy.name, 'aplicandole 1 quemadura y haciendole', dano_total, 'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                enemy.carga_quemado += 1
                                self.health += 15 * self.lcura * self.rcura
                                self.energy += 15
                                self.energy -= 30
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print (self.name, ' se vuelve loco y se quema a si mismo aplicandose 1 quemadura y haciendose', 100 * self.power / self.defense, 'de daño')
                                    self.health -= 100 * self.power / self.defense
                                    self.carga_quemado += 1
                                    self.health += 15 * self.lcura * self.rcura
                                    self.energy += 15
                                    self.energy -= 30
                                    self.energy += 3
                                else:
                                    dano = 100 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (self.name, 'quema a', enemy.name, 'aplicandole 1 quemadura y haciendole', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_quemado += 1
                                    self.health += 15 * self.lcura * self.rcura
                                    self.energy += 15
                                    self.energy -= 30
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        self.cooldown1 = self.nturnos + 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'mordida ignea':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede hacer nada')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 55:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (enemy.name, 'se aparta y no le alcanzas')
                            self.energy -= 26.5
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                dano = 50 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print (uno.name, 'se abalanza sobre', enemy.name, ', echando fuego por la boca lo muerdes haciendole 2 quemaduras y', dano_total, 'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                enemy.carga_quemado += 2
                                self.health += 30 * self.lcura * self.rcura
                                self.energy += 30
                                self.energy -= 55
                                self.cooldown2 += self.nturnos + 2
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print (uno.name, 'se vuelve loco y echando fuego por la boca se muerde haciendose 2 quemaduras y', 50 * self.power / self.defense, 'de daño')
                                    self.health -= 50 * self.power / self.defense
                                    self.carga_quemado += 2
                                    self.health += 30 * self.lcura * self.rcura
                                    self.energy += 30
                                    self.energy -= 55
                                    self.energy += 3
                                else:
                                    dano = 50 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (uno.name, 'se abalanza sobre', enemy.name, ', echando fuego por la boca lo muerdes haciendole 2 quemaduras y', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_quemado += 2
                                    self.health += 30 * self.lcura * self.rcura
                                    self.energy += 30
                                    self.energy -= 55
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        self.cooldown2 = self.nturnos + 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'rafaga ignea':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede atacar')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 180:
                            print (uno.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print (self.name, 'falla el golpe!')
                            self.energy -= 90
                            self.energy += 3
                        else:
                            if self.locura == 0:
                                dano = 300 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print (self.name, 'lanza una ráfaga de bolas ígneas aplicando 3 quemaduras a', enemy.name, 'e infligiendole', dano_total,'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                enemy.carga_quemado += 3
                                self.health += 45 * self.lcura * self.rcura
                                self.energy += 45
                                self.energy -= 180
                                self.energy += 3
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print (self.name, 'se vuelve loco y lanza una ráfaga de bolas ígneas a si mismo aplicandose 3 quemaduras e infligiendose', 300 * self.power / self.defense,'de daño')
                                    self.health -= 300 * self.power / self.defense
                                    self.carga_quemado += 3
                                    self.health += 45 * self.lcura * self.rcura
                                    self.energy += 45
                                    self.energy -= 180
                                    self.energy += 3
                                else:
                                    dano = 300 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (self.name, 'lanza una ráfaga de bolas ígneas aplicando 3 quemaduras a', enemy.name, 'e infligiendole', dano_total,'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_quemado += 3
                                    self.health += 45 * self.lcura * self.rcura
                                    self.energy += 45
                                    self.energy -= 180
                                    self.energy += 3
                            else:
                                print ('ERROR')
                        self.cooldown3 = self.nturnos + 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'venda':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (uno.name, 'no tiene suficiente energia')
                            break
                        curaaaaa = randint(0, 100)
                        if curaaaaa > self.precicura: 
                            print ('¡falla la venda!')
                            self.energy -= 35
                            self.energy += 3
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te pones una venda que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 3
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 3
                            else:
                                print ('Te pones una venda que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaaa = randint(0, 100)
                        if energiaaaa > self.precienergia: 
                            print (self.name, 'falla la canalización!')
                            self.energy += 3
                        else:
                            print (self.name, 'canaliza y recupera', 60 * self.power, 'de energía')
                            self.energy += 60 * self.power
                            self.energy += 3
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad rafaga ignea se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100)
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('Estás inmovilizado por', self.inmovilizado,'turnos')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
diablillo = Diablillo('Gillmore', 2000, 2000, 145, 1, 1, 75, 100, 90, 90, 80, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Support ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, cargado, cargadocooldown, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.cargado = cargado
        self.cargadocooldown = cargadocooldown
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: mago')
        print ('Nivel de salud:', self.health)
        print ('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "escudo", aumenta la vida en 10 y la defensa en 0.05, cuesta 12 de energía, tiene',self.preci1,'% precisión')
        print ('Ataque 2: "agilizar", aumenta la velocidad en 8, cuesta 30 de energía y tiene', self.preci2 ,'% precisión, y 1 turno de cooldown')
        print ('Ataque 3: "purificador" carga el aire de un hechizo que quita todas las cargas de todos los personajes (en cada turno), no cuesta energia')
        print ('Ataque super: "sobrecargar", aumenta el poder de tu objetivo en 3 después de 3 turnos esa potenciación se quita y con ella 300 de vida, además tiene un 15% de probabilidades de quitarse 200 de vida extra, cuesta 20 de energía, tiene ', self.preci3 ,'% precisión y un cooldown de 3 turnos')
        print ('Poción curativa: "cura", cura 80 de vida (afecta la mitad del poder), cura 1 hemorragia y 1 quemadura, cuesta 70 de energía y tiene', self.precicura ,'% precisión')
        print ('Canalización: "energia", recupera 80 de energía y tiene', self.precienergia ,'% precisión')
        print ('Habilidad pasiva: "maleta", tienes dos habilidades pasivas extras')
        print ('Habilidad pasiva: "apoyo", puedes dar tu cura a tu objetivo escribiendo "curar", además de poder canalizar para tu objetivo escribiendo "energiar"')
        print ('Habilidad pasiva: "extra", tienes un ataque tres al que no se puede bajar la precisión')
        print ('(Cada turno recuperas 4 de energia) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for suporttt in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    turn = input('Turno del mago ayudante:')
                    if turn.lower() == 'escudo':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown1 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        unooo = randint(0, 100)
                        if unooo > self.preci1: 
                            print ('¡', self.name, 'falla el encantamiento!')
                            self.energy -= 5
                            self.energy += 4
                        else:
                            print ('Invocas un escudo sobre', enemy.name, 'que aumenta su vida en', 10 * self.power,'y su defensa en', 0.05 * self.power)
                            enemy.health += 10 * self.power
                            enemy.defense += 0.05 * self.power
                            self.energy -= 10
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'agilizar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 30:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        dooos = randint(0, 100)
                        if dooos > self.preci2: 
                            print (self.name, 'se confunde de hechizo y convierte uno de sus calcetines en un gorrión')
                            self.energy -= 15
                            self.energy += 4
                        else:
                            print ('Aumentas la velocidad de', enemy.name, 'en', 8 * self.power)
                            enemy.velocity += 8 * self.power
                            self.energy -= 30
                            self.energy += 4
                        self.cooldown2 = self.nturnos +  2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'purificador':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.carga_stun > 0:
                            print (self.name, 'está stuneado y no puede hacer nada')
                            self.carga_stun -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 0:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        print (self.name, 'carga el aire de un hechizo que quita todas las cargas de todos los personajes')
                        checar_campos()
                        campo.purificador = 1 
                        self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'sobrecargar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede lanzar este hechizo')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (1, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 20:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treees = randint(0, 100)
                        if treees > self.preci3: 
                            print ('¡', self.name, 'se equivoca de hechizo y convierte su bota en una manzana!')
                            self.energy -= 10
                            self.energy += 4
                        else:
                            self.cargado = enemy
                            if self.cargado == support:
                                print ('Te cargas durante 3 turnos para aumentar tu poder en 3')
                                self.power += 3
                                self.cooldown3 += self.nturnos + 4
                                self.energy -= 20
                                self.energy += 4
                                print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                                print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                                break
                            print ('Cargas a', enemy.name, 'durante 3 turnos para aumentar su poder en 3')
                            enemy.power += 3
                            self.energy -= 20
                            self.energy += 4
                        self.cooldown3 = self.nturnos + 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'cura':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        curaaa = randint(0, 100)
                        if curaaa > self.precicura: 
                            print ('Se rompe la poción!')
                            self.energy -= 35
                            self.energy += 4
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te tomas una poción que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 2
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 2
                            else:
                                print ('Te tomas una poción que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_hemorragia > 0:
                                    self.carga_hemorragia -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 70
                                self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'curar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        curaaa = randint(0, 100)
                        if curaaa > self.precicura: 
                            print ('Se rompe la poción!')
                            self.energy -= 35
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            print ('Le das una poción a', enemy.name, 'que le cura', 80 * (self.power/2) ,'de vida')
                            enemy.health += 80 * (self.power/2)
                            if enemy.carga_hemorragia > 0:
                                enemy.carga_hemorragia -= 1
                            if enemy.carga_quemado > 0:
                                enemy.carga_quemado -= 1
                            self.energy -= 70
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaa = randint(0, 100)
                        if energiaaa > self.precienergia: 
                            print ('¡', self.name, 'falla la canalización!')
                            self.energy += 4
                        else:
                            print (self.name, 'canaliza y recupera', 80 * self.power, 'de energía')
                            self.energy += 80 * self.power
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energiar':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaa = randint(1, 100)
                        if energiaaa > self.precienergia: 
                            print ('¡', self.name, 'falla la canalización!')
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        else:
                            print (self.name, 'canaliza y recupera', 80 * self.power, 'de energía para', enemy.name)
                            enemy.energy += 80 * self.power
                            if self.energy < 0:
                                self.health -= 800
                            self.energy += 4
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La habilidad sobrecargar se puede volver a lanzar en el turno', self.cooldown3)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100)
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('(Las inmovilizaciones no te afectan)')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
                    if self.cargadocooldown > 0:
                        self.cargadocooldown -= 1
                        if self.cargadocooldown == 0:
                            print ('A', self.cargado.name, 'se le acaba el poder de la sobrecarga')
                            self.cargado.power -= 3
                            sobrecargaaaa = randint (1, 100)
                            if sobrecargaaaa <= 15:
                                self.cargado.health -= 800
                                print (self.cargado.name, 'se quita 800 de vida debido a la repentina bajada de poder')
                            else:
                                self.cargado.health -= 500
                                print (self.cargado.name, 'se quita 500 de vida debido a la repentina bajada de poder')
support = Support ('Wymond', 1780, 1780, 180, 1, 1, 36, 120, 120, 200, 100, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, '', 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Chiquitin():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, ko, lcura, rcura, sangre, mutado, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3): 
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.ko = ko
        self.lcura = lcura
        self.rcura = rcura
        self.sangre = sangre
        self.mutado = mutado
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def print_info(self):
        print ('Tipo: misterioso')
        print('Nivel de salud:', self.health)
        print('Energía:', self.energy)
        print ('Poder:', self.power)
        print ('Defensa:', self.defense)
        print ('Velocidad:', self.velocity)
        print ('Ataque 1: "bocajarro", inflige 5 de daño entre 10 a 50 veces, cuesta 2 de energía, tiene', self.preci1 ,'% precisión, 1 turno de cooldown y tiene 20% de probabilidades de infligir un sangrado en tu enemigo')
        print ('Ataque 2: "mordida ignea", inflige 50 de daño (si afecta el poder) y le haces 2 quemadura (no afecta el poder), cuesta 8 de energía, tiene 1 turno de cooldown y un', self.preci2 ,'% precisión')
        print ('Ataque super: "Ira", aumenta tu poder en 1 (no afecta el poder), cuesta 10 de energía, tiene ', self.preci3 ,'% precisión y 1 turno de cooldown')
        print ('Vendas: "venda", cura 80 de vida (no afecta el poder), cura 1 sangrado y 1 quemadura, cuesta 5 de energía y tiene ', self.precicura ,'% precisión')
        print ('Canalización: "energia", recupera 4 de energía y ', self.precienergia ,'% precisión')
        print ('Habilidad pasiva: "regenerativo", al principio de tu turno recuperas toda tu vida')
        print ('(Cada turno recuperas 2 de energia)(Si te quedas con energía negativa pierdes 800 puntos de vida) (Lo que hagas en tu turno será multiplicado por el poder y el daño que recibas será dividido por la defensa)', '\n')
    def hello(self):
        print ('NUEVO HÉROE. Salido del casino, es ¡', self.name, '!', '\n')
        self.print_info()
    def turno(self, enemy):
        for chiquitin in range (1):
            if self.health <= 0:
                break
            else:
                if campo.sol == 1:
                    if self.carga_hielo > 0:
                        print ('El calor descongela a', self.name)
                        self.carga_hielo = 0
                    if self.carga_stun > 0:
                        print ('El calor espabila a', self.name, 'y lo quita de su ensimismamiento (stuneo)')
                        self.carga_stun = 0
                if self.carga_hielo > 0:
                    print (self.name, 'está congelado y no puede hacer nada')
                    self.carga_hielo -= 1
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                if self.carga_stun > 0:
                    #cargas
                    cargas(self)
                    #el turno
                    self.carga_stun -= 1
                    print (self.name, 'está stuneado y no puede hacer nada, turnos restantes:', self.carga_stun)
                    print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                    print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    break
                else:
                    self.health = self.maxhealth
                    print (self.name, 'regenera su vida')
                    turn = input('Turno del chiquitín:')
                    if turn.lower() == 'bocajarro':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            self.silenciado -= 1
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 2:
                            print (self.name, 'no tiene suficiente energia)', '\n')
                            break
                        unoooo = randint(0, 100)
                        if unoooo > self.preci1: 
                            print ('Fallas el golpe')
                            self.energy -= 1
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                bocajarro = randint (10, 50)
                                dano = (5 * self.power / enemy.defense) * bocajarro
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print (self.name, 'le da un bocajarro de', bocajarro, 'golpes a', enemy.name, ', le inflige', dano_total ,'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                punetazooo = randint (1, 100)
                                if punetazooo <= 20:
                                    enemy.carga_sangrado += 1
                                    print ('Tras un fuerte puñetazo un sangrado surge en', enemy.name)
                                self.energy -= 2
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    bocajarro = randint (10, 50)
                                    print (self.name, 'se vuelve loco y se da un bocajarro de', bocajarro, 'golpes a si mismo, se inflige', (5 * self.power / self.defense) * bocajarro, 'de daño')
                                    self.health -= (5 * self.power / self.defense) * bocajarro
                                    punetazooo = randint (1, 100)
                                    if punetazooo <= 20:
                                        self.carga_sangrado += 1
                                        print ('Tras un fuerte puñetazo un sangrado surge en', self.name)
                                    self.energy -= 2
                                    self.energy += 2
                                else:
                                    bocajarro = randint (10, 50)
                                    dano = (5 * self.power / enemy.defense) * bocajarro
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (self.name, 'le da un bocajarro de', bocajarro, 'golpes a', enemy.name, ', le inflige', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    punetazooo = randint (1, 100)
                                    if punetazooo <= 20:
                                        enemy.carga_sangrado += 1
                                        print ('Tras un fuerte puñetazo un sangrado surge en', enemy.name)
                                    self.energy -= 2
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown1 = self.nturnos + 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'mordida ignea':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede atacar')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            print (self.name, 'está inmovilizado y no puede moverse y por lo tanto no puede atacar')
                            self.inmovilizado -= 1
                            break
                        
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 8:
                            print (self.name, 'no tiene suficiente energia')
                            break
                        if self.cooldown2 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        doooos = randint(0, 100)
                        if doooos > self.preci2: 
                            print (enemy.name, 'se aparta y no le alcanzas')
                            self.energy -= 4
                            self.energy += 2
                        else:
                            if self.locura == 0:
                                dano = 50 * self.power / enemy.defense
                                reflejo = dano * enemy.reflejar 
                                dano_total = dano - reflejo
                                enemy.health -= dano_total
                                self.health -= reflejo
                                print (uno.name, 'se abalanza sobre', enemy.name, ', echando fuego por la boca lo muerdes haciendole 2 quemaduras y', dano_total, 'de daño')
                                if enemy.reflejar > 0:
                                    print (enemy.name, 'refleja', reflejo, 'de daño')
                                enemy.carga_quemado += 2
                                self.energy -= 8
                                self.energy += 2
                            elif self.locura > 0 and self.locura <= 100:
                                locuraaa = randint (1, 100)
                                if locuraaa > self.locura:
                                    print (uno.name, 'se vuelve loco y echando fuego por la boca se muerde haciendose 2 quemaduras y', 50 * self.power / self.defense, 'de daño')
                                    self.health -= 50 * self.power / self.defense
                                    self.carga_quemado += 2
                                    self.energy -= 8
                                    self.energy += 2
                                else:
                                    dano = 50 * self.power / enemy.defense
                                    reflejo = dano * enemy.reflejar 
                                    dano_total = dano - reflejo
                                    enemy.health -= dano_total
                                    self.health -= reflejo
                                    print (uno.name, 'se abalanza sobre', enemy.name, ', echando fuego por la boca lo muerdes haciendole 2 quemaduras y', dano_total, 'de daño')
                                    if enemy.reflejar > 0:
                                        print (enemy.name, 'refleja', reflejo, 'de daño')
                                    enemy.carga_quemado += 2
                                    self.energy -= 8
                                    self.energy += 2
                            else:
                                print ('ERROR')
                        self.cooldown2 = self.nturnos + 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'ira':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede enfurecerse')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 10:
                            print (self.name, 'no tiene suficiente energia', '\n')
                            break
                        if self.cooldown3 > self.nturnos:
                            print ('Esta habilidad aún está en cooldawn')
                            break
                        treeees = randint(0, 100)
                        if treeees > self.preci3: 
                            print ('Fallas!')
                            self.energy -= 5
                            self.energy += 2
                        else:
                            print (self.name, 'se enfurece y aumenta su poder en uno, ¡', enemy.name, 'apurate en matarlo!!')
                            self.power += 1
                            self.energy -= 10
                            self.energy += 2
                        self.cooldown3 = self.nturnos + 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'venda':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede curarse')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        if self.energy <= 70:
                            print (self.energy, 'no tiene suficiente energia')
                            break
                        curaaaaa = randint(0, 100)
                        if curaaaaa > self.precicura: 
                            print ('¡falla la venda!')
                            self.energy -= 2.5
                            self.energy += 2
                        else:
                            if self.health >= self.maxhealth - 80 * (self.power/2) and self.health < self.maxhealth:
                                print ('Te pones una venda que te cura toda la vida')
                                self.health = self.maxhealth
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 5
                                self.energy += 2
                            elif self.health >= self.maxhealth:
                                print ('Ya supera la vida máxima, por lo tanto no se cura')
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy += 2
                            else:
                                print ('Te pones una venda que te cura', 80 * (self.power/2) ,'de vida')
                                self.health += 80 * (self.power/2)
                                if self.carga_sangrado > 0:
                                    self.carga_sangrado -= 1
                                if self.carga_quemado > 0:
                                    self.carga_quemado -= 1
                                self.energy -= 5
                                self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'energia':
                        #cargas
                        cargas(self)
                        #el turno
                        if self.silenciado > 0:
                            print (self.name, 'está silenciado y no puede canalizar')
                            self.silenciado -= 1
                            break
                        elif self.inmovilizado > 0:
                            self.inmovilizado -= 1
                        elif self.carga_paralizado > 0:
                            paraliza = randint (0, 100)
                            if paraliza <= 40:
                                print (self.name, 'está paralizado y no puede hacer nada')
                                self.carga_paralizado -= 1
                                break
                            else:
                                print (self.name, 'no se paraliza')
                                self.carga_paralizado -= 1
                        energiaaaa = randint(0, 100)
                        if energiaaaa > self.precienergia: 
                            print (self.name, 'falla la canalización!')
                            self.energy += 2
                        else:
                            print (self.name, 'canaliza y recupera', 4 * self.power, 'de energía')
                            self.energy += 4
                            self.energy += 2
                        print ('A', enemy.name, 'le quedan', enemy.health, 'puntos de vida,', enemy.energy, 'puntos de energia, su poder es de', enemy.power, ', su defensa es de', enemy.defense,'y su velocidad de', enemy.velocity,',y tiene', enemy.carga_hemorragia, 'hemorragias,', enemy.carga_sangrado, 'sangrados,', enemy.carga_quemado, 'quemaduras,', enemy.carga_cura, 'cargas de cura,', enemy.carga_veneno, 'cargas de veneno', enemy.carga_maldita, 'cargas malditas y está', enemy.carga_hielo + enemy.carga_stun + enemy.carga_paralizado, 'turnos congelados/stuneados/paralizados')
                        print ('Tienes', self.health, 'puntos de vida, tu poder es de', self.power, ', tu defensa es de', self.defense,'y tu velocidad de', self.velocity, ', te quedan', self.energy, 'puntos de energía, tienes', self.carga_hemorragia, 'hemorragias,', self.carga_sangrado, 'sangrados,', self.carga_quemado, 'quemaduras,', self.carga_cura,'cargas de cura,', self.carga_veneno, 'cargas de veneno y', self.carga_maldita, 'cargas malditas y estás', self.carga_hielo + self.carga_stun + self.carga_paralizado, 'turnos congelados/stuneados/paralizados', '\n')
                    elif turn.lower() == 'stats':
                        if self.silenciado > 0:
                            print ('Estás silenciado')
                        else:
                            print ('Estás en el turno', self.nturnos)
                            print ('La precisión del ataque uno es de: ', self.preci1, '%')
                            print ('La precisión del ataque dos es de: ', self.preci1, '%')
                            print ('La precisión del ataque tres es de: ', self.preci3, '%')
                            print ('La precisión de la cura es de: ', self.precicura, '%')
                            print ('La precisión de la canalización uno es de: ', self.precienergia, '%')
                            print ('El lanzamiento de curación es de:', self.lcura * 100 ,'%')
                            print ('La cura recibida es de:', self.rcura * 100, '%')
                            #print ('La cantidad de sangre es de', self.sangre,'/100)
                            print ('La locura es del:', self.locura,'%')
                            print ('Estás silenciado por', self.silenciado,'turnos')
                            print ('Estás inmovilizado por', self.inmovilizado, 'turnos')
                            print ('Reflejas un', self.reflejar,'% del daño recibido')
                        self.turno (enemy)
                    else:
                        print ('Mal', '\n')
                        self.turno (enemy)
chiquitin = Chiquitin('$)¬"#@', 400, 400, 10, 1, 1, 32, 120, 90, 75, 80, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 100, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class BoxBlue ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, lcura, rcura, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.lcura = lcura
        self.rcura = rcura
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def turno (self):
        boxblue.nturnos += 1
        if self.carga_hielo > 0:
            print ('La caja está congelada y no es afectada por efectos de daño continuo')
            self.carga_hielo -= 1
        else:
            cargas(self)
boxblue = BoxBlue ('Caja Azul', 2000, 2000, 1000000, 1, 5, 0, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class BoxRed ():
    def __init__(self, name, maxhealth, health, energy, power, defense, velocity, preci1, preci2, preci3, precicura, precienergia, carga_veneno, carga_quemado, carga_sangrado, carga_hemorragia, carga_maldita, carga_hielo, carga_stun, carga_paralizado, carga_cura, tipo, mundo, nturnos, lcura, rcura, efectod1, efectodn1, tiempod1, efectod2, efectodn2, tiempod2, efectod3, efectodn3, tiempod3, efectod4, efectodn4, tiempod4, efectod5, efectodn5, tiempod5, efecto1, efecton1, tiempo1, efecto2, efecton2, tiempo2, efecto3, efecton3, tiempo3, efecto4, efecton4, tiempo4, efecto5, efecton5, tiempo5, locura, silenciado, inmovilizado, corrupcion, reflejar, dormido, focus, cooldown1, cooldown2, cooldown3):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health #número
        self.energy = energy
        self.power = power
        self.defense = defense
        self.velocity = velocity
        self.preci1 = preci1
        self.preci2 = preci2
        self.preci3 = preci3
        self.precicura = precicura
        self.precienergia = precienergia
        self.carga_veneno = carga_veneno
        self.carga_quemado = carga_quemado
        self.carga_sangrado = carga_sangrado
        self.carga_hemorragia = carga_hemorragia
        self.carga_maldita = carga_maldita
        self.carga_hielo = carga_hielo
        self.carga_stun = carga_stun
        self.carga_paralizado = carga_paralizado
        self.carga_cura = carga_cura
        self.tipo = tipo
        self.mundo = mundo
        self.nturnos = nturnos
        self.lcura = lcura
        self.rcura = rcura
        self.efectod1 = efectod1 #efecto (duradero)(duradero quiere decir que el efecto termina cuando el tiempo se agota)
        self.efectodn1 = efectodn1 #efecto (duradero numero)
        self.tiempod1 = tiempod1 #tiempo (duradero)
        self.efectod2 = efectod2
        self.efectodn2 = efectodn2
        self.tiempod2 = tiempod2
        self.efectod3 = efectod3
        self.efectodn3 = efectodn3
        self.tiempod3 = tiempod3
        self.efectod4 = efectod4
        self.efectodn4 = efectodn4
        self.tiempod4 = tiempod4
        self.efectod5 = efectod5
        self.efectodn5 = efectodn5
        self.tiempod5 = tiempod5
        self.efecto1 = efecto1 #efecto que se aplica cada turno, el último será el que marque la variable de tiempo
        self.efecton1 = efecton1 #efecto (numero)
        self.tiempo1 = tiempo1
        self.efecto2 = efecto2 
        self.efecton2 = efecton2 
        self.tiempo2 = tiempo2
        self.efecto3 = efecto3
        self.efecton3 = efecton3 
        self.tiempo3 = tiempo3
        self.efecto4 = efecto4
        self.efecton4 = efecton4 
        self.tiempo4 = tiempo4
        self.efecto5 = efecto5 
        self.efecton5 = efecton5 
        self.tiempo5 = tiempo5
        self.locura = locura #%
        self.silenciado = silenciado #solo poder usar ataque 1
        self.inmovilizado = inmovilizado
        self.corrupcion = corrupcion #solo 0 y 1
        self.reflejar = reflejar
        self.dormido = dormido
        self.focus = focus #cadena
        self.cooldown1 = cooldown1
        self.cooldown2 = cooldown2
        self.cooldown3 = cooldown3
    def turno (self):
        boxred.nturnos += 1
        if self.carga_hielo > 0:
            print ('La caja está congelada y no es afectada por efectos de daño continuo')
            self.carga_hielo -= 1
        else:
            cargas(self)
boxred = BoxRed ('Caja Roja', 2000, 2000, 1000000, 1, 5, 0, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, '', -1, 0, 0, 0, 0, 0, 0, 0, '', 0, 0, 0)

class Campo():
    def __init__ (self, lluvia, hierba, sol, nevar, purificador, trrr):
        self.lluvia = lluvia
        self.hierba = hierba
        self.sol = sol
        self.nevar = nevar
        self.purificador = purificador
        self.trrr = trrr
campo = Campo(0, 0, 0, 0, 0, 0)

#partidas

cuantosplayers = input ('Introdusca un numero del 2-4 para jugar una partida a muerte de ese mismo numero de jugadores o introduzca "atraco" para jugar un 3vs3 a destruir la caja enemiga')
if cuantosplayers == '2':
    uno = input('Jugador 1, escoja su personaje: Warrior, Magician, Hereje, Maldi, Thief, Shapeshifter, Mace, Fires, Snake Charner, Apostador, Natural, Diablillo, Chiquitin')
    while True:
        dos = input('Jugador 2, escoja su personaje: (No repetir)')
        if dos == uno:
            print ('No se pueden repetir personajes!!')
        else:
            break
    if uno.lower() == 'warrior':
        uno = guerrero
    elif uno.lower() == 'magician':
        uno = mago
    elif uno.lower() == 'hereje':
        uno = arquero
    elif uno.lower() == 'maldi':
        uno = maldito
    elif uno.lower() == 'thief':
        uno = robador
    elif uno.lower() == 'shapeshifter':
        uno = pantera
    elif uno.lower() == 'mace':
        uno = maza
    elif uno.lower() == 'fires':
        uno = igneo
    elif uno.lower() == 'snake charner':
        uno = serpientero
    elif uno.lower() == 'natural':
        uno = natural
    elif uno.lower() == 'apostador':
        uno = poker
    elif uno.lower() == 'diablillo':
        uno = diablillo
    elif uno.lower() == 'chiquitin':
        uno = chiquitin
    if dos.lower() == 'warrior':
        dos = guerrero
    elif dos.lower() == 'magician':
        dos = mago
    elif dos.lower() == 'hereje':
        dos = arquero
    elif dos.lower() == 'maldi':
        dos = maldito
    elif dos.lower() == 'thief':
        dos = robador
    elif dos.lower() == 'shapeshifter':
        dos = pantera
    elif dos.lower() == 'mace':
        dos = maza
    elif dos.lower() == 'fires':
        dos = igneo
    elif dos.lower() == 'snake charner':
        dos = serpientero
    elif dos.lower() == 'apostador':
        dos = poker
    elif dos.lower() == 'natural':
        dos = natural
    elif dos.lower() == 'diablillo':
        dos = diablillo
    elif dos.lower() == 'chiquitin':
        dos = chiquitin
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores bajando su defensa en 0.8')
        uno.defense -= 0.8
        dos.defense -= 0.8
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        if uno.tipo == 2:
            print (uno.name, 'recibe 0.25 más de defensa')
            uno.defense += 0.25
        if dos.tipo == 2:
            print (dos.name, 'recibe 0.25 más de defensa')
            dos.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        if uno.tipo == 3:
            print (uno.name, 'recibe 0.25 más de poder')
            uno.power += 0.25
        if dos.tipo == 3:
            print (dos.name, 'recibe 0.25 más de poder')
            dos.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        if uno.tipo == 1:
            print (uno.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            uno.defense += 0.2
            uno.velocity += 25
        if dos.tipo == 1:
            print (dos.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            dos.defense += 0.2
            dos.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        if uno.tipo == 0:
            print (uno.name, 'recibe 60 más de velocidad')
            uno.velocity += 60
        if dos.tipo == 0:
            print (dos.name, 'recibe 60 más de velocidad')
            dos.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        uno.preci1 -= 20
        uno.preci2 -= 20
        uno.preci3 -= 20
        uno.precicura -= 20
        uno.precienergia -= 20
        dos.preci1 -= 20
        dos.preci2 -= 20
        dos.preci3 -= 20
        dos.precicura -= 20
        dos.precienergia -= 20
    elif escenario == 12:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        uno.energy += 100000
        dos.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            uno.hello()
            dos.hello()
            while uno.health > 0 and dos.health > 0:
                if uno.velocity <= dos.velocity:
                    playone2 ()
                    playtwo2 ()

                elif uno.velocity > dos.velocity:
                    playtwo2 ()
                    playone2 ()
    elif escenario == 11:
        for escenario11_2 in range (1):
            print ('La pelea se desarrolla en medio de una densa niebla (tu objetivo se selecciona aleatoriamente)')
            uno.hello()
            dos.hello()
            while uno.health > 0 and dos.health > 0:
                if uno.velocity >= dos.velocity:
                    playone2random ()
                    playtwo2random ()

                elif uno.velocity < dos.velocity:
                    playtwo2random ()
                    playone2random ()
    if escenario != 10 or escenario != 11:
        uno.hello()
        dos.hello()
        while uno.health > 0 and dos.health > 0:
            if uno.velocity >= dos.velocity:
                playone2 ()
                playtwo2 ()

            elif uno.velocity < dos.velocity:
                playtwo2 ()
                playone2 ()

elif cuantosplayers == '3':
    uno = input('Jugador 1, escoja su personaje: Warrior, Magician, Hereje, Maldi, Thief, Shapeshifter, Mace, Healer, Fires, Snake Charner, Apostador, Natural, Diablillo, Support, Chiquitin')
    while True:
        dos = input('Jugador 2, escoja su personaje: (No repetir)')
        if dos == uno:
            print ('No se pueden repetir personajes!!')
        else:
            break
    while True:
        tres = input('Jugador 3, escoja su personaje:')
        if tres == uno or tres == dos:
            print ('No se pueden repetir personajes!!')
        else:
            break
    if uno.lower() == 'warrior':
        uno = guerrero
    elif uno.lower() == 'magician':
        uno = mago
    elif uno.lower() == 'hereje':
        uno = arquero
    elif uno.lower() == 'maldi':
        uno = maldito
    elif uno.lower() == 'thief':
        uno = robador
    elif uno.lower() == 'shapeshifter':
        uno = pantera
    elif uno.lower() == 'healer':
        uno = curandera
    elif uno.lower() == 'mace':
        uno = maza
    elif uno.lower() == 'fires':
        uno = igneo
    elif uno.lower() == 'snake charner':
        uno = serpientero
    elif uno.lower() == 'apostador':
        uno = poker
    elif uno.lower() == 'natural':
        uno = natural
    elif uno.lower() == 'diablillo':
        uno = diablillo
    elif uno.lower() == 'support':
        uno = support
    elif uno.lower() == 'chiquitin':
        uno = chiquitin
    if dos.lower() == 'warrior':
        dos = guerrero
    elif dos.lower() == 'magician':
        dos = mago
    elif dos.lower() == 'hereje':
        dos = arquero
    elif dos.lower() == 'maldi':
        dos = maldito
    elif dos.lower() == 'thief':
        dos = robador
    elif dos.lower() == 'shapeshifter':
        dos = pantera
    elif dos.lower() == 'healer':
        dos = curandera
    elif dos.lower() == 'mace':
        dos = maza
    elif dos.lower() == 'fires':
        dos = igneo
    elif dos.lower() == 'snake charner':
        dos = serpientero
    elif dos.lower() == 'apostador':
        dos = poker
    elif dos.lower() == 'natural':
        dos = natural
    elif dos.lower() == 'diablillo':
        dos = diablillo
    elif dos.lower() == 'support':
        dos = support
    elif dos.lower() == 'chiquitin':
        dos = chiquitin
    if tres.lower() == 'warrior':
        tres = guerrero
    elif tres.lower() == 'magician':
        tres = mago
    elif tres.lower() == 'hereje':
        tres = arquero
    elif tres.lower() == 'maldi':
        tres = maldito
    elif tres.lower() == 'thief':
        tres = robador
    elif tres.lower() == 'shapeshifter':
        tres = pantera
    elif tres.lower() == 'healer':
        tres = curandera
    elif tres.lower() == 'mace':
        tres = maza
    elif tres.lower() == 'fires':
        tres = igneo
    elif tres.lower() == 'snake charner':
        tres = serpientero
    elif tres.lower() == 'apostador':
        tres = poker
    elif tres.lower() == 'natural':
        tres = natural
    elif tres.lower() == 'diablillo':
        tres = diablillo
    elif tres.lower() == 'support':
        tres = support
    elif uno.lower() == 'chiquitin':
        uno = chiquitin
    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores bajando su defensa en 0.8')
        uno.defense -= 0.8
        dos.defense -= 0.8
        tres.defense -= 0.8
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        if uno.tipo == 2:
            print (uno.name, 'recibe 0.25 más de defensa')
            uno.defense += 0.25
        if dos.tipo == 2:
            print (dos.name, 'recibe 0.25 más de defensa')
            dos.defense += 0.25
        if tres.tipo == 2:
            print (tres.name, 'recibe 0.25 más de defensa')
            tres.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        if uno.tipo == 3:
            print (uno.name, 'recibe 0.25 más de poder')
            uno.power += 0.25
        if dos.tipo == 3:
            print (dos.name, 'recibe 0.25 más de poder')
            dos.power += 0.25
        if tres.tipo == 3:
            print (tres.name, 'recibe 0.25 más de poder')
            tres.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        if uno.tipo == 1:
            print (uno.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            uno.defense += 0.2
            uno.velocity += 25
        if dos.tipo == 1:
            print (dos.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            dos.defense += 0.2
            dos.velocity += 25
        if tres.tipo == 1:
            print (tres.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            tres.defense += 0.2
            tres.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        if uno.tipo == 0:
            print (uno.name, 'recibe 60 más de velocidad')
            uno.velocity += 60
        if dos.tipo == 0:
            print (dos.name, 'recibe 60 más de velocidad')
            dos.velocity += 60
        if tres.tipo == 0:
            print (tres.name, 'recibe 60 más de velocidad')
            tres.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        uno.preci1 -= 20
        uno.preci2 -= 20
        uno.preci3 -= 20
        uno.precicura -= 20
        uno.precienergia -= 20
        dos.preci1 -= 20
        dos.preci2 -= 20
        dos.preci3 -= 20
        dos.precicura -= 20
        dos.precienergia -= 20
        tres.preci1 -= 20
        tres.preci2 -= 20
        tres.preci3 -= 20
        tres.precicura -= 20
        tres.precienergia -= 20
    elif escenario == 12:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        uno.energy += 100000
        dos.energy += 100000
        tres.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            uno.hello()
            dos.hello()
            tres.hello()
            uno.hello()
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0:
                if uno.velocity <= dos.velocity and uno.velocity <= tres.velocity:
                    playone3 ()

                    if dos.velocity <= tres.velocity:
                        playtwo3 ()

                        playthree3 ()

                    elif dos.velocity > tres.velocity:
                        playthree3 ()

                        playtwo3 ()

                elif dos.velocity <= uno.velocity and dos.velocity <= tres.velocity:
                    playtwo3 ()

                    if uno.velocity <= tres.velocity:
                        playone3 ()
                        playthree3 ()

                    elif uno.velocity > tres.velocity:
                        playthree3 ()
                        playone3 ()

                elif tres.velocity <= dos.velocity and tres.velocity <= uno.velocity:
                    playthree3 ()

                    if uno.velocity <= dos.velocity:
                        playone3 ()
                        playtwo3 ()

                    elif uno.velocity > dos.velocity:
                        playtwo3 ()
                        playone3 ()

                if dos.health <= 0 and tres.health <= 0:
                    print (uno.name, 'WIIIIN')
                    break
                elif uno.health <= 0 and tres.health <= 0:
                    print (dos.name, 'WIIIIN')
                    break
                elif uno.health <= 0 and dos.health <= 0:
                    print (tres.name, 'WIIIIN')
                    break

            break
    elif escenario == 11:
        for escenario11_2 in range (1):
            print ('La pelea se desarrolla en medio de una densa niebla (tu objetivo se selecciona aleatoriamente)')
            uno.hello()
            dos.hello()
            tres.hello()
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0:
                if uno.velocity >= dos.velocity and uno.velocity >= tres.velocity:
                    playone3random ()

                    if dos.velocity >= tres.velocity:
                        playtwo3random ()

                        playthree3random ()

                    elif dos.velocity < tres.velocity:
                        playthree3random ()

                        playtwo3random ()

                elif dos.velocity >= uno.velocity and dos.velocity >= tres.velocity:
                    playtwo3random ()

                    if uno.velocity >= tres.velocity:
                        playone3random ()
                        playthree3random ()

                    elif uno.velocity < tres.velocity:
                        playthree3random ()
                        playone3random ()

                elif tres.velocity >= dos.velocity and tres.velocity >= uno.velocity:
                    playthree3random ()

                    if uno.velocity >= dos.velocity:
                        playone3random ()
                        playtwo3random ()

                    elif uno.velocity < dos.velocity:
                        playtwo3random ()
                        playone3random ()

                if dos.health <= 0 and tres.health <= 0:
                    print (uno.name, 'WIIIIN')
                    break
                elif uno.health <= 0 and tres.health <= 0:
                    print (dos.name, 'WIIIIN')
                    break
                elif uno.health <= 0 and dos.health <= 0:
                    print (tres.name, 'WIIIIN')
                    break
    if escenario != 10 or escenario != 11:
        uno.hello()
        dos.hello()
        tres.hello()
        while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0:
            if uno.velocity >= dos.velocity and uno.velocity >= tres.velocity:
                playone3 ()

                if dos.velocity >= tres.velocity:
                    playtwo3 ()

                    playthree3 ()

                elif dos.velocity < tres.velocity:
                    playthree3 ()

                    playtwo3 ()

            elif dos.velocity >= uno.velocity and dos.velocity >= tres.velocity:
                playtwo3 ()

                if uno.velocity >= tres.velocity:
                    playone3 ()
                    playthree3 ()

                elif uno.velocity < tres.velocity:
                    playthree3 ()
                    playone3 ()

            elif tres.velocity >= dos.velocity and tres.velocity >= uno.velocity:
                playthree3 ()

                if uno.velocity >= dos.velocity:
                    playone3 ()
                    playtwo3 ()

                elif uno.velocity < dos.velocity:
                    playtwo3 ()
                    playone3 ()

            if dos.health <= 0 and tres.health <= 0:
                print (uno.name, 'WIIIIN')
                break
            elif uno.health <= 0 and tres.health <= 0:
                print (dos.name, 'WIIIIN')
                break
            elif uno.health <= 0 and dos.health <= 0:
                print (tres.name, 'WIIIIN')
                break

elif cuantosplayers == '4':
    uno = input('Jugador 1, escoja su personaje: Warrior, Magician, Hereje, Maldi, Thief, Shapeshifter, Mace, Healer, Fires, Snake Charner, Apostador, Natural, Diablillo, Support, Chiquitin')
    while True:
        dos = input('Jugador 2, escoja su personaje: (No repetir)')
        if dos == uno:
            print ('No se pueden repetir personajes!!')
        else:
            break
    while True:
        tres = input('Jugador 3, escoja su personaje:')
        if tres == uno or tres == dos:
            print ('No se pueden repetir personajes!!')
        else:
            break
    while True:
        cuatro = input('Jugador 4, escoja su personaje:')
        if cuatro == uno or cuatro == dos or cuatro == tres:
            print ('No se pueden repetir personajes!!')
        else:
            break
    if uno.lower() == 'warrior':
        uno = guerrero
    elif uno.lower() == 'magician':
        uno = mago
    elif uno.lower() == 'hereje':
        uno = arquero
    elif uno.lower() == 'maldi':
        uno = maldito
    elif uno.lower() == 'thief':
        uno = robador
    elif uno.lower() == 'shapeshifter':
        uno = pantera
    elif uno.lower() == 'healer':
        uno = curandera
    elif uno.lower() == 'mace':
        uno = maza
    elif uno.lower() == 'fires':
        uno = igneo
    elif uno.lower() == 'snake charner':
        uno = serpientero
    elif uno.lower() == 'apostador':
        uno = poker
    elif uno.lower() == 'natural':
        uno = natural
    elif uno.lower() == 'diablillo':
        uno = diablillo
    elif uno.lower() == 'support':
        uno = support
    elif uno.lower() == 'chiquitin':
        uno = chiquitin
    if dos.lower() == 'warrior':
        dos = guerrero
    elif dos.lower() == 'magician':
        dos = mago
    elif dos.lower() == 'hereje':
        dos = arquero
    elif dos.lower() == 'maldi':
        dos = maldito
    elif dos.lower() == 'thief':
        dos = robador
    elif dos.lower() == 'shapeshifter':
        dos = pantera
    elif dos.lower() == 'healer':
        dos = curandera
    elif dos.lower() == 'mace':
        dos = maza
    elif dos.lower() == 'fires':
        dos = igneo
    elif dos.lower() == 'snake charner':
        dos = serpientero
    elif dos.lower() == 'apostador':
        dos = poker
    elif dos.lower() == 'natural':
        dos = natural
    elif dos.lower() == 'diablillo':
        dos = diablillo
    elif dos.lower() == 'support':
        dos = support
    elif dos.lower() == 'chiquitin':
        dos = chiquitin
    if tres.lower() == 'warrior':
        tres = guerrero
    elif tres.lower() == 'magician':
        tres = mago
    elif tres.lower() == 'hereje':
        tres = arquero
    elif tres.lower() == 'maldi':
        tres = maldito
    elif tres.lower() == 'thief':
        tres = robador
    elif tres.lower() == 'shapeshifter':
        tres = pantera
    elif tres.lower() == 'healer':
        tres = curandera
    elif tres.lower() == 'mace':
        tres = maza
    elif tres.lower() == 'fires':
        tres = igneo
    elif tres.lower() == 'snake charner':
        tres = serpientero
    elif tres.lower() == 'apostador':
        tres = poker
    elif tres.lower() == 'natural':
        tres = natural
    elif tres.lower() == 'diablillo':
        tres = diablillo
    elif tres.lower() == 'support':
        tres = support
    elif tres.lower() == 'chiquitin':
        tres = chiquitin
    if cuatro.lower() == 'warrior':
        cuatro = guerrero
    elif cuatro.lower() == 'magician':
        cuatro = mago
    elif cuatro.lower() == 'hereje':
        cuatro = arquero
    elif cuatro.lower() == 'maldi':
        cuatro = maldito
    elif cuatro.lower() == 'thief':
        cuatro = robador
    elif cuatro.lower() == 'shapeshifter':
        cuatro = pantera
    elif cuatro.lower() == 'healer':
        cuatro = curandera
    elif cuatro.lower() == 'mace':
        cuatro = maza
    elif cuatro.lower() == 'fires':
        cuatro = igneo
    elif cuatro.lower() == 'snake charner':
        cuatro = serpientero
    elif cuatro.lower() == 'apostador':
        cuatro = poker
    elif cuatro.lower() == 'natural':
        cuatro = natural
    elif cuatro.lower() == 'diablillo':
        cuatro = diablillo
    elif cuatro.lower () == 'support':
        cuatro = support
    elif cuatro.lower() == 'chiquitin':
        cuatro = chiquitin
    escenario = randint (1, 12)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores bajando su defensa en 0.8')
        uno.defense -= 0.8
        dos.defense -= 0.8
        tres.defense -= 0.8
        cuatro.defense -= 0.8
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        if uno.tipo == 2:
            print (uno.name, 'recibe 0.25 más de defensa')
            uno.defense += 0.25
        if dos.tipo == 2:
            print (dos.name, 'recibe 0.25 más de defensa')
            dos.defense += 0.25
        if tres.tipo == 2:
            print (tres.name, 'recibe 0.25 más de defensa')
            tres.defense += 0.25
        if cuatro.tipo == 2:
            print (cuatro.name, 'recibe 0.25 más de defensa')
            cuatro.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        if uno.tipo == 3:
            print (uno.name, 'recibe 0.25 más de poder')
            uno.power += 0.25
        if dos.tipo == 3:
            print (dos.name, 'recibe 0.25 más de poder')
            dos.power += 0.25
        if tres.tipo == 3:
            print (tres.name, 'recibe 0.25 más de poder')
            tres.power += 0.25
        if cuatro.tipo == 3:
            print (cuatro.name, 'recibe 0.25 más de poder')
            cuatro.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        if uno.tipo == 1:
            print (uno.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            uno.defense += 0.2
            uno.velocity += 25
        if dos.tipo == 1:
            print (dos.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            dos.defense += 0.2
            dos.velocity += 25
        if tres.tipo == 1:
            print (tres.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            tres.defense += 0.2
            tres.velocity += 25
        if cuatro.tipo == 1:
            print (cuatro.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            cuatro.defense += 0.2
            cuatro.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        if uno.tipo == 0:
            print (uno.name, 'recibe 60 más de velocidad')
            uno.velocity += 60
        if dos.tipo == 0:
            print (dos.name, 'recibe 60 más de velocidad')
            dos.velocity += 60
        if tres.tipo == 0:
            print (tres.name, 'recibe 60 más de velocidad')
            tres.velocity += 60
        if cuatro.tipo == 0:
            print (cuatro.name, 'recibe 60 más de velocidad')
            cuatro.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        uno.preci1 -= 20
        uno.preci2 -= 20
        uno.preci3 -= 20
        uno.precicura -= 20
        uno.precienergia -= 20
        dos.preci1 -= 20
        dos.preci2 -= 20
        dos.preci3 -= 20
        dos.precicura -= 20
        dos.precienergia -= 20
        tres.preci1 -= 20
        tres.preci2 -= 20
        tres.preci3 -= 20
        tres.precicura -= 20
        tres.precienergia -= 20
        cuatro.preci1 -= 20
        cuatro.preci2 -= 20
        cuatro.preci3 -= 20
        cuatro.precicura -= 20
        cuatro.precienergia -= 20
    elif escenario == 12:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        uno.energy += 100000
        dos.energy += 100000
        tres.energy += 100000
        cuatro.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            uno.hello()
            dos.hello()
            tres.hello()
            cuatro.hello()
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0:
                if uno.velocity <= dos.velocity and uno.velocity <= tres.velocity and uno.velocity <= cuatro.velocity:
                    playone4 ()

                    if dos.velocity <= tres.velocity and dos.velocity <= cuatro.velocity:
                        playtwo4 ()

                        if tres.velocity <= cuatro.velocity:
                            playthree4 ()
                            playfour4 ()

                        elif tres.velocity > cuatro.velocity:
                            playfour4 ()
                            playthree4 ()

                    elif tres.velocity <= dos.velocity and tres.velocity <= cuatro.velocity:
                        playthree4 ()

                        if dos.velocity <= cuatro.velocity:
                            playtwo4 ()
                            playfour4 ()

                        elif dos.velocity > cuatro.velocity:
                            playfour4 ()
                            playtwo4 ()

                    elif cuatro.velocity <= dos.velocity and cuatro.velocity <= tres.velocity:
                        playfour4 ()

                        if dos.velocity <= tres.velocity:
                            playtwo4 ()
                            playthree4 ()

                        elif dos.velocity > tres.velocity:
                            playthree4 ()
                            playtwo4 ()

                elif dos.velocity <= uno.velocity and dos.velocity <= tres.velocity and dos.velocity <= cuatro.velocity:
                    playtwo4 ()

                    if uno.velocity <= tres.velocity and uno.velocity <= cuatro.velocity:
                        playone4 ()

                        if tres.velocity <= cuatro.velocity:
                            playthree4 ()
                            playfour4 ()
                                
                        elif tres.velocity > cuatro.velocity:
                            playfour4 ()
                            playthree4 ()
                        
                    elif tres.velocity <= uno.velocity and tres.velocity <= cuatro.velocity:
                        playthree4 ()
                    
                        if uno.velocity <= cuatro.velocity:
                            playone4 ()
                            playfour4 ()
                            
                        elif uno.velocity > cuatro.velocity:
                            playfour4 ()
                            playone4 ()

                    elif cuatro.velocity <= uno.velocity and cuatro.velocity <= tres.velocity:
                        playfour4 ()
                        
                        if uno.velocity <= tres.velocity:
                            playone4 ()
                            playthree4 ()

                        elif uno.velocity > tres.velocity:
                            playthree4 ()
                            playone4 ()

                elif tres.velocity <= uno.velocity and tres.velocity <= dos.velocity and tres.velocity <= cuatro.velocity:
                    playthree4 ()

                    if dos.velocity <= uno.velocity and dos.velocity <= cuatro.velocity:
                        playtwo4 ()

                        if uno.velocity <= cuatro.velocity:
                            playone4 ()
                            playfour4 ()

                        elif uno.velocity > cuatro.velocity:
                            playfour4 ()
                            playone4 ()

                    elif uno.velocity <= dos.velocity and uno.velocity <= cuatro.velocity:
                        playone4 ()
                    
                        if dos.velocity <= cuatro.velocity:
                            playtwo4 ()
                            playfour4 ()
                            
                        elif dos.velocity > cuatro.velocity:
                            playfour4 ()
                            playtwo4 ()

                    elif cuatro.velocity <= dos.velocity and cuatro.velocity <= uno.velocity:
                        playfour4 ()

                        if dos.velocity <= uno.velocity:
                            playtwo4 ()
                            playone4 ()

                        elif dos.velocity > uno.velocity:
                            playone4 ()
                            playtwo4 ()
                
                elif cuatro.velocity <= uno.velocity and cuatro.velocity <= dos.velocity and cuatro.velocity <= tres.velocity:
                    playfour4 ()

                    if uno.velocity <= dos.velocity and uno.velocity <= tres.velocity:
                        playone4 ()

                        if dos.velocity <= tres.velocity:
                            playtwo4 ()
                            playthree4 ()

                        elif dos.velocity > tres.velocity:
                            playthree4 ()
                            playtwo4 ()
                        
                    elif dos.velocity <= uno.velocity and dos.velocity <= tres.velocity:
                        playtwo4 ()
                    
                        if uno.velocity <= tres.velocity:
                            playone4 ()

                            playthree4 ()
                            
                        elif uno.velocity > tres.velocity:
                            playthree4 ()
                            playone4 ()

                    elif tres.velocity <= uno.velocity and tres.velocity <= dos.velocity:
                        playthree4 ()
                        
                        if uno.velocity <= dos.velocity:
                            playone4 ()
                            playtwo4 ()
                            
                        elif uno.velocity > dos.velocity:
                            playtwo4 ()
                            playone4 ()

                if dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0:
                    print (uno.name, 'WIIIIN')
                    break
                elif uno.health <= 0 and tres.health <= 0 and cuatro.health <= 0:
                    print (dos.name, 'WIIIIN')
                    break
                elif uno.health <= 0 and dos.health <= 0 and cuatro.health <= 0:
                    print (tres.name, 'WIIIIN')
                    break
                elif uno.health <= 0 and dos.health <= 0 and tres.health <= 0:
                    print (cuatro.name, 'WIIIIN')
                    break
    elif escenario == 11:
        for escenario11_2 in range (1):
            print ('La pelea se desarrolla en medio de una densa niebla (tu objetivo se selecciona aleatoriamente)')
            uno.hello()
            dos.hello()
            tres.hello()
            cuatro.hello()
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0:
                if uno.velocity >= dos.velocity and uno.velocity >= tres.velocity and uno.velocity >= cuatro.velocity:
                    playone4random ()

                    if dos.velocity >= tres.velocity and dos.velocity >= cuatro.velocity:
                        playtwo4random ()

                        if tres.velocity >= cuatro.velocity:
                            playthree4random ()
                            playfour4random ()

                        elif tres.velocity < cuatro.velocity:
                            playfour4random ()
                            playthree4random ()

                    elif tres.velocity >= dos.velocity and tres.velocity >= cuatro.velocity:
                        playthree4random ()

                        if dos.velocity >= cuatro.velocity:
                            playtwo4random ()
                            playfour4random ()

                        elif dos.velocity < cuatro.velocity:
                            playfour4random ()
                            playtwo4random ()

                    elif cuatro.velocity >= dos.velocity and cuatro.velocity >= tres.velocity:
                        playfour4random ()

                        if dos.velocity >= tres.velocity:
                            playtwo4random ()
                            playthree4random ()

                        elif dos.velocity < tres.velocity:
                            playthree4random ()
                            playtwo4random ()

                elif dos.velocity >= uno.velocity and dos.velocity >= tres.velocity and dos.velocity >= cuatro.velocity:
                    playtwo4random ()

                    if uno.velocity >= tres.velocity and uno.velocity >= cuatro.velocity:
                        playone4random ()

                        if tres.velocity >= cuatro.velocity:
                            playthree4random ()
                            playfour4random ()
                                
                        elif tres.velocity < cuatro.velocity:
                            playfour4random ()
                            playthree4random ()
                        
                    elif tres.velocity >= uno.velocity and tres.velocity >= cuatro.velocity:
                        playthree4random ()
                    
                        if uno.velocity >= cuatro.velocity:
                            playone4random ()
                            playfour4random ()
                            
                        elif uno.velocity < cuatro.velocity:
                            playfour4random ()
                            playone4random ()

                    elif cuatro.velocity >= uno.velocity and cuatro.velocity >= tres.velocity:
                        playfour4random ()
                        
                        if uno.velocity >= tres.velocity:
                            playone4random ()
                            playthree4random ()

                        elif uno.velocity < tres.velocity:
                            playthree4random ()
                            playone4random ()

                elif tres.velocity >= uno.velocity and tres.velocity >= dos.velocity and tres.velocity >= cuatro.velocity:
                    playthree4random ()

                    if dos.velocity >= uno.velocity and dos.velocity >= cuatro.velocity:
                        playtwo4random ()

                        if uno.velocity >= cuatro.velocity:
                            playone4random ()
                            playfour4random ()

                        elif uno.velocity < cuatro.velocity:
                            playfour4random ()
                            playone4random ()

                    elif uno.velocity >= dos.velocity and uno.velocity >= cuatro.velocity:
                        playone4random ()
                    
                        if dos.velocity >= cuatro.velocity:
                            playtwo4random ()
                            playfour4random ()
                            
                        elif dos.velocity < cuatro.velocity:
                            playfour4random ()
                            playtwo4random ()

                    elif cuatro.velocity >= dos.velocity and cuatro.velocity >= uno.velocity:
                        playfour4random ()

                        if dos.velocity >= uno.velocity:
                            playtwo4random ()
                            playone4random ()

                        elif dos.velocity < uno.velocity:
                            playone4random ()
                            playtwo4random ()
                
                elif cuatro.velocity >= uno.velocity and cuatro.velocity >= dos.velocity and cuatro.velocity >= tres.velocity:
                    playfour4random ()

                    if uno.velocity >= dos.velocity and uno.velocity >= tres.velocity:
                        playone4random ()

                        if dos.velocity >= tres.velocity:
                            playtwo4random ()
                            playthree4random ()

                        elif dos.velocity < tres.velocity:
                            playthree4random ()
                            playtwo4random ()
                        
                    elif dos.velocity >= uno.velocity and dos.velocity >= tres.velocity:
                        playtwo4random ()
                    
                        if uno.velocity >= tres.velocity:
                            playone4random ()

                            playthree4random ()
                            
                        elif uno.velocity < tres.velocity:
                            playthree4random ()
                            playone4random ()

                    elif tres.velocity >= uno.velocity and tres.velocity >= dos.velocity:
                        playthree4random ()
                        
                        if uno.velocity >= dos.velocity:
                            playone4random ()
                            playtwo4random ()
                            
                        elif uno.velocity < dos.velocity:
                            playtwo4random ()
                            playone4random ()

                if dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0:
                    print (uno.name, 'WIIIIN')
                    break
                elif uno.health <= 0 and tres.health <= 0 and cuatro.health <= 0:
                    print (dos.name, 'WIIIIN')
                    break
                elif uno.health <= 0 and dos.health <= 0 and cuatro.health <= 0:
                    print (tres.name, 'WIIIIN')
                    break
                elif uno.health <= 0 and dos.health <= 0 and tres.health <= 0:
                    print (cuatro.name, 'WIIIIN')
                    break

    if escenario != 10 or escenario != 11:
        uno.hello()
        dos.hello()
        tres.hello()
        cuatro.hello()
        while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0:
            if uno.velocity >= dos.velocity and uno.velocity >= tres.velocity and uno.velocity >= cuatro.velocity:
                playone4 ()

                if dos.velocity >= tres.velocity and dos.velocity >= cuatro.velocity:
                    playtwo4 ()

                    if tres.velocity >= cuatro.velocity:
                        playthree4 ()
                        playfour4 ()

                    elif tres.velocity < cuatro.velocity:
                        playfour4 ()
                        playthree4 ()

                elif tres.velocity >= dos.velocity and tres.velocity >= cuatro.velocity:
                    playthree4 ()

                    if dos.velocity >= cuatro.velocity:
                        playtwo4 ()
                        playfour4 ()

                    elif dos.velocity < cuatro.velocity:
                        playfour4 ()
                        playtwo4 ()

                elif cuatro.velocity >= dos.velocity and cuatro.velocity >= tres.velocity:
                    playfour4 ()

                    if dos.velocity >= tres.velocity:
                        playtwo4 ()
                        playthree4 ()

                    elif dos.velocity < tres.velocity:
                        playthree4 ()
                        playtwo4 ()

            elif dos.velocity >= uno.velocity and dos.velocity >= tres.velocity and dos.velocity >= cuatro.velocity:
                playtwo4 ()

                if uno.velocity >= tres.velocity and uno.velocity >= cuatro.velocity:
                    playone4 ()

                    if tres.velocity >= cuatro.velocity:
                        playthree4 ()
                        playfour4 ()
                            
                    elif tres.velocity < cuatro.velocity:
                        playfour4 ()
                        playthree4 ()
                    
                elif tres.velocity >= uno.velocity and tres.velocity >= cuatro.velocity:
                    playthree4 ()
                
                    if uno.velocity >= cuatro.velocity:
                        playone4 ()
                        playfour4 ()
                        
                    elif uno.velocity < cuatro.velocity:
                        playfour4 ()
                        playone4 ()

                elif cuatro.velocity >= uno.velocity and cuatro.velocity >= tres.velocity:
                    playfour4 ()
                    
                    if uno.velocity >= tres.velocity:
                        playone4 ()
                        playthree4 ()

                    elif uno.velocity < tres.velocity:
                        playthree4 ()
                        playone4 ()

            elif tres.velocity >= uno.velocity and tres.velocity >= dos.velocity and tres.velocity >= cuatro.velocity:
                playthree4 ()

                if dos.velocity >= uno.velocity and dos.velocity >= cuatro.velocity:
                    playtwo4 ()

                    if uno.velocity >= cuatro.velocity:
                        playone4 ()
                        playfour4 ()

                    elif uno.velocity < cuatro.velocity:
                        playfour4 ()
                        playone4 ()

                elif uno.velocity >= dos.velocity and uno.velocity >= cuatro.velocity:
                    playone4 ()
                
                    if dos.velocity >= cuatro.velocity:
                        playtwo4 ()
                        playfour4 ()
                        
                    elif dos.velocity < cuatro.velocity:
                        playfour4 ()
                        playtwo4 ()

                elif cuatro.velocity >= dos.velocity and cuatro.velocity >= uno.velocity:
                    playfour4 ()

                    if dos.velocity >= uno.velocity:
                        playtwo4 ()
                        playone4 ()

                    elif dos.velocity < uno.velocity:
                        playone4 ()
                        playtwo4 ()
            
            elif cuatro.velocity >= uno.velocity and cuatro.velocity >= dos.velocity and cuatro.velocity >= tres.velocity:
                playfour4 ()

                if uno.velocity >= dos.velocity and uno.velocity >= tres.velocity:
                    playone4 ()

                    if dos.velocity >= tres.velocity:
                        playtwo4 ()
                        playthree4 ()

                    elif dos.velocity < tres.velocity:
                        playthree4 ()
                        playtwo4 ()
                    
                elif dos.velocity >= uno.velocity and dos.velocity >= tres.velocity:
                    playtwo4 ()
                
                    if uno.velocity >= tres.velocity:
                        playone4 ()

                        playthree4 ()
                        
                    elif uno.velocity < tres.velocity:
                        playthree4 ()
                        playone4 ()

                elif tres.velocity >= uno.velocity and tres.velocity >= dos.velocity:
                    playthree4 ()
                    
                    if uno.velocity >= dos.velocity:
                        playone4 ()
                        playtwo4 ()
                        
                    elif uno.velocity < dos.velocity:
                        playtwo4 ()
                        playone4 ()

            if dos.health <= 0 and tres.health <= 0 and cuatro.health <= 0:
                print (uno.name, 'WIIIIN')
                break
            elif uno.health <= 0 and tres.health <= 0 and cuatro.health <= 0:
                print (dos.name, 'WIIIIN')
                break
            elif uno.health <= 0 and dos.health <= 0 and cuatro.health <= 0:
                print (tres.name, 'WIIIIN')
                break
            elif uno.health <= 0 and dos.health <= 0 and tres.health <= 0:
                print (cuatro.name, 'WIIIIN')
                break

elif cuantosplayers.lower() == 'atraco':
    print ('(Para poner de objetivo a una caja escribe "caja roja / caja azul")')
    uno = input('Jugador 1 (Equipo azul), escoja su personaje: Warrior, Magician, Hereje, Maldi, Thief, Shapeshifter, Mace, Healer, Fires, Snake Charner, Apostador, Natural, Diablillo, Support, Chiquitin')
    while True:
        cuatro = input('Jugador 4 (Equipo rojo), escoja su personaje: (No repetir)')
        if cuatro == uno:
            print ('No se pueden repetir personajes!!')
        else:
            break
    while True:
        dos = input('Jugador 2 (Equipo azul), escoja su personaje:')
        if dos == uno or dos == cuatro:
            print ('No se pueden repetir personajes!!')
        else:
            break
    while True:
        cinco = input('Jugador 5 (Equipo rojo), escoja su personaje:')
        if cinco == uno or cinco == dos or cinco == cuatro:
            print ('No se pueden repetir personajes!!')
        else:
            break
    while True:
        tres = input('Jugador 3 (Equipo azul), escoja su personaje:')
        if tres == uno or tres == dos or tres == cuatro or tres == cinco:
            print ('No se pueden repetir personajes!!')
        else:
            break
    while True:
        seis = input('Jugador 6 (Equipo rojo), escoja su personaje:')
        if seis == uno or seis == dos or seis == cuatro or seis == cinco or seis == tres:
            print ('No se pueden repetir personajes!!')
        else:
            break
    if uno.lower() == 'warrior':
        uno = guerrero
    elif uno.lower() == 'magician':
        uno = mago
    elif uno.lower() == 'hereje':
        uno = arquero
    elif uno.lower() == 'maldi':
        uno = maldito
    elif uno.lower() == 'thief':
        uno = robador
    elif uno.lower() == 'shapeshifter':
        uno = pantera
    elif uno.lower() == 'healer':
        uno = curandera
    elif uno.lower() == 'mace':
        uno = maza
    elif uno.lower() == 'fires':
        uno = igneo
    elif uno.lower() == 'snake charner':
        uno = serpientero
    elif uno.lower() == 'apostador':
        uno = poker
    elif uno.lower() == 'natural':
        uno = natural
    elif uno.lower() == 'diablillo':
        uno = diablillo
    elif uno.lower() == 'support':
        uno = support
    elif uno.lower() == 'chiquitin':
        uno = chiquitin
    if dos.lower() == 'warrior':
        dos = guerrero
    elif dos.lower() == 'magician':
        dos = mago
    elif dos.lower() == 'hereje':
        dos = arquero
    elif dos.lower() == 'maldi':
        dos = maldito
    elif dos.lower() == 'thief':
        dos = robador
    elif dos.lower() == 'shapeshifter':
        dos = pantera
    elif dos.lower() == 'healer':
        dos = curandera
    elif dos.lower() == 'mace':
        dos = maza
    elif dos.lower() == 'fires':
        dos = igneo
    elif dos.lower() == 'snake charner':
        dos = serpientero
    elif dos.lower() == 'apostador':
        dos = poker
    elif dos.lower() == 'natural':
        dos = natural
    elif dos.lower() == 'diablillo':
        dos = diablillo
    elif dos.lower() == 'support':
        dos = support
    elif dos.lower() == 'chiquitin':
        dos = chiquitin
    if tres.lower() == 'warrior':
        tres = guerrero
    elif tres.lower() == 'magician':
        tres = mago
    elif tres.lower() == 'hereje':
        tres = arquero
    elif tres.lower() == 'maldi':
        tres = maldito
    elif tres.lower() == 'thief':
        tres = robador
    elif tres.lower() == 'shapeshifter':
        tres = pantera
    elif tres.lower() == 'healer':
        tres = curandera
    elif tres.lower() == 'mace':
        tres = maza
    elif tres.lower() == 'fires':
        tres = igneo
    elif tres.lower() == 'snake charner':
        tres = serpientero
    elif tres.lower() == 'apostador':
        tres = poker
    elif tres.lower() == 'natural':
        tres = natural
    elif tres.lower() == 'diablillo':
        tres = diablillo
    elif tres.lower() == 'support':
        tres = support
    elif tres.lower() == 'chiquitin':
        tres = chiquitin
    if cuatro.lower() == 'warrior':
        cuatro = guerrero
    elif cuatro.lower() == 'magician':
        cuatro = mago
    elif cuatro.lower() == 'hereje':
        cuatro = arquero
    elif cuatro.lower() == 'maldi':
        cuatro = maldito
    elif cuatro.lower() == 'thief':
        cuatro = robador
    elif cuatro.lower() == 'shapeshifter':
        cuatro = pantera
    elif cuatro.lower() == 'healer':
        cuatro = curandera
    elif cuatro.lower() == 'mace':
        cuatro = maza
    elif cuatro.lower() == 'fires':
        cuatro = igneo
    elif cuatro.lower() == 'snake charner':
        cuatro = serpientero
    elif cuatro.lower() == 'apostador':
        cuatro = poker
    elif cuatro.lower() == 'natural':
        cuatro = natural
    elif cuatro.lower() == 'diablillo':
        cuatro = diablillo
    elif cuatro.lower () == 'support':
        cuatro = support
    elif cuatro.lower() == 'chiquitin':
        cuatro = chiquitin
    if cinco.lower() == 'warrior':
        cinco = guerrero
    elif cinco.lower() == 'magician':
        cinco = mago
    elif cinco.lower() == 'hereje':
        cinco = arquero
    elif cinco.lower() == 'maldi':
        cinco = maldito
    elif cinco.lower() == 'thief':
        cinco = robador
    elif cinco.lower() == 'shapeshifter':
        cinco = pantera
    elif cinco.lower() == 'healer':
        cinco = curandera
    elif cinco.lower() == 'mace':
        cinco = maza
    elif cinco.lower() == 'fires':
        cinco = igneo
    elif cinco.lower() == 'snake charner':
        cinco = serpientero
    elif cinco.lower() == 'apostador':
        cinco = poker
    elif cinco.lower() == 'natural':
        cinco = natural
    elif cinco.lower() == 'diablillo':
        cinco = diablillo
    elif cinco.lower () == 'support':
        cinco = support
    elif cinco.lower() == 'chiquitin':
        cinco = chiquitin
    if seis.lower() == 'warrior':
        seis = guerrero
    elif seis.lower() == 'magician':
        seis = mago
    elif seis.lower() == 'hereje':
        seis = arquero
    elif seis.lower() == 'maldi':
        seis = maldito
    elif seis.lower() == 'thief':
        seis = robador
    elif seis.lower() == 'shapeshifter':
        seis = pantera
    elif seis.lower() == 'healer':
        seis = curandera
    elif seis.lower() == 'mace':
        seis = maza
    elif seis.lower() == 'fires':
        seis = igneo
    elif seis.lower() == 'snake charner':
        seis = serpientero
    elif seis.lower() == 'apostador':
        seis = poker
    elif seis.lower() == 'natural':
        seis = natural
    elif seis.lower() == 'diablillo':
        seis = diablillo
    elif seis.lower () == 'support':
        seis = support
    elif seis.lower() == 'chiquitin':
        seis = chiquitin

    escenario = randint (1, 11)
    if escenario == 1 or escenario == 2 or escenario == 3:
        print ('La pelea se desarrolla en una bella pradera (no pasa nada)')
    elif escenario == 4:
        print ('¡¡La pelea es una locura!! El caos consume a los jugadores bajando su defensa en 0.8')
        uno.defense -= 0.8
        dos.defense -= 0.8
        tres.defense -= 0.8
        cuatro.defense -= 0.8
        cinco.defense -= 0.8
        seis.defense -= 0.8
        boxblue.defense -= 0.8
        boxred.defense -= 0.8
    elif escenario == 5:
        print ('La pelea se desarrolla en un bosque entre sus árboles los personajes ágiles reciben 0.25 más de defensa')
        if uno.tipo == 2:
            print (uno.name, 'recibe 0.25 más de defensa')
            uno.defense += 0.25
        if dos.tipo == 2:
            print (dos.name, 'recibe 0.25 más de defensa')
            dos.defense += 0.25
        if tres.tipo == 2:
            print (tres.name, 'recibe 0.25 más de defensa')
            tres.defense += 0.25
        if cuatro.tipo == 2:
            print (cuatro.name, 'recibe 0.25 más de defensa')
            cuatro.defense += 0.25
        if cinco.tipo == 2:
            print (cinco.name, 'recibe 0.25 más de defensa')
            cinco.defense += 0.25
        if seis.tipo == 2:
            print (seis.name, 'recibe 0.25 más de defensa')
            seis.defense += 0.25
    elif escenario == 6:
        print ('La pelea se desarrolla además en una segunda dimención psiquica por donde las mentes de los magos se pueden mover afectando aún más en sus ataques (los magos tienen 0.25 más de poder)')
        if uno.tipo == 3:
            print (uno.name, 'recibe 0.25 más de poder')
            uno.power += 0.25
        if dos.tipo == 3:
            print (dos.name, 'recibe 0.25 más de poder')
            dos.power += 0.25
        if tres.tipo == 3:
            print (tres.name, 'recibe 0.25 más de poder')
            tres.power += 0.25
        if cuatro.tipo == 3:
            print (cuatro.name, 'recibe 0.25 más de poder')
            cuatro.power += 0.25
        if cinco.tipo == 3:
            print (cinco.name, 'recibe 0.25 más de poder')
            cinco.power += 0.25
        if seis.tipo == 3:
            print (seis.name, 'recibe 0.25 más de poder')
            seis.power += 0.25
    elif escenario == 7:
        print ('La pelea se desarrolla en una ciudad donde los guerreros tienen cobijo y se saben los caminos por lo que aumentan su defensa en 0.2 y su velocidad en 25')
        if uno.tipo == 1:
            print (uno.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            uno.defense += 0.2
            uno.velocity += 25
        if dos.tipo == 1:
            print (dos.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            dos.defense += 0.2
            dos.velocity += 25
        if tres.tipo == 1:
            print (tres.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            tres.defense += 0.2
            tres.velocity += 25
        if cuatro.tipo == 1:
            print (cuatro.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            cuatro.defense += 0.2
            cuatro.velocity += 25
        if cinco.tipo == 1:
            print (cinco.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            cinco.defense += 0.2
            cinco.velocity += 25
        if seis.tipo == 1:
            print (seis.name, 'recibe 0.2 más de defensa y 25 más de velocidad')
            seis.defense += 0.2
            seis.velocity += 25
    elif escenario == 8:
        print ('La pelea se desarrolla además en el metaverso donde los personajes misteriosos son muy veloces (aumentan su velocidad en 60)')
        if uno.tipo == 0:
            print (uno.name, 'recibe 60 más de velocidad')
            uno.velocity += 60
        if dos.tipo == 0:
            print (dos.name, 'recibe 60 más de velocidad')
            dos.velocity += 60
        if tres.tipo == 0:
            print (tres.name, 'recibe 60 más de velocidad')
            tres.velocity += 60
        if cuatro.tipo == 0:
            print (cuatro.name, 'recibe 60 más de velocidad')
            cuatro.velocity += 60
        if cinco.tipo == 0:
            print (cinco.name, 'recibe 60 más de velocidad')
            cinco.velocity += 60
        if seis.tipo == 0:
            print (seis.name, 'recibe 60 más de velocidad')
            seis.velocity += 60
    elif escenario == 9:
        print ('La pelea se desarrolla por la noche por lo que su visión empeora reduciendo sus precisiones en 20%')
        uno.preci1 -= 20
        uno.preci2 -= 20
        uno.preci3 -= 20
        uno.precicura -= 20
        uno.precienergia -= 20
        dos.preci1 -= 20
        dos.preci2 -= 20
        dos.preci3 -= 20
        dos.precicura -= 20
        dos.precienergia -= 20
        tres.preci1 -= 20
        tres.preci2 -= 20
        tres.preci3 -= 20
        tres.precicura -= 20
        tres.precienergia -= 20
        cuatro.preci1 -= 20
        cuatro.preci2 -= 20
        cuatro.preci3 -= 20
        cuatro.precicura -= 20
        cuatro.precienergia -= 20
        cinco.preci1 -= 20
        cinco.preci2 -= 20
        cinco.preci3 -= 20
        cinco.precicura -= 20
        cinco.precienergia -= 20
        seis.preci1 -= 20
        seis.preci2 -= 20
        seis.preci3 -= 20
        seis.precicura -= 20
        seis.precienergia -= 20
    elif escenario == 11:
        print ('Una infinita fuente de energia abastece a todos los personajes con 100k de energia')
        uno.energy += 100000
        dos.energy += 100000
        tres.energy += 100000
        cuatro.energy += 100000
        cinco.energy += 100000
        seis.energy += 100000
    elif escenario == 10:
        for escenario10_2 in range (1):
            print ('La pelea está patas arriba y los menos veloces atacan primero')
            uno.hello()
            dos.hello()
            tres.hello()
            cuatro.hello()
            cinco.hello()
            seis.hello()
            velocities = list()
            velocities.append (uno.velocity)
            velocities.append (dos.velocity)
            velocities.append (tres.velocity)
            velocities.append (cuatro.velocity)
            velocities.append (cinco.velocity)
            velocities.append (seis.velocity)
            while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0 or cinco.health >= 0 or seis.health:
                velocities.sort()
                first = velocities [0]
                second = velocities [1]
                third = velocities [2]
                fourth = velocities [3]
                fiveth = velocities [4]
                sixth = velocities [5]
                if first == uno.velocity:
                    playone6atraco ()
                if first == dos.velocity:
                    playtwo6atraco ()
                if first == tres.velocity:
                    playthree6atraco ()
                if first == cuatro.velocity:
                    playfour6atraco ()
                if first == cinco.velocity:
                    playfive6atraco()
                if first == seis.velocity:
                    playsix6atraco ()
                if boxblue.health <= 0 and boxred.health:
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break
                if second == uno.velocity:
                    playone6atraco ()
                if second == dos.velocity:
                    playtwo6atraco ()
                if second == tres.velocity:
                    playthree6atraco ()
                if second == cuatro.velocity:
                    playfour6atraco ()
                if second == cinco.velocity:
                    playfive6atraco()
                if second == seis.velocity:
                    playsix6atraco ()
                if boxblue.health <= 0 and boxred.health:
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break
                if third == uno.velocity:
                    playone6atraco ()
                if third == dos.velocity:
                    playtwo6atraco ()
                if third == tres.velocity:
                    playthree6atraco ()
                if third == cuatro.velocity:
                    playfour6atraco ()
                if third == cinco.velocity:
                    playfive6atraco()
                if third == seis.velocity:
                    playsix6atraco ()
                if boxblue.health <= 0 and boxred.health:
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break
                if fourth == uno.velocity:
                    playone6atraco ()
                if fourth == dos.velocity:
                    playtwo6atraco ()
                if fourth == tres.velocity:
                    playthree6atraco ()
                if fourth == cuatro.velocity:
                    playfour6atraco ()
                if fourth == cinco.velocity:
                    playfive6atraco()
                if fourth == seis.velocity:
                    playsix6atraco ()
                if boxblue.health <= 0 and boxred.health:
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break
                if fiveth == uno.velocity:
                    playone6atraco ()
                if fiveth == dos.velocity:
                    playtwo6atraco ()
                if fiveth == tres.velocity:
                    playthree6atraco ()
                if fiveth == cuatro.velocity:
                    playfour6atraco ()
                if fiveth == cinco.velocity:
                    playfive6atraco()
                if fiveth == seis.velocity:
                    playsix6atraco ()
                if boxblue.health <= 0 and boxred.health:
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break
                if sixth == uno.velocity:
                    playone6atraco ()
                if sixth == dos.velocity:
                    playtwo6atraco ()
                if sixth == tres.velocity:
                    playthree6atraco ()
                if sixth == cuatro.velocity:
                    playfour6atraco ()
                if sixth == cinco.velocity:
                    playfive6atraco()
                if sixth == seis.velocity:
                    playsix6atraco ()
                if boxblue.health <= 0 and boxred.health:
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break
                boxred.turno()
                boxblue.turno()
                if boxblue.health <= 0 and boxred.health:
                    print ('Hay empate debido a una destrucción mutua de ambas cajas')
                    break
                elif boxred.health <= 0:
                    print ('Equipo azul WIIIIN')
                    break
                elif boxblue.health <= 0:
                    print ('Equipo rojo WIIIIN')
                    break

    if escenario != 10:
        uno.hello()
        dos.hello()
        tres.hello()
        cuatro.hello()
        cinco.hello()
        seis.hello()
        velocities = list()
        velocities.append (uno.velocity)
        velocities.append (dos.velocity)
        velocities.append (tres.velocity)
        velocities.append (cuatro.velocity)
        velocities.append (cinco.velocity)
        velocities.append (seis.velocity)
        while uno.health >= 0 or dos.health >= 0 or tres.health >= 0 or cuatro.health >= 0 or cinco.health >= 0 or seis.health:
            velocities.sort()
            first = velocities [5]
            second = velocities [4]
            third = velocities [3] 
            fourth = velocities [2]
            fiveth = velocities [1] 
            sixth = velocities [0]
            if first == uno.velocity:
                playone6atraco ()
            if first == dos.velocity:
                playtwo6atraco ()
            if first == tres.velocity:
                playthree6atraco ()
            if first == cuatro.velocity:
                playfour6atraco ()
            if first == cinco.velocity:
                playfive6atraco()
            if first == seis.velocity:
                playsix6atraco ()
            if boxblue.health <= 0 and boxred.health <= 0 :
                print ('Hay empate debido a una destrucción mutua de ambas cajas')
                break
            elif boxred.health <= 0:
                print ('Equipo azul WIIIIN')
                break
            elif boxblue.health <= 0:
                print ('Equipo rojo WIIIIN')
                break
            if second == uno.velocity:
                playone6atraco ()
            if second == dos.velocity:
                playtwo6atraco ()
            if second == tres.velocity:
                playthree6atraco ()
            if second == cuatro.velocity:
                playfour6atraco ()
            if second == cinco.velocity:
                playfive6atraco()
            if second == seis.velocity:
                playsix6atraco ()
            if boxblue.health <= 0 and boxred.health <= 0:
                print ('Hay empate debido a una destrucción mutua de ambas cajas')
                break
            elif boxred.health <= 0:
                print ('Equipo azul WIIIIN')
                break
            elif boxblue.health <= 0:
                print ('Equipo rojo WIIIIN')
                break
            if third == uno.velocity:
                playone6atraco ()
            if third == dos.velocity:
                playtwo6atraco ()
            if third == tres.velocity:
                playthree6atraco ()
            if third == cuatro.velocity:
                playfour6atraco ()
            if third == cinco.velocity:
                playfive6atraco()
            if third == seis.velocity:
                playsix6atraco ()
            if boxblue.health <= 0 and boxred.health <= 0:
                print ('Hay empate debido a una destrucción mutua de ambas cajas')
                break
            elif boxred.health <= 0:
                print ('Equipo azul WIIIIN')
                break
            elif boxblue.health <= 0:
                print ('Equipo rojo WIIIIN')
                break
            if fourth == uno.velocity:
                playone6atraco ()
            if fourth == dos.velocity:
                playtwo6atraco ()
            if fourth == tres.velocity:
                playthree6atraco ()
            if fourth == cuatro.velocity:
                playfour6atraco ()
            if fourth == cinco.velocity:
                playfive6atraco()
            if fourth == seis.velocity:
                playsix6atraco ()
            if boxblue.health <= 0 and boxred.health <= 0:
                print ('Hay empate debido a una destrucción mutua de ambas cajas')
                break
            elif boxred.health <= 0:
                print ('Equipo azul WIIIIN')
                break
            elif boxblue.health <= 0:
                print ('Equipo rojo WIIIIN')
                break
            if fiveth == uno.velocity:
                playone6atraco ()
            if fiveth == dos.velocity:
                playtwo6atraco ()
            if fiveth == tres.velocity:
                playthree6atraco ()
            if fiveth == cuatro.velocity:
                playfour6atraco ()
            if fiveth == cinco.velocity:
                playfive6atraco()
            if fiveth == seis.velocity:
                playsix6atraco ()
            if boxblue.health <= 0 and boxred.health <= 0:
                print ('Hay empate debido a una destrucción mutua de ambas cajas')
                break
            elif boxred.health <= 0:
                print ('Equipo azul WIIIIN')
                break
            elif boxblue.health <= 0:
                print ('Equipo rojo WIIIIN')
                break
            if sixth == uno.velocity:
                playone6atraco ()
            if sixth == dos.velocity:
                playtwo6atraco ()
            if sixth == tres.velocity:
                playthree6atraco ()
            if sixth == cuatro.velocity:
                playfour6atraco ()
            if sixth == cinco.velocity:
                playfive6atraco()
            if sixth == seis.velocity:
                playsix6atraco ()
            if boxblue.health <= 0 and boxred.health <= 0:
                print ('Hay empate debido a una destrucción mutua de ambas cajas')
                break
            elif boxred.health <= 0:
                print ('Equipo azul WIIIIN')
                break
            elif boxblue.health <= 0:
                print ('Equipo rojo WIIIIN')
                break
            boxred.turno()
            boxblue.turno()
            if boxblue.health <= 0 and boxred.health <= 0:
                print ('Hay empate debido a una destrucción mutua de ambas cajas')
                break
            elif boxred.health <= 0:
                print ('Equipo azul WIIIIN')
                break
            elif boxblue.health <= 0:
                print ('Equipo rojo WIIIIN')
                break
