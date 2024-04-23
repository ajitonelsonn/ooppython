class Shoe:
    # Klase Shoe ne'e define propriedades no metodus ba sapatu

    def __init__(self, shoe_color, shoe_size, shoe_style, shoe_price):
        # Metodu inisializasaun ne'e kria instansia sapatu ho atributus sira
        self.color = shoe_color  # Define kór sapatu
        self.size = shoe_size  # Define tamañu sapatu
        self.style = shoe_style  # Define estilu sapatu
        self.price = shoe_price  # Define presu sapatu
    
    def change_price(self, new_price):
        # Metodu ne'e muda presu sapatu ho formula ida
        self.price = 0.81 * new_price  # Muda presu sapatu ho deskontu 19%
        
    # def discount(self, discount):
    #     # Metodu ne'e kalkula presu sapatu depois de deskontu
    #         self.diskontu=self.price * (1 - discount)  # Retorna presu sapatu depois de deskontu
    #         self.price = self.diskontu
    #         return self.diskontu


    def discount(self, diskontu):
        # Metodu ne'e kalkula presu sapatu ho diskontu nian
        return self.price * (1 - diskontu)  # Aplika diskontu ba presu sapatu no retorna valor ne'e
