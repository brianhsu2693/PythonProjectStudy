# 讀取檔案
def read_file(file_name):  # 建立read_file function
    lines = []  # 建立一個空清單
    with open(file_name, 'r', encoding='utf-8') as f:  # 使用with open開啟檔案，並指定檔案名為f
                                                        # 因為檔案有中文，所以要指定讀取的編碼格式為utf-8
        for line in f:  # 使用line變數一行行的讀取f檔案
            lines.append(line.strip())  # 將line讀取出來的資料去除\n，再裝進lines清單
    return lines  #記得！ 要回傳出來！

# 檔案內文格式轉換
def convert(lines):  # 建立轉換function
    new = []  # 建立一個空清單
    person = None  # person初始化為無值
    for line in lines:  # 使用line變數去一行行的讀取lines清單
        if line == 'Char Lene':  # 如果讀取出來的字串等於'Char Lene'，就存入變數person裡
            person = 'Char Lene'
            continue  # 跳過並進入下一輪
        elif line == 'Brian Hsu':  # 如果讀取出來的字串等於'Brian Hsu'，就存入變數person裡
            person = 'Brian Hsu'
            continue  # 跳過並進入下一輪
        if person:  # 如果person有值的話，就做下面那行指令
            new.append(person + '：' + line)
    return new  # 回傳new清單

def write_file(file_name, lines):
    with open(file_name, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

# 建立主要的main function
def main():
    lines = read_file('chat.txt')  # 使用read_file function並在()裡輸入要開啟的檔案名
                                   # 然後將結果存到lines變數
    lines = convert(lines)  # 使用convert function來轉換內文格式，並在()中填入要轉換的lines清單

    write_file('chat_output.txt', lines)  # 使用write_file function來寫入檔案，()中指定新增的檔案名與要投入寫檔案功能運算的來源
    return lines  # 回傳lines變數資料


# 執行main function並列印出來
main()



