# Tabel PC-1
pc1_table = [
    57,  49,  41,  33,  25,  17,   9,
     1,  58,  50,  42,  34,  26,  18,
    10,   2,  59,  51,  43,  35,  27,
    19,  11,   3,  60,  52,  44,  36,
    63,  55,  47,  39,  31,  23,  15,
     7,  62,  54,  46,  38,  30,  22,
    14,   6,  61,  53,  45,  37,  29,
    21,  13,   5,  28,  20,  12,   4
]

# Fungsi untuk melakukan permutasi PC-1
def permute_pc1(key64):
    c0d0 = ""
    for index in pc1_table:
        c0d0 += key64[index - 1]
    return c0d0

# Contoh penggunaan
key64 = "0100001101000001010100000101001101001100010011110100001101001011"
c0d0 = permute_pc1(key64)
print("C0D0 =", c0d0)
