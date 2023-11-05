# Tabel Ekspansi
expansion_table = [
    32,  1,  2,  3,  4,  5,  4,  5,
     6,  7,  8,  9,  8,  9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32,  1
]

# Fungsi untuk melakukan Ekspansi
def expansion(data32):
    expanded_data = ""
    for index in expansion_table:
        expanded_data += data32[index - 1]
    return expanded_data

# Fungsi untuk melakukan XOR antara dua bitstring
def xor(bitstring1, bitstring2):
    result = ""
    for b1, b2 in zip(bitstring1, bitstring2):
        result += '1' if b1 != b2 else '0'
    return result

# Input Data R1-R16
Ri = "10000101000110101110001110100111"

# Input Kunci K1-K16
keys = "101000001001001000100010001010110111001001000110"

# Lakukan Ekspansi pada Ri
expanded_R = expansion(Ri)


# XOR dengan kunci Ki
Ai = xor(expanded_R, keys)


# Tampilkan hasil pada setiap iterasi
print(f"Ekspansi dari Ri = {expanded_R}")
print(f"Vektor Matriks Ai = {Ai}")
print()


