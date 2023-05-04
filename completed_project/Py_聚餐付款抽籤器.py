# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")  # 使用.split()function來切割字串並存為清單
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_len = len(names)  # 計算清單長度(清單內的數量)
payer_num = random.randint(0, names_len - 1)  # 使用.randint()function來來選擇隨機抽出的範圍
                                              # ()中的0為起始，names_len-1為清單結尾
payer = names[payer_num]  # 將抽出來的數字帶入names清單做索引，並存入payer變數作為抽出來的付款人

print(f'{payer} is going to buy the meal today! ')