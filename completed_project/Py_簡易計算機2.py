def symbols(n1, n2, n3):
    if n3 == '+':
        return (f'計算結果：{n1} + {n2} = {n1 + n2}')
    elif n3 == '-':
        return (f'計算結果：{n1} - {n2} = {n1 - n2}')
    elif n3 == '*':
        return (f'計算結果：{n1} * {n2} = {n1 * n2}')
    elif n3 == '/':
        if n2 == 0:
            return '除數不能為 0'
        else:
            return (f'{n1} / {n2} = {n1 / n2}')
    else:
        print('輸入錯誤，無法計算！')


print('「數字a」 加減乘除 「數字b」 等於 「結果」')
print(symbols(int(input('請輸入數字 a : ')), int(input('請輸入數字 b : ')), input('輸入 + - * / : ')))
