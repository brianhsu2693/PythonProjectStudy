students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]

def second_highest(students):
    grades = [s[1] for s in students]  # 取出所有學生的分數
    grades = sorted(grades, reverse=True)  # 使用sorted function，對grades列表進行排序
                                           # reverse=True參數，表示要反向排序，由高到低排序分數
    second = grades[1]  # 取出第二高的分數
    printed = set()  # 用來儲存已經印出過的學生名字
    for s in students:
        if s[1] == second:  # 如果學生的分數等於第二高的分數
            if s[0] not in printed:  # 如果學生名字還沒被印出過
                print(s[0])  # 印出學生的名字
                printed.add(s[0])  # 把學生名字加入printed set中，表示已經印出過了

# 呼叫 function
second_highest(students)