score = int(input('請輸入分數：'))

if 70 > score >= 60:
    grade = 'D'
elif 80 > score >= 70:
    grade = 'C'
elif 90 > score >= 80:
    grade = 'B'
elif score >= 90:
    grade = 'A'
else:
    grade = 'F'
print(f'{score} 分，等第為 {grade}')