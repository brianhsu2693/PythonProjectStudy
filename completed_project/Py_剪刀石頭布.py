rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random  # 導入隨機模組
data = [rock, paper, scissors]  # 把剪刀石頭布裝入一個data清單中，後續可以做索引對照

ask_user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))  # 用戶輸入並把內容轉為整數
if ask_user in [0, 1, 2]:  # 檢查用戶輸入的內容有沒有在[0,1,2]清單裡面
    user = data[ask_user]  # 如果有，對照data清單的索引號碼找出用戶出的剪刀石頭布並存入user變數中
    print(f'you：{user}')  # 列印
else:
    print('Input errors, please re-enter')  # 用戶輸入的內容沒有在[0,1,2]清單裡面，列印錯誤提示
    exit()

npc = random.choice(data)  # 使用random.choice()抽牌函式來隨機抽取data裡的元素並存入npc變數中
print(f'npc；{npc}')  # 列印

if user == npc:
    print('It is a draw')  # 如果用戶跟電腦出一樣的，那就平手
elif user == rock and npc == scissors:  # 如果用戶出石頭，電腦出剪刀，用戶贏
    print('you win')
elif user == paper and npc == rock:  # 如果用戶出布，電腦出石頭，用戶贏
    print('you win')
elif user == scissors and npc == paper:  # 如果用戶出剪刀，電腦出布，用戶贏
    print('you win')
else:
    print('you lose')  #以上都不是，那就是用戶輸