# 2D Lists = list of lists

Guns = ["Rifle","Pistol","Bow"]
Ammo = ["Arrows","7.62","9mm"]
Items = ["AidKit","Grenade","Knife"]
Backpack = [Guns,Ammo,Items]
Inventory = [Backpack]
# tuple
        
Chamber = ("Empty_Chamber","Loaded_Chamber","Empty_Chamber","Empty_Chamber","Empty_Chamber","Empty_Chamber")

if Backpack:
    print("\nInventory:"+"\n"*2+"Backpack:")
else: 
    print("Inventory:\n")

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
print("Genshin Impact:\n")
for x in GI_Characters:
    print(x)

# GI_CharsGearEquipped = GI_Characters.union(Weapons) Basicamente, cria uma variavel para armazenar os valores somados,
# sem de fato somar os 2 em si.

print("\nDragon Ball Z & Naruto:\n")
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

# Functions :
print("\nFunctions:""\n")

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
def Genshin(**kwargs):
    for key,value in kwargs.items():
        print(value,end=" ") # end deixa tudo em uma linha apenas
    print("\n")
kwargs_end_Genshin = False
if kwargs_end_Genshin:print("Usando .items para kwargs, e end para value in kwargs:"),Genshin(razor="Electro",retentora="Anemo",thoma="Pyro",kirara="Dendro",ayaka="Cryo",navia="Geo",tartaglia="Hydro")



def Genshin(**kwargs):
    for key,value in kwargs.items():
        print(value) 
           
kwargs_Genshin = False
if kwargs_Genshin:print("Usando .items para kwargs, sem end para value in kwargs:"),Genshin(razor="Electro",retentora="Anemo",thoma="Pyro",kirara="Dendro",ayaka="Cryo",navia="Geo",tartaglia="Hydro")


# Método str.Format 
#            Concede mais controle para os usuários mostrar o output
print("\nStrFormat:\n")

body_part = "fist"
head_part = "face"

print("the {1} punched the {0}".format(body_part,head_part))
print("the {body_part} punched the {head_part}".format(head_part="face",body_part="fist"))

text = "Goku está em forma {}"
print(text.format("base"))
print(text.format("super sayajin\n"))

number = 10000
print("The number is {:,.2f}".format(number))
print("The number is {:b} in binary representation.".format(number))
print("The number is {:o} in octadecimal representation.".format(number))
print("The number is {:x} in hexadecimal representation.".format(number))
print("The number is {:E} in scientific notation.".format(number))

import random

x = random.randint(1,6)
y = random.random()

print("Numero aleatorio de 1 até 6: "+str(x))

attacklist = ['kamehameha','kaioken','strike']
z = random.choice(attacklist)
print("Ataque aleatório da lista de ataques Z:",z+"\n")

print("Embaralhamento:")
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)

treino_exception = False
if treino_exception:
    try:
        numerator = float(input("Enter a number to divide: "))
        denominator = float(input("Enter a number to divide by: "))
        result = numerator / denominator
    except ZeroDivisionError as e:
        print("You can't divide by zero.")
    except ValueError as e:
        print("Enter only numbers.")
    except Exception as e:
        print("Something is wrong with ur ass code.")
    else:
        print(result)
    finally:
        print("This will always execute.")

import os

path = "D:\\"

if os.path.exists(path):
    print("\nO caminho é existente.")
    if os.path.isfile(path):
        print("E é um arquivo.\n")
    elif os.path.isdir(path):
        print("E é uma pasta.\n")
else:
    print("\nO Caminho não existe.")


abrir_arquivo = False
if abrir_arquivo:
    try:
        with open(r"C:\Users\gabri\OneDrive\Área de Trabalho\Python\Test.txt") as file: # Abre o arquivo em questão como variavel 'file' em um caminho especifico,
            print(file.read())                                                          # mas poderia abrir em um caminho predefinido.                                                          
    except FileNotFoundError:                                                           
        print("Não deu pra achar, Caralho!")
    print(file.closed) # Printa true se o arquivo estiver fechado e false caso contrario.



abrir_arquivo_2nd = False
if abrir_arquivo_2nd == "Write":
    try:
        text="Esse eh o conteudo SOBREPOSTO do arquivo." # Usando metodo 'w', (Write) na função open.
        with open("C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Python\\WriteOrAppend.txt",'w') as Write:
            Write.write(text)
    except FileNotFoundError:
        print("Não deu pra achar, Caralho!")

elif abrir_arquivo_2nd == "Append": 
    try:
        text="\nEsse eh o conteudo JUNTADO do arquivo." # Usando metodo 'a', (Append) na função open.
        with open("C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Python\\WriteOrAppend.txt",'a') as Append:
            Append.write(text)
    except FileNotFoundError:
        print("Não deu pra achar, Caralho!")

elif abrir_arquivo_2nd == "Original":
    try:
        text="Esse eh o conteudo ORIGINAL do arquivo." # Usando metodo 'w', (Write) na função open.
        with open("C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Python\\WriteOrAppend.txt",'w') as Original:
            Original.write(text)
    except FileNotFoundError:
        print("Não deu pra achar, Caralho!")

# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a folder
# copy2() =     copy() + copies metadata (file's creation and modification times)

import shutil

#     shutil.copy('ARQUIVOINUTIL.txt',r'C:\Users\gabri\OneDrive\Área de Trabalho\PASTA PARA ESTUDOS PYTHON')

