正確密碼 = '123456'
for 次數 in range(5):  # 用for迴圈執行5次輸入密碼的機會
    密碼 = input('請輸入密碼：')  # 要求使用者輸入密碼
    if 密碼 == 正確密碼:   # 判斷輸入的密碼是否正確
        print('密碼正確')
        break  # 如果密碼正確，就跳出迴圈
    elif 密碼 != 正確密碼 and 次數<4:  # 如果密碼不正確且還有輸入次數，則列印提示訊息
        print('密碼不正確，請重新輸入！')
        print(f'您還剩下{4-次數}次機會')
    else:  # 如果輸入錯誤密碼5次，則列印帳號鎖定的訊息
        print('您已經輸入太多次錯誤密碼，帳號已被鎖定！')