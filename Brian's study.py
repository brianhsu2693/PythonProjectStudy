cm = input('請輸入你的身高(公分)；')
cm = float(cm)  # 將字串轉為整數
m = cm / 100  # 將身高公分單位轉換為公尺
kg = input('請輸入你的體重(體重)：')
kg = float(kg)  # 將字串轉為浮點數
BMI = kg / (m ** 2)  #BMI計算公式

print(f'您的BMI數值為：{BMI}')

if BMI <  18.5:
    print('體重過輕')
elif 18.5 <= BMI < 24:
    print('太棒了！ 你有健康的體位，請好好抱持！')
elif 24 <= BMI < 30:
    print('請注意，你輕度肥胖，要小心身體狀況！')
elif 30 <= BMI < 35:
    print('請注意，你中度肥胖，要小心身體狀況！')
elif BMI >= 35:
    print('請注意，你重度肥胖，要小心身體狀況！')

