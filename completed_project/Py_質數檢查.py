# 設計一個可以檢查用戶輸入的數字是不是質數
# 宣告is_prime等於True
# 使用for迴圈遍歷range(2到所輸入的數字)
# 如果遍歷出的數值可以整除，代表不是質數，便將is_prime改為False
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

# 使用if判斷式來判斷is_prime的狀態是Ture或False並列印對應狀態
    if is_prime == True:
        print('It\'s a prime number.')
    else:
        print('It\'s not a prime number.')

# 讓用戶輸入要投入的內容並呼叫prime_checker function
# 將用戶輸入的內容與function()內的參數進行對應
n = int(input('Check this number: '))
prime_checker(number=n)


