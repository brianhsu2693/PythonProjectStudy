# while open是用來打開文件的一個內建函式
# while open()內先寫要開啟的檔案名，後面再寫執行指令('r'為read讀取模式)
# encoding='utf-8' 因為內文有中文，所以要指定文件的編碼方式為utf-8
# as f: 意思就是把Hello,world!.txt這個檔案當做f，以後要用到這個檔案只要呼叫f就行了
data = []  # 建立一個空清單
with open('Hello_world!.txt', 'r', encoding='utf-8') as f:
    for line in f:  # 宣告一個line變數，用for迴圈一行行的讀取f檔案
        data.append(line.strip())  # 用append函式新增資料進data清單，資料內容從line取得
                                   # 用.strip將從line取得的內容去除換行符號與前後空白
print(data)


