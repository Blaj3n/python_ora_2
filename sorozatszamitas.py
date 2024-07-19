szam1 = 0
for i in range(1, 101):
    szam1 += i # szam1 = szam1 + i
print("A számok összege: ", szam1)
print(f"A számok összege: {szam1} ") # ez a kettő sor teljesen ugyanaz, csak
# a második kicsit formázhatóbb.

szam2 = 1
for i in range(1, 101, 1): # [x, y[
    szam2 *= i # szam2 = szam2 * i
print("A számok szorzata: ", szam2)

szamlista = [1, 5, 4, 3, 7, 8, 8, 9, -5, 4, 5]

szam3 = 0
for elem in szamlista:
    szam3 += elem
print("A számlista összege: ", szam3)