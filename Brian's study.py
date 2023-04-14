# 讀取檔案
def read_file():  # 建立read_file function
    lines = []  # 建立一個空清單
    with open('chat.txt', 'r', encoding='utf-8') as f:  # 使用with open開啟檔案，並指定檔案名為f
                                                        # 因為檔案有中文，所以要指定讀取的編碼格式為utf-8

        for line in f:  # 使用line變數一行行的讀取f檔案
            lines.append(line)  # 將line讀取出來的檔案裝進lines清單
    return lines  #記得！ 要回傳出來！

lines = read_file()
print(lines)