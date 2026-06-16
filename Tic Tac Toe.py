# Updated project
# Second commit

lenta = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
dabartinis_zaidejas = "X"


def rodyti_lenta():
    print(lenta[0], "|", lenta[1], "|", lenta[2])
    print("---------")
    print(lenta[3], "|", lenta[4], "|", lenta[5])
    print("---------")
    print(lenta[6], "|", lenta[7], "|", lenta[8])

def ar_yra_laimetojas():
    if lenta[0] == lenta[1] == lenta[2] and not lenta [0].isdigit():
        return True
    if lenta[3] == lenta[4] == lenta[5] and not lenta [3].isdigit():
        return True
    if lenta[6] == lenta[7] == lenta[8] and not lenta [6].isdigit():
        return True
    if lenta[0] == lenta[3] == lenta[6] and not lenta[0].isdigit():
        return True
    if lenta[1] == lenta[4] == lenta[7] and not lenta[1].isdigit():
        return True
    if lenta[2] == lenta[5] == lenta[8] and not lenta[2].isdigit():
        return True
    if lenta[0] == lenta[4] == lenta[8] and not lenta[0].isdigit():
        return True
    if lenta[2] == lenta[4] == lenta[6] and not lenta[2].isdigit():
        return True

    return False

def ar_lygiosios():
    for langelis in lenta:
        if langelis.isdigit():
            return False

    return True

rodyti_lenta()

while True:

    print("Dabar žaidžia:", dabartinis_zaidejas)
    pasirinkimas = input("Pasirinkite skaičių nuo 1 iki 9: ")

    if not pasirinkimas.isdigit():
        print("Iveskite skaiciu!")
        continue

    pasirinkimas = int(pasirinkimas)

    if pasirinkimas < 1 or pasirinkimas > 9:
        print("Neteisingai ivestas skaicius!")
        continue

    indeksas = pasirinkimas - 1
    print("Jūs pasirinkote: ", pasirinkimas)

    if lenta[indeksas].isdigit():
        lenta[indeksas] = dabartinis_zaidejas

        rodyti_lenta()

        if ar_yra_laimetojas():
            print(dabartinis_zaidejas, "Laimėjo!")
            break

        if ar_lygiosios():
            print("Lygiosios!")
            break

        if dabartinis_zaidejas == "X":
            dabartinis_zaidejas = "O"

        else:
            dabartinis_zaidejas = "X"
    else:
        print("Ši vieta užimta!")
