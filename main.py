def vytvor_utulek():
    return {}

def pridej_zvire(utulek, jmeno, druh, vek):
    utulek[jmeno] = {"druh": druh, "vek": vek}

def vypis_zvirata(utulek):
    for jmeno, info in utulek.items():
        druh = info["druh"]
        vek = info["vek"]
        if vek == 1:
            print(f"{jmeno} je {druh} a je mu {vek} rok.")
        elif 2 <= vek <= 4:
            print(f"{jmeno} je {druh} a jsou mu {vek} roky.")
        else:
            print(f"{jmeno} je {druh} a je mu {vek} let.")

utulek = vytvor_utulek()
pridej_zvire(utulek, "Míca", "kočka", 3)
pridej_zvire(utulek, "Baryk", "pes", 5)
pridej_zvire(utulek, "Fido", "králík", 1)
vypis_zvirata(utulek)