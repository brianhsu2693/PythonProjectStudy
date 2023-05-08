import random  # 匯入random生成隨機數模組

# 定義所需的字母、符號和數字
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', ',','%','&','(',')','*','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print('歡迎使用PyPassword密碼生成器！')

# 讓使用者輸入所需的字母、符號和數字數量
user_letters = int(input('請輸入需要的字母數量：\n'))
user_symbols = int(input('請輸入需要的符號數量：\n'))
user_numbers = int(input('請輸入需要的數字數量：\n'))

# 建立空清單
password_list = []

# 生成包含所需字母的清單
# 這兩行程式碼的作用是將隨機選擇的字母添加到密碼清單中，重複user_letters次，以產生一個指定數量字母的隨機密碼。
for p in range(1, user_letters + 1):
    password_list.append(random.choice(letters))

# 生成包含所需符號的清單
for p in range(1, user_symbols + 1):
    password_list.append(random.choice(symbols))

# 生成包含所需數字的清單
for p in range(1, user_numbers + 1):
    password_list.append(random.choice(numbers))

print(f'打亂前的密碼清單：\n{password_list}')  # 印出包含所需元素的清單
random.shuffle(password_list)  # 將列表中的元素打亂
print(f'打亂後的密碼清單：\n{password_list}')  # 印出打亂後的列表

# 在Python中，字串和整數不能直接相加，所以需要將清單中的元素逐一連接起來形成字串。
# 將列表中的元素連接起來形成字串，即生成一個隨機密碼
password = ''
for p in password_list:
    password += p
print(f'生成的密碼為：{password}')  # 印出生成的密碼
