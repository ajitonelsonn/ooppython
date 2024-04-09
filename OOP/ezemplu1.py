class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        return "Au Au!"

class Gato(Animal):
    def som(self):
        return "Miau!"

# Kria instánsia sira hosi klasifikasaun
rex = Cachorro("Rex", 3)
mimi = Gato("Mimi", 2)

# Aksesu ba atributu sira
print(rex.nome)  # Sai "Rex"
print(mimi.idade)  # Sai 2

# Chamada ba métodu sira
print(rex.som())  # Sai "Au Au!"
print(mimi.som())  # Sai "Miau!"
