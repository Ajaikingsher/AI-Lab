scores = list(map(int, input("Enter scores separated by space: ").split()))
n = len(scores)

mean = sum(scores) / n

scores.sort()
if n % 2 == 0:
    median = (scores[n//2 - 1] + scores[n//2]) / 2
else:
    median = scores[n//2]

maximum = max(scores)
minimum = min(scores)

total = 0
for s in scores:
    total += (s - mean) ** 2
std_dev = (total / n) ** 0.5

grades = []
for s in scores:
    if s >= 90:
        grades.append('A')
    elif s >= 80:
        grades.append('B')
    elif s >= 70:
        grades.append('C')
    elif s >= 60:
        grades.append('D')
    else:
        grades.append('F')

print("\n--- Results ---")
print("Mean:", round(mean, 2))
print("Median:", median)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Standard Deviation:", round(std_dev, 2))

print("\n--- Grades ---")
for i in range(n):
    print("Student", i+1, ": Score =", scores[i], ", Grade =", grades[i])
