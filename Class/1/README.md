# Konseitu baziku 
```python
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
    # Definisaun class Hero. Class ne'e serve nudar template ba object hero sira.
    # 'pass' signifika katak class ne'e laiha konteudu ka funsaun ruma iha momentu ne'e.

hero1 = Hero()  #Object/Instance
hero2 = Hero()
hero3 = Hero()
# Kria object sira husi class Hero. Cada object representa hero ida-idak.

hero1.name = "sniper"
hero1.health = 100
# Defini atributu 'name' ho 'health' ba hero1. Naran hero1 sniper ho saude 100.

hero2.name = "sven"
hero2.health = 200
# Defini atributu 'name' ho 'health' ba hero2. Naran hero2 sven ho saude 200.

hero3.name = "kharu"
hero3.health = 1000
# Defini atributu 'name' ho 'health' ba hero3. Naran hero3 kharu ho saude 1000.

#Atu print sai hero 1 ne'e object ka lae?
print(hero1)
# Printa referencia ba object hero1. Ne'e sei mostra lokasi memoria ne'ebe object ne'e aloja.

#Atu print sai saida deit mak hero ne'e iha
print(hero1.__dict__)
# Printa dicionario ne'ebe representa atributu sira ne'ebe hero1 iha. Ne'e hanesan forma ida atu haree atributu sira ne'ebe object ida iha.

```