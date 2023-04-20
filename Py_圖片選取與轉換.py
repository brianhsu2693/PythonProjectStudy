from PIL import Image  # 匯入Pillow圖像處理套件
import os  # 匯入os套件

pic = Image.open('merlin_superJumbo.png')  # 使用Image物件的open function來開啟指定的圖片('填入檔名')
print(f'檔案格式：{pic.format} \n圖片尺寸：{pic.size} \n圖片模組：{pic.mode}')  # 列印圖檔資訊(格式、尺寸、模組)
pic = pic.convert('L')  # 使用convert fouction的L指令來將圖片轉換為黑白照片，轉換完畢後存回pic變數中
pic.show()  # 開啟修改後的圖片
pic.save('testing.png')  # 把修改後的圖片另存為'指定檔名'的圖片

for file in os.listdir('.'):  # 設立file變數並使用os套件裡的listdir fouction把'.'指定位置的資料夾裡面的檔案都讀取過
    print(file)