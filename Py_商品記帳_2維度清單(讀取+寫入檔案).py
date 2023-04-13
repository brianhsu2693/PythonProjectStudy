projects = []  # 宣告一個空的清單

# 讀取外部檔案
with open('products.csv', 'r', encoding='utf-8') as f:  # 開啟products.csv檔案，用utf-8讀取並命名為f
    for line in f:  # 設立line變數並使用for loop來讀取f的內容
        name, price = line.strip().split(',')  # 讀取出來的內容去\n跟使用逗號做切割，並存回name與price裡
        projects.append([name, price])  # 用[name, price]小清單的模式裝入projects[]大清單中
print(projects)
print(f'清單中總共有{len(projects)}個商品')

# 用戶輸入資料並寫入清單中
while True:  # 使用無限迴圈來執行
    name = input('請輸入商品名稱：')  # 請用戶輸入商品名稱
    if name == 'q':  # Quit 離開輸入模式
        break
    price = input('請輸入商品價格：')  # 請用戶輸入商品價格
                                     # 放在離開模式底下的用意是當用戶輸入的是真正的商品，才需要輸入價格
    p = [name, price]  # 建立1個小清單p，把用戶輸入的name跟price裝進p小清單
    projects.append(p)  # 把p小清單裝到projects大清單

# 列印清單檔案
print(f'清單中的項目有：{projects}')
print(f'清單中總共有{len(projects)}個商品')
print('--------- 分隔線1 ---------')
print(f'第一個商品的名稱為：{projects [0][0]}')  # 把projects大清單中的第1格內的第1格拿出來
print(f'第一個商品的價格為：{projects [0][1]}')  # 把projects大清單中的第1格內的第2格拿出來
print('--------- 分隔線2 ---------')
for p in projects:  # 宣告一個變數p，使用for loop將projects清單內的資料一個個取出
    print(f'{p[0]}價格是{p[1]}元')  # 列印出每個取出的小清單內的數值

# 寫入外部檔案
with open('products.csv', 'w', encoding='utf-8') as f:  # 打開一個檔案並預定使用寫入功能，將該檔案暫時命名為f
                                                        # encoding='utf-8' 因為內文有中文，所以要指定文件的編碼方式為utf-8
    f.write('產品,價格\n')  # 增加products.csv的欄位抬頭
    for p in projects:  # 使用變數P去把projects清單內資料一個個取出
        f.write(p[0] + ',' + p[1] + '\n')  # 將變數p取到的每一筆資料，參照指定的格式寫入f檔案裡