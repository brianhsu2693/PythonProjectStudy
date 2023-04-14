def is_leap(year):  # 宣告1個is_leap function
    if year % 4 != 0:  # 設計判斷公式
        return  False  # 回傳判斷結果
    elif year % 100 != 0:
        return  True
    elif year % 400 != 0:
        return  False
    elif year % 3200 != 0:
        return True
    else:
        return False

while True:  # 設立一個重複輸入的迴圈
    keyin_year = input('請輸入要查詢的年份，或輸入 q 退出程序：')  # 設計用戶輸入位置
    if keyin_year == 'q':  # 如果用戶輸入q就退出程序
        break

    result_year = is_leap(int(keyin_year))  # 將用戶輸入的字串轉為整數
                                        # 在將轉好的整數帶入is_leap function做運算
                                        # 將運算結果存在result_year變數裡

    if result_year == True:  # 如果取得的結果是True，列印{}年份是閏年
        print(f'{keyin_year} 是閏年')
    else:
        print(f'{keyin_year} 不是閏年')
