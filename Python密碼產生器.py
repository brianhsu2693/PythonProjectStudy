import random  # 匯入random生成隨機數模組
import string  # 匯入string文字相關語法模組

數字 = string.digits  # 產生0到9的數字
英文 = string.ascii_letters  # 產生英文大小寫字母
字母表 = list(數字 + 英文)  # 此為產生密碼的材料，另外使用list語法將字串轉為清單

random.shuffle(字母表)  # 使用shuffle語法將清單打亂
密碼長度 = int(input('你的密碼要幾位數呢?'))  # 讓用戶輸入密碼位數，並用int語法將字串轉換成整數
密碼 = ''.join(字母表[:密碼長度])  # 採用[:?]清單語法擷取字母表中的前幾位數
                                # 採用''.join()語法將清單轉換為一般字串
print(f'你生成的亂數密碼為： {密碼}')