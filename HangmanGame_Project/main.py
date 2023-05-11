# 匯入random模組
# 使用來自hangman_words.py的word_list
import random
from hangman_words import word_list

# 使用random的choice函式來抽單字並存入chosen_word變數
# chosen_word代表系統抽到的單字
chosen_word = random.choice(word_list)


# 建立結束遊戲的變數
# 建立遊戲中的生命次數
end_of_game = False
lives = 6

# 使用來自hangman_art.py的logo，在遊戲開始時打印出來
from hangman_art import logo
print(logo)

# Testing code
# print(f'答案是: {chosen_word}')

# 建立display空白清單做為'_'提示字數使用
# 使用for_in迴圈來變遍歷word_length的range(單字長度做為遍歷次數)
# 每遍歷1筆，就在display清單中增加1筆'_'
display = []
for i in range(len(chosen_word)):
    display += '_'

# 使用While迴圈判斷，如果沒有結束遊戲，讓用戶輸入英文字母
# 將用戶所輸入的英文字母全轉換為小寫
while not end_of_game:
    guess = input('Guess a letter: ').lower()

    # 如果用戶輸入了他們已經猜過的字母，請顯示該字母並告知使用者。
    if guess in display:
        print(f'You\'ve already guessed {guess}')

    # 使用for_in迴圈來遍歷單詞的每個位置的字母
    # 檢查每個位置上的字母是否與猜測的字母相同，如果相同將顯示列表中對應位置的'_'更新為該字母
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        # print(f'目前位置: {i}\n 目前字母: {letter}\n 猜測的字母: {guess}')
        if letter == guess:
            display[i] = letter

    # 檢查用戶是否猜錯
    # 如果用戶填入的字母不在單字中，列印該字母並告知他們不在該單字中
    if guess not in chosen_word:
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')

    # 將生命次數-1
    # 如果生命次數等於0，就結束遊戲並告知用戶輸了
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose.')

    # 將列表中的所有元素結合起來，轉換成字串做為後續判斷使用
    print(f"{' '.join(display)}")

    # 使用空格將'display'列表中的元素連接起來，並列印出來，顯示用戶猜中的字母和未猜中的空格。
    if '_' not in display:
        end_of_game = True
        print('You win.')

    # 使用來自hangman_art.py的stages
    # 每個迴圈列印對應生命次數的stages圖形
    from hangman_art import stages
    print(stages[lives])