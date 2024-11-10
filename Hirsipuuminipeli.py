import random

def hirsipuu():
    sanalista = ["ihminen", "koodikieli", "lepakko", "javascript", "videopeli", "steam", "numero", "kirja", "tietokone", "lopputyö", "tuberkuloosi", "haimasyöpä", "arvata", "joulu", "joululoma", "kesäloma"]
    oikea_sana = random.choice(sanalista).lower()
    arvattu_sana = ['_'] * len(oikea_sana)
    yritykset = 8
    arvatut_kirjaimet = []

    print("Hirsipuu: Arvaa oikea sana!")
    print("Tämä sana on", len(oikea_sana), "kirjainta pitkä:", " ".join(arvattu_sana))

    while yritykset > 0 and '_' in arvattu_sana:
        arvaus = input("Arvaa kirjain: ").lower()

        if len(arvaus) != 1 or not arvaus.isalpha():
            print("Muista laittaa vain yksi kirjain.")
            continue

        if arvaus in arvatut_kirjaimet:
            print("Kirjain on jo arvattu")
            continue

        arvatut_kirjaimet.append(arvaus)

        if arvaus in oikea_sana:
            for i in range(len(oikea_sana)):
                if arvaus == oikea_sana[i]:
                    arvattu_sana[i] = arvaus
            print("Oikein! kirjain oli:", " ".join(arvattu_sana))
        else:
            yritykset -= 1
            print("Väärin! Sinulla on", yritykset, "yritystä jäljellä.")

    if '_' not in arvattu_sana:
        print("Oikein meni, sana oli:", oikea_sana)
        return "Voitto"
    else:
        print("Hävisit. Oikea sana oli:", oikea_sana)
        return "Häviö"
