import random

def piilotettu_sana_peli():
    sanalista = ["KONE", "PYTHON", "KOODI", "KOIRA", "KALA", "LUONTO", "JOULU", "KESÄ", "SYKSY"]
    valittu_sana = random.choice(sanalista)

    ruudukko = []
    for _ in range(6):
        rivi = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6)]
        ruudukko.append(rivi)

    r = random.randint(0, 5)

    max_sarakkeet = 6 - len(valittu_sana)
    if max_sarakkeet < 0:
        max_sarakkeet = 0
    c = random.randint(0, max_sarakkeet)

    ruudukko[r][c:c + len(valittu_sana)] = list(valittu_sana)
    sanan_sijainti = (r, c)

    print("Löydä sana ruudukosta:")
    for rivi in ruudukko:
        print(" ".join(rivi))

    arvaus = input("\nArvaa sana: ")

    if arvaus.upper() == valittu_sana:
        print("Arvasit oikein.")
        return "Voitto"
    else:
        print(f"Väärin! '{arvaus}' ei ollut oikea sana.")
        print("Oikea sana oli:", valittu_sana)
        print("Sana sijaitsi rivillä", sanan_sijainti[0] + 1)
        return "Häviö"
