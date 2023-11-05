# Vektor P(Bi) (P(B1)-P(B16))
P_Bi = "00101111001011101111010111011010"

# Vektor Li-1 (L1-L16)
Li_1 = "01110100101110011001000011111011"


# Fungsi XOR antara dua vektor bit
def xor(bitstring1, bitstring2):
    result = ""
    for b1, b2 in zip(bitstring1, bitstring2):
        result += '1' if b1 != b2 else '0'
    return result


# XOR P(Bi) dengan Li untuk mendapatkan Ri
R = xor(P_Bi, Li_1)

print(f"Print Ri = {R}")
print()