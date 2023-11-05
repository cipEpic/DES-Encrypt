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

# Fungsi untuk melakukan fungsi F
def feistel_function(Ri, Ki):
    # Di sini Anda dapat menambahkan implementasi fungsi F yang sesuai dengan DES
    # Contoh sederhana: XOR antara Ri dan Ki
    return xor(Ri, Ki)

# Data awal (L0 dan R0)
L0 = "11111111101110000111011001010111"
R0 = "00000000000000000000011010000011"

# Kunci K1-K16 - Masukkan kunci Anda di sini (pastikan panjang 48 bit)
keys = [
    "000110110000001011101111111111000111000001110010",
    "011110011010111011011001110110111100100111100101",
    "010101011111110010001010010000101100111110011001",
    # Tambahkan kunci K2-K16 di sini
]

# Lakukan iterasi 16 kali
for i in range(16):
    # Lakukan Ekspansi pada Ri
    expanded_R = expansion(R0)

    # Hitung fungsi F
    F = feistel_function(R0, keys[i])

    # XOR dengan kunci Ki
    Ai = xor(expanded_R, keys[i])

    # Hitung Li+1 = R0 dan Ri+1 = Li XOR F
    Li = R0
    Ri = xor(L0, F)

    # Tampilkan hasil pada setiap iterasi
    print(f"Iterasi {i + 1}:")
    print(f"Li = {Li}")
    print(f"Ri = {Ri}")
    print(f"Ekspansi dari Ri = {expanded_R}")
    print(f"Vektor Matriks Ai = {Ai}")
    print()

    # R0 dan L0 menjadi Li dan Ri untuk iterasi berikutnya
    L0, R0 = Li, Ri
