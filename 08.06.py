
class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def atbulai(self):
        return self.tekstas[::-1]

    def mažosiomis(self):
        return self.tekstas.lower()

    def didžiosiomis(self):
        return self.tekstas.upper()

    def eiles_numeris(self, numeris):
        return self.tekstas.split()[numeris - 1]

    def zodziai(self, zodis):
        return self.tekstas.count(zodis)

    def pakeisti(self, senas, naujas):
        return self.tekstas.replace(senas, naujas)

    def statistika(self):
        zodziu_kiekis = len(self.tekstas.split())

        skaiciai = 0
        didziosios = 0
        mazosios = 0

        for simbolis in self.tekstas:
            if simbolis.isdigit():
                skaiciai += 1
            if simbolis.isupper():
                didziosios += 1
            if simbolis.islower():
                mazosios += 1

        return zodziu_kiekis, skaiciai, didziosios, mazosios


sakinys1 = Sakinys("Labas rytas")
sakinys2 = Sakinys("Labas rytas Lietuva")
sakinys3 = Sakinys("Labas rytas Labas")
sakinys4 = Sakinys("Labas123")

print(sakinys1.atbulai())
print(sakinys1.mažosiomis())
print(sakinys1.didžiosiomis())
print(sakinys2.eiles_numeris(2))
print(sakinys3.zodziai("Labas"))
print(sakinys3.pakeisti("Labas rytas", "Sveikas"))
print(sakinys4.statistika())














