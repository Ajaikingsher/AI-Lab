import statistics as st

scores = list(map(int, input("Enter scores: (comma separated): ").split()))

mean = st.mean(scores)
median = st.median(scores)
minimum = min(scores)
maximum = max(scores)
std_dev = st.pstdev(scores)

def grade(s):
    if s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    elif s >= 70:
        return "C"
    elif s >= 60:
        return "D"
    else:
        return "F"

print("Mean:", round(mean, 2))
print("Median:", median)
print("Max:", maximum)
print("Min:", minimum)
print("Std Dev:", round(std_dev, 2))

for i, s in enumerate(scores, 1):
    print("Student", i, "Score:", s, "Grade:", grade(s))
