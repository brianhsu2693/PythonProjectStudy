from PIL import Image  # 匯入Pillow圖像處理套件中的Image物件
import os  # 匯入os套件

for file in os.listdir('original_picture'):  # 使用os套件裡的listdir function把資料夾內的檔案列出來('original_picture'指定資料夾)，並使用file變數去一個個讀取
    if file.endswith('.png'):  # 使用endswith function(字串功能)來讀取結尾是.png的檔名

        pic = Image.open(os.path.join('original_picture', file))  # 使用Image物件的open function來開啟指定的資料夾圖片('original_picture', file)，然後存入pic變數
                                                                  # 使用os.path.join()將文件路徑組合在一起



        print(f'檔案格式：{pic.format} \n圖片尺寸：{pic.size} \n圖片模組：{pic.mode}')  # 列印圖檔資訊(格式、尺寸、模組)
        pic = pic.convert('L')  # 使用convert function的L指令來將圖片轉換為黑白照片，轉換完畢後存回pic變數中
        pic.save(os.path.join('grey_pictrue', file[:-4] + '_grey.png'))  # 把修改後的pic(圖片)使用save function來另存為'指定檔名'的圖片
                                           # 使用os.path.join()將文件路徑組合在一起
                                           # [:-4]使用清單分割法來決定要拿取的字串(:就是從0開始拿取，-4就是拿到倒數第4個字就停止)
                                           # 最後使用字串相加法，加上'指定的字串'

