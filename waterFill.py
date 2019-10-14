#泛水填充法
import numpy
'''
泛水填充法
'''
class WaterFilled() :
    def __init__(self) :
        self.regional = [[] for i in range(100)]
        self.signal = 1

    def filled(self,pixel) :
        if  type(pixel) != numpy.ndarray :
            raise Exception("传入的参数不是列表")
        #获取x轴y轴的长度
        x_len,y_len = len(pixel[0]),len(pixel)
        #获取二维数据的所有点的坐标集合
        points = [(x,y) for x in range(x_len) for y in range(y_len)]
        #循环遍历所有的点
        for point in points :
            #寻找黑点，若周围八个点有黑点，则打入标记
            if pixel[point[1]][point[0]] ==0 :
                self.__setPointValue(point[0],point[1],x_len,y_len,pixel)

        return pixel

    def splitRegion(self,count,pixel) :
        if  type(pixel) != numpy.ndarray :
            raise Exception("传入的参数不是列表")

        sort_reginon = sorted(self.regional,key=lambda lis: len(lis),reverse=True)
        for index,points in enumerate(sort_reginon) :
            if index < count :
                continue
            for x,y in points :
                pixel[y][x] = 255

                


    def __setPointValue(self,x,y,x_len,y_len,pixel) :
        #周围八个点的坐标
        points = [(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1)]
        for point in points :
            #将超出区域的点排除
            if point[0] >= x_len or point[1] >= y_len or point[0] < 0 or point[1] < 0 :
                continue
            #记录点的值
            p = int(pixel[point[1]][point[0]])
            if p > 0 and p < 255 :
                pixel[y][x] = p
                #区域的点数加 1
                self.regional[p].append((x,y))
                break
               
        if pixel[y][x] > 0 and x>0 and pixel[y][x] > pixel[y][x-1] and pixel[y][x-1] > 0:
            print("x="+str(x)+" y="+str(y)+ " "+str(pixel[y][x])+" <->"+str(pixel[y][x-1]))
            #将所有等于p的点更新成pixel[y][x-1] 的值
            p = int(pixel[y][x])
            for m,n in self.regional[p]:
                q = int(pixel[y][x-1])
                pixel[n][m] = q
                self.regional[q].append((m,n))
            self.regional[self.signal-1] = []         
        #如果当前点的值没有变,可认为是区域的第一个访问点
        if pixel[y][x] == 0 :
            pixel[y][x] = self.signal
            #记录区域的点数
            self.regional[self.signal].append((x,y))
            self.signal += 1