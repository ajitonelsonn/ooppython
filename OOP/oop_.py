#Konseitu baziku
#Programming paradigma >> cara berpikir
#Structural > Procedural - Programing - Di esekusi berdasarkan urutan --Serial
#Object > Oriented - Programing - Semua di angaap object/instanse - karik buat n'ebe hanesan ita halo template or class

# Object-Oriented Programming

#Ezemplu class hero: 
#Tamba nia nu'dar template entaun nia iha valor rua mak hanesan:
#1. atrribute hanesan "Ne'ebe hero iha": naran, power, deffence
#2. Method "mak ida ne'ebe hero bele halo" : meneyerang, bertahan, begerak


#Pois berdasarkan template iha leten ne'e agora ita halo object
#object sei foti iha leten

class Hero: #template
    pass


hero1 = Hero()  #Object/Instance
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "kharu"
hero3.health = 1000

#Atu print sai hero 1 ne'e object ka lae?
print(hero1)
#Atu print sai saida deit mak hero ne'e iha
print(hero1.__dict__)

