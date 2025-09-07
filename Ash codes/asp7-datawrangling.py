import pandas as pd
df = pd.read_csv(r"C:\Users\USER\OneDrive\Desktop\python asp.csv")

df.fillna(0, inplace=True)

report = df.pivot_table(index='Region', values='Sales', aggfunc='sum')

print("--- Sales Report by Region ---")
print(report)



#csv text
Region,Sales
East,2000
North,2000
South,3700
West,3700