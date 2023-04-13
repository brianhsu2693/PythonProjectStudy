projects = []  # 宣告一個空的清單
while True:  # 使用無限迴圈來執行
    name = input('請輸入商品名稱：')  # 請用戶輸入商品名稱
    if name == 'q':  # Quit 離開輸入模式
        break
    price = input('請輸入商品價格：')  # 請用戶輸入商品價格
                                    # 放在離開模式底下的用意是當用戶輸入的是真正的商品，才需要輸入價格
    p = [name, price]  # 建立1個小清單p，把用戶輸入的name跟price裝進p小清單
    projects.append(p)  # 把p小清單裝到projects大清單

print(f'輸入清單中的項目有：{projects}')
print(f'清單中總共有{len(projects)}個商品')
print('--------- 分隔線 ---------')
print(f'第一個商品的名稱為：{projects [0][0]}')  # 把projects大清單中的第1格內的第1格拿出來
print(f'第一個商品的價格為：{projects [0][1]}')  # 把projects大清單中的第1格內的第2格拿出來
