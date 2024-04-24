#Tur fali mai ita tama ba Method
#Method "mak ida ne'ebe hero bele halo" : meneyerang, bertahan, begerak
#Method iha interaksi rua ne'e mak hanesan : interaksi antara klient no interaski antara object

# Defini klase Hero
class Hero:
    total_hero = 0  # Variável estátika ne'ebé kalkula total hero sira

    # Konstrutor ho parameter sira: inputName, inputHealt, inputPower, inputArmor
    def __init__(self, inputName, inputHealt, inputPower, inputArmor):
        self.name = inputName  # Atribui naran ba instância
        self.health = inputHealt  # Atribui saúde ba instância
        self.power = inputPower  # Atribui poder ba instância
        self.armor = inputArmor  # Atribui armadura ba instância
        Hero.total_hero += 1  # Inkrementa total hero kada kria instância foun

    #Method without return an argument
    # Método ne'ebé imprime naran hero nian
    def se(self):
        print("Hau nia naran mak: " + self.name)

    #Method with argument
    # Método ne'ebé aumenta saúde hero nian
    def healthUp(self, up):
        self.health += up  # Aumenta saúde ho valor ne'ebé fornese iha argumento 'up'

    #Method with return
    # Método ne'ebé returna saúde atual hero nian
    def getHealth(self):
        return self.health  # Returna atributu saúde

# Kria instância hero1 ho naran "Xanana" no atributu sira seluk
hero1 = Hero("Xanana", 1000, 500, 70)
# Kria instância hero2 ho naran "Monteiro" no atributu sira seluk
hero2 = Hero("Monteiro", 2000, 400, 80)
# Kria instância hero3 ho naran "Kharu" no atributu sira seluk
hero3 = Hero("Kharu", 1200, 700, 30)

# Xamada método 'se' ba hero2 ne'ebé imprime naran
hero2.se()

# Imprime saúde atual husi hero1
print(hero1.health)
# Aumenta saúde hero1 ho 100
hero1.healthUp(100)
# Imprime saúde foun husi hero1
print(hero1.health)

# Imprime saúde atual husi hero1 no hero2 uza método 'getHealth'
print(hero1.getHealth())
print(hero2.getHealth())
