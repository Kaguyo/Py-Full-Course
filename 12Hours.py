# 2D Lists = list of lists

Guns = ["Rifle","Pistol","Bow"]
Ammo = ["Arrows","7.62","9mm"]
Items = ["AidKit","Grenade","Knife"]

Backpack = [Guns,Ammo,Items]

Inventory = [Backpack]

# tuple = Collection which is ordered and unchangeable
#         Used to group together related data
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


print("How many empty chambers are there? "+str(Chamber.count("Empty_Chamber"))+".")