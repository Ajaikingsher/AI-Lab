import pandas as pd

df = pd.read_csv("C:/Users/Admin/Downloads/test.csv")

df.fillna(0, inplace=True)

report = df.pivot_table(index='Region', values='Sales', aggfunc='sum')

print("\n--- Sales Report by Region ---")
print(report)

