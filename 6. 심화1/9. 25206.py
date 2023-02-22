import sys

def gradeConversion(grade: str):
	if grade == "A+":
		return 4.5
	elif grade == "A0":
		return 4.0
	elif grade == "B+":
		return 3.5
	elif grade == "B0":
		return 3.0
	elif grade == "C+":
		return 2.5
	elif grade == "C0":
		return 2.0
	elif grade == "D+":
		return 1.5
	elif grade == "D0":
		return 1.0
	else:
		return 0.0

totalCredit = 0
totalGrade = 0

for i in range(0, 20):
	s = sys.stdin.readline().rstrip().split()
	credit = float(s[1])
	grade = s[2]

	if grade == "P":
		continue
	else:
		totalCredit += credit
		totalGrade += gradeConversion(grade) * credit

print(totalGrade / totalCredit)