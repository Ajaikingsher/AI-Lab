from sklearn.linear_model import LogisticRegression

X = [[5, 40], [2, 20], [8, 45], [1, 10], [6, 35], [3, 25]]
y = [1, 0, 1, 0, 1, 0]

model = LogisticRegression()
model.fit(X, y)

hours = float(input("Enter hours studied: "))
classes = int(input("Enter number of classes attended: "))

prediction = model.predict([[hours, classes]])[0]

if prediction == 1:
    print("Prediction: PASS ✅")
else:
    print("Prediction: FAIL ❌")
