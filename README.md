# OOP PYTHON
OOP (Object-Oriented Programming) iha Python nia laran kria oportunidade atu implementa estrutura ida ne'ebé organiza kodigu iha forma ne'ebé atribui atributu no métodu ba objetu sira. Ida ne'e bele ajuda haforsa abstrasaun no modularidade iha kodigu.

Iha Python, OOP inklui konseitu sira hanesan:

1. **Objetu**: Ne'ebé hanesan instánsia husi klasifikasaun. Objeto iha atributu no métodu sira.

2. **Klase**: Ne'ebé hanesan estrutura ida ne'ebé define atributu no métodu sira. Instánsia sira hosi klasifikasaun ne'e bele kria.

3. **Atributu**: Ne'ebé hanesan variável ne'ebé ligadu ba objetu.

4. **Métodu**: Ne'ebé hanesan funsaun ne'ebé ligadu ba objetu.

Exemplu sinplifikadu kona-ba OOP iha Python:

Iha kódigu kraik ne'e, iha klasifikasaun `Animal` ne'ebé iha atributu `nome` no `idade` no métodu `som`. Klase sira seluk hanesan `Cachorro` no `Gato` estende klasifikasaun `Animal` no sobresai (override) métodu `som` atu hatudu som espesífiku hosi kada animal. Depois kria instánsia hosi klasifikasaun sira no uza atributu no métodu sira.

```python
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
```
