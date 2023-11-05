# Vektor R16 dan L16
R16 = "01011011100101110110010100100001"
L16 = "10000101000110101110001110100111"

# Tabel Inverse Initial Permutation (IP-1)
ip1_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Gabungkan R16 dan L16
merged = R16 + L16

# Permutasi akhir dengan tabel IP-1
final_permuted = ""
for position in ip1_table:
    final_permuted += merged[position - 1]

# Konversi vektor hasil akhir ke format heksadesimal
cipher_hex = hex(int(final_permuted, 2))[2:]  # Mengabaikan "0x" di awal heksadesimal

# Output vektor hasil akhir dan cipher dalam format heksadesimal
print("Hasil Akhir (IP-1):", final_permuted)
print("Cipher (HEX):", cipher_hex)