# 設計一個format_name function，並帶有f_name, l_name輸入孔
# 先簡易判斷用戶是否輸入空白文字，若是輸入空白文字則return回傳告知提示
# 接著將用戶所輸入的名字使用.title()來轉換標題大小寫並return回傳(順便加入f格式化字串)
def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return '你沒有提供有效的輸入'
    else:
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return f'轉換結果: {formated_f_name} {formated_l_name}'


# 呼叫format_name()function並進行列印輸出
# format_name()function的參數投入孔使用input()讓用戶自行輸入
print(format_name(input('What is your first name? '), input('What is your last name? ')))
