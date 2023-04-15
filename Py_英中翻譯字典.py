words = {
    'ramen': '拉麵',
    'pasta': '義大利麵',
    'rice': '米飯',
    'noodle': '麵'
}

# 增加字典中的鍵值(在words字典中，將'茶'存入左邊的'tea'裡面)
words['tea'] = '茶'

print('使用說明：\n直接輸入要翻譯的英文字\n或輸入all列出全部\n或輸入key_in增加資料\n或輸入q離開\n')

while True:
    key = input('請輸入文字：')
    if key in words:
        print(f'{key} 中文翻譯為：{words[key]}')
    elif key == 'all':
        print(words)
    elif key == 'q':
        print('離開程式')
        break

    elif key == 'key_in':
        new_key = input('輸入要新增的字(英文)：')
        new_value = input(f'請輸入{new_key}對應的翻譯字(中文)：')
        words[new_key] = new_value

    else:
        print('查無此單字，請重新輸入')
