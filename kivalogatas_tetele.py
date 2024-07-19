szamlista = [1, 5, 4, 3, 7, 8, 8, 9, -5, 4, 5]
paros_szamok = []
paratlan_szamok = []

print(f"A számlista páros számai: ", end="") # end="" az egyik printhez hozzácsatolja a következőt.
for i in range(0, len(szamlista)):
    if szamlista[i] % 2 == 0: # ez a mondat magyarul úgy hangzik, hogy ha a szamlistáNAK az i-edik eleme osztható 2-vel 0 maradékkal, akkor...
        paros_szamok.append(szamlista[i])
print(paros_szamok)

print(f"A számlista páratlan számai: ", end="")
for i in range(0, len(szamlista)):
    if szamlista[i] % 2 == 1:
        paratlan_szamok.append(szamlista[i])
print(paratlan_szamok)

# az osztással kapcsolatban kérdeztél. Jogos.
# MOD: %, y % x = z, ez az előbbi maradékos osztást jelenti,
# (példán keresztül) ha y osztható x-szel z maradékot ad.
#
# DEV: //, egész osztás, azaz -> x // 2 -> ez azt jelenti nekünk,
# hogy az x-et el fogja úgy osztani kettővel, hogy egész számot ad vissza. 9 // 2 => 4
#
# Osztás: /, ez a sima osztás jel, szimplán eloszt egy számot.
#
# Kerekíteni akarunk, akkor a round()-ot használjuk.