password = '12345'  # 設定密碼
user_try = 3  # 設定輸入次數
while True:
    pwd = input('請輸入密碼：')
    user_try = user_try - 1  # 計算使用次數

    if pwd == password:
        print('密碼正確')
        break  # 密碼正確，跳出迴圈
    else:
        print('密碼輸入錯誤')
        if user_try > 0:
            print(f'你還有{user_try} 次機會')
        else:
            print('輸入太多次錯誤，帳號已被鎖定！')
            break  # 輸入太多次錯誤，跳出迴圈
