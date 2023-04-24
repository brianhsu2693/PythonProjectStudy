one_list = [1, 3, 9, 5, 6, 8, 15, 20, 28]  # 建立一個數字清單

def find_max(one_list):  # 設立一個function，()括號中填入清單名稱
    if not one_list:  # 如果投入function的清單不是one_list就返回值0
        return 0

    max_num = one_list[0]  # 設立一個最大值變數，將清單中的第一個數字存入做預設
    for num in one_list:  # 使用for迴圈，並設立一個變數num去1筆筆的讀取清單內容
        if num > max_num:  # 如果讀取出來的內容大於man_num目前的數字
            max_num = num  # 那就將num存入max_num(覆蓋)
    return max_num  # 回傳max_num數值

print(f'全部清單：{one_list}')  # 列印全部清單
print(f'清單中最大數值為：{find_max(one_list)}')  # 列印清單最大值
