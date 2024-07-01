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