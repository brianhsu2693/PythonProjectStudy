list = []  # 宣告1個空的list清單
with open('LINE2-Viki.txt', 'r', encoding='utf-8-sig') as f:  # 打開txt檔案，指定utf-8編碼讀取並命名為f
                                                              # 當取得的字串前面有奇怪的符號，則使用utf-8-sig編碼來讀取
    for line in f:  # 使用line變數去一行行的讀取f檔案
        list.append(line.strip())  # 將line讀取到的檔案先去除換行\n標記再存到list清單中

for line in list:  # 使用line變數去一行行的讀取list清單
    s = line.split(' ')  # line讀去到的檔案使用.split去做切割('空白'為切割點)
                         # 將s列印出來會發現時間跟人名黏在一起，例如['13:34Viki', '那是據點代號']
    time = s[0][:5]  # 因s清單第1個字串中的前5格是時間，是固定不變動的，所以使用s[0][:5]取前5格資料存入time變數(作為時間)
    name = s[0][5:]  # 取s清單第1個字串中的第5格(含)以後的資料存入name變數(做為人名)

    print(name)

