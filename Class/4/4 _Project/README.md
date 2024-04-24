# Exerciciu OOP simples

``` python
#GAME SIMPLES
# Kria joku simples ne'ebé involve hero rua ne'ebé ataka malu-malu

class Hero:
    # Inisializasaun klase Hero ho atributu sira ne'ebe inklui naran, saúde, forsa atake, no númeru armadura
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name  # naran hero
        self.health = health  # saúde hero
        self.attackPower = attackPower  # forsa atake hero
        self.armor = armorNumber  # númeru armadura hero
        self.total_ataka = 0  # kontador atake total
        self.total_atakasaun= 0  # kontador total atakasaun (vezes ne'ebé hero diserang)

    # Metodu ataka ne'ebe simu objektu lawan (hero seluk) hanesan argumentu
    def ataka(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)  # imprime mensajen atake
        self.total_ataka += 1  # aumenta kontador atake
        print(self.name + ' menyerang ' + lawan.name+' hamutuk: '+ str(self.total_ataka))  # imprime total atake
        lawan.diserang(self, self.attackPower)  # xama metod diserang iha objektu lawan
        
    # Metodu diserang ne'ebe simu objektu lawan no forsa atake husi lawan
    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' diserang '+ lawan.name)  # imprime mensajen ne'ebe hateten katak hero diserang
        print("---------")
        attack_diterima = attackPower_lawan / self.armor  # kalkula atake ne'ebe diterima ho divide forsa atake ho armadura
        print(f"Hero Lawan: {lawan.name} nia atack power: {attackPower_lawan}")
        print(f"Hero ne'ebe atakasaun: {self.name} nia armor: {self.armor}")
        print('serangan terasa: '+ str(attack_diterima))  # imprime forsa atake ne'ebe diterima
        print("---------")
        self.health -= attack_diterima  # reduz saúde ho atake ne'ebe diterima
        print('darah ' + self.name + ' tersisa '+ str(self.health))  # imprime saúde atual hero
        self.total_atakasaun+=1  # aumenta kontador atakasaun
        print(self.name + ' simu atakasaun hamutukuk: ' + str(self.total_atakasaun))  # imprime total atakasaun

# Kria objektu sniper ho klase Hero
sniper = Hero('sniper', 100, 10, 5)
# Kria objektu gatotkacha ho klase Hero
gatotkacha = Hero('gatotkacha', 100, 20, 10)

# Kria objektu Kharu ho klase Hero
kharu = Hero('kharu', 100, 30, 20)

# sniper ataka gatotkacha
sniper.ataka(gatotkacha)
print("\n")
# sniper ataka gatotkacha fali
sniper.ataka(gatotkacha)
print("\n")
# gatotkacha ataka sniper
gatotkacha.ataka(sniper)
print("\n")
# sniper ataka gatotkacha fali
sniper.ataka(gatotkacha)
print("\n")
# gatotkacha ataka sniper fali
gatotkacha.ataka(sniper)
print("\n")
# kharu ataka sniper
kharu.ataka(sniper)

```




In the provided Python code, `self.attackPower` is used in the method call `lawan.diserang(self, self.attackPower)` to pass the attack power of the current hero (`self`) to the method `diserang` of the opposing hero (`lawan`). This is necessary because the `diserang` method needs to know the attack power of the attacker to calculate the damage received after considering the armor of the hero being attacked.

Here's a breakdown of the process:
- `self.attackPower` refers to the attack power attribute of the hero who is currently attacking.
- When `self.ataka(lawan)` is called, it signifies that the current hero is attacking the opponent (`lawan`).
- Inside the `ataka` method, `lawan.diserang(self, self.attackPower)` is called. This means the opponent (`lawan`) is being attacked and needs to process the attack.
- The `diserang` method of the opponent (`lawan`) takes two parameters: the attacking hero (`self`) and the attack power of the attacking hero (`self.attackPower`).
- The `diserang` method uses these parameters to calculate the effective damage by considering the armor of the hero being attacked and then updates the health of the attacked hero accordingly.

This mechanism allows the simulation of an attack between two heroes, where each hero's specific attack power and armor are taken into account to determine the outcome of the attack.