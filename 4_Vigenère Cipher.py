plain = "this is a secret"
key = "key"

# Repeat key to match plaintext length
full_key = (key * (len(plain)//len(key) + 1))[:len(plain)]

# Encrypt
enc = ""
for p, k in zip(plain, full_key):
    if p.isalpha():
        base = ord('a')
        enc += chr((ord(p) - base + (ord(k) - base)) % 26 + base)
    else:
        enc += p

# Decrypt
dec = ""
for c, k in zip(enc, full_key):
    if c.isalpha():
        base = ord('a')
        dec += chr((ord(c) - base - (ord(k) - base)) % 26 + base)
    else:
        dec += c

print("Plaintext :", plain)
print("Key       :", key)
print("Encrypted :", enc)
print("Decrypted :", dec)
