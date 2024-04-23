from shoe import Shoe  # Importa klase Shoe husi ficheiru shoe

shoe_one = Shoe('brown', 7.5, 'sneaker', 110)  # Kria instansia shoe_one ho atributu sira: kór maron, numeru 7.5, tipu sneaker, no presu $110
shoe_two = Shoe('white', 4.5, 'flip-flop', 80)  # Kria instansia shoe_two ho atributu sira: kór branu, numeru 4.5, tipu flip-flop, no presu $80

print(shoe_one.color)  # Imprime kór husi shoe_one
print(shoe_one.price)  # Imprime presu husi shoe_one

shoe_two.change_price(90)  # Altera presu husi shoe_two ba $90
print(shoe_two.price)  # Imprime presu atualizado husi shoe_two

shoe_one.color = 'blue'  # Altera kór husi shoe_one ba azul
shoe_one.size = 5.0  # Altera numeru husi shoe_one ba 5.0
shoe_one.price = 78  # Altera presu husi shoe_one ba $78

print(shoe_two.discount(0.5))  # Imprime presu ho deskontu husi shoe_two (deskontu 50%)

discounted_price = shoe_two.discount(0.5)  # Kalkula no asina presu ho deskontu husi shoe_two ba variavel discounted_price
print("Discounted Price:", discounted_price)  # Imprime presu ho deskontu husi shoe_two
