zvirata = ["pes", "kočka", "králík", "had"]

def zvire_zacinajici_k(zvirata):
    k_zvirata = []
    for zvire in zvirata:
        if "k" in zvire[0]:
            k_zvirata.append(zvire)
    return k_zvirata

print(zvire_zacinajici_k(zvirata))
