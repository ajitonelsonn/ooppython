# Nota Sira Kona-ba Programasaun Orientadu ba Objeto
Agora, ita sei hakerek script Python ida ne'ebé separadu ne'ebé uza klase sapatu nian. Iha folder ne'ebé hanesan, presiza atu kria ficheiru ida seluk ne'ebé naran project.py. Iha ficheiru ne'e, ita  hakarak uza klase sapatu nian. Primeiru, ita presiza importa klase sapatu hosi nia hakerek from shoe import Shoe. Shoe ki'ik refere ba ficheiru shoe.py, entretantu shoe boot refere ba klase ne'ebé defini iha ficheiru ne'e.

### shoe.py
```python
class Shoe:

    def __init__(self, shoe_color, shoe_size, shoe_style, shoe_price):
        self.color = shoe_color
        self.size = shoe_size
        self.style = shoe_style
        self.price = shoe_price
    
    def change_price(self, new_price):
        self.price = 0.81 * new_price
        
    def discount(self, discount):
        return self.price * (1 - discount)
```
### project.py
```python

from shoe import Shoe

shoe_one = Shoe('brown', 7.5, 'sneaker', 110) 
shoe_two = Shoe('white', 4.5, 'flip-flop', 80)

print(shoe_one.color)
print(shoe_one.price)

shoe_two.change_price(90)
print(shoe_two.price)

shoe_one.color = 'blue'
shoe_one.size = 5.0
shoe_one.price = 78
```

Ita bele espesifika naran ficheiru no klase ho naran ne'ebé ita hakarak. Sira la'ós presiza atu hanesan. Ita  halo ida ne'e hanesan konveniénsia de'it. Agora, iha project.py, ita bele uza klase sapatu nian. Se ita  hatene, kodigu agora modulár ona. Ita sei hakerek kodigu ida ne'ebé uza klase sapatu nian.

Klase sapatu iha metodu ida atu muda presu sapatu nian. Iha ficheiru project.py, ita bele haree iha linha 9, shoe_two.change_price(90). Iha Python, ita mós bele muda valor atributu ho sintaxe tuir mai, shoe_one.color = ‘blue’, shoe_one.size = 5.0, no shoe_one.price = 78. Iha desvantajen balu kona-ba asesu atributu direitamente versus hakerek metodu ba asesu no hatudu atributu sira.

Iha termus programasaun orientadu ba objeto,
Regra Python nian la'ós hanesan ketat ho iha língua programasaun seluk. 
Iha língua sira hanesan C++, ita bele deklara ho explísitu se objetu ida bele muda ka asesu valor atributu direitamente. Python la iha opsaun ida ne'e.
Nia di'ak liu muda valor ho metodu se iha komparasaun ho muda valor direitamente.

Muda valor liuhosi metodu oferese ita flexibilidade liu iha tempu naruk. Maibé se unidade medida sira substitui, por exemplu, loja ne'e inicialmente hanesan atu servisu ho dólar Amerikanu no agora presiza atu funciona ho euro. Se ita muda atributu direitamente hanesan iha linha 14, se de'it de'it ita presiza uza euro, ita tenke muda ne'e manualmente. Ita tenke halo ne'e iha ne'ebé ita asesu atributu presu direitamente.

Se, iha parte seluk, ita uza metodu hanesan metodu muda presu, entaun ita presiza de'it ba klase sapatu no muda metodu orijinal ida de'it. Ita sei multiplika ho, por exemplu, 0.81 atu konverte husi dólar ba euro. Se ita fila fali ba project.py, linha hanesan número 9, ita b la presiza muda presu husi dólar ba euro manualmente tanba konversaun sei kuida ida ne'e ba ita iha klase sapatu.
