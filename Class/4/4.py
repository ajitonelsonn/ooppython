# Jogo Simples
# Cria um jogo simples que envolve dois heróis atacando um ao outro

class Hero:
    # Inicialização da classe Hero com atributos incluindo nome, saúde, poder de ataque e número de armadura
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name  # nome do herói
        self.health = health  # saúde do herói
        self.attackPower = attackPower  # poder de ataque do herói
        self.armor = armorNumber  # número de armadura do herói
        self.total_attacks = 0  # contador de ataques totais
        self.total_being_attacked = 0  # contador total de vezes sendo atacado

    # Método para atacar que recebe um objeto adversário (outro herói) como argumento
    def attack(self, opponent):
        print(f"{self.name} ataca {opponent.name}")  # imprime mensagem de ataque
        self.total_attacks += 1  # incrementa contador de ataques
        print(f"{self.name} atacou {opponent.name} um total de: {self.total_attacks} vezes")  # imprime total de ataques
        opponent.be_attacked(self, self.attackPower)  # chama método be_attacked no objeto adversário
        
    # Método para ser atacado que recebe um objeto adversário e o poder de ataque do adversário
    def be_attacked(self, opponent, attackPower_opponent):
        print(f"{self.name} foi atacado por {opponent.name}")  # imprime mensagem de ser atacado
        print("---------")
        received_attack = attackPower_opponent / self.armor  # calcula o ataque recebido dividindo o poder de ataque pela armadura
        print(f"Adversário: {opponent.name} poder de ataque: {attackPower_opponent}")
        print(f"Herói atacado: {self.name} armadura: {self.armor}")
        print(f"Ataque recebido: {received_attack}")  # imprime o poder de ataque recebido
        print("---------")
        self.health -= received_attack  # reduz a saúde com o ataque recebido
        print(f"Saúde de {self.name} restante: {self.health}")  # imprime a saúde atual do herói
        self.total_being_attacked += 1  # incrementa contador de vezes sendo atacado
        print(f"{self.name} foi atacado um total de: {self.total_being_attacked} vezes")  # imprime total de vezes sendo atacado

# Cria objeto sniper da classe Hero
sniper = Hero('sniper', 100, 10, 5)
# Cria objeto gatotkacha da classe Hero
gatotkacha = Hero('gatotkacha', 100, 20, 10)

# Cria objeto Kharu da classe Hero
kharu = Hero('kharu', 100, 30, 20)

# sniper ataca gatotkacha
sniper.attack(gatotkacha)
print("\n")
# sniper ataca gatotkacha novamente
sniper.attack(gatotkacha)
print("\n")
# gatotkacha ataca sniper
gatotkacha.attack(sniper)
print("\n")
# sniper ataca gatotkacha novamente
sniper.attack(gatotkacha)
print("\n")
# gatotkacha ataca sniper novamente
gatotkacha.attack(sniper)
print("\n")
# kharu ataca sniper
kharu.attack(sniper)