import os
import fitz # 導入的是fitz
from PIL import Image
from tkinter import *
from tkinter.filedialog import askdirectory

rotate = int(0) # 設置圖片的旋轉角度
zoom_x = 2.0 # 設置圖片相對於PDF文件在X軸上的縮放比例
zoom_y = 2.0 # 設置圖片相對於PDF文件在Y軸上的縮放比例


#GUI 取得資料夾路徑
def ask_inputPath():
    root = Tk()
    path_ = askdirectory()
    root.withdraw()
    return(path_)

def main():
    input = ask_inputPath()
    output= os.path.join(input, 'img\\')
    print('Start pdf to img')
    if not os.path.isdir(output):
        os.mkdir(output)

    if os.path.isdir(input):
        #列出所有的檔案
        files = os.listdir(input)
        #只處理 pdf 檔案
        for f in files:
            if ".pdf" in f:
            #打開pdf 文件
                pdf = fitz.open(os.path.join(input, f))
                for pg in range(0, pdf.pageCount):
                    page = pdf[pg]
                    trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
                    pm = page.getPixmap(matrix=trans, alpha=False)
                    #開始轉圖
                    f_name=f.split('.')[0]
                    pm.writePNG(output+f_name+str(pg)+".jpg")
    else:
        print('Direction path not exist, please check the path.')

if __name__ == '__main__':
    main()
