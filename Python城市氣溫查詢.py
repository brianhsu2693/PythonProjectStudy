import requests  #匯入requests HTTP模組

city_name = input('請輸入城市名稱：')  #定義城市名稱
api = '5a5ebd4a81ac0920b1d58b63f5ba6691'  #填入api key
URL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}'  #填入api url
天氣資料 = requests.get(URL)  #使用requests模組的get語法來送出這一行網址
氣溫 = int((天氣資料.json()['main']['temp']-273.15))  #使用.json語法將取得的資料轉成字典
                                                    #對照api文件範例，找到main標題下的temp(溫度)，將兩個標題輸入到程式碼裡
                                                    #字典裏面用的是克氏溫標，要-273.15才是攝氏溫度
                                                    #將輸出的天氣資料使用int語法轉成整數
print(f'目前的氣溫{氣溫}度')


