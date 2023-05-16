# 原學生字典
student_scores = {
    'Harry': 81,
    'Ron': 78,
    'Hermione': 99,
    'Draco': 74,
    'Neville': 62,
}

# 建立一個空的學生成績評比字典
student_grades = {}

# 使用for迴圈來讀取原學生字典
# 將讀取出來的學生名字透過字典索引的方式來讀取學生成績，並將成績存入score變數
# 使用if判斷式來做分數的評比，並將評比結果用dict_name['key'] = 'str'方法來存入新字典
for i in student_scores:
    score = student_scores[i]
    if score > 90:
        student_grades[i] = 'Outstanding'
    elif score > 80:
        student_grades[i] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[i] = 'Acceptable'
    else:
        student_grades[i] = 'Fail'

print(student_grades)