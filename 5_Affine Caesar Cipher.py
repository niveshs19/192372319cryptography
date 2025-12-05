import math

# Affine encryption
def affine_encrypt(text, a, b):
    result = ""
    for ch in text.lower():
        if ch.isalpha():
            p = ord(ch) - ord('a')
            c = (a * p + b) % 26
            result += chr(c + ord('a'))
        else:
            result += ch
    return result

# Affine decryption
def affine_decrypt(cipher, a, b):
    result = ""
    # modular inverse of a mod 26
    a_inv = pow(a, -1, 26)
    for ch in cipher.lower():
        if ch.isalpha():
            c = ord(ch) - ord('a')
            p = (a_inv * (c - b)) % 26
            result += chr(p + ord('a'))
        else:
            result += ch
    return result

# Inputs (inside code)
text = "affine cipher"
a = 5
b = 8

enc = affine_encrypt(text, a, b)
dec = affine_decrypt(enc, a, b)

print("Plaintext :", text)
print("a =", a, " b =", b)
print("Encrypted :", enc)
print("Decrypted :", dec)
