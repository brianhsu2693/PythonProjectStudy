#(1)將原程式法重新分析並進行重構
#(2)設計4個function來呈現清晰架構

# 讀取外部檔案
def read_file(file_name):
    products = []  # 宣告一個空的清單
    import os
    if os.path.isfile(file_name):  # 檢查products.csv有沒有在資料夾內
        print('找到檔案！開始執行！')

    # Yes → 讀取外部檔案
        with open(file_name, 'r', encoding='utf-8') as f:  # 開啟products.csv檔案，用utf-8讀取並命名為f
            for line in f:  # 設立line變數並使用for loop來讀取f的內容
                if '產品,價格' in line:  # 判斷清單的'產品,價格'抬頭，如果有的話就跳過迴圈
                    continue  # continue跳下一個迴圈的意思(通常都寫在迴圈很高的位置)
                name, price = line.strip().split(',')  # 讀取出來的內容去\n跟使用逗號做切割，並存回name與price裡
                products.append([name, price])  # 用[name, price]小清單的模式裝入projects[]大清單中
        print(products)
        print(f'清單中總共有{len(products)}個商品')
        return products  # (很重要)function最後一行記得將寫在清單內的資料回傳出來

    # No → 提示訊息
    else:
        print('找不到檔案，請協助卻認同目錄下是否有該檔案！')

# 用戶輸入資料並寫入清單中
def user_input(products):
    while True:  # 使用無限迴圈來執行
        name = input('請輸入商品名稱：')  # 請用戶輸入商品名稱
        if name == 'q':  # Quit 離開輸入模式
            break
        price = input('請輸入商品價格：')  # 請用戶輸入商品價格
                                         # 放在離開模式底下的用意是當用戶輸入的是真正的商品，才需要輸入價格
        p = [name, price]  # 建立1個小清單p，把用戶輸入的name跟price裝進p小清單
        products.append(p)  # 把p小清單裝到projects大清單
    return products  # (很重要)function最後一行記得將寫在清單內的資料回傳出來

# 列印清單資料
def print_products(products):
    print(f'清單中的項目有：{products}')
    print(f'清單中總共有{len(products)}個商品')
    print('--------- 分隔線1 ---------')
    print(f'第一個商品的名稱為：{products [0][0]}')  # 把projects大清單中的第1格內的第1格拿出來
    print(f'第一個商品的價格為：{products [0][1]}')  # 把projects大清單中的第1格內的第2格拿出來
    print('--------- 分隔線2 ---------')
    for p in products:  # 宣告一個變數p，使用for loop將projects清單內的資料一個個取出
        print(f'{p[0]}價格是{p[1]}元')  # 列印出每個取出的小清單內的數值

# 寫入外部檔案
def write_file(file_name, products):
    with open(file_name, 'w', encoding='utf-8') as f:  # 打開一個檔案並預定使用寫入功能，將該檔案暫時命名為f
                                                            # encoding='utf-8' 因為內文有中文，所以要指定文件的編碼方式為utf-8
        f.write('產品,價格\n')  # 增加products.csv的欄位抬頭
        for p in products:  # 使用變數P去把projects清單內資料一個個取出
            f.write(p[0] + ',' + p[1] + '\n')  # 將變數p取到的每一筆資料，參照指定的格式寫入f檔案裡

# function執行區
products = read_file('products.csv')  # 因為執行結果有回傳資料回來，所以要宣告個變數來存下來
products = user_input(products)  # 因為執行結果有回傳資料回來，所以要宣告個變數來存下來
print_products(products)  # 無回傳值，故直接執行
write_file('products.csv', products)  # 無回傳值，故直接執行