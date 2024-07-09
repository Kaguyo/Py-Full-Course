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
class Character:                    # Define Character
    Alive = True

    health = 'This character has Health ({})'                 
    attack = 'This character has Attack ({})'
    defense = 'This character has Defense ({})'

class March7th(Character):          # Herda Character
    def Element1():
        print('This character has Ice element')
        print(Character.health.format(40))
        print(Character.defense.format(100))
        print(Character.attack.format(20))
        
class DanHeng(Character):           # Herda Character
    def Element2():
        print('This character has Imaginary element')
        print(Character.health.format(40))
        print(Character.defense.format(50))
        print(Character.attack.format(70))
class Seele(Character):             # Herda Character
    def Element3():
        print('This character has Quantum element and shes goddamn beautiful')
        print(Character.health.format(40))
        print(Character.defense.format(50))
        print(Character.attack.format(110))


class Weapon(Seele,DanHeng,March7th): # Herda as 3 Classes anteriores / MultipleInheritance
                                    
    def Scythe():
        print('This character uses a Scythe and she is baddass.')
    
    def Spear():        
        print('This character uses a Spear')
    
    def Bow():         
        print('This character uses a Bow')

print('\nMarch 7th:')
march7th = (Weapon.Element1(), Weapon.Bow()) 
print('\nDan Heng:')
danheng = (Weapon.Element2(), Weapon.Spear())
print('\nSeele Vollerei:')
seele = (Weapon.Element3(), Weapon.Scythe())    # Graças a MultipleInheritance, através de Weapon posso acessar 
                                                # o conteudo de cada method que cada classe possuí.  Do contrário-
                                                # Teria que usar classe Seele.Element,DanHeng.Element etc...
