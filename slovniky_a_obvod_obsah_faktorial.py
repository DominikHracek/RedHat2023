def obvod(strana_a):
    print(f"Obvod ctverce je: {4*strana_a}")

def obsah(strana_a):
    print(f"Obsah ctverce je: {strana_a**2}")

def faktorial(cislo_na_faktorial):
    faktorial = 1
    for i in range(1, cislo_na_faktorial+1):
        faktorial *= i
    print(f"Faktorial čísla {cislo_na_faktorial} je: {faktorial}")

def main(parametr):
    obvod(parametr)
    obsah(parametr)
    faktorial(parametr)

parametr = int(input("S jakým číslem chceš počítat: "))
main(parametr)

slovnik = {}

pocet_cisel_ve_slovniku = int(input("Kolik čísel ve slovníku: "))
for i in range(pocet_cisel_ve_slovniku):
    key = input("Key: ")
    value = float(input("Value: "))
    slovnik[key] = value

soucet = 0
for key, value in slovnik.items():
    soucet += value
print(soucet)