print("我一定會學會 Python")
from time import sleep  # 從time模組中匯入sleep函數

class Clock(object):  # 定義一個clock的class
    def __init__(self, hour=0, minute=0, second=0):  # 定義clock的屬性並初始化作業
        self.hour = hour  # 時
        self.minute = minute  # 分
        self.second = second  # 秒

    def run(self):  # 定義一個run的方法
        self.second += 1  # 秒+1
        if self.second == 60:  # 當秒數為60，分數+1，秒數歸0
            self.second = 0
            self.minute += 1
            if self.minute == 60:  # 當分數為60，時數+1，分數歸0
                self.minute = 0
                self.hour += 1
                if self.hour == 24:  # 當時數24，時數歸0
                    self.hour = 0

    def show(self):  #定 義show(顯示時間)的方法
        return '%02d : %02d : %02d' % (self.hour, self.minute, self.second)
        # 用於將時間格式化為‘%02d : %02d : %02d’的形式，其中%02d表示整數佔兩位，不足兩位時在前面補0
        # (self.hour, self.minute, self.second) 分別表示時、分、秒，用於填充佔位符%

def main():
    clock_A = Clock(23, 59, 58)  # 創建object並填入物件參數
    while True:  # 進入無限迴圈
        print(clock_A.show())  # 顯示時間
        sleep(1)  # 等待1秒
        clock_A.run()  # 時鐘運作，持續前進1秒

if __name__ == '__main__':
    main()

    [[[[[[[[]]]]]]]]
    [[[[[[[[]]]]]]]]