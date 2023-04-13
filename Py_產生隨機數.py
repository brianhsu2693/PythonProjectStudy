import random  # 匯入random模組

for i in range(5):  # 宣告1個i變數，採用for loop去一筆一筆讀取range(5)清單資料
    r = random.randint(1, 100)  # 宣告變數r，隨機產生範圍1~100中的數字
    print(f'這是第 {i + 1} 次產生隨機數 {r}。')  # 列印次數與range清單範圍有直接關係