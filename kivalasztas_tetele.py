szamlista = [1, 5, 4, 3, 7, 8, 8, 9, -5, 4, 5] # len = hosszúság, hány elemet tartalmaz a lista?

# a len mindig számot ad vissza, hisz arra vagyunk kíváncsiak,
# hogy hány elemet tartalmaz a lista
# azt csak is egy számmal tudjuk meghatározni.

# Az elem helye a listában: 3, az elem maga: 4.
# Az elem helye a listában: 10, az elem maga: 4.

index = 0
for elem in szamlista:
    index += 1
    if elem == 4:
        print(f"Az elem helye a listában: {index}, az elem maga: {elem}. ")

print()

# Ez a kiválasztás tétel:

print("Kiválasztás Tétel: ")
for i in range(0, len(szamlista)): # [[, len(szamlista) = 11, a range()-be csak szám kerülhet -> int
    if szamlista[i] == 4:
        print(f"Az elem helye a listában: {i + 1}, az elem maga: {szamlista[i]}. ")
# Ha egy feladatban azt látod, hogy az összeset jelenítse meg,
# akkor az esetek nagy százalékában ezt a fajta iterálást használjuk
print()
# És mi van, ha szigorúan csak egy adatra kiváncsi, tehát nem kell az összeset megjeleníteni, csak egyet?
print("Ez pedig csak egyet ír ki: [break] ")
for i in range(0, len(szamlista)): # [[, len(szamlista) = 11, a range()-be csak szám kerülhet -> int
    if szamlista[i] == 4:
        print(f"Az elem helye a listában: {i + 1}, az elem maga: {szamlista[i]}. ")
        break