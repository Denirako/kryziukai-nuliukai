
class Automobilis:

    def __init__(self, metai, modelis, variklis):
        self.metai = metai
        self.modelis = modelis
        self.variklis = variklis

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti(self):
        print("Degalai įpilti")

class Elektromobilis(Automobilis):

    def pildyti(self):
        print("Baterija įkrauta")

    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")


audi = Automobilis(2020, "Audi A6", "Diesel")
tesla = Elektromobilis(2024, "Tesla", "Electric")

audi.vaziuoti()
audi.stoveti()
audi.pildyti()

tesla.vaziuoti()
tesla.stoveti()
tesla.pildyti()
tesla.vaziuoti_autonomiskai()