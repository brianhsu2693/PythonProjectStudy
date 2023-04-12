data = []  # 建立空清單
count = 0  # 建立計數器，從0開始
with open('reviews.txt', 'r') as f:  # 使用with oppen讀取檔案並將檔案宣告成f
    for line in f:  # 宣告一個line變數，使用for loop一行行的讀取f檔案
        data.append(line)  # 將line讀取到的資料寫入data清單中
        count += 1  # 上面每寫1筆，計數器+1
        if count % 1000 == 0:  # 每當計數器數字除以1000餘數等於0時，則列印當下長度
            print(len(data))

print(f'總共有：{len(data)} 筆資料。')  # 列印清單長度
print('------------- 分隔線 -------------')  # 分隔線
print(data[0])  # 索引清單第一筆
print('------------- 分隔線 -------------')  # 分隔線
print(data[0:3])  # 索引清單第一筆到第三筆
