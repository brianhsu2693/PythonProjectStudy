# 預設字典
words = {
    'ramen': '拉麵',
    'pasta': '義大利麵',
    'rice': '米飯',
    'noodle': '麵'
}

# 範例：增加字典中的鍵值(在words字典中，將'茶'存入左邊的'tea'裡面)
words['tea'] = '茶'

# 列印使用說明
print('使用說明：\n直接輸入要翻譯的英文字\n或輸入all列出全部\n或輸入key_in增加資料\n或輸入q離開\n')

# While loop重複執行查詢輸入
while True:
    key = input('請輸入文字：')
    if key in words:
        print(f'{key} 中文翻譯為：{words[key]}')
    elif key == 'all':
        print(words)
    elif key == 'q':
        print('離開程式')
        break

# 新增字典內容指令，
# 要設立兩個新的變數來儲存用戶填入的資料
# 使用words[變數A] = 變數B 來存入字典 (在words字典中，將變數B存入變數A裡面)
    elif key == 'key_in':
        new_key = input('輸入要新增的字(英文)：')
        new_value = input(f'請輸入{new_key}對應的翻譯字(中文)：')
        words[new_key] = new_value

#查無關鍵字的文字反饋
    else:
        print('查無此單字，請重新輸入')