source = 'Test.txt'
destination = r'C:\Users\gabri\OneDrive\Área de Trabalho\PASTA PARA ESTUDOS PYTHON\Test.txt'

try:
    if os.path.exists(destination):
        print("There already is a file there\n")
    else:
        os.replace(source,destination)
        print(source+" was moved\n")
except FileNotFoundError:
    print(source+" was not found\n")


def deletando_arquivos_pastas():
    
    File_and_Dir = True
    if File_and_Dir:
        # Output pra organizar console
        print("Primeiro bloco da funcao:")
        # Declarando variavel guardando nome seguinte dado a uma pasta.
        Nome_da_Pasta = 'Folder with content'
        # Verificando se ja existe tal pasta.
        if os.path.exists(Nome_da_Pasta):
            print("There already is a folder named "+Nome_da_Pasta)
        else:
        # Criando a pasta com o nome anteriormente declarado.
            os.mkdir(Nome_da_Pasta)
        # Verificando se o arquivo ja esta dentro da pasta criada.
        if os.path.exists(r'C:\Users\gabri\OneDrive\Área de Trabalho\Python\TWELVE HOURS PYTHON\Folder with content\file.txt'):
            print("The file already is in the folder")
        else:
            # Declarando variavel guardando nome seguinte dado a um arquivo.
            file_and_dir = 'arquivo.txt'
            
            # Verificando se ja existe o arquivo em questão.
            if os.path.exists(file_and_dir):
                print("The file "+file_and_dir+" already exists.")
            # Criando o arquivo se ainda não existir.
            else:
                with open(file_and_dir,'w') as FandDir:
                    FandDir.write('Este arquivo foi gerado automaticamente')
                    print('O arquivo '+file_and_dir+' foi criado.')
            # Movendo o arquivo para dentro da pasta.
                os.replace(file_and_dir,r'C:\Users\gabri\OneDrive\Área de Trabalho\Python\TWELVE HOURS PYTHON\Folder with content\file.txt')
            # Verificando se o arquivo foi de fato movido para dentro da pasta.
                if os.path.exists(r'C:\Users\gabri\OneDrive\Área de Trabalho\Python\TWELVE HOURS PYTHON\Folder with content\file.txt'):
                    print("The file was moved succesfully")
            # Por fim mensagem de sucesso do algoritmo :)
                if os.path.exists(r'C:\Users\gabri\OneDrive\Área de Trabalho\Python\TWELVE HOURS PYTHON\Folder with content\file.txt'):
                    print("A porra da pasta existe, e o arquivo esta dentro dela.")
            # Mensagem de fracasso total >:(
                else:
                    print("Lixo nao sabe nem fazer algoritmo.\n")

        # !!!!!! Trecho pra apagar a porra toda !!!!!! 
        Quero_Excluir_Esta_Pasta = False
        if Quero_Excluir_Esta_Pasta:
        # Criando handling para erro de permissão.
            try:
                shutil.rmtree(Nome_da_Pasta)
                print("Apagou a porra toda.\n")
            except PermissionError as e:
            # Exibindo erro encontrado, e também mensagem de erro personalizada.
                print(e)
                print('Fraco, impotente, nao tem permissao para deleter o proprio arquivo.\n')

    File = True
    if File:
        print("\nSegundo bloco da funcao:")
        file_content = ''
        file_source = 'file.txt'
        if os.path.exists(file_source):
            print("Item "+file_source+" found")
        else:
            with open(file_source,'w') as file:
                file.write(file_content)
            if os.path.exists(file_source):
                print("File "+file_source+" was created")
            else:
                print("File couldn't be created")
        try:
            if os.path.exists(file_source):
                os.remove(file_source)
                if os.path.exists(file_source):
                    print(file_source+" was not deleted")
                else:
                    print(file_source+" was deleted")
            else:
                print(file_source+" was not found")
        except PermissionError:
            print("You do not have permission to delete that")
    else:
        print("The function seems unfunctional, try turning booleans at the top to true.")

    Folder = True
    if Folder:
        print("\nTerceiro bloco da funcao:")
        folder_source = 'Folder'
        if os.path.exists(folder_source):
            print("Item "+folder_source+" found")
        else:
            os.mkdir(folder_source)
            print("Directory "+folder_source+" was created")

        try:
            if os.path.exists(folder_source):
                os.rmdir(folder_source)
                if os.path.exists(folder_source):
                    (folder_source+" was not deleted")
                else:
                    print(folder_source+" was deleted")
            else:
                print(folder_source+" was not found")
        except PermissionError:
            print("You do not have permission to delete that")
    else:
        print("The function seems unfunctional, try turning booleans at the top to true.")

deletar_e_criar = False
if deletar_e_criar:deletando_arquivos_pastas()

print("\nModulos, agora deu o caraio memo: ")
#   module = a file containing python code. May contain functions, classes, etc.
#   used with modular programming, which is to separate a program into parts

#   Metodo 1: importa um modulo podendo usar 'alias' para entao usar dot e escolher qual funçao/variavel usar.
import Modules as mdl
mdl.hello
#   Metodo 2: importa uma extensao de funcoes diretamente do modulo, 
#   assim podendo apenas chamar as funcoes sem precisar do nome do modulo.

from Modules import funcao_multipla as f1, funcao_multipla2, funcao_mutlipla3 as f3
f1()
funcao_multipla2()
f3()