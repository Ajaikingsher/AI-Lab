import numpy as np
from scipy import stats

data = list(map(float, input("Enter sample data: ").split()))
popmean = float(input("Enter population mean: "))
alpha = float(input("Enter alpha: "))

t, p = stats.ttest_1samp(data, popmean)

print("t =", round(t, 4), " p =", round(p, 4))
print("Result:", "Reject H0" if p < alpha else "Fail to Reject H0")
