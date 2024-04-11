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







# Programming Paradigms in Python
Referencia : geeksforgeeks [https://www.geeksforgeeks.org/programming-paradigms-in-python/]

Paradigma mos bele koalia hanesan mekanizmu atu rezolve problema ka halo tarefa sira. Paradigma programasaun ne'e hanesan abordajen atu rezolve problema hodi utiliza linguajen programasaun balu ka mos ita bele dehan katak ne'e hanesan metodu atu rezolve problema hodi utiliza ferramentas no teknika sira ne'ebe mak disponivel ba ita ho abordajen balu. Iha linguajen programasaun barak ne'ebe mak hatudu maibé hotu-hotu presiza atu segui estratéjia balu bainhira sira implementa no metodu/estratéjia ne'e mak paradigma sira. Além de variedade sira husi linguajen programasaun, iha moós variedade sira husi paradigma atu satisfaze kada pedidu.

<img src='https://media.geeksforgeeks.org/wp-content/uploads/20200311232159/programmin-paradigms.png'>

Tuir referencia www.geeksforgeeks.org, Python suporta tipos tolu paradigma programasaun:

1. Paradigma programasaun Orientadu ba Objektu
2. Paradigma programasaun Orientadu ba Prosesu
3. Paradigma programasaun Funcional

## Paradigma programasaun Orientadu ba Objektu
Iha paradigma programasaun orientadu ba objektu, objektu sira mak elementu prinsipál paradigma nian. Objektu sira bele hatudu hanesan instánsia husi klasa ne'ebé iha dadus membru no funsaun métodu. Além disso, estilo orientadu ba objektu halo relasiona entre dadus membru no funsaun métodu sira ne'ebé suporta enkapsulamentu no ho ajuda husi konseitu heransa nian, kodigu bele reutilizável, maibé desvantajen prinsipál paradigma programasaun orientadu ba objektu nian mak bainhira kodigu la hetan hanesan ne'ebé di'ak, entaun programa bele sai monstus.


### Ezemplu
```python
# class Emp has been defined here 
class Emp: 
	def __init__(self, name, age): 
		self.name = name 
		self.age = age 
	
	def info(self): 
		print("Hello, % s. You are % s old." % (self.name, self.age)) 

# Objects of class Emp has been 
# made here		 
Emps = [Emp("John", 43), 
	Emp("Hilbert", 16), 
	Emp("Alice", 30)] 

# Objects of class Emp has been 
# used here 
for emp in Emps: 
	emp.info() 

```

Note: Ba Informasaun liu tan bele hare iha link ne'e : https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/

## Paradigma programasaun Orientadu ba Prosesu

Iha paradigma programasaun orientadu ba prosesu, série husi etapa komputasionál sei divididu iha módulu sira ne'ebé signifika katak kodigu grupu iha funsaun sira no kodigu sei hetan ezekusaun seriál etapa husi etapa, então bazeia ba komunikasaun kodigu seríal atu instrui komputador ho kada etapa atu realiza tarefa ida mak determinada. Paradigma ida ne'e ajuda iha modularidade kodigu no modularizasaun normalmente hahu husi implementasaun funsionál. Paradigma programasaun ida ne'e ajuda iha organizasaun fasil ba ita nia iten sira ne'ebé relasionadu ho difikuldade no kada fail husi arka hanesan nia kontenedor.

### Ezemplu
```python
# Procedural way of finding sum 
# of a list 

mylist = [10, 20, 30, 40] 

# modularization is done by 
# functional approach 
def sum_the_list(mylist): 
	res = 0
	for val in mylist: 
		res += val 
	return res 

print(sum_the_list(mylist)) 

```
Note: Ba Informasaun liu tan bele hare iha link ne'e : https://www.geeksforgeeks.org/functional-programming-in-python/


## Paradigma programasaun Funcional

Paradigma programasaun funcional mak paradigma iha ne'ebé hotu-hotu iha estilo funsaun matematika puru. Konhesidu hanesan paradigma deklarativu tanba nia uza deklarasaun liu husi eskriptu. Nia uza funsaun matemátiku no trata kada eskriptu hanesan espressaun funsional hodi prodús valor. Funksaun lambda ka rekursaun mak abordajen báziku ne'ebé uza hodi implementa nia. Paradigma sira ne'ebé maka foku prinsipálmente iha "tanba sa mak rezolve" iha leten "tanba kona-ba resolução". Abilidade atu trata funsaun sira hanesan valor no pasu sira hanesan arguméntu halo kodigu sai hanesan ne'ebé bele loke no kompreende di'ak liu.

### Vantajens:

1. Fasil atu kompriende
2. Halo debugging no teste sai fasil liu
3. Hamoris komprensaun no lejibilidade kodigu nian



mylist = [11, 22, 33, 44] 

# Recursive Functional approach 
def sum_the_list(mylist): 
	
	if len(mylist) == 1: 
		return mylist[0] 
	else: 
		return mylist[0] + sum_the_list(mylist[1:]) 

# lambda function is used 
print(functools.reduce(lambda x, y: x + y, mylist)) 

```

Note: Ba Informasaun liu tan bele hare iha link ne'e : https://www.geeksforgeeks.org/functional-programming-in-python/
