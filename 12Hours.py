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

print("Difference: ",Dbz.difference(Naruto))
print("Intersection: ",Dbz.intersection(Naruto))

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
print("Nome contrario:",nome[-1::-1])      # O index negativo, inverte a posição de index.