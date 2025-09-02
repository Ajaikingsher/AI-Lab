import collections
import collections.abc

# Patch for Python 3.10+ compatibility (fixes kanren/unification issues)
collections.Iterator = collections.abc.Iterator
collections.Hashable = collections.abc.Hashable
collections.Mapping = collections.abc.Mapping
collections.MutableMapping = collections.abc.MutableMapping

from kanren import Relation, facts, run, var, conde

doctor, treats = Relation(), Relation()

facts(doctor, ("dr_smith",), ("dr_jones",), ("dr_lee",), ("dr_williams",), ("dr_davis",))
facts(treats,
    ("dr_smith", "flu"), ("dr_smith", "allergy"),
    ("dr_jones", "cold"),
    ("dr_lee", "covid"), ("dr_lee", "pneumonia"),
    ("dr_williams", "diabetes"),
    ("dr_davis", "hypertension")
)

def is_skilled(p):
    return conde((doctor(p), treats(p, var())),)

q = input("Enter query: ").strip().lower()
x = var(); skilled = run(0, x, is_skilled(x))

if q.startswith("who"):
    print("✓ Skilled doctors:") if skilled else print("X None found.")
    for s in skilled:
        print("-", s.replace("_", " ").title())
elif q.startswith("is"):
    name = q.replace("?", "").split()[1]
    print(f"✓ Yes, {name.title()} is skilled.") if name in skilled else print(f"X No, {name.title()} is not skilled.")
else:
    print("X Invalid query.")
