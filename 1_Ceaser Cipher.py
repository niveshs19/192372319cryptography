text = "HELLO"
k = 3

result = ""
for c in text:
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        result += chr((ord(c) - base + k) % 26 + base)
    else:
        result += c

print("Text:", text)
print("Shift:", k)
print("Encrypted:", result)
