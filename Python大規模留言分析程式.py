data = []  # 建立空的留言清單
count = 0  # 建立計數器，從0開始
with open('reviews.txt', 'r') as f:  # 使用with oppen讀取檔案並將檔案宣告成f
    for line in f:  # 宣告一個line變數，使用for loop一行行的讀取f檔案
        data.append(line)  # 將line讀取到的資料寫入data清單中
        count += 1  # 上面每寫1筆，計數器+1
        if count % 1000 == 0:  # 每當計數器數字除以1000餘數等於0時，則列印當下長度
            print(len(data))
print(f'總共有：{len(data)} 筆留言')  # 列印清單長度
print(f'第一筆留言字數為 {len(data[0])} 字母')

len_sum = 0  # 建立計算長度，從0開始
for d in data:  # 宣告一個變數d採用for loop去一筆一筆讀取data清單
    len_sum += len(d)  # 在for迴圈裡，將d每次遍歷出來的留言長度相加在一起
print(f'全部留言字數總和為 {len_sum} 字母')  # 列印全部留言長度
print(f'每筆留言平均字數為 {int((len_sum / len(data)))} 字母')  #將全部留言長度/全部留言筆數，並使用int取整數

new_100 = []  # 建立空的篩選清單
for d in data:  # 宣告一個變數d採用for loop去一筆一筆讀取data清單
    if len(d) < 100:  # 如果讀取出的留言長度小於100
        new_100.append(d)  # 就新增到new_100篩選清單中
print(f'留言低於100個字數的有 {len(new_100)} 筆')  # 列印留言長度小於100的筆數

good = []  # 建立空的篩選清單
for d in data:
    if 'good' in d:
        good.append(d)
print(f'留言提到good的有 {len(good)} 筆')