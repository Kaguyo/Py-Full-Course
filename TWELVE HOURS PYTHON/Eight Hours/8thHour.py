# Method Overriding:
print()
class Voicechat:
    
    def talk(speak):                    # NAME PLUS IT'S PARAMETER also known as : Method Signature
        print('An user said something')

class User(Voicechat):
    
    def talk(speak):                       
        print('An user heard something')

user = User()                           # Output of object will be the nearest associated with itself
user.talk()                             # before relying on a method that may inherit from a parent class
print()
#   ------------------------------

''' Method Chaining:            Chamar multiplos métodos sequencialmente, cada chamado faz uma ação
                                no mesmo objeto e retorna self'''

class Anel:
    def material(self):
        print('Este anel é feito de ouro')
        return self
    
    def valor(self):
        print('Este anel vale R$ 7.000,00')
        return self
    
    def peso(self):
        print('Este anel pesa 9 gramas')
        return self
    
    def formato(self):
        print('Este anel tem a joia em formato hexangular')

anel = Anel()

anel.material()\
    .valor()\
    .peso()\
    .formato()
print()

# Super() = Function used to given acess to the methods of a parent class.
#           Returns a temporary object of a parent class when used

class Keqing:

    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

class Daisy(Keqing):

    def __init__(self, age, weight):
        super().__init__(age, weight)
    
    def fase(self):
        return self.age*self.weight

class Peach(Keqing):
    
    def __init__(self, age, weight, height):
        super().__init__(age, weight)
        self.height = height

keqing = Keqing(19,60)
peach = Peach(19, 60, 173)

print(Daisy.fase())