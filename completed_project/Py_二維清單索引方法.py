row1 = ['⬜️','️⬜️','️⬜️']
row2 = ['⬜️','️⬜️','️⬜️']
row3 = ['⬜️','️⬜️','️⬜️']
map = [row1, row2, row3]
print(map)
print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you want to put? ')  # 用戶輸入2位數字代表要選擇的位置

x = int(position[0])  # 索引[0]找出用戶輸入的第1個數字，並轉換成整數，然後存為變數x
                      # x代表索引第幾個子清單
y = int(position[1])  # 索引[1]找出用戶輸入的第2個數字，並轉換成整數，然後存為變數y
                      # y代表所以x子清單中的位置
map[x - 1][y - 1] = 'X'  # 索引2維清單的位置，並將該位置內容更換為'X'字串
                         # map[0][]第一格放入變數x-1代表著縱向第2格
                         # map[][1]第二格放入變數x-1代表著橫向第1格
print(map)
print(f"{row1}\n{row2}\n{row3}")
