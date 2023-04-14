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
    person = None  # person初始化為無值
    allen_word_count = 0  # allen說的字數初始化0
    viki_word_count = 0  # viki說的字數初始化0
    allen_sticker_count = 0  # allen的貼圖初始化0
    viki_sticker_count = 0  # viki的貼圖初始化0
    allen_image_count = 0  # allen的貼圖初始化0
    viki_image_count = 0  # viki的貼圖初始化0

    for line in lines:  # 使用line變數去一行行的讀取lines清單
        s = line.split(' ')  # 使用.split切割line讀出來的每句話(切割點為空白)
        time = s[0]
        name = s[1]

        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)

        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)


    print(f'Allen 共說了 {allen_word_count} 個字，傳了 {allen_sticker_count} 個貼圖，{allen_pic_count} 個圖片。')
    print(f'Viki 共說了 {viki_word_count} 個字，傳了 {viki_sticker_count} 個貼圖，{viki_pic_count} 個圖片。')


# 寫入檔案
def write_file(file_name, lines):  # 定義write_file寫入 function
    with open(file_name, 'w', encoding='utf-8') as f:  # 打開檔案並指定為f檔名
        for line in lines:  # 使用line變數去一行行的讀取lines清單
            f.write(line + '\n')  # 將讀取的資料加上\換行符號來寫入f檔案


# 建立主要的main function
def main():
    lines = read_file('LINE-Viki.txt')  # 使用read_file function並在()裡輸入要開啟的檔案名
                                   # 然後將結果存到lines變數
    lines = convert(lines)  # 使用convert function來轉換內文格式，並在()中填入要轉換的lines清單

    #write_file('LINE-Viki_output.txt', lines)  # 使用write_file function來寫入檔案，()中指定新增的檔案名稱與要投入寫檔案功能運算的來源
    return lines  # 回傳lines變數資料


# 執行main function(檢查同目錄下有沒有產生新的檔案)
main()



