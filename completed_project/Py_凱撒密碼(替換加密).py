# 字母表
# 重複兩次是為了能夠索引字母表尾部位移後的字母
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z'
]


# 設計1個加密function
# 新增1個空的加密字串(用來存放遍歷並位移完成的字母)
# 使用for迴圈遍歷user_text的字串
# 使用index來索引用戶輸入的每個字母(i)在alphabet字母表的哪個位置，並將索引出來數值存在position變數裡
# 將原位置表加上位移數，存成新的位置表
# 使用[]填入新位置表數值來索引字母表，每次遍歷出來的字母存入new_letter
# 最後將每次遍歷並位移完成的字母使用+=存入cipher_text字串裡
# 列印
def encrypt(user_text, user_shift):
    cipher_text = ''
    for i in user_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += i
    print(f'The encoded text is {cipher_text}')


def decrypt(user_text, user_shift):
    decrypt_text = ''
    for i in user_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position - shift
            new_letter = alphabet[new_position]
            decrypt_text += new_letter
        else:
            decrypt_text += i
    print(f'The encoded text is {decrypt_text}')


# 設立While迴圈來重複執行
# 用戶輸入加解密指令，若輸入的不是'encode'和'decode'，做錯誤告知提示
# 輸入goodbye就離開程式
# 續上，如果用戶輸入'encode'和'decode'，讓用戶輸入加解密字串
# 續上，如果用戶輸入'encode'和'decode'，讓用戶輸入加解密位移數
# 為了上用戶可以輸入26個以上的位移數，使用位移數除以26並取餘數來當位移數
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'goodbye' to end:\n")
    if direction == 'goodbye':
        print('Good bey~')
        break
    elif direction != 'encode' and direction != 'decode':
        print('Command input error, please re-enter')
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26

        # 執行函式
        if direction == 'encode':
            encrypt(user_text=text, user_shift=shift)
        elif direction == 'decode':
            decrypt(user_text=text, user_shift=shift)
