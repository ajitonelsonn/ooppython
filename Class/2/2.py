#Tur fali mai ita tama ba Constructor _init_()
#No ita halo atribute langsung

# Kria klase Hero ho atributu sira ne'ebé define nia naran, saúde, forsa, no armadura
class Hero: #template
    # Funsaun konstrutór ne'ebé ita boot sira sei uza atu kria instánsia husi klase Hero
    def __init__(self, inputName, inputHealt, inputPower, inputArmor):
        # Atribui valor inputName ba atributu name husi instánsia
        self.name = inputName
        # Atribui valor inputHealt ba atributu health husi instánsia
        self.health = inputHealt
        # Atribui valor inputPower ba atributu power husi instánsia
        self.power = inputPower
        # Atribui valor inputArmor ba atributu armor husi instánsia
        self.armor = inputArmor

# Kria instánsia hero1 husi klase Hero ho naran "Sniper", saúde 100, forsa 250, no armadura 400
hero1 = Hero("Sniper", 100, 250, 400)
# Kria instánsia hero2 husi klase Hero ho naran "mirana", saúde 100, forsa 15, no armadura 1
hero2 = Hero("mirana", 100, 15, 1)
# Kria instánsia hero3 husi klase Hero ho naran "Kharu", saúde 1000, forsa 100, no armadura 0
hero3 = Hero("Kharu", 1000, 100, 0)

# Imprime atributu sira husi hero1 uza metodu __dict__ ne'ebé bele hatudu atributu sira ho nia valor
print(hero1.__dict__)
# Imprime atributu sira husi hero2 uza metodu __dict__ ne'ebé bele hatudu atributu sira ho nia valor
print(hero2.__dict__)
# Imprime atributu sira husi hero3 uza metodu __dict__ ne'ebé bele hatudu atributu sira ho nia valor
print(hero3.__dict__)

# Imprime valor husi atributu name husi hero1
print(hero1.name)
# Imprime valor husi atributu health husi hero2
print(hero2.health)
# Imprime valor husi atributu armor husi hero3
print(hero3.armor)