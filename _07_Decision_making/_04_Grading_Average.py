""" print Grading system and Average of class
"""
cls_avg = int(input('Enter a class Average marks:'))
marks = int(input('Enter marks:'))
if marks < 50:
    grade = 'F'
elif marks <= 70:
    grade = 'D'
elif marks <= 80:
    grade = 'C'
elif marks <= 90:
    grade = 'B'
else:
    grade = 'A'
print('Grade: ', grade)

k = (marks / cls_avg) * 100
print(k)
if k >= 90:
    print('Top Rank')
elif k >= 80:
    print('Modirate Rank')
else:
    print('Below average Rank')
