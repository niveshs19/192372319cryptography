key = "keyword"
text = "playfairexample"

# Remove j and duplicates, build 5x5 matrix
key = key.replace("j", "i")
matrix = []
for c in key + "abcdefghijklmnopqrstuvwxyz":
    if c not in matrix and c != "j":
        matrix.append(c)
matrix = [matrix[i*5:(i+1)*5] for i in range(5)]

def pos(ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

# Prepare pairs
pairs = []
i = 0
while i < len(text):
    a = text[i]
    b = text[i+1] if i+1 < len(text) else "x"
    if a == b:
        pairs.append(a + "x")
        i += 1
    else:
        pairs.append(a + b)
        i += 2

# Encrypt
cipher = ""
for p in pairs:
    r1, c1 = pos(p[0])
    r2, c2 = pos(p[1])

    if r1 == r2:  # same row
        cipher += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2:  # same column
        cipher += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:  # rectangle
        cipher += matrix[r1][c2] + matrix[r2][c1]

print("Key       :", key)
print("Plaintext :", text)
print("Ciphertext:", cipher)
