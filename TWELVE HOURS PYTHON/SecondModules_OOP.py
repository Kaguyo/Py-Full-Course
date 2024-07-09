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

march7th = March7th.Element()
danheng = DanHeng.Element()
seele = Seele.Element()