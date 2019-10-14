import numpy
#降噪 pixel 二维数组
def reductNoise(pixel) :
    if  type(pixel) != numpy.ndarray :
        raise Exception("传入的参数不是列表")
    #x轴的长度,y轴的长度
    x_len,y_len = len(pixel[0]),len(pixel)
    #同步扫描x轴，遇到独立的像素点，设置为255，即白点
    #x_list 表示x纵向上的点的值集合
    for x in range(x_len) :
        x_list = [pixel[y][x] for y in range(y_len)]
        for index,item in enumerate(x_list) :
            if index >1 and index < y_len-1 and item < 255:
                if item < x_list[index-1] and item < x_list[index+1] :
                    pixel[index][x] = 255
            # if index >2 and index < y_len-2 and item < 255 :
            #     if  x_list[index-1]<x_list[index-2] and x_list[index-1] < x_list[index+1] :
            #         pixel[index][x] = 255
            #         pixel[index-1][x] = 255
            #     if  x_list[index+1]<x_list[index+2] and x_list[index+1] < x_list[index-1] :
            #         pixel[index][x] = 255
            #         pixel[index+1][x] = 255

    for y in range(y_len) :
        y_list = [pixel[y][x] for x in range(x_len)]
        for index,item in enumerate(y_list) :
            if index >1 and index < x_len-1 and item <255:
                if item < y_list[index-1] and item < y_list[index+1] :
                    pixel[y][index] = 255
            # if index >2 and index < x_len-2 and item <255 :
            #     if y_list[index-1] < y_list[index-2] and y_list[index-1] < y_list[index+1] :
            #         pixel[y][index] = 255
            #         pixel[y][index-1] = 255
            #     if y_list[index+1] < y_list[index+2] and y_list[index+1] < y_list[index-1] :
            #         pixel[y][index] = 255
            #         pixel[y][index+1] = 255

    return pixel

def arrayTrim(pixel) :
    if  type(pixel) != numpy.ndarray :
        raise Exception("传入的参数不是列表")
    #x轴的长度,y轴的长度
    x_len,y_len = len(pixel[0]),len(pixel)
    #同步扫描x轴，遇到独立的像素点，设置为255，即白点
    horiz = ['0' for i in range(x_len)]
    #x_list 表示x纵向上的点的值集合
    for x in range(x_len) :
        x_list = [pixel[y][x] for y in range(y_len)]
        for index,item in enumerate(x_list) :
            if pixel[index][x] == 0 :
                horiz[x] =  '1'
                break 
    print("max_x========"+''.join(horiz))
    min_x,max_x = horiz.index('1'),find_last(''.join(horiz),'1')
    return pixel[0:y_len-1,min_x:max_x]

def find_last(string,str):
    last_position=-1
    while True:
        position=string.find(str,last_position+1)
        print(position)
        if position==-1:
            return last_position
        last_position=position