#Tur fali mai ita tama ba Class no Instance variables 
#No hatene nia diferensa entre Class no Instance variables

class Hero: # Defini klase naran Hero
    # Variável klase
    total = 0  # Variável klase naran total, inisia ho valor 0

    def __init__(self, inputName, inputHealt, inputPower, inputArmor):
        # Método konstrutór hodi kria instánsia Hero nian
        
        # Variáveis instánsia
        self.name = inputName  # Variável instánsia naran name, simu valor husi inputName
        self.health = inputHealt  # Variável instánsia naran health, simu valor husi inputHealt
        self.power = inputPower  # Variável instánsia naran power, simu valor husi inputPower
        self.armor = inputArmor  # Variável instánsia naran armor, simu valor husi inputArmor
        Hero.total += 1  # Aumenta valor total iha klase Hero nian
        print("Aumenta Hero ho naran: "+ inputName)  # Imprime mensajen ne'ebé hatudu naran Hero foun

hero1 = Hero("Sniper", 100, 250, 400)  # Kria instánsia Hero naran Sniper
print("Total Hero: " + str(Hero.total))  # Imprime total Hero nian

hero2 = Hero("mirana", 100, 15, 1)  # Kria instánsia Hero naran mirana
print("Total Hero: " + str(Hero.total))  # Imprime total Hero nian

hero3 = Hero("Kharu", 1000, 100, 0)  # Kria instánsia Hero naran Kharu
print("Total Hero: " + str(Hero.total))  # Imprime total Hero nian
