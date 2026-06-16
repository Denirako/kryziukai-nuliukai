import datetime


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo

    def skaiciuoti_dienas(self):
        siandien = datetime.datetime.today()
        skirtumas = siandien - self.dirba_nuo
        return skirtumas.days

    def paskaiciuoti_atlyginima(self):
        dienos = self.skaiciuoti_dienas()
        atlyginimas = dienos * 8 * self.valandos_ikainis
        return atlyginimas

class NormalusDarbuotojas(Darbuotojas):
    def skaiciuoti_dienas(self):
    if darbo_dienos += 1
        
