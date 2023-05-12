# 匯入math模組(用於無條件進位法使用)
import math

# 計算多少面積需要購買多少罐油漆
# 設計一個paint_calc function(油漆面積計算機)
# 設計投幣孔所接收的的內容參數屬性(牆高, 牆寬, 1罐油漆覆蓋面積)
# 公式： 罐數 =（壁高 x 壁寬）÷ 每罐油漆的覆蓋面積 (因為不能買半罐油漆，若有小數點，需要無條件進位)
# 將計算結果列印出來告知用戶
def paint_calc(height, width, cover):
    quantity = math.ceil(test_h * test_w / cover)
    print(f'You\'ll need {quantity} cans of paint.')

# 讓用戶輸入要投入的內容並呼叫paint_calc function
# 將用戶輸入的內容與function()內的參數進行對應
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


