keyword = "CIPHER".lower()
plain = "abcdefghijklmnopqrstuvwxyz"

# Build cipher alphabet from keyword
cipher = ""
for c in keyword:
    if c not in cipher:
        cipher += c

for c in plain:
    if c not in cipher:
        cipher += c

print("Plain  :", plain)
print("Cipher :", cipher)


# Encryption
def encrypt(text):
    result = ""
    for c in text.lower():
        if c in plain:
            result += cipher[plain.index(c)]
        else:
            result += c
    return result

# Decryption
def decrypt(text):
    result = ""
    for c in text.lower():
        if c in cipher:
            result += plain[cipher.index(c)]
        else:
            result += c
    return result


# Example
message = "attack at dawn"
enc = encrypt(message)
dec = decrypt(enc)

print("Message     :", message)
print("Encrypted   :", enc)
print("Decrypted   :", dec)
