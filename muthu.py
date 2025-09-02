def implies(p, q):
    return (not p) or q

def iff(p, q):
    return p == q

A, B, C = True, False, True

print("A ∧ ¬C =", A and not C)
print("(A ∨ B) ∧ C =", (A or B) and C)
print("¬B ∨ A =", (not B) or A)
print("A → C =", implies(A, C))
print("B ↔ C =", iff(B, C))
