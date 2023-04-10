import random  # 匯入random模組
r = random.randint(1, 100)  # 從1~10中隨機產生一個數字
count = 0  # 初始化count (count等於猜題次數)

while True:  # 執行無限迴圈
    count += 1  # count = count + 1 (每執行一次都會+1，用來計算共執行幾次)
    num = input('請猜 1 ~ 100 的數字：')  # 讓用戶輸入數字
    num = int(num)  # 字串型態轉換為整數
    if num == r:
        print('太厲害了，你猜對了！')
        print(f'這是你猜的第 {count} 次！')  # 列印猜題次數(這裡會加是因為下一行就是跳出迴圈了)
        break  # 跳出迴圈
    elif num > r:  # 給用戶的答案提示
        print('答案比你小')
    elif num < r:
        print('答案比你大')
    print(f'這是你猜的第 {count} 次！')  # 列印猜題次數
