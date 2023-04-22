# 創立Class
# Class的名稱要大寫(這是規矩)
class Students:
    def __init__(self, name, score):  # initialize 初始化 (定義屬性)
        self.name = name
        self.score = score
        #self.score = score
        print('我誕生了！！')
    def do_homework(self):  # 定義功能function
        print('我在寫作業')

    def study(self):  # 定義功能function
        print('我在讀書')
        self.score += 5  # 設計透過讀書的方式，來增加分數
                         # 我(self)的分數(score)= +5分

    def sleep(self):
        print('i am sleeping ~ zzzZZZ')


# 創造object(物件)
# Class名稱加上()，就是建立object(物件)的意思
# 如果()裡面有投入參數的話，系統就會自動投入__init__初始化那邊的參數投入位置
s1 = Students('Brian', 90)  # 創立物件，投入屬性，再存過去左邊的變數
s2 = Students('Charlene', 95)  # ()裡面有投入'Charlene'名稱與95分數，系統自動投入__init__初始化那邊的name位置
print(f'{s1.name} 的分數為 {s1.score} 分')
print(f'{s2.name} 的分數為 {s2.score} 分')

s1.study()  # s1學生透過study() function來增加分數
print(f'{s1.name} 的分數為 {s1.score} 分')


# s1.do_homework()  # 物件使用功能 object use function
# s1.study()  # object use function
# s1.sleep()  # object use function

