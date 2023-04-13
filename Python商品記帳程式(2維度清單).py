projects = []  # 宣告一個空的清單
while True:  # 使用無限迴圈來執行
    name = input('請輸入商品名稱：')  # 請用戶輸入商品名稱
    if name == 'q':  # Quit 離開輸入模式
        break
    price = input('請輸入商品價格：')  # 請用戶輸入商品價格
                                    # 放在離開模式底下的用意是當用戶輸入的是真正的商品，才需要輸入價格
    p = []  # 建立1個空的小清單
    p.append(name)  # 把用戶輸入的name裝進p小清單
    p.append(price)  # 把用戶輸入的price裝進p小清單
    projects.append(p)  # 把p小清單裝到projects大清單




print(f'輸入清單中的項目有：{projects}')
print(f'總共有{len(projects)}個')
