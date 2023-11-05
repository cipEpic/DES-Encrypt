# Tabel pergeseran bit 16 putaran
shift_table = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

# Fungsi untuk melakukan Left Shift pada C0 dan D0 untuk 16 putaran
def left_shift_16_rounds(c0d0):
    c0d0_shifted = c0d0
    c0, d0 = c0d0[:28], c0d0[28:]

    for round_number in range(1, 17):
        shift_amount = shift_table[round_number - 1]
        
        # Pergeseran bit sesuai dengan shift_amount
        c0 = c0[shift_amount:] + c0[:shift_amount]
        d0 = d0[shift_amount:] + d0[:shift_amount]
        
        c0d0_shifted = c0 + d0
        print(f"C0D0 Shifted (Round {round_number}) =", c0d0_shifted)
    
    return c0d0_shifted

# Contoh penggunaan
c0d0 = "00000000111111110000000000001110100100110000101100001100"
final_c0d0 = left_shift_16_rounds(c0d0)
