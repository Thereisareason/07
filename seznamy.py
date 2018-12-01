zvirata = ["pes", "kočka", "králík", "had"]
mensi_zvirata = []



def zvire_mensi_nez_pet(zvirata):
    for zvire in zvirata:
        if (len(zvire) < 5):
            mensi_zvirata.append(zvire)
    return mensi_zvirata

print(zvire_mensi_nez_pet(zvirata))
