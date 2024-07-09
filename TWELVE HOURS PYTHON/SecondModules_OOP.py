class Ataque:
    # Class variable: Inside class, Outside constructor.

    Slots = int(4)                       # Class variable

    def __init__(self,Nome,Tipo,Categoria,PP,Power,Accuracy,Target):
        self.Nome = Nome            # Instance variable
        self.Tipo = Tipo            # Instance variable
        self.Categoria = Categoria  # Instance variable
        self.PP = PP                # Instance variable
        self.Power = Power          # Instance variable
        self.Accuracy = Accuracy    # Instance variable
        self.Target = Target        # Instance variable

    def move(self):
        print(self.Nome+' was executed')
#   -----------------------------------
class Character:
    Alive = True

    def Health():
        print('This character has Health')
    
    def Attack():
        print('This character has Attack')

    def Defense():
        print('This character has Defense')

class March7th(Character):
    def Element():
        print('This character has Ice element')

class DanHeng(Character):
    def Element():
        print('This character has Imaginary element')

class Seele(Character):
    def Element():
        print('This character has Quantum element and shes goddamn beautiful')

class Weapon:

    def Scythe(self=Seele):         # Herda a classe Seele, qual está também herdando toda classe Character,
                                    # que por sua vez está sendo apenas definida, no topo das classes
        print('This character uses a Scythe and she is baddass.')
    
    def Spear(self=DanHeng):        # Herda a classe DanHeng, qual está também herdando toda classe Character,
                                    # que por sua vez está sendo apenas definida, no topo das classes
        print('This character uses a Spear')
    
    def Bow(self=March7th):         # Herda a classe March7th, qual está também herdando toda classe Character,
                                    # que por sua vez está sendo apenas definida, no topo das classes
        print('This character uses a Bow')

print('March 7th:')
march7th = (Character.Health(), Character.Attack(), Character.Defense(), Weapon.Bow())
print('\nDan Heng:')
danheng = (Character.Health(), Character.Attack(), Character.Defense(), Weapon.Spear())
print('\nSeele Vollerei:')
seele = (Character.Health(), Character.Attack(), Character.Defense(), Weapon.Scythe())
