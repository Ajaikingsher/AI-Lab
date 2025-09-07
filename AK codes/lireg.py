import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    'Hours_Studied': [5, 3, 8, 2, 7, 4],
    'Attendance': [1, 1, 1, 0, 1, 0],
    'Passed': [1, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

X = df[['Hours_Studied', 'Attendance']]
y = df['Passed']

model = LogisticRegression()
model.fit(X, y)

print("\n--- Predict Student Performance ---")
try:
    hrs = float(input("Enter hours studied: "))
    att = int(input("Enter attendance (1=Present, 0=Absent): "))

    user_input = pd.DataFrame([[hrs, att]], columns=['Hours_Studied', 'Attendance'])
    prediction = model.predict(user_input)

    if prediction[0] == 1:
        print("Prediction: The student is likely to PASS.")
    else:
        print("Prediction: The student is likely to FAIL.")
except ValueError:
    print("Invalid input! Please enter numeric values only.")
