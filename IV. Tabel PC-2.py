# Tabel PC-2
pc2_table = [
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Fungsi untuk melakukan permutasi PC-2
def permute_pc2(cndn):
    k = ""
    for index in pc2_table:
        k += cndn[index - 1]
    return k

# Contoh penggunaan untuk C1D1
c1d1 = "00000001111111100000000000001101001001100001011000011001"
k1 = permute_pc2(c1d1)
print("K1 =", k1)

c2d2 = "00000011111111000000000000001010010011000010110000110011"
k2 = permute_pc2(c2d2)
print("K2 =", k2)

c3d3 = "00001111111100000000000000001001001100001011000011001110"
k3 = permute_pc2(c3d3)
print("K3 =", k3)

c4d4 = "00111111110000000000000000000100110000101100001100111010"
k4 = permute_pc2(c4d4)
print("K4 =", k4)

c5d5 = "11111111000000000000000000000011000010110000110011101001"
k5 = permute_pc2(c5d5)
print("K5 =", k5)

c6d6 = "11111100000000000000000000111100001011000011001110100100"
k6 = permute_pc2(c6d6)
print("K6 =", k6)

c7d7 = "11110000000000000000000011110000101100001100111010010011"
k7 = permute_pc2(c7d7)
print("K7 =", k7)

c8d8 = "11000000000000000000001111110010110000110011101001001100"
k8 = permute_pc2(c8d8)
print("K8 =", k8)

c9d9 = "10000000000000000000011111110101100001100111010010011000"
k9 = permute_pc2(c9d9)
print("K9 =", k9)

c10d10 = "00000000000000000001111111100110000110011101001001100001"
k10 = permute_pc2(c10d10)
print("K10 =", k10)

c11d11 = "00000000000000000111111110001000011001110100100110000101"
k11 = permute_pc2(c11d11)
print("K11 =", k11)

c12d12 = "00000000000000011111111000000001100111010010011000010110"
k12 = permute_pc2(c12d12)
print("K12 =", k12)

c13d13 = "00000000000001111111100000000110011101001001100001011000"
k13 = permute_pc2(c13d13)
print("K13 =", k13)

c14d14 = "00000000000111111110000000001001110100100110000101100001"
k14 = permute_pc2(c14d14)
print("K14 =", k14)

c15d15 = "00000000011111111000000000000111010010011000010110000110"
k15 = permute_pc2(c15d15)
print("K15 =", k15)

c16d16 = "00000000111111110000000000001110100100110000101100001100"
k16 = permute_pc2(c16d16)
print("K16 =", k16)