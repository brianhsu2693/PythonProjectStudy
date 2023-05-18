############### Blackjack規則 #####################

##牌堆的大小無限制。
##沒有小丑牌。
##J、Q、K都計為10分。
##A可以計為11或1分。
##使用以下列表作為牌組：
##cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
##列表中的牌被抽中的機會相等。
##抽到的牌不會從牌組中移除。
##電腦扮演莊家的角色。

##################### 提示 #####################

#  提示1：訪問以下網站，試玩Blackjack遊戲：
#  https://games.washingtonpost.com/games/blackjack/
#  然後在這裡試玩已完成的Blackjack項目：
#  http://blackjack-final.appbrewery.repl.run
#  提示2：閱讀此程序要求的分解：
#  http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#  然後嘗試為該程序創建自己的流程圖。
#  提示3：下載並閱讀我創建的流程圖：
#  https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


# 匯入random隨機模組
# 從art.py檔案叫出logo變數內容
import random
from art import logo


# 創建一個名為deal_card()的函式，做為從牌組中隨機抽張牌功能
# 建立撲克牌cards清單[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] (備註：11是A)
# 使用random模組中的choice()抽牌函式來抽取cards清單中的牌並存成card變數
def deal_card():
    ''' 從牌組中隨機抽張牌 '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# 創建名為calculate_score()的函式，做為計算分數功能。(有包含一個清單投入的投幣孔)
# 在calculate_score()函式內檢查是否有blackjack(兩張牌：A+10)，若是則回傳0而不是回傳實際得分 (0代表拿到黑傑克)
# 在calculate_score()函式內檢查11(ace)。如果分數已經超過21，就刪除11並將其替換為1
# 將所投入的清單內容用sum()函式進行加總並return
def calculate_score(cards):
    '''計算分數'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# 創建為compare()的函式，並傳入user_score和computer_score。如果電腦和使用者的得分相同，則是平局。如果電腦有一個21點（黑杰克），那麼使用者輸了。
# 如果使用者有一個21點（黑杰克），那麼使用者贏了。如果使用者得分超過21，那麼使用者輸了。如果電腦得分超過21，那麼電腦輸了。如果以上情況都不符合，則得分最高的玩家獲勝。
def compare(user_score, computer_score):
    '''比較牌面大小'''
    if user_score == computer_score:
        return '平手🙃'
    elif user_score > 21 and computer_score > 21:
        return '你輸了，你超過二十一點😤'
    elif computer_score == 0:
        return '輸了，對手有二十一點😱'
    elif user_score == 0:
        return '你贏了，你有二十一點😎'
    elif user_score > 21:
        return '你輸了，你超過二十一點😭'
    elif computer_score > 21:
        return '你贏了，對手超過二十一點😁'
    elif user_score > computer_score:
        return '你贏了😃'
    else:
        return '對手贏了😤'


# 創建名為play_game()的函式，做為開始遊戲。
def play_game():
    '''開始遊戲'''
    # 建立用戶卡牌的空清單與電腦卡牌的空清單
    # 預設結束遊戲為False
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # 使用for迴圈來執行，並指定range(2次)
    # 在for迴圈底下執行用.append()將deal_card()函式抽出的牌存入user_cards[]與computer_cards[]空清單裡面
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # 設立while無限迴圈來重複執行用戶端的抽牌邏輯(遊戲尚未結束is_game_over=False的情況下)
    # 調用calculate_score()函式來計算user分數並存成user_score變數
    # 調用calculate_score()函式來計算computer分數並存成computer_score變數
    # 列印用戶的牌與分數；列印電腦的第1張牌
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'你的牌：{user_cards}, 目前分數：{user_score}')
        print(f'對手的第 1 張牌 [{computer_cards[0]}]')
        print()

        # 如果user或computer擁有0(等於黑傑克21點)或user超過21點，就結束遊戲
        # 如果遊戲還沒有結束，詢問用戶是否要再抽一張牌
        # 如果用戶填「y」，則使用deal_card()函式來抽牌並append()添加到user_cards清單內
        # 如果用戶填「n」，則遊戲結束
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            aks_again_choice = input('輸入 \'y\' 來抽取一張牌，輸入 \'n\' 停止抽牌: ')
            if aks_again_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # 用戶完成後就輪到電腦抽牌了，設立while迴圈，只要電腦分數不等於0(黑傑克21點)和分數小於17就執行迴圈內容
    # 電腦抽新牌並調用calculate_score()函式來重新計算電腦的分數，計算後的分數並存回computer_score變數
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f'你最後的牌：{user_cards}, 最終分數：{user_score}')
    print(f'對手最後的牌：{computer_cards}, 最終分數：{computer_score}')
    print(compare(user_score, computer_score))


# 提示14：詢問用戶是否要重新啟動遊戲。如果他們回答是，請清除控制台並開始新的二十一點遊戲並顯示 art.py 中的徽標。
while input('你想玩二十一點遊戲嗎？ 請輸入 \'y\' 或 \'n\': ') == 'y':
    play_game()