class Animal:
    # Defini klase Animal ne'ebé atua nudár klase baze
    def __init__(self, nome, idade):
        # Konstrutór ne'ebé defini naran no idade animal nian
        self.nome = nome  # Inisializa atributu nome
        self.idade = idade  # Inisializa atributu idade

    def som(self):
        # Métodu abstratu som ne'ebé sei implementa iha klase derivadu sira
        pass

class Cachorro(Animal):
    # Klase Cachorro, herda husi klase Animal
    def som(self):
        # Implementa métodu som ba Cachorro
        return "Au Au!"  # Retorna som ida ne'ebé Cachorro halo

class Gato(Animal):
    # Klase Gato, herda husi klase Animal
    def som(self):
        # Implementa métodu som ba Gato
        return "Miau!"  # Retorna som ida ne'ebé Gato halo

# Kria instánsia sira hosi klasifikasaun
rex = Cachorro("Rex", 3)  # Kria instánsia ida husi klase Cachorro ho naran Rex no idade 3
mimi = Gato("Mimi", 2)  # Kria instánsia ida husi klase Gato ho naran Mimi no idade 2

# Aksesu ba atributu sira
print(rex.nome)  # Imprime naran Rex
print(mimi.idade)  # Imprime idade Mimi nian (2)

# Chamada ba métodu sira
print(rex.som())  # Imprime som husi Cachorro ("Au Au!")
print(mimi.som())  # Imprime som husi Gato ("Miau!")
