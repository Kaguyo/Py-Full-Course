def dano_causado():

    print("Quanto de ATK você tem?")
    Atk = int(input())
    print("ATK:", Atk)

    print("Quanto de Multiplicador de Skill você tem?")
    Multiplier = float(input())
    print("Multiplicador de Skill:",str(Multiplier)+"%")

    print("Quanto de Dano Crítico você tem?")
    CritDMG = float(input())
    print("Dano Crítico:",str(CritDMG)+"%")

    print("Quanto de Bonus de Dano você tem?")
    BonusDMG = float(input())
    print("Bonus de Dano:",str(BonusDMG)+"%")

    print("Quanto de Bonus de Dano de Skill você tem?")
    MultiplierBonus = float(input())
    print("Bonus de Multiplicador de Skill:",str(MultiplierBonus)+"%")

    print("Quanto de Defesa seu inimigo tem?")
    Def_enemy = int(input())
    print("Defesa inimigo:", Def_enemy)

    print("Quanto de Resistencia do Inimigo?")
    Resistance = float(input())
    print("Resistencia do Inimigo:",str(Resistance)+"%")

    print("Qual o Level do Inimigo?")
    Lvl_enemy = int(input())
    print("Level do Inimigo:",Lvl_enemy)

    print("Quanto de Debuff na Resistência do Inimigo?")
    DebuffRes = float(input())
    print("Quantidade de Debuff na Resistência do Inimigo:",str(DebuffRes)+"%")

    Verdadeira_EnemyDef = Def_enemy * (Lvl_enemy / 100 + 1)
    resist_effect = (Resistance - DebuffRes) / 100
    Dano = (Atk-Verdadeira_EnemyDef)*(Multiplier/100)*(CritDMG/100+1)*(BonusDMG/100+1)*(MultiplierBonus/100+1)*(1-resist_effect)
    if Dano > 0:
        print("Opçao 1 Dano Causado:",Dano)
    elif Dano < 0:
        Dano = 1
        print(" Opçao 2 Dano Causado:",Dano)
    else: print(" Opçao 3 Dano Causado:",Dano)

dano_causado()
