# Given mappings:
# E (4) → B (1)
# T (19) → U (20)

P1, C1 = 4, 1
P2, C2 = 19, 20

# Solve for a
diffC = (C2 - C1) % 26
diffP = (P2 - P1) % 26

for a in range(26):
    if (a * diffP) % 26 == diffC:
        break

# Solve for b
b = (C1 - a * P1) % 26

print("a =", a)
print("b =", b)
