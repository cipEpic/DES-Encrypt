# kemudian B1 dipermutasi menggunakan matriks permutasi dan menjadi P(B1)

# Vektor Bi (B1-B16)
Bi = "01011101100111001111011100111010"

# Tabel P-Box
p_box = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# Buat vektor hasil setelah permutasi P-Box
B_permuted = ""
for position in p_box:
    B_permuted += Bi[position - 1]

# Output vektor Bi setelah permutasi P-Box
print("Vektor Bi setelah permutasi P-Box:", B_permuted)