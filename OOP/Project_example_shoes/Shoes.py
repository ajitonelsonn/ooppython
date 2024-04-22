#Object-Oriented Programming (OOP) Vocabulary
#Class
#Remember that a class represents a blueprint.
#mak hanesan blueprint ne'ebe konsiste methods no attributes.
#Object
# instance class nian. Ida ne'e bele ajuda hodi hanoin objectu sira iha real world hanesan: a yellow pencil, a small dog, a yellow shoe, etc. Objectu bele iha abstract barak.
#Attribute
#hanesan descriptor ka characteristic. Exemplu hanesan colour, length, size, etc. Atributtu sira ne'e bele foti valor espesifiku sira hanesan  blue, 3 inches, large, etc.
#Method
#ne hanesan aksaun ne'ebe mak class ka objetu sei eble foti.



#1. Iha ne'e ita sei halo class ho naran sapatu. Class iha nia atribute sira mak hanesan kor, foli, medida,style
class Sapatu:
    def __init__(self, kor, folin, medida, style):
        self.kor = kor
        self.folin = folin  # Assuming folin is meant to be the price
        self.medida = medida
        self.style = style        
        
#Python uza __init__ atu kria objetu sapatu espesífiku. 
# Iha parte seluk, varivél self bele hanesan tricky atu kompriende iha inísio. 
# self guarda atributu sira hanesan kór, medida, no seluk tan, hodi hateten katak atributu sira ne'e disponível iha hela klasse Sapatu. 
#essentially self hanesan dictionary ne'ebe holds ita nia atribute sira hotu no attribute values moss.


#Anota katak troka folin ho metodu diskontu ne’e em geral hanesan python function. 
# Contohnya, python function laiha return buat ruma, tan ne’e troka folin metodu, ida ne’e la return buat ruma. 
# Ida ne’e so deit troka value iha atributu folin nian. Metodu diskontu, no entantu, nia return buat ruma, return ida ne’e mak hanesan presu diskontu.


#Additional: Function vs Method
#Function no method ne’e similar liu, rua ne’e  uza keyword ne’ebe hanesan. 
# Sira moss iha inputs no return outputs. 
# Nia kontrariu mak method ne’e iha class nia laran, iha ne’ebe function ne’e laos iha class nia laran or outside.


#2. Nia moss iha metodu troka_folin, no metodu ida ne'e nia output mk hanesan folin diskontu nian
# Ita checout methodu troka folin hodi hare tok oinsa self ne'e servisu.

    def troka_folin(self, folin_foun):
        self.folin = folin_foun

    def discount(self, discount_rate):
        discounted_folin = self.folin * (1 - discount_rate)
        self.folin = discounted_folin  # Update the folin attribute to reflect the discounted price
        return discounted_folin
    
#Ita tama liu ba self-variable
#Karik ita define objetu rua, oinsa python bele halo differensia objetu rua ne’e?
# Tan ne’e iha ne’ebe self-mai iha play. 
# Karik ita bolu troka_folin metodu  iha shoe_one, oinsa python bele hatene no muda price ba shoe one laos shoe 2?

shoe_one = Sapatu('brown', 110, '7.5', 'sneaker')  # Assuming the third parameter is the size and the fourth is the price
shoe_two = Sapatu('white', 80, '4.5', 'flip-flop')

print(f"Folin Pertama: {shoe_one.folin}")

shoe_one.troka_folin(100)  # Assuming this is meant to change the price to 100

print(f"Troka folin: {shoe_one.folin}")

#halo fali diskontu moss
# Apply a 50% discount and print the discounted price
discounted_price = shoe_one.discount(0.5)  # Assuming the discount rate is 0.5 for 50%

print(f"Troka folin + discontu: {discounted_price}")


#self dehan ba python iha ne’ebe hodi hare ba computer’s memory ba shoe_one object,
#  no depois python troka presu  ba shoe_one object.
#  Bainhira ita bolu troka_presu method, shoe_one.change_price(125), self sei implikamente passa
