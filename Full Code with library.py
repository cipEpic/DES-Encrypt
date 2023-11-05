from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Convert the plaintext and key to binary
plaintext = "DOMISILI".encode('utf-8')
key = "CAPSLOCK".encode('utf-8')

# Ensure that the key is 8 bytes long (DES key length)
if len(key) != 8:
    raise ValueError("The key must be 8 bytes long.")

# Initialize the DES cipher with ECB mode
cipher = DES.new(key, DES.MODE_ECB)

# Pad the plaintext if needed (DES requires input to be a multiple of 8 bytes)
block_size = DES.block_size
if len(plaintext) % block_size != 0:
    plaintext += b' ' * (block_size - len(plaintext) % block_size)

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Convert the ciphertext to a hexadecimal string
ciphertext_hex = ciphertext.hex()

# Convert the ciphertext to binary
ciphertext_binary = ''.join(f'{byte:08b}' for byte in ciphertext)

# Output the encrypted ciphertext in hexadecimal format
print("Encrypted Text (HEX):", ciphertext_hex)

# Output the encrypted ciphertext in binary format
print("Encrypted Text (Binary):", ciphertext_binary)