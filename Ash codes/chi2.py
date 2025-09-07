import numpy as np
from scipy import stats

n = int(input("No. of categories: "))
obs = [float(input(f"Obs {i+1}: ")) for i in range(n)]
exp = [float(input(f"Exp {i+1}: ")) for i in range(n)]

chi2, p = stats.chisquare(obs, exp)

print("Chi2 =", round(chi2, 4), " p =", round(p, 4))
print("Result:", "Reject H0" if p < 0.05 else "Fail to Reject H0")
