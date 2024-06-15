# 2D Lists = list of lists

Guns = ["Rifle","Pistol","Bow"]
Ammo = ["Arrows","7.62","9mm"]
Items = ["AidKit","Grenade","Knife"]
Backpack = [Guns,Ammo,Items]
Inventory = [Backpack]
# tuple
        
Chamber = ("Empty_Chamber","Loaded_Chamber","Empty_Chamber","Empty_Chamber","Empty_Chamber","Empty_Chamber")

print("\n")
if Backpack:
    print("Inventory:"+"\n"*2+"Backpack:")
else: 
    print("Inventory:"+"\n")

for x in Backpack:
    print(x)
print("\n""in Backpacks slot[0][0] there is: "+Backpack[0][0]+".")


if Chamber.count("Loaded_Chamber") == 1:
    print(str(Chamber.count("Loaded_Chamber"))+" Round left.")
elif Chamber.count("Loaded_Chamber") > 1:
    print(str(Chamber.count("Loaded_Chamber"))+" Rounds left.")
else:
    print("No Rounds left.")


print("How many empty chambers are there? "+str(Chamber.count("Empty_Chamber"))+".""\n")

# set

GI_Characters = {"keqing","hutao","diluc","xiao","ayaka"}
Weapons = {"staff of homa","mistsplitter","jade spear","wolfs gravestone","jade cutter"}
Weapons.add("geppaku haran")
Weapons.remove("mistsplitter")
# Weapons.clear() 
GI_Characters.update(Weapons)
print("Genshin Impact:""\n")
for x in GI_Characters:
    print(x)

# GI_CharsGearEquipped = GI_Characters.union(Weapons) Basicamente, cria uma variavel para armazenar os valores somados,
# sem de fato somar os 2 em si.

print("\n""Dragon Ball Z & Naruto:""\n")
Dbz = {"goku","vegeta","gohan","fans"}
Naruto = {"naruto","sasuke","itachi","fans"}

print("Difference:",Dbz.difference(Naruto))
print("Intersection:",Dbz.intersection(Naruto))

# Dictionary
# Obs, datatype não importa.
print("\n""Dictionary:""\n")
Ayaka = 1
Cryo = 2

Elementos = {Ayaka:Cryo,
             "Baizhu":"Dendro",
             "Keqing":"Electro",}

Elementos.update({"Shenhe":"Cryo"})
Elementos.update({"Jean":"Anemo"})
Elementos.update({"Jean":"Mondstadt"})
# Elementos.pop(Ayaka) remove ayaka
# Elementos.clear()

print("Key ayaka:",Elementos[Ayaka])
print("Key baizhu:",Elementos["Baizhu"])
print("Get:",Elementos.get("Hutao"))
print("Keys:",Elementos.keys())
print("Values:",Elementos.values())
print("Items:",Elementos.items())


# Loop for para formatalizar e exibir primeiro elemento e segundo elemento de cada linha
for key,value in Elementos.items():
    print("for:",key, value)

nome ="goku"
if(nome[0].islower()):
    print("\n""Index:",nome[0::3].upper()) # Duplo ponto duplo("::") significa slicing.
                                           # Enquanto apenas duplo ponto(":") significa range.
print("Nome contrario:",nome[-1::-1],"\n")      # O index negativo, inverte a posição de index.

# Tests :

print("Testes:","\n")
number1 = True
number2 = True
number3 = 3
number4 = 4
if number1 and (not number2 or number3 < number4):
    print("o not aplica apenas ao proximo parametro/variavel.")
else: print("sim o not, aplica em todos dentro de uma tupla ou à direita.")

print("\n")
# Functions :
print("Functions:""\n")

# Testes tuplas e variaveis
def calcular_desconto(total, cupom):
    if cupom == "DESC10":
        desconto = total * 0.1
        return desconto
    else:
        return 0

# Chamada da função e impressão do desconto
desconto = False
if desconto:
    desconto_final = calcular_desconto(100, "DESC10")
    print("Desconto aplicado:", desconto_final, "(Estudando uso de Return)")



