import cv2
import numpy as np
import time
import os
import glob
import sys
import reductNoise
import pytesseract
from PIL import Image
from waterDropleCut import WaterCutting
from waterFill import WaterFilled


for file in os.listdir("easy_img") :
    fileName= file.split(".")[0]
    filepath = os.path.join("easy_img",file) 
    im = cv2.imread(filepath)
    #将图片转成灰度图
    im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(os.path.join("image",fileName+"_gray.jpg"),im_gray)
    #将像素做二值化处理
    ret,im_res = cv2.threshold(im_gray,240,255,cv2.THRESH_BINARY)
    # cv2.imwrite(os.path.join("image",fileName+"_threshold.jpg"),im_res)
    # #用高斯模糊对图片进行降噪
    # kernel = 1/9*np.array([[1,2,1],[2,4,2],[1,2,1]])
    # im_blur = cv2.filter2D(im_inv,-1,kernel)
    # cv2.imwrite(os.path.join("image",fileName+"_filter2d.jpg"),im_inv)
    # #对图片进行进一轮的二值化处理
    # ret,im_res = cv2.threshold(im_blur,150,255,cv2.THRESH_BINARY_INV)
    # cv2.imwrite(os.path.join("image",fileName+"_threshold2.jpg"),im_res)

    print("第二轮二值化处理完毕。。。。")

    #根据扫描法对图片降噪处理
    results = reductNoise.reductNoise(im_res)
    # cv2.imwrite(os.path.join("image",fileName+"_reductNoise.jpg"),im_res)
    print("扫描法处理完毕。。。。")

    #去除两边的空白
    im_res = reductNoise.arrayTrim(im_res)
    # cv2.imwrite(os.path.join("image",fileName+"_arrayTrim.jpg"),im_res)

    #使用泛水填充法对图片进行区域划分
    waterFill = WaterFilled()
    waterFill.filled(im_res)
    waterFill.splitRegion(8,im_res)
    ret,im_res = cv2.threshold(im_res,100,255,cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join("image",fileName+"_waterFill.jpg"),im_res)
    print("泛水填充法处理完毕。。。。。")

    #对图片进行切割
    x_len = len(im_res[0])
    y_len = len(im_res)
    cut_step = int(x_len/4)
    cut_points = [cut_step,cut_step*2,cut_step*3,cut_step*4]
    for index,point in enumerate(cut_points) :
        try :
            results = [[0] for i in range(y_len)]
            waterCutt = WaterCutting(point,0,im_res)
            results[0] = [im_res[0][i] for i in range(index*cut_step,point)]
            temp_y = 0
            while 1==1 :
                x,y = next(waterCutt)
                #如果y大于temp_y 则results增加一行
                if y > temp_y :
                    results[y] = [im_res[y][i] for i in range(index*cut_step,point)]
                else :
                    results[y].append(im_res[y][x])
        except StopIteration :
            im_result = np.asarray(results)
            im_result = cv2.resize(im_result, (60, 60))
            kernel = 1/9*np.array([[1,2,1],[2,4,2],[1,2,1]])
            im_result = cv2.filter2D(im_result,-1,kernel)
            # char = pytesseract.image_to_string(im_result,lang="normal",config="--psm 10")
            # print("char===="+char)
            cv2.imwrite(os.path.join("char",fileName+"_waterCutting"+"_"+str(index)+".jpg"),im_result)
            del results
            print("处理完毕了")
    print("水滴切割法处理完毕。。。。。")

