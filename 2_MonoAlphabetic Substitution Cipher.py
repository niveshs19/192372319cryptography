plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "qwertyuiopasdfghjklzxcvbnm"   # key

text = "hello world"

# Encrypt
enc = ""
for c in text:
    enc += cipher[plain.index(c)] if c in plain else c

# Decrypt
dec = ""
for c in enc:
    dec += plain[cipher.index(c)] if c in cipher else c

print("Plain :", text)
print("Encrypted :", enc)
print("Decrypted :", dec)
