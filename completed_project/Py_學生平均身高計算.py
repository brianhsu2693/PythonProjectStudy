# 輸入學生身高資料，範例：156 178 165 171 187
# 使用.split()來切割字串，並存入student_heights清單
# 使用列表解析將清單的字串轉換成整數
student_heights = input("Input a list of student heights：\n").split()
student_heights = [int(n) for n in student_heights]

# 計算學生身高總和
sum_of_height = 0
for n in student_heights:
    sum_of_height += n
print(f'學生身高總和為：{sum_of_height} 公分')

#使用len()計算人數並算出身學生高平均值
number_of_people = len(student_heights)
average = sum_of_height / number_of_people
print(f'學生人數為：{number_of_people} 人')

#四捨五入
ave = round(average)
print(f'學生平均身高為：{ave} 公分')
