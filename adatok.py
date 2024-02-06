from Szamitogep import Szamitogep


def peldanyositas():
    peldany1 = Szamitogep("win", 32)
    peldany2 = Szamitogep("mac", 16)
    peldany3 = Szamitogep("win", 16)
    szamitogepek = []
    szamitogepek.append(peldany1)
    szamitogepek.append(peldany2)
    szamitogepek.append(peldany3)

    return szamitogepek

def listakiiras(lista):
    for i in range(len(lista)):
        oprsz = lista[i].oprsz
        ram = lista[i].ram
        print(f"{oprsz} ({ram} ")

# ez a rövid verzió
# listakiiras(peldanyositas())


# hosszabb verzió
# gepeklistaja = peldanyositas()
# listakiiras(gepeklistaja)


# összegzés tétele
def osszegzes(szamitogepek):
    print("Átlag: ", end="")
    gyujto = 0
    for i in range(len(szamitogepek)):
        gyujto += szamitogepek[i].ram
    print(round(gyujto / len(szamitogepek), 3))


# maximum kiválasztás tétele
def maximum(szamitogepek):
    print("Legöbb ramot tartalmazó oprendszer: ", end="")
    index = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[i].ram > szamitogepek[index].ram:
            index = i
    print(szamitogepek[index].oprsz)


# megszámlálás tétele
def megszamlalas(szamitogepek):
    print("Hány windows-os gépünk van?", end="")
    gyujto = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[i].oprsz == "win":
            gyujto += 1

    print(f" {gyujto}db ")


# eldöntés tétele
def eldontes(szamitogepek):
    vizsgaltram = 48
    print(f"Van-e {vizsgaltram} GB-nál nagyobb windows?: ", end="")
    van = False
    for i in range(len(szamitogepek)):
        if szamitogepek[i].ram > vizsgaltram and szamitogepek[i].oprsz == "win":
            van = True

    if van == True:
        print("Van ilyen gép")
    else:
        print("Nincs ilyen gép")


gepeklistaja = peldanyositas()
listakiiras(gepeklistaja)
osszegzes(gepeklistaja)
maximum(gepeklistaja)
megszamlalas(gepeklistaja)
eldontes(gepeklistaja)