# Programa de dano causado :
def dano_causado():

    Atk = int(input("Quanto de Atk vc tem?: "))
    print("ATK:", Atk,"\n")

    Multiplier = float(input("Quanto de Multiplicador de Skill você tem?: "))
    print("Multiplicador de Skill:",str(Multiplier)+" %")

    CritDMG = float(input("Quanto de Dano Crítico você tem?: "))
    print("Dano Crítico:",str(CritDMG)+" %")

    BonusDMG = float(input("Quanto de Bonus de Dano você tem?: "))
    print("Bonus de Dano:",str(BonusDMG)+" %")

    MultiplierBonus = float(input("Quanto de Bonus de Dano de Skill você tem?: "))
    print("Bonus de Multiplicador de Skill:",str(MultiplierBonus)+" %")

    Def_enemy = int(input("Quanto de Defesa seu inimigo tem?: "))
    print("Defesa inimigo:", Def_enemy)

    Resistance = float(input("Quanto de Resistencia do Inimigo?: "))
    print("Resistencia do Inimigo:",str(Resistance)+" %")

    DebuffRes = float(input("Quanto de Debuff na Resistência do Inimigo?: "))
    print("Quantidade de Debuff na Resistência do Inimigo:",str(DebuffRes)+" %")

    Lvl_enemy = int(input("Qual o Level do Inimigo?: "))
    print("Level do Inimigo:",Lvl_enemy)

    Verdadeira_EnemyDef = Def_enemy * (Lvl_enemy / 100 + 1)
    resist_effect = (Resistance - DebuffRes) / 100
    Dano = (Atk-Verdadeira_EnemyDef)*(Multiplier/100)*(CritDMG/100+1)*(BonusDMG/100+1)*(MultiplierBonus/100+1)*(1-resist_effect)
    if Dano > 0:
        print("Dano Causado:",int(Dano))
    elif Dano < 0:
        Dano = 1
        print("Dano Causado:",int(Dano))
    else: print("Dano Causado:",int(Dano))

Hit_taken = False
if Hit_taken:dano_causado()
else: pass

# "*"arguments = will pack the arguments into a tuple
#                useful so that a function can accept a varying amount of arguments
def add(*stuff):
    sum = 0
    for i in stuff:
        sum += i
    return sum

Add = False
if Add:
    print(add(1,2,3,4,5,6),"(Argumento *)")



# Quantas vezes while é utilizado até o N tornar-se 1 :
def probleman3i1():
    n = int(input("Digite um valor inteiro: "))
    i = 0
    
    if n == 1:
        print(0)
    else:
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = n * 3 + 1
            i = i + 1
        
    print("A quantidade de vezes que a função foi chamada foi:",i)

Probleman3i1 = False
if Probleman3i1:probleman3i1()
else: pass


def hanoi(n):
    torre1 = ""
    torre2 = ""
    torre3 = ""
    for i in range(n, 0, -1):
        torre1 += str(i)
    while len(torre3) < n:
        print("!!!!!Contador de voltas!!!!!"+"\n")
        if torre1 and (not torre2 or torre1[-1] < torre2[-1]):
            torre2 += torre1[-1]
            torre1 = torre1[:-1] # Atualiza o valor após transferência de disco.
            print("IF Mova o disco %s da torre 1 para a torre 2." % torre2[-1])
        else:
            torre1 += torre2[-1]
            torre2 = torre2[:-1] # Atualiza...
            print("ELSE Mova o disco %s da torre 2 para a torre 1." % torre1[-1])
        print("Valor das torres: torre1: "+torre1+" torre2: "+torre2+" torre3: "+torre3)
        if torre1 and (not torre3 or torre1[-1] < torre3[-1]):
            torre3 += torre1[-1]
            torre1 = torre1[:-1] # Atualiza...
            print("IF Valor da torre 3:",torre3[0:-1])
            print("IF Mova o disco %s da torre 1 para a torre 3." % torre3[-1])
        else:
            torre1 += torre3[-1]
            torre3 = torre3[:-1] # Atualiza...
            print("ELSE Mova o disco %s da torre 3 para a torre 1." % torre1[-1],)
        print("Valor das torres: torre1: "+torre1+" torre2: "+torre2+" torre3: "+torre3)
        if torre2 and (not torre3 or torre2[-1] < torre3[-1]):
            torre3 += torre2[-1]
            torre2 = torre2[:-1]
            print("IF Mova o disco %s da torre 2 para a torre 3." % torre3[-1])
        else:
            torre2 += torre3[-1]
            torre3 = torre3[:-1]
            print("ELSE Mova o disco %s da torre 3 para a torre 2." % torre2[-1])
        print("Valor das torres: torre1: "+torre1+" torre2: "+torre2+" torre3: "+torre3)

Hanoi = False
if Hanoi:hanoi(4)


# Kwargs
print("Usando .items para kwargs, e end para value in kwargs:")
def Genshin(**kwargs):
    for key,value in kwargs.items():
        print(value,end=" ") # end deixa tudo em uma linha apenas
    print("\n")

kwargs_end_Genshin = True
if kwargs_end_Genshin:Genshin(razor="Electro",retentora="Anemo",thoma="Pyro",kirara="Dendro",ayaka="Cryo",navia="Geo",tartaglia="Hydro")


print("Usando .items para kwargs, sem end para value in kwargs:")
def Genshin(**kwargs):
    for key,value in kwargs.items():
        print(value) 
    print("\n")
    
kwargs_Genshin = True
if kwargs_Genshin:Genshin(razor="Electro",retentora="Anemo",thoma="Pyro",kirara="Dendro",ayaka="Cryo",navia="Geo",tartaglia="Hydro")


# Método str.Format 
#            Concede mais controle para os usuários mostrar o output
print("StrFormat:")

Ataques = {}

Personagens = ["Pain","Madara","Sasuke","Orochimaru"]

