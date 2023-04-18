# 1.讀取檔案與進度顯示(每2000顯示1次)
# 2.統計全部留言筆數
# 3.統計第一筆留言字數
data = []  # 建立空的留言清單
count = 0  # 建立計數器，從0開始
with open('reviews.txt', 'r') as f:  # 使用with oppen讀取檔案並將檔案宣告成f
    for line in f:  # 宣告一個line變數，使用for loop一行行的讀取f檔案
        data.append(line)  # 將line讀取到的資料寫入data清單中
        count += 1  # 上面每寫1筆，計數器+1
        if count % 2000 == 0:  # 每當計數器數字除以2000餘數等於0時，則列印當下長度
            print(len(data))
print(f'總共有：{len(data)} 筆留言')  # 列印清單長度
print(f'第一筆留言字數為 {len(data[0])} 字母')


# 4.統計全部留言字數
# 5.統計每筆留言平均數
len_sum = 0  # 建立計算長度，從0開始
for d in data:  # 宣告一個變數d採用for loop去一筆一筆讀取data清單
    len_sum += len(d)  # 在for迴圈裡，將d每次遍歷出來的留言長度相加在一起
print(f'全部留言字數總和為 {len_sum} 字母')  # 列印全部留言長度
print(f'每筆留言平均字數為 {int((len_sum / len(data)))} 字母')  # 將全部留言長度/全部留言筆數，並使用int取整數


# 6.統計留言低於100字的筆數
new_100 = []  # 建立空的篩選清單
for d in data:  # 宣告一個變數d採用for loop去一筆一筆讀取data清單
    if len(d) < 100:  # 如果讀取出的留言長度小於100
        new_100.append(d)  # 就新增到new_100篩選清單中
print(f'留言低於100個字數的有 {len(new_100)} 筆')  # 列印留言長度小於100的筆數


# 7.統計留言提到good的筆數
good = []  # 建立空的篩選清單
for d in data:  # 宣告一個變數d採用for loop去一筆一筆讀取data清單
    if 'good' in d:  # 如果讀取出來檢查有good字串
        good.append(d)  # 就新增到good篩選清單中
print(f'留言提到good的有 {len(good)} 筆')  # 列印留言提到good關鍵字的筆數


# 8.統計全部留言單字出現的次數字
word_count = {}  # 建立1個空的字典{鍵:值, 鍵:值}
for d in data:  # d是1筆留言(字串); data是筆201506筆的總清單
    words = d.strip().split(' ')  # 用strip()去除d的換行符號與空格，用split(' ')並指定空白處作為切割點來切割d字串，最後存入words清單
    for word in words:  # 使用word變數去一行行讀取words清單的內容
        if word in word_count:  # 如果讀出來的word有出現word_count字典裡，就去↓
            word_count[word] += 1  # word_count字典中查找word，並把word對應的值+1。 範例{word:n+1}  __(n為原本已存在的值)
                                   # 字典名稱xxx[key_name] 為查詢字典內的資料
        else:
            word_count[word] = 1  # 不然就，新增word(new_key)進入word_count字典，並設立對應值為1。 範例{word:1}
print(f'word_count 字典內，總共有 {len(word_count)} 個單字')  # 列印字典全部的單字數量


# 9.列出出現次數超過12萬次的單字
for word in word_count:
    if word_count[word] > 120000:
        print(word, word_count[word])


# 10.查詢單字出現過的次數
while True:
    key_word = input('請輸入查詢字：')
    if key_word in word_count:
        print(f'{key_word} 總共出現過 {word_count[key_word]} 次')
        break
    else:
        print('查無此單字，請重新輸入')

# print(f'使用超過300次的單字有 {len(word)} 個')


