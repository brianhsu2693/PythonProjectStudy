# 設計一個calculate function，並設計3個投幣孔(n1=數字a,n2=數字b,n3=計算符號)
# 進行除法計算時，程式需要先判斷除數是否為0，因為除數為0會導致運行時錯誤
def calculate(n1, n2, n3):
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


# 在列印輸出這邊設計讓用戶填入要計算的參數
print('「數字a」 加減乘除 「數字b」 等於 「結果」')
print(calculate(int(input('請輸入數字 a : ')), int(input('請輸入數字 b : ')), input('輸入 + - * / : ')))
